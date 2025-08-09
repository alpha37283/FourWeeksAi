State quest => https://www.youtube.com/watch?v=_L39rN6gz7Y
# Decision Tree 
classifies into categories => classification tree 
classified into numeric values => regression tree
but data can also be mixed 

same concept as tree Data structure 

# Measure the impurity: we put lowest impurity feature on the root 
impure => containment of mixed output     
Gini impurity 
Entropy: randomness => number of green samples / number of red samples 
Information Gain

# Gini impurity 
Gini Impurity of leaf node = 1 - (the probability of yes) ^ 2 - (the probability of no) ^ 2 
Weighted Gini Impurity 

- if data is numeric => calculate average of adjacent data columns
- if some node contains impurity split it further into more feature
- output of the leaves values are with most votes. 
- prune: a technique to prevent overfitting 
- prevent trees from overgrowing reduces overfitting 

https://www.youtube.com/watch?v=PHxYNGo8NcI




# Random forest: solves bias and overfitting issue in decision tree => https://www.youtube.com/watch?v=gkXX4h3qYm4
- ensemble decision trees 
- takes random sample of data 
- a group of decision tree 
- more decision tree with more features/factors => better the model performs 
- if some decision tree is not relevant we ignore them. 
- reduces overfitting 
- reduces bias: when there is certain degree of error induced in the model
# parameters : node size, number of trees, number of features
- more the trees more time will be taken to train the model

# Ensemble learning technique : 
| Feature / Aspect        | **Bagging (Bootstrap Aggregating)**                    | **Boosting**                                                         | **Stacking**                                                            |
| ----------------------- | ------------------------------------------------------ | -------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Goal**                | Reduce **variance** (avoid overfitting)                | Reduce **bias** (make weak models strong)                            | Combine diverse models for better predictions                           |
| **Data Sampling**       | Random sampling **with replacement** (bootstrap)       | Sequential sampling — each model focuses on mistakes of the previous | Usually uses full dataset for each model                                |
| **Model Training**      | Models trained **independently** in parallel           | Models trained **sequentially**, each correcting previous errors     | Models trained independently, then meta-model learns from their outputs |
| **Model Type**          | Typically same type (e.g., decision trees)             | Often same type but sequentially improved                            | Can be same or different types (heterogeneous)                          |
| **Combination Method**  | Majority vote (classification) or average (regression) | Weighted vote/average based on model performance                     | Meta-learner combines predictions                                       |
| **Speed**               | Faster (parallelizable)                                | Slower (sequential training)                                         | Slower (two-stage process)                                              |
| **Risk of Overfitting** | Lower than a single model                              | Higher if not regularized properly                                   | Can overfit if base models or meta-model are too complex                |
| **Famous Algorithms**   | Random Forest, Bagged Trees                            | AdaBoost, Gradient Boosting, XGBoost, LightGBM                       | Stacked Generalization, Blending                                        |
| **When to Use**         | When model has **high variance**                       | When model has **high bias**                                         | When you want to combine strengths of very different models             |


# Rule of Thumb
- High bias → bad at both train & test.
- High variance / overfitting → great at train, bad at test.
- Perfect generalization → close train & test scores.

