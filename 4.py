#so now writing something new thus bro, let us get started buddy 
# so now nthis is the temperature conversion program thus bro.
#so in this we will also add like lower key coz if dont do so than our program will not worl as lower key is not ther in that bro 
unit = input("enter the unit in celsius or farhenit: ").lower()
temp = float(input("enter the temperature: "))
if unit == "C".lower:
    temp = round(temp * 9) /5 +32
    print(f"the tempertaure in farhenheit is {temp}")
elif unit == "F".lower:
        temp = round(temp -32  ) * 5/9 
        print(f"the temperature in celcisus is {temp} c")
else:
        print("please enter valid dstails only sir")