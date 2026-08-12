# CalC functions

def calc(in1, in2):
   def add(a, b):
      return a + b
   
   def sub(a, b):
      return a - b
   
   def mul(a, b):
      return a * b
   
   def div(a, b):
      return a / b
   
   add = add(in1,in2)
   mul = mul(in1,in2)
   div = div(in1,in2)
   sub = sub(in1,in2)
   
   return f"\naddition: {add}\nMultiple: {mul}\nSubtraction: {sub}\ndivition: {div}"


