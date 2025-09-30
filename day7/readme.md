Machine Learning & Deep Learning — Important Terms (Intermediate Level)
🔹 1. Mathematical Foundations (Prerequisites)
# Linear Algebra
Vectors, Matrices, Dot product, Matrix multiplication
Eigenvalues/Eigenvectors, Determinants
# Calculus
Derivatives, Gradients
Partial derivatives, Chain rule (important for backpropagation)
# Probability & Statistics
Probability distributions (Normal, Bernoulli, Binomial, etc.)
Bayes’ Theorem
Expectation, Variance, Covariance

# Optimization
Gradient Descent
Learning Rate, Momentum
Stochastic Gradient Descent (SGD)
Logarithms & Exponentials
Used in log-loss, softmax, exponential functions

🔹 2. Important Functions (Activation Functions)
Sigmoid → squashes values between 0 and 1
Tanh → squashes between -1 and 1
ReLU (Rectified Linear Unit) → f(x) = max(0, x)
Leaky ReLU → avoids "dying ReLU" problem
Softmax → converts raw scores into probabilities (multi-class classification)

🔹 3. Loss Functions
# Regression
Mean Squared Error (MSE)
Mean Absolute Error (MAE)
Huber Loss

# Classification
Binary Cross-Entropy (Log Loss)
Categorical Cross-Entropy
Hinge Loss (SVMs)
Advanced (but good to know)
KL Divergence (in deep learning, probabilistic models)

🔹 4. Regularization Techniques

L1 Regularization (Lasso) → encourages sparsity (feature selection)
L2 Regularization (Ridge) → shrinks weights but keeps all
Elastic Net → mix of L1 + L2
Dropout (Deep Learning) → randomly drops neurons during training
Early Stopping → stop training when validation error stops improving
Batch Normalization → normalizes activations across mini-batches

🔹 5. Ensemble Learning

Bagging (Bootstrap Aggregating)
Train multiple models on random subsets of data
Combine results (e.g., Random Forest)

Boosting
Train models sequentially, each correcting errors of previous
Examples: AdaBoost, Gradient Boosting, XGBoost, LightGBM, CatBoost

Stacking
Combine predictions of multiple models using a meta-model

Voting
Hard voting (majority class) or Soft voting (average probabilities)

🔹 6. Key ML Algorithms

# Linear Models
Linear Regression, Logistic Regression
Tree-based Models
Decision Trees, Random Forests, Gradient Boosted Trees
Support Vector Machines (SVMs)
K-Nearest Neighbors (KNN)
Naïve Bayes

# Clustering
K-Means, Hierarchical Clustering, DBSCAN

# Dimensionality Reduction
PCA, t-SNE, UMAP

🔹 7. Deep Learning Concepts

Neural Networks
Neurons, Layers (Input, Hidden, Output)
Weights, Biases
Forward Propagation, Backpropagation
CNNs (Convolutional Neural Networks)
Convolutions, Filters/Kernels, Pooling
RNNs (Recurrent Neural Networks)
LSTM, GRU (for sequential data)
Transformers (intro level)

# Attention mechanism
Optimization in DL
Adam, RMSProp, SGD with Momentum

🔹 8. Evaluation Metrics

# Regression
R², RMSE, MAE

# Classification
Accuracy, Precision, Recall, F1-score
Confusion Matrix
ROC Curve, AUC

# Clustering
Silhouette Score
Others
Log Loss, Cross-Entropy Loss

🔹 9. Data Preprocessing
Handling missing values
Normalization & Standardization
One-hot encoding (categorical variables)

Feature scaling
Train-test split, Cross-validation
Feature engineering