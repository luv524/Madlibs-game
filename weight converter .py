# now we are creating a weight creator programm thus buddy 
weight = float(input("enter the weight you want us to converte: "))
unit = input("what unit u would like sir k or l: " )
if unit == "k":
    print(round(weight * 2.20462))
elif unit == "l":
    print(round(weight / 2.20462))
else:
    print("please enter something valid only sir")