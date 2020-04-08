n = float(input("Digite o valor de n:"))
p = float(input("Digite o valor de p:"))

def fatorial(x):
  fatorial = 1
  while x >= 1:
      fatorial = fatorial * x
      x = x - 1
  return fatorial


coeficiente = (fatorial(n)/(fatorial(p) * fatorial(n - p)))
print("Coeficiente binomial:", coeficiente)
