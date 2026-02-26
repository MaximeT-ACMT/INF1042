def can_go_outside(temperature, rain):
    return temperature >= 15 and rain == "no"
temperature = float(input("temperature"))
rain = input("is it raining ? (answer with yes or no)")
if can_go_outside(temperature, rain):
    print("access to go outside")
else: 
    print("stay inside")