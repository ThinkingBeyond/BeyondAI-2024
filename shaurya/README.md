![BeyondAI Banner for Research Projects](../BeyondAI_Banner_Research_Projects_2024.png)

# DOUBLE DESCENT VS OVERFITTING IN DEEP LEARNING
THE PROBLEM STATEMENT:

The interplay between overfitting and double descent in deep learning challenges traditional learning theory. Investigating this transition reveals how model capacity, data properties, and regularization influence generalization. Understanding these dynamics is crucial for optimizing overparameterized models and addressing practical challenges in training large neural networks on diverse and noisy datasets.
   
OVERFITTING:

Overfitting occurs in machine learning when a model learns the training data too well, including its noise and random fluctuations, rather than capturing the underlying patterns. As a result, the model performs well on the training data but poorly on unseen or test data.

DOUBLE DESCENT:

Double descent is a machine learning phenomenon where a model's error on unseen data doesn't just keep increasing as the model gets more complex. Instead, after initially worsening, the error improves again if the model becomes very complex. This challenges the old idea that more complexity always leads to worse performance.

HOW WAS THE MODEL DESIGNED:

   1. A flexible feedforward neural network (FlexibleNN) was developed to study the effects of model complexity on performance.

   2. The MNIST dataset was used for training and evaluation, consisting of grayscale images of handwritten digits.

   3. The model was trained using cross-entropy loss and SGD optimizer, with training and testing across epochs to analyze performance trends like overfitting and double descent.

   4. Training and test losses were plotted across epochs for each model configuration. This allowed the identification of overfitting regions and the double descent behavior as model complexity increased.

EFFECT OF INCREASING MODEL COMPLEXITY

   1. Increasing the number and size of hidden layers initially improved performance, reducing both training and test loss.

   2. Beyond a certain complexity, overfitting occurred, evidenced by a significant divergence between training and test loss.

   3. Double Descent Phenomenon: For highly complex models, test loss showed an initial increase (overfitting) followed by a decrease as model capacity grew further, demonstrating double descent behavior.

PERFORMANCE TRENDS: 
   1.  Simpler models struggled to capture patterns effectively, resulting in higher training and test loss.

   2. Intermediate-complexity models balanced generalization and overfitting, achieving optimal performance.

   3. Loss Visualization: Training and test loss curves provided clear visual evidence of overfitting and the transition to the double descent phase as model complexity increased.

CONCLUSION:

This study demonstrated the double descent phenomenon, where increasing model complexity initially caused overfitting but later improved generalization. These findings highlight the complex relationship between model capacity and performance.

> The research poster for this project can be found in the [BeyondAI Proceedings 2024](https://thinkingbeyond.education/beyondai_proceedings_2024/).
