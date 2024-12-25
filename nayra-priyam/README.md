![BeyondAI Banner for Research Projects](../BeyondAI_Banner_Research_Projects_2024.png)

# Optimizing MLPs for MNIST

**by**
- Nayra Saadawy
- Priyam Raul

**mentor**
- Prof. Devendra Singh

---
# Project Description

This project compares loss values across epochs and observes how they changed with different settings, such as activation functions, learning rates, and step sizes. By testing these parameters, we aimed to understand their impact on model behavior and identify the best combination to achieve optimal results.

# Motivation

The primary motivation for this research was to understand the factors that hinder or enhance the performance of Multi-Layer Perceptrons (MLPs). Neural networks often rely on various parameters—such as activation functions, learning rates, and step sizes—that significantly influence their training behavior and convergence. By systematically studying the impact of these parameters, we aimed to uncover their role in optimizing performance and minimizing loss values.

This project focused on testing simple MLP models to demonstrate how parameter choices affect loss values across epochs. While the changes observed were not drastic for smaller models, the findings emphasize the importance of fine-tuning parameters. For more complex MLPs, similar adjustments could lead to significant improvements in performance, highlighting the value of systematic experimentation.


# Method and Implementation

The code goes through different versions of MLPs, testing one parameter at a time step by step. For each test, it measures loss values to see how each setup performs.

The code starts by importing the usual libraries—`torch`, `torch.nn`, and `torchvision`. Then, it sets up the MLP structure. Since MNIST images are 28x28 pixels, the input layer has 784 neurons. The neuron count shrinks layer by layer until the output layer, which has 10 neurons (one for each digit). 

The FashionMNIST dataset was prepared and loaded into the model. We used the **Adam optimizer** because it works well with ReLU activation, and the loss function was **CrossEntropyLoss**. The training loop printed the loss after every epoch and plotted graphs to make comparisons easier.

**Weight Initialization**: He initialization was used to reduce overfitting and gradient issues, and biases were set to 0.

## Testing Parameters

Here’s how the testing went:

- **Activation Functions**: We tried Sigmoid, ReLU, Tanh, and Leaky ReLU. Sigmoid and ReLU gave the lowest loss values.  
- **Learning Rates**: We tested 0.0001, 0.001, and 0.01, fixing the activation function to either Sigmoid or ReLU. The best learning rate for both was 0.001.  
- **Step Sizes**: We tested step sizes of 20, 30, and 40 while keeping the learning rate at 0.001 and trying both Sigmoid and ReLU.  

# Results

After all the testing, the best combination we found was **Sigmoid activation**, a **learning rate of 0.001**, and a **step size of 30**. This gave a final loss value of **0.1734** and a runtime of **210.87 seconds**.  


# Conclusion

In this research, we systematically explored the effects of key parameters—activation function, learning rate, and step size—on the performance of a Multi-Layer Perceptron (MLP) model. By optimizing each parameter iteratively, we identified the closest as possible to ideal configuration: the **Sigmoid activation function**, a **learning rate of 0.001**, and a **step size of 20**. This combination yielded the most effective model in terms of performance and convergence.

The results emphasize the critical role of parameter tuning in neural network design. Even small adjustments can have a significant impact on model behavior and effectiveness, making systematic experimentation essential for achieving optimal results.


# References

- Glorot, X., & Bengio, Y. (2010). *Understanding the difficulty of training deep feedforward neural networks*. In Proceedings of the thirteenth international conference on artificial intelligence and statistics (pp. 249-256). JMLR Workshop and Conference Proceedings.  
- Musa, A., & Aliyu, F. (2019, October). *Performance evaluation of multi-layer perceptron (MLP) and radial basis function (RBF)*. In 2019 2nd International Conference of the IEEE Nigeria Computer Chapter (NigeriaComputConf) (pp. 1-5). IEEE.





> The research poster for this project can be found in the [BeyondAI Proceedings 2024](https://thinkingbeyond.education/beyondai_proceedings_2024/).
