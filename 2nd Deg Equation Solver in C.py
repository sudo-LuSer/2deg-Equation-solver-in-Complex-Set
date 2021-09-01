import math
import numpy
def Delta_helper(a,b,c):
	return (b**2 - (4*a*c))
def SolveTheEquationInR(a,b,c):
	delta = Delta_helper(a,b,c)
	if(delta>0):
		x_1 = (-b - numpy.sqrt(delta))/(2*a)
		x_2 = (-b + numpy.sqrt(delta))/(2*a)
		return x_1,x_2
	elif(delta==0):
		x=(-b/2*a)
		return x
def SolveTheEquationInC(a,b,c):
	delta=str(Delta_helper(a,b,c))
	a_2=str(2*a)
	b_=str(-b)
	x_1=str('('+b_ + '- i*sqrt('+delta+'))/'+a_2)
	x_2=str('('+b_ + '+ i*sqrt('+delta+'))/'+a_2)
	return x_1,x_2
def main():
	print ('-'*150)
	print ("\t"*5 + "2DEG EQUATION SOLVER IN COMPLEX SET (a(z^2) + bz + c = 0)" + "\t"*5)
	print ('-'*150)
def input_and_solve():
	try:
		a=input ("\t" + "Enter the constant a please :")
		b=input ("\t" + "Enter the constant b please :")
		c=input ("\t" + "Enter the constant c please :")
	except ValueError:
		print("Enter intgers please ! and (a doesn't equal to 0) !")
		input_and_solve()
	except ZeroDivisionError:
		print("a should be inequal to 0 please !")
		input_and_solve()
	if(Delta_helper(a,b,c)>=0):
		if(Delta_helper(a,b,c)==0):
			solution = str(SolveTheEquationInR(a,b,c))
			print(str("the solution of your equation is z = " + solution ))
		else:
			solution = str(SolveTheEquationInR(a,b,c))
			print(str("the group of solution for your equation is :" + solution ))
	else:
		solution = str(SolveTheEquationInC(a,b,c))
		print(str("the group of solution for your equation is :" + solution ))
while True:
	print("\n\n")
	choice=int(input("1-Equation solver :\n2-Exit :\nEnter a choice :"))
	if(choice==2):
		exit()
	print("\n\n")
	main()
	print("\n\n")
	input_and_solve()