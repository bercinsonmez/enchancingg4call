# Body-Mass Index Calculator
height = float(input("Please enter your height in cm: "))
weight = float(input("Please enter your weight in kg: "))
BMI = round(weight / (height/100)**2,2) #round ve ,2 diyerek de virgülden sonra basamak ayarlayabilirsin
print("Your BMI is",format(BMI, ".2f")) #ya da format .2f ile de yapabilirsin
if ( BMI < 16):
   print("severely underweight")

elif ( BMI >= 16 and BMI < 18.5):
   print("underweight")

elif ( BMI >= 18.5 and BMI < 25):
   print("Healthy")

elif ( BMI >= 25 and BMI < 30):
   print("overweight")

elif ( BMI >=30):
   print("severely overweight")

#Here we have used elif (else if) because once we satisfy a condition we don’t want to check the rest of the statements.
