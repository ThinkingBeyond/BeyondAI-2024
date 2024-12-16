![BeyondAI Banner for Research Projects](../BeyondAI_Banner_Research_Projects_2024.png)

# Weight Initialization for MLPs

**Student Researchers**

- Osewuike Igue
- Gulalaiy Khankhel

**Research Mentor**

- Barbora Barancikova

---

## Motivation
  
In Multi-layer Perceptrons (**MLP**s), how the weights are initialized is very important in the training process, as well as the overall performance of the MLP. The right initialization can make training faster, avoid problems like vanishing or exploding gradients, and generally lead to better performance. This project looks into how different weight initialization methods impact MLPs' performance. We’re also interested in how these methods work together with things like **activation functions** and **optimizers**. Ultimately, the goal is to figure out which initialization strategies work best for different situations.



## The Research Questions we aim to answer include:

* How do different weight initialization methods affect the training  and overall performance of MLPs?
* How do initialization methods interact with other factors, like activation functions, optimizers and MLP Depth?
* Can we pinpoint the best weight initialization strategies in different scenarios?

---

### Setting Up the Environment

This project includes a `requirements.txt` file that lists all the Python packages and their versions used in this project. You can use this file to recreate the exact environment required to run the code.

---

### Dataset

This project uses the MNIST dataset for training and evaluation. To ensure that users do not need to manually download the dataset, the Colab notebook automatically fetches the required data file every time it is run.

**How It Works**

The following command in the notebook downloads the MNIST dataset (`mnist.pkl.gz`) from an open GitHub repository:

```bash
!wget -O mnist.pkl https://github.com/mnielsen/neural-networks-and-deep-learning/raw/master/data/mnist.pkl.gz
```

---

### Methodology & Implementation

We ran 3 main experiments to analyze the performance of Weight Initialization Methods including Zero Initialization, Random (Gaussian) Initialization, Xavier Initialization, and He Initialization. 

We hoped to study:

- The effect of different activations (**ReLU, Tanh, Sigmoid**) on the performance of different weight initialization methods.
- The effect of different optimizers (**SGD, Adam**) on the performance of different weight initialization methods.
- The effect of **MLP depth** on weight initialization performance in a shallow and deep architecture.

We trained the MLP on the **MNIST dataset** with a learning rate of 0.01, batch size of 150, and Cross Entropy Loss. For activation and optimizer experiments, the model used 2 hidden layers; for depth analysis, we compared 1 vs. 6 hidden layers.

---

### Results

Our results included many visualizations that provided insights into the performance of different weight initialization techniques. **Training Loss Trends** showcased how each method converges, and **Test Loss Trends** emphasized generalization performance. **Test Accuracy Trends** showed us how well our MLP performs on unseen data. Additionally, **Weight Distribution Histograms** before and after training showed us how initialization influences weight magnitudes, which can in turn affect stability and generalization. Lastly, **Activation Distributions** across layers helped us understand how different methods impact activation values. In our research poster, we were not able to include all visualizations, hence, for seeing all of our visualizations, feel free to check out our code.

---

### Conclusion

**Our** **research** shows that **Xavier** and **He** **Initialization** perform well across various setups: **Xavier** suits tanh and sigmoid, while **He** is ideal for ReLU. **Random Initialization** works for shallow models but risks gradient issues in deeper ones, while **Zero** **Initialization** fails entirely as it prevents learning. **He** initialization excels by maintaining gradient flow and avoiding inactive neurons hence ensuring faster convergence with ReLU. **Xavier** balances gradient propagation in deeper networks leading to better stability and test accuracy. In conclusion, **Xavier** and **He** are the best choices, **Random** is viable for simple models, and **Zero** should be avoided. 

---

### Future Research

Future research on this topic could explore additional weight initialization techniques, such as **LeCun** or **Orthogonal**. Moreover, our findings could be extended to more complex tasks and diverse datasets to test their generalisability and provide more insight into how different initializations interact with various architectures. This could help refine best practices across a wider range of applications.

---

### References

- Haykin, S. S. (2009). Neural networks and learning machines. Pearson Education.
- Glorot, X., & Bengio, Y. (2010). Understanding the difficulty of training deep feedforward neural networks.
- He, K., Zhang, X., Ren, S., & Sun, J. (2015). Delving deep into rectifiers: Surpassing human-level performance on imagenet classification.
- Javatpoint. (n.d.). Multi-layer perceptron in TensorFlow, from https://www.javatpoint.com/multi-layer-perceptron-in-tensorflow.

> The research poster for this project can be found in the [BeyondAI Proceedings 2024](https://thinkingbeyond.education/beyondai_proceedings_2024/).
