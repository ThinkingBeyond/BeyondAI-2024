![BeyondAI Banner for Research Projects](../BeyondAI_Banner_Research_Projects_2024.png)

# Kolmogorov Arnold Networks vs Multi-Layer Perceptrons 

## Project Description
This project focuses on comparing Kolmogorov-Arnold Networks (KANs) and Multi-Layer Perceptrons (MLPs) in classification tasks. The primary goal is to evaluate the claim made by Ziming Liu and colleagues in their paper, which suggests that KANs outperform MLPs. Through detailed analysis and experimentation, this study aims to validate or challenge their assertion.


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
   - **KANs**:  
     - **Wine Dataset**: `width=[13,5,3]`, `grid=5`, `k=3`.  
     - **Cancer Dataset**: `width=[9,5,5,5,2]`, `grid=5`, `k=3`.  
   - **MLPs**:  
     - **Wine Dataset**: `hidden_layer_sizes=(40,25,10)`, `max_iter=500`, `activation='tanh'`.  
     - **Cancer Dataset**: `hidden_layer_sizes=(5,5,5)`, `max_iter=1000`, `activation='tanh'`.  
     - Different width of KANs lower than the number of layers would be used 

3. **Metrics for Evaluation**:  
   - **Accuracy**: Measure of classification correctness.  
   - **Loss**: Convergence and overfitting behavior.  
   - **Precision, Recall, F1-Score**: Class-specific performance.  
   - **Execution Time**: Computational efficiency.  

4. **Training and Comparison**:  
   - Both models were trained over 100 epochs using different set of hidden layers 
   - Results included convergence curves for loss and accuracy, and confusion matrices to evaluate predictions.  

5. **Libraries**: `sklearn`, `pytorch`, `matplotlib`, `pykan`.  

## Result
1. In terms of convergence rate, both models converges at a similar though KAN converges faster. Each model reaching convergence within 10-50 EPOCHS.KAN converges with a higher execution time.

2. Both models reach a very high accuracy, recall, precision, f1-score. They have a lower loss. MLP has a loss of about 0.1% while KAN experiences a larger  loss of 12 -30%.

3. KAN is very sensitive to noise which requires careful hyperparameter tunning to prevent overfitting. Using GridSearchCV for both models, I was able to get the highest hyperparameter to be used for each model. Adjusting the hyperparameter of KAN makes converges 
fluctuate while adjusting that of MLP reduces the accuracy. 
## Conclusions
Both models are very good for classification. KAN performs similarly to  a MLP with lower number of layer.
> The research poster for this project can be found in the [BeyondAI Proceedings 2024](https://thinkingbeyond.education/beyondai_proceedings_2024/).
