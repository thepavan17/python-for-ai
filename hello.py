print("Hello, World!")

size = 42
slim = size>=40
if slim:
    print("slim")
else:
    print("not slim")
   40//2 
    40/2
    messy =  " hello world.  "
    print(messy.strip())

sana = "      always shouts on me.  "
print(sana.strip())

money = 1000
if money > 1000:
    print("u can buy snacks")
elif money < 1000:
    print("u cannot buy snacks")
elif money == 1000:
    print("u can buy snacks")

name = "pavan"
print(name.upper())
print(name.lower())
print(f"{name} is a good boy")
print(name.replace("p", "P"))
for i in range(10):
    print(i)
for i in range(3, 9, 24):
    print(i)
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list)
my_list.remove(3)
print(my_list)
our_list = [sana, "pavan", 32, "x", 5]
print(our_list[3])
our_list.append("new item")
our_list.remove("x")
our_list.insert(2, "inserted item")
print(our_list)
my_dict = {"name": "pavan", "age": 32, "city": "hyderabad"}
print(my_dict["name"])  
print(my_dict.get("age"))
print(my_dict.get("city"))
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
sana = {"name": "sana", "age": 30, "city": "bangalore"}
pavan = {"name": "pavan", "age": 32, "city": "hyderabad"}
amith = {"name": "amith", "age": 28, "city": "chennai"}
people = [sana, pavan, amith]
for person in people:
    print(person["name"])
    print(person["age"])
    print(person["city"])
def greet(name):
    print(f"Hello, {name}!")
    print(f"Welcome to the program, {name}!")
    print(f"Have a great day, {name}!")
greet("pavan")  
greet("sana")


def sana_emotion(sana_cat: int) -> int:
    if sana_cat == 1:
        print("sana is happy")
    elif sana_cat == 2:
        print("sana is sad")
    elif sana_cat == 3:
        print("sana is angry")
        sana_cat = 1
    else:
        print("sana has an unknown emotion")
    return sana_cat

sana_cat = 0
sana_cat = sana_emotion(sana_cat)
print("new sana_cat:", sana_cat)

def weather(temperature):
    if temperature > 30:
        print("It's hot outside.")
    elif temperature < 10:
        print("It's cold outside.") 
        temperature = 20
    else:
        print("The weather is moderate.")   

weather(35)

import math
print(math.sqrt(32))
print(math.pow(2, 3))
from math import sqrt, pow
print(sqrt(16))

import random
print(random.randint(1, 10))
print(random.choice(["apple", "banana", "cherry"]))

import datetime
now = datetime.datetime.now()
print("Current date and time:", now)

import os
print("Current working directory:", os.getcwd())

import requests

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

print(data)

import requests

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']

# Get temperature for different cities
paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)

print(f"Paris: {paris_temp}°C")
print(f"London: {london_temp}°C")
print(f"Tokyo: {tokyo_temp}°C")

import requests
from datetime import datetime, timedelta

# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Get Paris weather for past week
url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
print(data)
#---------------------------------------------
import pandas as pd

# Extract the daily data
daily_data = data['daily']

# Create a DataFrame
df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})

# Convert date strings to datetime
df['date'] = pd.to_datetime(df['date'])

print(df)
#---------------------------------------------
import matplotlib.pyplot as plt

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Paris Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('weather_chart.png')
plt.show()
#---------------------------------------------
import os

# Create data folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Save to CSV
df.to_csv('data/paris_weather.csv', index=False)
print("Data saved to data/paris_weather.csv")

#---------------------------------------------

class Person:
    def __init__(self, name, age): # Dunder method to initialize the object
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")  
lets = Person("Alice", 30)
lets.greet()
#---------------------------------------------
class APIConfig:
    def __init__(self, api_key, model="gpt-5.5-turbo", max_tokens=100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1"

# Create different configurations
# Using positional for required arg, named for optional
dev_config = APIConfig("sk-dev-key", max_tokens=50)

# Using all named arguments (clearest)
prod_config = APIConfig(api_key="sk-prod-key", model="gpt-4", max_tokens=1000)

# Access the configuration
print(dev_config.model)        # gpt-5.5-turbo
print(prod_config.model)       # gpt-4
print(prod_config.max_tokens)  # 1000













