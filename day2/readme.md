# Linear regression: 
statistical model, to show relationship between output variable and input variable
fitting a line through given data points so that we can make predications on unknown data
assuming that there is a linear relationship between the variables

y = m x + b
dependant = slope input + intercept(bias)

how do we fit a line ? 

residuals : difference between data point and the line
squared errors : take each of these residuals and square them 
if we total the squared errors it's called SUM OF SQUARE ERRORS/RESIDUALS known as loss function

# Mean Square Error: 
- sum of the square of difference between actual data points and predicted data points and divide them by
number of data points

we have to find such m and b which will reduce this loss function or error 

matrix decomposition, gradient descent etc etc are techniques 

Performance matrics: 
- R square 
- Standard error of estimate
- Prediction interval 
- Statistical significance

------------------------------------------------------------------
Thinks of it like x(input) and y(output) is given and we have to estimate the unknown equation
such that we can give equation some x and it can predict y. 
# Gradient Descent: 

A) cost function w.r.t m  
B) cost function w.r.t b

A 3d plot of cost function, m, and b.

Taking mini steps towards the global minima, for both A and B cases using partial derivatives 
convergence towards global minima. 

Coding steps:
- choose number of iter
- choose lr
In Function 
- choose initial value b_curr and m_curr
- calculate the cost function's value
- formulate the derivative of the cost function w.r.t b
- formulate the derivative of the cost function w.r.t m
- m_curr = m_curr - lr * m_der 
- same for b
- print value at each iter








