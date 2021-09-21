#Secure Multiplication, Protocl 4, Fantastic Four without Cheating Identification
	
import random



def JMP(x,p_no):
	if p_no == 1:
		l = [x,hash(x)]
		l = str(l).replace(',','')
		l = l[1:-1]
		f = open("/home/justanotherlad/Desktop/IISc/MP-SPDZ/Player-Data/Input-P0-0", "w")
		f.write(l)
		f.close()
	else:
		l = [x,hash(x)]
		l = str(l).replace(',','')
		l = l[1:-1]
		f = open("/home/justanotherlad/Desktop/IISc/MP-SPDZ/Player-Data/Input-P1-0", "w")
		f.write(l)
		f.close()

	#The rest of the protocl is executed in .mpc program





def INPLocal(x):
	x_1 = 0
	x_2 = 0
	x_3 = 0
	x_4 = x

	return [x_1, x_2, x_3, x_4]





def INP(x,p_no):
	random.seed(10)		#10 is the pre-shared Key here

	x_g = random.random()

	x_i = 0
	x_j = 0
	x_h = x - x_g

	JMP(x_h,p_no)

	return [x_i, x_j, x_g, x_h]









p_no = int(input("Enter your Player-No (1 or 2): "))
response = int(input("Do you want to give the input in the form of no., or as an array of shared input? Select Option 1/Option2: "))
if response ==1:
	X = int(input("Enter input X : "))
	Y = int(input("Enter input Y : "))
	x = INP(X,p_no)		#shared input X
	y = INP(Y,p_no)		#shared input Y
else:
	x = [int(item) for item in input("Enter shared input X : ").split()]
	y = [int(item) for item in input("Enter shared input Y : ").split()]


boo = int(input("Please enter your boolean value: "))

v1 = []
v2 = []

if boo ==0:
	for i in range(1,4):
		v1.append(INP(x[i]*y[0] + x[0]*y[i],p_no))

	for i in range(0,2):
		v2.append(INPLocal(x[i]*y[i]))

else:
	for i in range(1,4):
		for j in range(i+1,4):
			v1.append(INP(x[j]*y[i] + x[i]*y[j],p_no))

	for i in range(2,4):
		v2.append(INPLocal(x[i]*y[i]))



sum1= sum(list(map(sum, v1)))
sum2 = sum(list(map(sum, v2)))
ans  = sum1+sum2
print("Your answer is ",ans)
