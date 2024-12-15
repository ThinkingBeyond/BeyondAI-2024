![BeyondAI Banner for Research Projects](../BeyondAI_Banner_Research_Projects_2024.png)

# Comparing Transformers to LSTMs with Attention

# Motivation:
The "Attention is All You Need" paper introduced the Transformer model, which has revolutionized natural language processing (NLP). This research aims to compare the performance of Transformers to LSTMs with attention mechanisms, which were a dominant approach before Transformers. Understanding the strengths and weaknesses of each architecture is crucial for making informed choices in NLP tasks.

# Research Question:
After our thorough literature review, we decided to focus our research on the following question: How do Transformers compare to LSTMs with attention in performance and efficiency for text-based sentiment analysis?

# Method and Implementation:
Our approach was to read as much literature as we could find centred around the cornerstone "Attention is all you need" paper, as well as various LSTM focused research as well. After familiarising ourselves with the architectures of both models, we worked to implement them. After choosing and preparing the dataset of our choice, which was the IMDB dataset of positive and negative movie reviews, we worked together on google colab under the supervision of our mentor to design and then programme these models. Once complete, we then tested various metrics on our models to measure accuracy and precision, through metrics such as training time, memory usage and inference speed.

# Results:
What we found from our tests was that the transformer outperformed the LSTM for all metrics for accuracy and precision under similar training time, which we tried to keep as similar as possible to gain comparable results. What we did find however was that the transformer required more memory usage, and was therefore more resource intensive. 

# Conclusions:
Transformers generally outperform LSTMs with Attention in sentiment analysis tasks, excelling in both performance and efficiency. This makes them ideal for larger datasets and faster processing. However, LSTMs with Attention remain a viable alternative for scenarios with limited computational resources or a need for smaller models. Future research could explore hybrid models that combine the strengths of both architectures or investigate the application of Transformers to smaller, less structured datasets.

> The research poster for this project can be found in the [BeyondAI Proceedings 2024](https://thinkingbeyond.education/beyondai_proceedings_2024/).
