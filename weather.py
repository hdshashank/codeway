import requests
 
print("Welcome to the Weather Forecaster!\n")
print("Just Enter the City you want the weather report for and click on the button! It's that simple!\n")
city_name = input("Enter the name of the City : \n")
 
def Gen_report(C):
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

    try:
        data = requests.get(url)
        T = data.json()
    except:
        T = "Error Occurred"
    print(T)
     
Gen_report(city_name)