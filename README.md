# A Comparative Analysis: Machine Learning vs. Deep Learning Algorithms for Predicting Default Risk

## Introduction

By: George Kenji Putra

From: HCK-005

Dataset: **Home Credit Default Risk**

For more information regarding the dataset, kindly visit [here](https://www.kaggle.com/competitions/home-credit-default-risk/data).

Objective: 

The objective of this comparative analysis, titled `A Comparative Analysis: Machine Learning vs. Deep Learning Algorithms for Predicting Default Risk`, is to assess and compare the performance of machine learning and deep learning algorithms in predicting default risk for Home Credit. The primary goal is to determine the effectiveness of these algorithms in accurately predicting the likelihood of borrowers defaulting on their loan payments. By analyzing various factors such as credit history, financial information, and employment details, we aim to create reliable models that can evaluate the creditworthiness of potential borrowers.

Through this analysis, our objective is to make well-informed lending decisions and reduce default risks for Home Credit. By comparing the performance of machine learning and deep learning algorithms, we seek to identify which approach provides better predictive capabilities for assessing default risk. This evaluation will help ensure the financial stability of the lending institution while enabling the provision of credit access to qualified borrowers.

Deployment: For model deployment, please visit here: [Hugging Face](https://huggingface.co/spaces/agayabag/deploy_default_risk).

Conclusion:

Default risk assessment is crucial for lenders to evaluate borrowers' likelihood of failing to repay loans. The EDA reveals an imbalance in loan repayment rates and identifies relationships between features and loan repayment. Insights show that laborers and younger applicants have higher default risks, while certain occupation types face difficulties in repayment. These findings enable lenders to make informed decisions, design tailored products, and mitigate default risks.

The evaluation metric used is recall, which measures the proportion of true positive predictions. Minimizing false negatives is crucial to avoid financial loss, increased default risk, higher borrowing costs, and damage to trust and reputation. The LGBM model excels in handling large datasets but requires careful hyperparameter tuning. Feature engineering, exploring different algorithms, addressing imbalanced datasets, and proper hyperparameter tuning can further improve future results.
