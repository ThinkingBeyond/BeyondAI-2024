![BeyondAI Banner for Research Projects](../BeyondAI_Banner_Research_Projects_2024.png)

# Non - Linear Classifiers
This project aims to explore and compare the performance of various linear and non-linear classification techniques, highlighting their strengths and weaknesses when dealing with complex, non-linearly separable data. 

## Motivation
Linear classifiers, such as Logistic Regression (LR), are widely used for classification tasks due to their simplicity, interpretability, and efficiency. These models work by drawing a straight line (or hyperplane) to separate different classes in the feature space. However, their performance can be severely limited in real-world applications, where data is often complex and not linearly separable. In such cases, linear classifiers struggle to model the intricate relationships within the data, leading to poor accuracy and generalization.

Real-world data is rarely perfectly linear. Many datasets exhibit complex patterns that cannot be captured by simple linear decision boundaries. For instance, when classes are intertwined in circular, spiral, or other non-linear patterns, linear classifiers fail to separate them effectively. This highlights the need for non-linear classifiers, which are capable of modeling complex, non-linear decision boundaries that adapt to the underlying structure of the data.

In this research, we focus on non-linear classification techniques that can handle complex patterns. The models we explore include Support Vector Machines (SVM) with an RBF kernel, Decision Trees (DT), Random Forests (RF), Gradient Boosting (GB), and Naive Bayes (NB). These models have been specifically designed to overcome the limitations of linear classifiers by learning more flexible decision boundaries. Understanding their strengths, weaknesses, and applications will help guide the selection of appropriate models for different types of data.

---
## Research Question
What are the most common non-linear classification techniques?
This question aims to identify and explore the most widely used non-linear classification techniques, which in this study include SVM with an RBF kernel, Decision Trees, Random Forests, Gradient Boosting, and Naive Bayes.

How do these techniques differ in their underlying principles and assumptions?
Here, we will examine the theoretical foundations of each model. For example, SVM with an RBF kernel maps data to a higher-dimensional space to find a hyperplane, while Decision Trees and Random Forests build decision rules through recursive splitting of the feature space. Gradient Boosting leverages an ensemble approach to iteratively refine predictions, and Naive Bayes makes simplifying assumptions about the independence of features.

What are the strengths and weaknesses of each technique in terms of accuracy, complexity, and interpretability?
This question evaluates each model based on key metrics:
Accuracy: How well each model classifies data.
Complexity: Training time, computational demands, and model complexity.
Interpretability: How easily the model's decisions can be understood or explained.

How do these techniques perform on different types of non-linearly separable datasets?
Finally, we will assess how each model performs on datasets that are known to be non-linearly separable, considering how well they handle real-world data that exhibits complex, non-linear relationships.

---
## Method and Implementation
To evaluate the performance of various non-linear classifiers, we adopted a comprehensive experimental approach using three diverse datasets. Each dataset presented different levels of complexity and varying feature types, ensuring a broad evaluation of classifier performance across different real-world scenarios. The primary goal was to assess how well the classifiers can handle non-linearly separable data.
For each dataset, we split the data into 70% training and 30% testing sets. The training set was used to train the classifiers, while the testing set was employed to evaluate each model's ability to generalize to unseen data. This division ensures that the models were not overfitting to the data and that their performance was assessed fairly on data they had not encountered during training.

- **Classifiers Evaluated:**
We focused on evaluating the following non-linear classifiers:
Logistic Regression \ Support Vector Machine with an RBF kernel \ Decision Tree  \ Random Forest \ Gradient Boosting \ Naive Bayes

- **Performance Metrics:**
To evaluate the effectiveness of each classifier, we used a combination of performance metrics:
Accuracy - The overall percentage of correct predictions made by the classifier.
Precision - The proportion of true positive predictions relative to all positive predictions made.
Recall - The proportion of true positive predictions relative to all actual positive instances in the data.
F1-Score - The harmonic mean of precision and recall, offering a balanced measure of a model’s performance.
Training Time - The amount of time each model took to train on the dataset, which is crucial for understanding the computational efficiency of the classifier.

The models were implemented using Python and the scikit-learn library, which provides efficient implementations of the classifiers used. Data visualization was conducted using matplotlib to better understand the decision boundaries learned by each classifier. For each model, we recorded the training time and computed the classification metrics using scikit-learn's built-in functions.

## Results
In the analysis of the Moon dataset with high noise, the classifiers exhibited varying performance based on their strengths and limitations in handling noisy, non-linearly separable data.
SVM (RBF kernel) emerged as the top performer, slightly outperforming Logistic Regression by capturing complex, non-linear patterns in the data.
Logistic Regression and Naive Bayes both showed solid performance, but were less effective in managing the noise, with Naive Bayes struggling due to its assumptions about feature independence.
Random Forest and Gradient Boosting demonstrated robust performance, especially in terms of recall, but were still affected by the high noise levels, reducing their ability to generalize effectively. Gradient Boosting showed the best balance between precision and recall, making it a reliable choice despite the noise.
Decision Tree performed the weakest, struggling with overfitting and failing to generalize in the noisy environment.

## Conclusions 
- Logistic Regression and Naive Bayes are faster but less accurate.
- Random Forest and Gradient Boosting are effective for noisy or imbalanced datasets, balancing accuracy and robustness while reducing overfitting, though they are more computationally expensive than simpler classifiers.
- Overall, non-linear classifiers like SVM, Random Forest, and Gradient Boosting showed superior performance in dealing with noisy, complex data, while simpler linear classifiers, such as Logistic Regression and Naive Bayes, were less effective in this context.



> The research poster for this project can be found in the [BeyondAI Proceedings 2024](https://thinkingbeyond.education/beyondai_proceedings_2024/).
