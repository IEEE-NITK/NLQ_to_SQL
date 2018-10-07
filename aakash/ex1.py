import torch
def computeCost(X, y, theta):
    m = len(y)
    J = (0.5/m) * sum((torch.matmul(X,theta) - y)**2).item()
    return J
def computeCostMulti(X, y, theta):
    m = len(y)
    J = (0.5/m) * sum((torch.matmul(X, theta) - y)**2).item()
    return J

def featureNormalize(X):
    X = X.float()
    sigma = X.std(dim=0)
    mu = X.mean(dim=0)
    X_norm = (X-mu)/sigma
    return (X_norm, mu, sigma)

def gradientDescent(X, y, theta, alpha, num_iters):
    m = len(y)
    J_history = torch.zeros(num_iters,1)
    for iter in range(num_iters):
        theta = theta - (alpha/m) * tensor.mm(X.t(), torch.mm(X,theta)-y)
        J_history[iter] = computeCost(X, y, theta)
    return (theta, J_history)

def gradientDescentMulti(X, y, theta, alpha, num_iters):
    m = len(y)
    J_history = torch.zeros(num_iters, 1)
    for iter in range(num_iters):
        theta = theta - (alpha/m) * torch.mm(X.t(),torch.mm(X, theta)-y)
        J_history[iter] = computeCostMulti(X, y, theta)
    return (theta, J_history)

def normalEqn(X, y):
    theta = torch.mm(torch.mm(X.inverse(), X), torch.mm(X.inverse(), y))
    return theta

