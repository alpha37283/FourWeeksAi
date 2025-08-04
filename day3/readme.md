# Logistic Regression:
-predicts something true or false or discrete value 
-fits and S shape regression function 
-curve shows probability of something being true or false
-lower part of S and higher part of S
-can have multiple input variable
-can work with both continuos and discrete data
-we can check whether a certain variable is helping in making predictions or not
-in linear regression we use sum of square residuals but instead uses maximum likelihood


Problems: categorical data/classification problem
- whether the email is spam or not
- will customer will buy insurance or not


# NOTE: plot the data by plotting we can have many answers of simple problems/questions
- see which type of regression function fits better like S shape or Linear line 

# what we are doing: 
- y = mx + b
- we are using sigmoid
- sigmoid(z) = 1 / 1 + e ^ -z
- or 
- logisticRegression(z) = 1 / 1 + e ^ -(mx + b)



# parameters 

penalty: Type of regularization to apply ('l2' is default to prevent overfitting).
dual: Whether to solve the dual optimization problem (False is standard unless features > samples).
tol: Minimum improvement in loss required to continue training.
C: Inverse of regularization strength (lower C = stronger regularization).
fit_intercept: Whether to add an intercept (bias) to the model.
intercept_scaling: Scaling applied to the intercept when solver='liblinear'.
class_weight: Weights to handle imbalanced classes (None = all equal, 'balanced' = auto adjust).
random_state: Sets the seed for reproducibility of results.
solver: Optimization algorithm used for fitting the model ('lbfgs', 'liblinear', etc.).
max_iter: Maximum number of iterations for solver to converge.
multi_class: Strategy for multiclass classification ('ovr' or 'multinomial').
verbose: Controls how much output is shown during training (0 = silent).
warm_start: Reuse the solution of the previous fit to continue training.
n_jobs: Number of CPU cores to use (-1 means use all).
l1_ratio: Balance between L1 and L2 penalty (None unless using 'elasticnet' penalty).


# CAT CAR DOG DOG DOG MOBILE HOME  DOG  DOG  BIRD  => test data set 
  DOG DOG DOG NO  DOG   NO   DOG   NO  DOG  DOG    => predictions

# TRUE POSITIVE
- total 7 dogs
- out model predicted 4 dogs out of 7 
- compare the prediction with reality

# FALSE POSITIVE 
- 3 were predicted dog but in reality they were not dog 

# Number of predictions right 
right preds / total preds 

# Precision: prediction as base-line 
number of preds got right / TP + FP

# Recall : truth as base-line 
TP / TP + FN 

# F1 Score: harmonic mean of precision and recall: over all health of our model

# Overfitting 
when a line can be fit better to training data points/datasets but not in testing dataset 
we day that line is overfit

- regularization 
- boosting 
- bagging 

Underfitting: Not enough time / not enough dataset
solution:
increase time 
increase dataset 
pick different model 

Overfitting: The model performs very well on training data, but badly on testing data.
 Causes:
Model is too complex (too many layers/parameters)

Too little training data

Noisy data (contains errors or randomness)

Training for too long

