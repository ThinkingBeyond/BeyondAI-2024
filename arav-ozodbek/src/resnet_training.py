# Import Required Libraries
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np

# Define BasicBlock for ResNet
class BasicBlock(nn.Module):
    def __init__(self, in_channels, out_channels, stride=1):
        super(BasicBlock, self).__init__()
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=stride, padding=1)
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=1, padding=1)
        self.bn2 = nn.BatchNorm2d(out_channels)
        self.shortcut = nn.Sequential()

        if stride != 1 or in_channels != out_channels:
            self.shortcut = nn.Sequential(
                nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=stride),
                nn.BatchNorm2d(out_channels)
            )

    def forward(self, x):
        out = torch.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))
        out += self.shortcut(x)
        out = torch.relu(out)
        return out

# Define ResNet with adjustable layers
class ResNet(nn.Module):
    def __init__(self, num_blocks, num_classes=10):
        super(ResNet, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1)
        self.bn1 = nn.BatchNorm2d(16)
        self.in_channels = 16  # Start with 16 channels

        # Create layers dynamically
        self.layer1 = self._make_layer(16, num_blocks[0], stride=1)
        self.layer2 = self._make_layer(32, num_blocks[1], stride=2)
        self.layer3 = self._make_layer(64, num_blocks[2], stride=2)

        # Dynamically initialized during forward pass
        self.fc = None
        self.num_classes = num_classes

    def _make_layer(self, out_channels, blocks, stride):
        layers = []
        layers.append(BasicBlock(self.in_channels, out_channels, stride))  # First block
        self.in_channels = out_channels  # Update the number of input channels
        for _ in range(1, blocks):
            layers.append(BasicBlock(out_channels, out_channels))  # Remaining blocks
        return nn.Sequential(*layers)

    def forward(self, x):
        out = torch.relu(self.bn1(self.conv1(x)))  # Initial conv layer
        out = self.layer1(out)  # Layer 1
        out = self.layer2(out)  # Layer 2
        out = self.layer3(out)  # Layer 3
        out = torch.nn.functional.avg_pool2d(out, 4)  # Global average pooling

        if self.fc is None:
            flattened_size = out.view(out.size(0), -1).size(1)
            self.fc = nn.Linear(flattened_size, self.num_classes).to(out.device)

        out = out.view(out.size(0), -1)  # Flatten
        out = self.fc(out)  # Fully connected layer
        return out

# Dataset and DataLoader
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)

trainloader = torch.utils.data.DataLoader(trainset, batch_size=32, shuffle=True)
testloader = torch.utils.data.DataLoader(testset, batch_size=32, shuffle=False)

# Training Function
def train(model, device, trainloader, optimizer, criterion, epoch):
    model.train()
    total_loss = 0
    for inputs, targets in trainloader:
        inputs, targets = inputs.to(device), targets.to(device)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    return total_loss / len(trainloader)

# Testing Function
def test(model, device, testloader, criterion):
    model.eval()
    total_loss = 0
    with torch.no_grad():
        for inputs, targets in testloader:
            inputs, targets = inputs.to(device), targets.to(device)
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            total_loss += loss.item()
    return total_loss / len(testloader)

# Train and Evaluate Models
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model_variants = [
    {"name": "Small ResNet", "blocks": [1, 1, 1]},
    {"name": "Medium ResNet", "blocks": [2, 2, 2]},
    {"name": "Large ResNet", "blocks": [3, 3, 3]},
    {"name": "X-Large ResNet", "blocks": [4, 4, 4]},
    {"name": "XX-Large ResNet", "blocks": [5, 5, 5]},
    {"name": "XXX-Large ResNet", "blocks": [6, 6, 6]}
]

criterion = nn.CrossEntropyLoss()
train_losses = []
test_losses = []
num_params = []

for variant in model_variants:
    print(f"Training {variant['name']} with blocks {variant['blocks']}...")
    model = ResNet(variant["blocks"]).to(device)
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    num_params.append(sum(p.numel() for p in model.parameters()))  # Track number of parameters

    model_train_losses = []
    model_test_losses = []
    params_interval = 2000  # Adjust test loss calculation interval
    test_loss_step = []

    for epoch in range(1, 21):  # Train for 20 epochs
        train_loss = train(model, device, trainloader, optimizer, criterion, epoch)
        model_train_losses.append(train_loss)
        if epoch % 2 == 0:  # Take test loss every 2000 parameters (adjust interval here)
            test_loss = test(model, device, testloader, criterion)
            model_test_losses.append(test_loss)
    train_losses.append(model_train_losses)
    test_losses.append(model_test_losses)

# Plot Results
plt.figure(figsize=(12, 8))
for idx, variant in enumerate(model_variants):
    plt.plot(range(1, 21), train_losses[idx], label=f"{variant['name']} - Train Loss")
    plt.plot(range(1, 11), test_losses[idx], linestyle="--", label=f"{variant['name']} - Test Loss")
plt.xlabel("Number of Parameters")
plt.ylabel("Loss")
plt.legend()
plt.title("Test Train")
plt.show()