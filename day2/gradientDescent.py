import numpy as np

def gradient_descent(x, y, iterations, lr):
    # initial values of m and b
    m_curr = 0
    b_curr = 0


    n = len(x)

    for i in range(iterations):
        y_pred = m_curr * x + b_curr

        cost = (1 / n) * np.sum((y - y_pred) ** 2)

        m_der = -(2 / n) * np.sum(x * (y - y_pred))  # partial derivative w.r.t m
        b_der = -(2 / n) * np.sum(y - y_pred)        # partial derivative w.r.t b

        m_curr = m_curr - lr * m_der
        b_curr = b_curr - lr * b_der

        if i % 100 == 0:  # print every 100 iterations
            print(f"Iteration {i}: m = {m_curr:.4f}, b = {b_curr:.4f}, cost = {cost:.4f}")

    return m_curr, b_curr


x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

learning_rate = 0.01
iterations = 10000
m, b = gradient_descent(x, y, iterations, learning_rate)

print(f"\nFinal values: m = {m:.4f}, b = {b:.4f}")


# y = 2x + 3