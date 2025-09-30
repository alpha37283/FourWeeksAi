# Loss and Activation Functions Guide

This document summarizes the most important loss functions and activation functions, and when to use them based on the type of machine learning problem.

# Common Loss Functions and Their Usages

## For Regression

1. Mean Squared Error (MSE)
   L = (1/n) * Σ (y - y_hat)^2

   * Penalizes large errors more strongly
   * Use when outputs are continuous (e.g., house price prediction, stock values)

2. Mean Absolute Error (MAE)
   L = (1/n) * Σ |y - y_hat|

   * More robust to outliers than MSE
   * Use when you care about absolute differences

3. Huber Loss
   L = 0.5 * (y - y_hat)^2, if |y - y_hat| <= δ
   L = δ * |y - y_hat| - 0.5 * δ^2, otherwise

   * Combines MSE and MAE (quadratic for small errors, linear for large ones)
   * Use when you want robustness against outliers with smooth optimization

## For Binary Classification

1. Binary Crossentropy (Log Loss)
   L = - [ y*log(y_hat) + (1-y)*log(1-y_hat) ]

   * Used when output is probability of two classes
   * Example: spam detection, pass/fail prediction

## For Multiclass Classification

1. Categorical Crossentropy
   L = - Σ (y_i * log(y_hat_i))

   * True labels are one-hot encoded (e.g., [0,0,1,0])
   * Example: digit classification (0–9)

2. Sparse Categorical Crossentropy

   * Same as categorical crossentropy, but labels are integers (not one-hot)
   * Example: MNIST dataset (labels 0–9)

## For Imbalanced Problems

1. Weighted Crossentropy / Focal Loss

   * Assigns more weight to minority or hard-to-classify examples
   * Example: medical diagnosis where positive cases are rare but important

# Common Activation Functions and Their Usages

## Hidden Layers

1. ReLU (Rectified Linear Unit)
   f(x) = max(0, x)

   * Most common for hidden layers
   * Efficient and avoids vanishing gradients
   * Can suffer from “dead neurons”

2. Leaky ReLU / Parametric ReLU
   f(x) = max(αx, x)

   * Fixes dead neuron problem by allowing small negative slope

3. ELU / SELU

   * Variants of ReLU that improve stability in deeper networks

## Output Layers

1. Sigmoid
   f(x) = 1 / (1 + e^(-x))

   * Outputs probability between 0 and 1
   * Used in binary classification

2. Softmax
   f(z_i) = e^(z_i) / Σ e^(z_j)

   * Produces probability distribution across multiple classes
   * Used in multiclass classification

3. Linear (Identity)
   f(x) = x

   * No activation
   * Used in regression for continuous outputs

# Problem-to-Loss-and-Activation Mapping

| Problem Type                  | Output Activation                          | Loss Function                                 |
| ----------------------------- | ------------------------------------------ | --------------------------------------------- |
| Binary classification         | Sigmoid                                    | Binary Crossentropy                           |
| Multiclass classification     | Softmax                                    | Categorical / Sparse Categorical Crossentropy |
| Regression (real values)      | Linear                                     | MSE / MAE / Huber                             |
| Imbalanced classification     | Sigmoid / Softmax                          | Weighted BCE / Focal Loss                     |
| Autoencoders (reconstruction) | Sigmoid (if 0–1) / Linear (if real values) | MSE / BCE depending on data                   |

# Quick Intuition

* Use Linear + MSE/MAE for regression
* Use Sigmoid + BCE for binary classification
* Use Softmax + Categorical Crossentropy for multiclass classification
* Use ReLU (or variants) for hidden layers
