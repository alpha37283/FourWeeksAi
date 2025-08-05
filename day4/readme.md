~~# supervised vs unsupervised
- only difference is in data. 
- labeled data vs unlabeled data
- supervised => classification or regression 
- unsupervised => clustering 

Ensembling and bagging 
- combine many decision trees/models to a single model => ensembling algorithm => bagging 
- train multiple model on different subset of the data using method called bootstrapping. => a famous version is random forest

1. Supervised Learning

   A. Regression: continuos numeric target
      - Linear Regression: Fits a straight line to predict continuous values.
      - Ridge Regression: Linear regression with L2 regularization to prevent overfitting.
      - Lasso Regression: Linear regression with L1 regularization to reduce features.
      - Support Vector Regression (SVR): Uses margins to predict continuous outcomes.

   B. Classification: discrete categories 
      - Logistic Regression: Predicts probabilities for binary classes.
      - Naive Bayes: Applies Bayes’ theorem assuming feature independence.
      - Neural Networks: Layers of neurons learn patterns in complex data for classification.

   C. Common to Both Regression and Classification
      - Decision Tree: Splits data using conditions to predict continuous values or class labels.
      - Random Forest: Combines multiple decision trees for better prediction of values or classes.
        - removing multiple features randomly
        - Boosting: Sequentially builds weak learners to reduce error in regression or classification.
        - train model in sequence, each layer/sequence tries to fix previous model's output
        - more prone to overfitting 
        - types
          - adaboost 
          - gradient boost
          - xgboost 
          
      - Support Vector Machine (SVM): Can be adapted for both classification and regression tasks. Powerful in high dimension when higher number of features
        - use of kernal functions: turn features into new complex features, different types of functions 
      - K-Nearest Neighbors (KNN): Classifies based on majority label of nearby points. predict average of its k nearest neighbours, k is hyperparameter 
        - 1. Distance Metric: distance between query point and other data point need to be calculated
        - 2. Value of k: number of neighbours to check for a point e.g., k = 1 for one class it will be checked
               ---------Adv----------||------------disAdv---------
              1. easy to implement   || scalability difficult
              2. few hyperparams     || curse of dimensionality 
              3. adaptable to new data ||  overfitting
        
                      


2. Unsupervised Learning

   A. Clustering
      - K-Means: Groups data into K clusters based on similarity.
      - Hierarchical Clustering: Builds a tree of clusters based on similarity.
      - DBSCAN: Finds clusters based on dense regions in data.
      - Mean Shift: Locates clusters by shifting data points toward high-density areas.

   B. Dimensionality Reduction
      - PCA (Principal Component Analysis): Projects data onto fewer dimensions for simplification.
      - t-SNE: Visualizes high-dimensional data in 2D or 3D.
      - Autoencoders: Neural networks that compress and reconstruct data.

   C. Association Rule Learning
      - Apriori: Discovers frequent itemsets and association rules.
      - Eclat: Efficiently finds frequent itemsets using set intersections.



https://scikit-learn.org/stable/machine_learning_map.html