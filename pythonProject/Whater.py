from pyowm import OWM


owm = OWM('bea3a86964e0b0e3e38b675d924fa732')
mgr = owm.weather_manager()

plase = input("В якому ти місті?: ")

observation = mgr.weather_at_place(plase)
w = observation.weather
temp = observation.weather.temperature('celsius')['temp']

print("В місті: " + plase + " зараз " + str(w.detailed_status))
print("Температура повітря: " +  str(temp))

if temp < 2:
    print("Необхідно одягатися дуже тепло!")
elif temp < 10:
    print("Радимо одягнути куртку")
else:
    print("Комфортна погода, одягайтеся як бажаєте")














