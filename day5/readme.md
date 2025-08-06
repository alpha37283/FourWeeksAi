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


