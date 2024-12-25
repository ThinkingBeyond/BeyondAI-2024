![BeyondAI Banner for Research Projects](../BeyondAI_Banner_Research_Projects_2024.png)

# Machiene Learning in Early Detection of Diabetic Retinopathy
### Student Researcher
Nafiul Haque
### Mentor
Dr. Devendra Singh Dhami

## Description of Project
This project explores the application of machine learning models, specifically Convolutional Neural Networks (CNNs) and Vision Transformers (ViTs), for the detection and classification of Diabetic Retinopathy (DR). DR is a major cause of blindness globally, with over 1 million cases of blindness and 3.28 million cases of severe vision impairments. Early and accurate detection can significantly reduce its impact, especially in low-resource settings where healthcare access is limited.

## Motivation for Research Question
The project addresses the critical need for robust and accessible diagnostic tools for DR in diverse clinical and resource-constrained environments. By comparing the performance of CNNs and ViTs, this research aims to identify the optimal model for such contexts, contributing to improved healthcare outcomes.

## Research Question
Which machine learning model—Convolutional Neural Networks (CNNs) or Vision Transformers (ViTs)—performs better for detecting and classifying stages of Diabetic Retinopathy, particularly in low-resource settings?

## Method and Implementation
### Dataset
The Kaggle DR Dataset 2019, containing 224×224 retinal images, was used. The dataset includes images categorized into five diagnostic stages of DR.

### Image Augmentation
Augmentation techniques were employed to enhance dataset diversity:

*Rotation:* Random rotations up to ±15°.  
*Shifting:* Horizontal and vertical shifts up to 10%.  
*Shearing & Zooming:* Shearing up to 10% and zooming up to 20%.  
*Flipping:* Horizontal flipping.  
## Model Architectures
### CNN (Convolutional Neural Networks):

- Extracts local features using convolutional layers.
- Refines features through multiple layers.
- Fully connected layers categorize images based on DR stages.
### ViT (Vision Transformers):

- Splits images into 16×16 patches.
- Encodes spatial relationships with positional embeddings.
- Uses Transformer blocks with self-attention for feature extraction.
- Classifies images into diagnostic stages.
## Evaluation Metrics
- Training and validation accuracy
- F1-score
- Sensitivity and specificity
- Confusion matrices
## Results
### Binary Classification (DR vs. No DR)
- CNN: Exhibited higher training accuracy (91-95%) but suffered from significant validation accuracy drops with smaller datasets, indicating overfitting.
- ViT: Maintained stable validation accuracy (~63-94%), demonstrating better generalization.
### Multiclass Classification (DR Stages)
Both CNNs and ViTs showed similar trends for F1-scores, sensitivity, and specificity.
- CNNs achieved higher training accuracy but plateaued in validation accuracy (70-75%).
- ViTs displayed consistent performance (~73%) for training and validation, suggesting better generalization but limited peak performance.
## Conclusions
- ViTs: Offer better generalization and robustness, making them more suitable for diverse, unseen cases in low-resource settings.
- CNNs: Excel in extracting local features and distinguishing specific DR stages, performing well with well-augmented datasets.
- Hybrid Potential: Leveraging the complementary strengths of CNNs and ViTs could lead to optimized detection systems.
Future research could explore hybrid architectures, fine-tuning techniques, and testing on larger and more diverse datasets for enhanced performance and broader applicability.
## Reference
- Vishal Awasthi a, Namita Awasthi b, Hemant Kumar c, Shubhendra Singh c, Prabal Pratap Singh d. (2021). Optimized vision transformer for diabetic retinopathy detection using Harris Hawk optimization. 
- Gulshan, V., Peng, L., Coram, M., Stumpe, M. C., Wu, D., Narayanaswamy, A.,  & Webster, D. R. (2016). Development and validation of a deep learning algorithm for detection of diabetic retinopathy in retinal fundus photographs. Jama, 316(22), 2402-2410. 
- Ting, D. S. W., Cheung, C. Y. L., Lim, G., Tan, G. S. W., Quang, N. D., Gan, A., & Wong, T. Y. (2017). Development and validation of a deep learning system for diabetic retinopathy and related eye diseases using retinal images from multiethnic populations with diabetes. Jama, 318(22), 2211-2223.
- Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). Imagenet classification with deep convolutional neural networks. In Advances in neural information processing systems (pp. 1097-1105).

## Acknowledgement
- Dr. Devendra Singh Dhami
- Dr. Filip Bar
  
Mentorship and guidance were instrumental in shaping the methodology and execution of this project.
> **Further Reading**: A detailed overview of this project is presented in our research poster, available in the [BeyondAI Proceedings 2024](https://thinkingbeyond.education/beyondai_proceedings_2024/).
