![BeyondAI Banner for Research Projects](../BeyondAI_Banner_Research_Projects_2024.png)

# Kolmogrov Arnold Networks vs Multi-Layer Perceptrons 

Provide a description of your project including 

1. Motivation for the Research Question
   
While analyzing the paper written by Ziming Lui and partners,it was stated that the new network called KANs were going to overperform the MLPs in terms of convergence rate and accuracy with minimum number of layers. The outcome of their research seemed promising, but as a researcher, I decided to test the claim made and compare both models together to ascertain what was claimed. 

2. Research Question: I came up with three research question to prove/ refute this claim.

i. Do Kolmogorov Arnold Networks (KANs) exhibit faster convergence compared to Multi-Layer Perceptrons (MLPs) across different problem domains, particularly in low-dimensional and high-dimensional tasks?

ii. How do Kolmogorov Arnold Networks (KANs) and Multi-Layer Perceptrons (MLPs) compare in terms of performance metrics such as accuracy, f1 score, and recall, and what insights can be drawn about their strengths and weaknesses in handling various classification tasks?

iii. How do Kolmogorov Arnold Networks (KANs) and Multi-Layer Perceptrons (MLPs) address generalization challenges (overfitting, underfitting) when using their optimal hyperparameters, and how does hyperparameter tuning affect the stability of their training processes?



3. Methodology

Using MLPClassifier from sklearn

Using pykan from the paper 

I used two different datasets one with higher number of datapoints, and the other with relatively lower number.

Using the train and test split to divide my dataset and study the recalling capacity.

I plotted an accuracy curve as well as a loss curve to Visualize convergence rate or each of the model.

I also used larger epochs to test for overfitting in the modes.

4. Result
In accordance to the research question

i. Based on convergence rate,MLPs converge to an accuracy range of (97-100)%, while KANs didn't converge and also had a very fluctuating accuracy despite a longer execution time.

ii. In terms of accuracy MLP had higher accuracy than KANs, the highest accuracy attained by KANs was 97.5% while that of MLPs was 100%. 

In terms of f1 score, that of MLPs was higher than that of KANs.

In terms of recall, both models didn't recall poperly but MLP recalled better.

iii. The MLPs begin to overfit with datasets of a out 7000 datapoints at about 75-80 epochs. KANs had fluctuating accuracies and loss, it also didn't converge,and in turn doesn't generalize well.

5. Conclusions

Overall, I'll say MLPs perform better than KANs in terms of comparison task.

> The research poster for this project can be found in the [BeyondAI Proceedings 2024](https://thinkingbeyond.education/beyondai_proceedings_2024/).
