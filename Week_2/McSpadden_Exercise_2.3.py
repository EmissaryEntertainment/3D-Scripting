#Use each form of calculation besides modulus
print("2 + 5 = " + str(2+5))
print("2 - 5 = " + str(2-5))
print("2 * 5 = " + str(2*5))
print("2 / 5 = " + str(2/5))
print("2 ** 5 = " + str(2**5))

#Calculation whos resluts depend on order of operations
print("160 + 5 * 7 = " + str(160 + 5 * 7))
#Force change order of operations by using parenthesis
print("(160 + 5) * 7 = " + str((160 + 5) * 7))

#Long decimal result is not what is expected
print("0.1 + 0.2 = " + str(0.1+0.2))
#Find another calculation that results in a long decimal
print("3 * 0.1 = " + str(3*0.1))

#Using integer division to decide which version of python I am using
print("4 / 2 = " + str(4/2) + " Which means I have Python 3")