def evaluate(coeffs: list, x: float)->float:
    grad = len(coeffs)

    res = 0
    for i in range(grad):
        res += coeffs[i] * pow(x, grad-i-1)

    return res

def derivative(coeffs: list, x: float)->float:
    grad = len(coeffs)

    res = 0
    for i in range(grad-1):
        res += coeffs[i] * (grad - i - 1) * pow(x, grad-i-2)

    return res
    

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:

    return (derivative(g_coeffs, x) * evaluate(h_coeffs, x) - derivative(h_coeffs, x) * evaluate(g_coeffs,x)) / (evaluate(h_coeffs, x))**2 

