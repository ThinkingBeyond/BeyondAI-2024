![BeyondAI Banner for Research Projects](../BeyondAI_Banner_Research_Projects_2024.png)

# Comprehensive Investigation of Double Descent Behavior with Dropout and Weight Decay Regularization

## Project Overview

This project explores the double descent phenomenon, a non-monotonic relationship between model complexity and generalization performance that challenges the traditional bias-variance tradeoff in machine learning. We examine the roles of dropout and weight decay regularization in mitigating overfitting and enhancing model performance across various architectures.

### Research Question
How do regularization techniques (such as dropout and weight decay) influence the double descent phenomenon and mitigate overfitting across different deep learning model architectures?

### Key Objectives
- Investigate double descent behaviors in shallow networks, decision trees, and polynomial regression models.
- Analyze the effects of dropout and weight decay on generalization and overfitting.
- Combine regularization techniques to assess their synergistic impacts on double descent.

---

## Results Summary

- **Dropout:** Dropout rates between 0.1 and 0.2 effectively reduced overfitting, while higher rates (0.4) caused instability.
- **Weight Decay:** L2 regularization smoothed loss curves but required careful tuning to avoid underfitting.
- **Combined Regularization:** Dropout and weight decay together yielded consistent improvements, balancing overfitting and underfitting.

### Learn More
You can find the research paper [here](https://drive.google.com/file/d/1F_3VUV4J0GOjqTEzMFSqhkPkT-amtfYM/view).

---

## Contributions

### Team Members
- **E. Ozodbek**
- **A. Arav**

### Mentor
- **Emilie Gregoire**

---

## Acknowledgements

This project is part of BeyondAI 2024. Special thanks to the program organizers, our mentor **Emilie Gregoire**, and our peers for their valuable feedback.

---

## Suggestions

If you prefere other IDEs (eg. VS code) you might want to use **.py** codes which we provided in **src** folder.

---

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- GPU support for optimal performance (optional but recommended)
- Required Python libraries listed in `requirements.txt`

### Installation
```bash
# 1. Clone this repository:
git clone https://github.com/ThinkingBeyond/BeyondAI-2024.git
cd BeyondAI-2024

# 2. Install dependencies:
pip install -r requirements.txt

# 3. Verify installation by running a Python script (e.g., resnet_training.py):
python src/resnet_training.py

> The research poster for this project can be found in the [BeyondAI Proceedings 2024](https://thinkingbeyond.education/beyondai_proceedings_2024/).
