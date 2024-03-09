#Biểu thức: x**2 - 4*x + 4
x = float(input())
eta=float(input())
step=int(input())
for i in range(1, step+1):
  x_min = x - eta*(2*x-4)
  accuracy = abs(x_min-x)
  if (accuracy < 1e-3):
    print(f"x_min = {x_min}, loss_function = {x_min**2 - 4*x + 4}, after {i} step")
    break
  else:
    x = x_min
    
if (accuracy >= 1e-3):
  print(f"Cannot find x_min after {step} step with learning rate eta = {eta}")