from mypackage import calc_utils 
from mypackage import weather_utils


x = input("num or weather: ")

if x == "num":
    w = input("sq , su: ")
    n = int(input("enter num: "))

    if w == "sq":
        print(calc_utils.sq(n))
    elif w == "cu":
        print(calc_utils.cu(n))
    else:
        print("wrong")

elif x == "weather":

    e = input("today weather or forecast: ")

    if e == "today weather":
        print(weather_utils.today_weather)
    elif e == "forecast":
        print(weather_utils.forecast)
    else:
        print("wrong")
else:
    print("wrong")