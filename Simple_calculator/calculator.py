def addition(num1,num2):# define a function for addition of two numbers
  return num1 + num2
def subtraction(num1,num2):
  return num1 - num2
def multiplication(num1,num2):
  return num1 * num2
def division(num1,num2): # Define a function for division of two numbers, with error handling for division by zero
  if num2==0:
    return "error: division by zero is not allowed." 
  return num1/num2
def power(num1,num2): 
  return num1 ** num2
def square(num1,num2):
  return num1 ** num2
def cube(num1,num2):
  return num1 ** num2
def square_root(num1,num2):
  return num1 ** (1/num2)
def cube_root(num1,num2):
  return num1 ** (1/num2)
def modulus(num1,num2):
  return num1 % num2
def simple_calculator(): # define a calculator function to execute different operations based on user input
  # Display the calculator interface
  print("my simple calculator")
  print("select operation")
  print("a. addition")
  print("b.subtraction")
  print("c.multiplication")
  print("d.division")
  print("e.power")
  print("f.square")
  print("g.cube")
  print("h.square_root")
  print("i.cube_root")
  print("j.modulus")
  print("k.exit")
  while True:  # Keep running until user chooses to exit
    select = input("enter (a,b,c,d,e,f,g,h,i,j,k):")  #select an operation from the list
    if select in ["a","b","c","d","e","f","g","h","i","j"]:
      num1 = float(input("enter the first number:"))
      num2 = float(input("enter the second number:"))
      if select == "a":## Perform operation based on the user's selection
        print(f":{addition(num1,num2)}") # Call addition function then print the result
      elif select == "b":
        print(f":{subtraction(num1,num2)}")
      elif select == "c":
        print(f":{multiplication(num1,num2)}")
      elif select == "d":
        print(f":{division(num1,num2)}")
      elif select == "e":
        print(f":{power(num1,num2)}")
      elif select == "f":
        print(f":{square(num1,num2)}")
      elif select == "g":
        print(f":{cube(num1,num2)}")
      elif select == "h":
        print(f":{square_root(num1,num2)}")
      elif select == "i":
        print(f":{cube_root(num1,num2)}")
      elif select == "j":
        print(f":{modulus(num1,num2)}")
    else:
        if select == "k":
          print("invalid input, exit")  # If input invalid option, display a message
          break
simple_calculator()