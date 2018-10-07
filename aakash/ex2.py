import torch

def costFunction(theta, X, y):
    m = len(y)
    grad = torch.zeros(len(theta))
    J = (-1/m)*torch.mm(y.t(), torch.sigmoid(torch.mm(X, theta))) + torch.mm((1-y).t(), torch.log(1-torch.sigmoid(torch.mm(X, theta))))
    grad = (1/m) * torch.mm(X.t(), torch.sigmoid(torch.mm(X, theta)-y))
    return (J, grad)

def costFunctionReg(theta, X, y, lam):
    m = len(y)
    t = theta[1:]
    J = costFunction(theta, X, y)[0] + (lam/(2*m)) * sum(t**2).item()
    grad = (1/m) * torch.mm(X.t(), torch.sigmoid(torch.mm(X, theta)-y))
    grad[1:] += (1/m) * lam * t
    return (J, grad)

def predict(theta, X):
    m = X.size(0) #no of training examples
    p = (torch.sigmoid(torch.mm(X, theta)) >= 0.5)
    return p

