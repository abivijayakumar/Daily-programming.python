x = 5 #global variable
def f1():
  global x
  x = 15
  y = 10
  print("x=%d y=%d"%(x,y))
  f1()
  print(x)
