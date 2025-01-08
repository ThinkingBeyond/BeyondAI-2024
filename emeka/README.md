![BeyondAI Banner for Research Projects](../BeyondAI_Banner_Research_Projects_2024.png)

# Kolmogorov Arnold Networks vs Multi-Layer Perceptrons 

## Project Description
This project focuses on comparing Kolmogorov-Arnold Networks (KANs) and Multi-Layer Perceptrons (MLPs) in classification tasks. The primary goal is to evaluate the claim made by Ziming Liu and colleagues in their paper, which suggests that KANs perform similarly to MLPs with less parameters. Through detailed analysis and experimentation, this study aims to validate or challenge their assertion. We also aim to identify differences in the execution of each model.


## Motivation
Introduction of newer neural network architectures, like Kolmogorov-Arnold Networks (KANs), offers promising alternatives to traditional models such as Multi-Layer Perceptrons (MLPs). KANs claim to provide superior performance in terms of flexibility, convergence rates, and handling complex non-linear problems. However, these claims need to be tested on real-world datasets.
The motivation behind the project is to bridge the gap by comparing the performance of KANs and MLPs across multiple metrics, including accuracy, loss, convergence behavior,f1 score, precision, recall, and execution time. By doing so, the study seeks to provide valuable insights for researchers and industries making use of these models to guide them in model selection for classification tasks.
## Research Questions
1. Do Kolmogorov Arnold Networks (KANs) exhibit faster convergence compared to Multi-Layer Perceptrons (MLPs) across different datasets, for instance, low-datapoint and high-datapoints datasets?

2. How do Kolmogorov Arnold Networks (KANs) and Multi-Layer Perceptrons (MLPs) compare in terms of performance metrics such as accuracy,loss,f1 score,precision, and recall, and what insights can be drawn about their strengths and weaknesses in handling various classification tasks?

3. How do Kolmogorov Arnold Networks (KANs) and Multi-Layer Perceptrons (MLPs) address generalization challenges (overfitting, underfitting), and how does hyperparameter tuning affect the stability of their training processes?



## Methodology
1. **Datasets**:  
   - **Wine Dataset**: 174 samples with 13 features, classifying 3 wine types.  
   - **Wisconsin Breast Cancer Dataset**: 699 samples with 9 features, classifying 2 cancer types (benign vs. malignant).  
   - Preprocessing included standardization and train-test splitting.  

2. **Model Implementation**:
   The models were compared by adjusting the width of the layers, using a moderate width,larger width and a smaller.The models were run 3 times to get different result at different width. Hyperparameter tunnig using GridSearchCV was used to get the best parameter and hyperparameter for the layers chosen.
   - **Wine Dataset**: 2 hidden layers for each model comparison run.
   - **Wisconsin Breast Cancer Dataset**: 1 hidden layer for each model comparison run
   
4. **Metrics for Evaluation**:  
   - **Accuracy**: Measure of classification correctness.  
   - **Loss**: Convergence and overfitting behavior.  
   - **Precision, Recall, F1-Score**: Class-specific performance.  
   - **Execution Time**: Computational efficiency.  

5. **Training and Comparison**:  
   - Both models were trained over 100 epochs using different set of hidden layers 
   - Results included convergence curves for loss and accuracy, and confusion matrices to evaluate predictions.  

6. **Libraries**: `sklearn`, `pytorch`, `matplotlib`, `pykan`.  

## Result
1. MLP converges faster than KAN, as observed in the accuracy and loss graphs. This indicates that MLP reaches optimal performance in fewer epochs, making it suitable for tasks requiring quick results.

2. Both MLP and KAN achieve similar levels of final accuracy, with a difference of less than 0.03. However, MLP's accuracy was greater than KAN's accuracy. MLP also has significantly less loss values compared to KAN.

3. Both models exhibit strong generalization. Testing accuracy is comparable to training accuracy for both MLP and KAN, with no signs of overfitting. This confirms that both models are robust and reliable for unseen data. KAN requires keen hyperparameter tunning as it is very sensitive to noise, the graph displayed deflection to noise even after careful tuning.
## Conclusions
1. The results after comprehensive comparison of MLP and KAN over both dataset indicates that both models can achieve similar accuracies for classification, but MLP demonstrates faster convergence and better execution time.
2. MLP is computationally more efficient than KAN, particularly for larger datasets. Its faster convergence and lower execution time make it a better choice for high-dimensional or time-sensitive applications.
3. For tasks requiring quick training and prediction times (e.g., real-time or large-scale systems), MLP is the preferred choice due to its faster convergence and lower computational cost.
> The research poster for this project can be found in the [BeyondAI Proceedings 2024](https://thinkingbeyond.education/beyondai_proceedings_2024/).
