- Business Recommendations Based on Model Findings
  The model's classification report shows significant class imbalance, with precision and recall for class 1 (customers at risk of churn) being low. Here’s an analysis and actionable business recommendations:

- Key Insights

1.  High Accuracy but Poor Recall for Churn (Class 1):
    The model accurately identifies non-churning customers (class 0) with high precision and recall (99% recall for class 0).
    However, the model struggles to identify customers likely to churn (class 1), as indicated by the low recall (2%).

2.  Class Imbalance Issue:
    The dataset likely contains significantly fewer churn cases compared to non-churn cases, leading the model to focus on the majority class (non-churn).

3.  Low Macro F1-Score:
    A macro F1-score of 0.46 highlights the need for improvements in the model's ability to predict churn accurately.

- Actionable Recommendations

1.  Improve Model Performance on Churn Prediction:

a. Data Augmentation:
Use techniques like SMOTE (Synthetic Minority Oversampling Technique) to balance the dataset by generating synthetic samples for the minority class (churn cases).

b. Rebalance Class Weights:
Adjust the class weights in the model to penalize misclassifications of churn cases more heavily.
For example, in Scikit-learn’s models: class_weight='balanced'.

c. Algorithm Tuning:
Experiment with models like Gradient Boosting (e.g., XGBoost, LightGBM), which handle class imbalance more effectively.
Perform hyperparameter tuning (e.g., grid search or random search) to optimize performance.

2.  Business Strategies to Address Churn:
    a. Early Intervention Programs:
    Identify customers flagged by the model as potential churn risks (even with low precision) and provide personalized incentives, such as discounts, loyalty rewards, or exclusive offers.

b. Focus on High-Value Customers:
Prioritize intervention efforts for customers with higher lifetime value (CLV), as retaining these customers has the greatest business impact.

c. Customer Surveys:
Conduct surveys for churn-flagged customers to understand pain points and dissatisfaction areas, then use these insights to improve services.

3.  Use Soft Probabilities for Prioritization:
    a. Instead of hard predictions (0 or 1), use churn probabilities to rank customers by churn risk. Target the top 10%-20% of customers with the highest probabilities for retention strategies.

4.  Implement Customer Segmentation:
    Segment customers based on key features such as tenure, engagement score, and spending habits to tailor churn prevention strategies effectively.

- Example:
  Long-tenure, high-value customers: Provide loyalty perks or exclusive services.
  Short-tenure, low-engagement customers: Focus on onboarding and educational campaigns to increase platform engagement.

5.  Monitor and Refine the Model:
    Regularly update the model with recent data to capture changing customer behaviors and improve performance over time.

- Next Steps for the Business

1.  Enhance Data Quality:
    Gather more data on churn-specific behaviors to enrich the dataset.
    Include features like customer complaints, social media interactions, or product reviews to improve predictive accuracy.

2.  Pilot Retention Campaigns:
    Test churn prevention strategies on a small group of customers to measure effectiveness before scaling up.

3.  Track Key Metrics Post-Implementation:
    Monitor churn rate, customer retention rate, and ROI from retention campaigns to assess the success of the implemented strategies.

By focusing on these recommendations, the business can mitigate churn more effectively while improving the model’s ability to identify high-risk customers.

- HOW TO RUN THE API

1.  install flask using the pip intstall flask command.
2.  Test the API by running the Flask app... (python app.py)
3.  Send a POST request using the curl tool

    (curl -X POST -H "Content-Type: application/json" \
    -d '{"Age": 45, "Gender": 1, "Location": 0, "Tenure": 50, "AvgTransactionFrequency": 2.5, "LastTransactionDays": 30, "TotalSpending": 1500, "EngagementScore": 85, "EmailOpenRate": 0.7, "TimeSpentOnPlatform": 10, "IsSubscribed": 1}' \
    http://127.0.0.1:5000/predict)

- To Deploy the API
  Choose a deployment platform for your API. Common options include:

Cloud Platforms:
AWS (Lambda with API Gateway or EC2)
Google Cloud Run
Microsoft Azure App Service
Containerized Deployment:
Use Docker to package your API into a container and deploy on Kubernetes or Docker Hub.
