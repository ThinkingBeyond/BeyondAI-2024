![BeyondAI Banner for Research Projects](../BeyondAI_Banner_Research_Projects_2024.png)

# Comparing Transformers to LSTMs with Attention

## Motivation

The "Attention is All You Need" paper introduced the Transformer model, a milestone that revolutionized natural language processing (NLP). Before this, LSTMs with attention mechanisms dominated the field. By comparing these two architectures, this research aims to provide insights into their strengths, weaknesses, and suitability for NLP tasks.

## Research Question

How do Transformers compare to LSTMs with attention in performance and efficiency for text-based sentiment analysis?

## Methodology

To address this question, we:

1. **Conducted a Literature Review**: We reviewed foundational papers, including "Attention is All You Need" and seminal works on LSTMs with attention mechanisms.

2. **Dataset Selection**: The IMDb reviews dataset, containing 50,000 evenly split positive and negative movie reviews, was chosen for its balance and suitability for binary classification tasks.

3. **Model Implementation**: Under our mentor's guidance, we implemented both models in Google Colab using the PyTorch library:

   - **Transformer**: Leveraging pre-trained BERT, we built a Transformer network with a classification head.
   - **LSTM with Attention**: Using existing libraries, we implemented an LSTM network enhanced by an attention mechanism.

4. **Evaluation Metrics**: To compare performance and efficiency, we measured:

   - **Accuracy, Precision, Recall, and F1-Score**: To assess prediction quality.
   - **Training Time and Inference Speed**: For efficiency comparison.
   - **Memory Usage**: To evaluate computational resource requirements.

## Results

Our findings highlighted:

- **Performance**: Transformers achieved higher accuracy, precision, recall, and F1-scores compared to LSTMs with attention. They excel at handling long-range dependencies and complex sentence structures.
- **Efficiency**:
  - **Training Time**: Transformers required slightly more time (~6 minutes vs. ~5 minutes for LSTMs over 5 epochs).
  - **Inference Speed**: Transformers processed inputs faster (~12 ms/example vs. ~20 ms/example for LSTMs).
  - **Memory Usage**: Transformers demanded significantly more memory (2.5 GB vs. 1.5 GB for LSTMs during training).
- **Resource Sensitivity**: While Transformers excel in performance, their higher computational demands make LSTMs preferable for resource-constrained environments.

## Conclusions

Transformers demonstrate superior performance and efficiency in sentiment analysis tasks, making them ideal for large datasets and scenarios requiring scalability and high accuracy. However, LSTMs with attention remain a practical choice for smaller datasets or low-resource environments.

### Key Takeaways

- **Transformer Advantages**: Scalability, parallel processing, and exceptional handling of long-text dependencies.
- **LSTM with Attention Advantages**: Lower memory usage, simpler architecture, and suitability for small-scale applications.

> **Further Reading**: A detailed overview of this project is presented in our research poster, available in the [BeyondAI Proceedings 2024](https://thinkingbeyond.education/beyondai_proceedings_2024/).

