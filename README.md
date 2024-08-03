## Intelligent Prompt Classification for AI Task Routing

**Project Description**

The objective is to classify user prompts into predefined categories and sub-categories. This classification is crucial for routing user requests to the most appropriate AI platform or tool, enhancing the efficiency and accuracy of AI-powered applications. 

**Dataset**

A synthetic dataset of over 300 user prompts was generated for this project. The prompts were designed to be diverse and evenly distributed across the following categories and sub-categories:

**Categories & Sub-categories**

* **Communication**
    * Chatbots and Virtual Assistants
    * Conversation
    * Mental health
* **Music and Audio**
    * Music Creation
    * Speech Generation
    * Podcast Content Creation
* **Programming and Development**
    * Coding and Programming Assistance
    * API Integration
* **Business and Productivity**
    * Presentation Creation
    * Email Generation

**Methodologies**

Three distinct approaches were implemented and evaluated for prompt classification:

1. **Fine-tuned BERT for Hierarchical Classification**

   * **Approach:** A pre-trained BERT model that was fine-tuned using the Hugging Face `transformers` library. Two separate AutoModelForSequenceClassification models were trained: one for cluster classification and another for sub-classification within the predicted cluster.
   * **Strengths:** BERT's ability to capture contextual information in language makes it well-suited for this task. With sufficient data, fine-tuned BERT models can achieve state-of-the-art results in text classification.
   * **Limitations:** Computationally expensive, especially with larger datasets and complex models. Prone to overfitting on smaller datasets.

2. **Traditional Machine Learning**

   * **Approach:**  Classic machine learning algorithms (Logistic Regression, SVM, Naive Bayes) were trained on TF-IDF (Term Frequency-Inverse Document Frequency) vectors extracted from the prompts. Preprocessing included punctuation removal, stop word removal, and lemmatization.
   * **Strengths:**  Relatively simple to implement and computationally less demanding than deep learning approaches. Logistic Regression provided the best results in this case.
   * **Limitations:**  May not capture complex language nuances as effectively as deep learning models. Requires significant feature engineering and a large amount of data for optimal performance.

3. **Prompt Engineering with Large Language Models (LLMs)**

   * **Approach:**  Leveraged the power of LLMs (using OpenAI's API) with carefully crafted prompt templates for each cluster and sub-category. A two-stage prompting approach was used: first to identify the cluster and then to predict the sub-class using a cluster-specific prompt.
   * **Strengths:**  Can achieve impressive results with less training data than traditional methods. Highly adaptable and can be easily extended with new categories or tasks.
   * **Limitations:**  Relies on the quality of prompt engineering and the inherent uncertainty of LLM outputs. Can be more challenging to systematically evaluate and debug compared to traditional models.

**Evaluation and Ranking**

The performance of each approach was evaluated using accuracy and F1-score metrics:

| Approach                               | Accuracy | F1-Score |
|----------------------------------------|----------|----------|
| 1. Fine-tuned BERT                     | 99%      | 98%      |
| 2. Traditional ML (Logistic Regression) | 96.8%    | 96.7%    |
| 3. LLMs and Prompt Engineering        | 84%      | 86%      |

**Ranking (Best to Worst)**

1. **Fine-tuned BERT:** Achieved the highest accuracy and F1-score, likely due to its ability to learn complex language representations. However, the high scores might be attributed to overfitting given the limited dataset size.
2. **LLMs and Prompt Engineering:**  Showed promising results with less data dependence, highlighting the potential of LLMs for this task. Further improvements in prompt engineering and LLM capabilities could lead to even better performance.
3. **Traditional ML:** The performance of Logistic Regression was mediocre at best, mainly due to the limited dataset size and the need for more sophisticated feature engineering.

**Conclusion**

This project demonstrates the effectiveness of different approaches for prompt classification. The choice of the best approach depends on factors such as dataset size, computational resources, and desired accuracy levels.
