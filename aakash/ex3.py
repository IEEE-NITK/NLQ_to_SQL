import torch
from scipy import optimize

def costFunction(theta, X, y):
    m =len(y)
    J = (-1/m) * (torch.mm(y.t(),torch.log(torch.sigmoid(torch.mm(X, theta)))) + torch.mm((1-y).t(), torch.log(1 - torch.sigmoid(torch.mm(X, theta)))))
    grad = (1/m) * torch.mm(X.t(), torch.sigmoid(torch.mm(X, theta))-y)
    return (J, grad)

def costFunctionReg(theta, X, y, lam):
    m = len(y)
    t = theta[1:]
    J = costFunction(theta, X, y)[0] + (lam/(2*m)) * sum(t**2).item()
    grad = (1/m) * torch.mm(X.t(),torch.sigmoid(torch.mm(X, theta))-y)
    grad[1:] += (lam/m) * t
    return (J, grad)

def lrCostFunction(theta, X, y, lam):
    m = len(y)
    J = (-1/m) * (torch.mm(y.t(),torch.log(torch.sigmoid(torch.mm(X, theta)))) + torch.mm((1-y).t(), torch.log(1-torch.sigmoid(torch.mm(X, theta))))) + (lamb/(2*m))*sum(theta[1:]**2).item()
    grad = (1/m) * torch.mm(X.t(), torch.sigmoid(torch.mm(X, theta))-y)
    grad[1:] += (lamb/(m)) * theta[1:]
    return (J, grad)

def costForFmin(theta, X, y, lamb):
    theta = torch.from_numpy(theta)
    X = torch.from_numpy(X)
    y = torch.from_numpy(y)
    return lrCostFunction(theta, X, y, lamb)[0].item()

def oneVsAll(X, y, num_labels, lam):
    n = X.size(1) #no of fields
    m = X.size(0) #of of test cases
    X = torch.cat((torch.ones(m,1), X), 1)
    all_theta = torch.empty()
    for i in range(num_labels):
        initial_theta = torch.zeros(n+1,1)
        result = optimize.fmin(costForFmin, x0 = initial_theta.numpy(), args=(X.numpy(), (y==i).numpy(), lamb), maxiter=500, full_output=True)
        theta = torch.from_numpy(result[0])
        all_theta = torch.cat((all_theta, theta.t()),1)
        return all_theta
        
def predict(Theta1, Theta2, X): #neural net of 1 hidden layer
    m = X.size(0)
    num_labels = Theta2.size(0)

    a1 = torch.cat((torch.ones(m,1), X), 1)
    a2 = torch.sigmoid(torch.mm(a1, Theta1.t()))
    a2 = torch.cat((torch.ones(len(a2),1), a2), 1)
    a3 = torch.sigmoid(torch.mm(a2, Theta2.t()))

    return a3.argmax()

def predictOneVsAll(all_theta, X):
    m = X.size(0)
    num_lables = all_theta.size(0)
    X = torch.cat((torch.ones(m,1), X), 1)
    res = torch.mm(X, all_theta.t())
    return res.argmax(0)

