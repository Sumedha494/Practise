#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

def get_weather(city, api_key):
    """Get current weather for a city"""

    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Celsius
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather(data):
    """Display weather information"""

    if data:
        city = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']

        print("\n" + "=" * 40)
        print(f"🌍 Weather in {city}, {country}")
        print("=" * 40)
        print(f"🌡️  Temperature: {temp}°C")
        print(f"🤔 Feels Like: {feels_like}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"☁️  Condition: {description.title()}")
        print(f"💨 Wind Speed: {wind_speed} m/s")
        print("=" * 40)
    else:
        print("❌ City not found!")

# Main
API_KEY = "your_api_key_here"  # Replace with your API key

city = input("🏙️ Enter city name: ")
weather_data = get_weather(city, API_KEY)
display_weather(weather_data)


# In[ ]:


import requests

def get_weather_icon(condition_id):
    """Return emoji based on weather condition"""

    if condition_id >= 200 and condition_id < 300:
        return "⛈️"   # Thunderstorm
    elif condition_id >= 300 and condition_id < 400:
        return "🌧️"   # Drizzle
    elif condition_id >= 500 and condition_id < 600:
        return "🌧️"   # Rain
    elif condition_id >= 600 and condition_id < 700:
        return "❄️"   # Snow
    elif condition_id >= 700 and condition_id < 800:
        return "🌫️"   # Fog/Mist
    elif condition_id == 800:
        return "☀️"   # Clear
    elif condition_id > 800:
        return "☁️"   # Clouds
    else:
        return "🌤️"

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {e}")
        return None

def display_weather(data):
    if not data:
        print("❌ Could not fetch weather data!")
        return

    # Extract data
    city = data['name']
    country = data['sys']['country']
    temp = data['main']['temp']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    visibility = data.get('visibility', 0) / 1000  # Convert to km
    description = data['weather'][0]['description']
    condition_id = data['weather'][0]['id']
    wind_speed = data['wind']['speed']
    wind_deg = data['wind'].get('deg', 0)
    clouds = data['clouds']['all']

    # Get icon
    icon = get_weather_icon(condition_id)

    # Wind direction
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    wind_dir = directions[int((wind_deg + 22.5) / 45) % 8]

    # Display
    print()
    print("╔" + "═" * 45 + "╗")
    print(f"║  {icon} WEATHER IN {city.upper()}, {country}".ljust(46) + "║")
    print("╠" + "═" * 45 + "╣")
    print(f"║  🌡️  Temperature    : {temp}°C".ljust(46) + "║")
    print(f"║  📊 Min/Max        : {temp_min}°C / {temp_max}°C".ljust(46) + "║")
    print(f"║  🤔 Feels Like     : {feels_like}°C".ljust(46) + "║")
    print(f"║  ☁️  Condition      : {description.title()}".ljust(46) + "║")
    print(f"║  💧 Humidity       : {humidity}%".ljust(46) + "║")
    print(f"║  🔵 Pressure       : {pressure} hPa".ljust(46) + "║")
    print(f"║  👁️  Visibility     : {visibility:.1f} km".ljust(46) + "║")
    print(f"║  💨 Wind           : {wind_speed} m/s {wind_dir}".ljust(46) + "║")
    print(f"║  ☁️  Cloud Cover    : {clouds}%".ljust(46) + "║")
    print("╚" + "═" * 45 + "╝")

# Main
API_KEY = "your_api_key_here"

print("🌤️ WEATHER APP")
print("=" * 30)

city = input("Enter city name: ")
data = get_weather(city, API_KEY)
display_weather(data)


# In[ ]:


import requests
from datetime import datetime

def get_forecast(city, api_key):
    """Get 5-day weather forecast"""

    base_url = "http://api.openweathermap.org/data/2.5/forecast"

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except:
        return None

def get_icon(condition_id):
    if condition_id >= 200 and condition_id < 300:
        return "⛈️"
    elif condition_id >= 300 and condition_id < 600:
        return "🌧️"
    elif condition_id >= 600 and condition_id < 700:
        return "❄️"
    elif condition_id >= 700 and condition_id < 800:
        return "🌫️"
    elif condition_id == 800:
        return "☀️"
    else:
        return "☁️"

def display_forecast(data):
    if not data:
        print("❌ Could not fetch forecast!")
        return

    city = data['city']['name']
    country = data['city']['country']

    print()
    print("╔" + "═" * 55 + "╗")
    print(f"║  📅 5-DAY FORECAST FOR {city.upper()}, {country}".ljust(56) + "║")
    print("╠" + "═" * 55 + "╣")

    # Group by date
    daily_data = {}

    for item in data['list']:
        date = item['dt_txt'].split(' ')[0]

        if date not in daily_data:
            daily_data[date] = {
                'temps': [],
                'conditions': [],
                'icons': []
            }

        daily_data[date]['temps'].append(item['main']['temp'])
        daily_data[date]['conditions'].append(item['weather'][0]['description'])
        daily_data[date]['icons'].append(item['weather'][0]['id'])

    # Display each day
    for date, info in list(daily_data.items())[:5]:
        avg_temp = sum(info['temps']) / len(info['temps'])
        min_temp = min(info['temps'])
        max_temp = max(info['temps'])

        # Most common condition
        condition = max(set(info['conditions']), key=info['conditions'].count)
        icon_id = max(set(info['icons']), key=info['icons'].count)
        icon = get_icon(icon_id)

        # Format date
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        day_name = date_obj.strftime('%A')
        formatted_date = date_obj.strftime('%d %b')

        print(f"║  {icon} {day_name:<10} {formatted_date}  │  {min_temp:.0f}°-{max_temp:.0f}°C  │  {condition.title():<15}".ljust(56) + "║")

    print("╚" + "═" * 55 + "╝")

# Main
API_KEY = "your_api_key_here"

print("📅 5-DAY WEATHER FORECAST")
print("=" * 35)

city = input("Enter city name: ")
forecast_data = get_forecast(city, API_KEY)
display_forecast(forecast_data)


# In[ ]:


import requests

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }

        try:
            response = requests.get(self.base_url, params=params)
            if response.status_code == 200:
                return response.json()
            return None
        except:
            return None

    def get_icon(self, condition_id):
        icons = {
            range(200, 300): "⛈️",
            range(300, 400): "🌧️",
            range(500, 600): "🌧️",
            range(600, 700): "❄️",
            range(700, 800): "🌫️",
            range(800, 801): "☀️",
            range(801, 900): "☁️"
        }

        for r, icon in icons.items():
            if condition_id in r:
                return icon
        return "🌤️"

def compare_cities(api, cities):
    """Compare weather of multiple cities"""

    print()
    print("╔" + "═" * 65 + "╗")
    print("║" + "🌍 WEATHER COMPARISON".center(65) + "║")
    print("╠" + "═" * 65 + "╣")
    print("║" + f"{'City':<15}{'Temp':>8}{'Feels':>8}{'Humidity':>10}{'Condition':<20}".center(65) + "║")
    print("╠" + "═" * 65 + "╣")

    for city in cities:
        data = api.get_weather(city)

        if data:
            name = data['name'][:12]
            temp = f"{data['main']['temp']:.0f}°C"
            feels = f"{data['main']['feels_like']:.0f}°C"
            humidity = f"{data['main']['humidity']}%"
            condition = data['weather'][0]['description'].title()[:18]
            icon = api.get_icon(data['weather'][0]['id'])

            row = f"║  {icon} {name:<12}{temp:>8}{feels:>8}{humidity:>10}  {condition:<18}║"
            print(row)
        else:
            print(f"║  ❌ {city:<12} - Not Found".ljust(65) + "║")

    print("╚" + "═" * 65 + "╝")

# Main
API_KEY = "your_api_key_here"

api = WeatherAPI(API_KEY)

print("🌍 MULTI-CITY WEATHER")
print("=" * 35)
print("Enter city names (comma separated)")
cities_input = input("Cities: ")

cities = [city.strip() for city in cities_input.split(',')]
compare_cities(api, cities)


# In[ ]:


import requests

def get_weather_and_aqi(city, api_key):
    """Get weather and air quality"""

    # Get coordinates first
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct"
    geo_params = {'q': city, 'appid': api_key, 'limit': 1}

    try:
        geo_response = requests.get(geo_url, params=geo_params)
        geo_data = geo_response.json()

        if not geo_data:
            return None, None

        lat = geo_data[0]['lat']
        lon = geo_data[0]['lon']

        # Get weather
        weather_url = "http://api.openweathermap.org/data/2.5/weather"
        weather_params = {
            'lat': lat,
            'lon': lon,
            'appid': api_key,
            'units': 'metric'
        }
        weather_response = requests.get(weather_url, params=weather_params)
        weather_data = weather_response.json()

        # Get air quality
        aqi_url = "http://api.openweathermap.org/data/2.5/air_pollution"
        aqi_params = {
            'lat': lat,
            'lon': lon,
            'appid': api_key
        }
        aqi_response = requests.get(aqi_url, params=aqi_params)
        aqi_data = aqi_response.json()

        return weather_data, aqi_data

    except Exception as e:
        print(f"Error: {e}")
        return None, None

def get_aqi_level(aqi):
    """Get AQI level description"""
    levels = {
        1: ("Good", "🟢"),
        2: ("Fair", "🟡"),
        3: ("Moderate", "🟠"),
        4: ("Poor", "🔴"),
        5: ("Very Poor", "🟣")
    }
    return levels.get(aqi, ("Unknown", "⚪"))

def display_weather_aqi(weather, aqi):
    if not weather:
        print("❌ Could not fetch data!")
        return

    city = weather['name']
    temp = weather['main']['temp']
    humidity = weather['main']['humidity']
    description = weather['weather'][0]['description']

    print()
    print("╔" + "═" * 50 + "╗")
    print(f"║  🌍 WEATHER & AIR QUALITY - {city.upper()}".ljust(51) + "║")
    print("╠" + "═" * 50 + "╣")
    print(f"║  🌡️  Temperature  : {temp}°C".ljust(51) + "║")
    print(f"║  💧 Humidity     : {humidity}%".ljust(51) + "║")
    print(f"║  ☁️  Condition    : {description.title()}".ljust(51) + "║")
    print("╠" + "═" * 50 + "╣")

    if aqi and 'list' in aqi:
        aqi_index = aqi['list'][0]['main']['aqi']
        components = aqi['list'][0]['components']

        level, icon = get_aqi_level(aqi_index)

        print(f"║  {icon} Air Quality  : {level} (Index: {aqi_index})".ljust(51) + "║")
        print("╠" + "═" * 50 + "╣")
        print("║  📊 POLLUTANTS:".ljust(51) + "║")
        print(f"║     PM2.5  : {components['pm2_5']:.1f} μg/m³".ljust(51) + "║")
        print(f"║     PM10   : {components['pm10']:.1f} μg/m³".ljust(51) + "║")
        print(f"║     NO2    : {components['no2']:.1f} μg/m³".ljust(51) + "║")
        print(f"║     O3     : {components['o3']:.1f} μg/m³".ljust(51) + "║")
        print(f"║     CO     : {components['co']:.1f} μg/m³".ljust(51) + "║")

    print("╚" + "═" * 50 + "╝")

# Main
API_KEY = "your_api_key_here"

print("🌍 WEATHER & AIR QUALITY APP")
print("=" * 35)

city = input("Enter city name: ")
weather, aqi = get_weather_and_aqi(city, API_KEY)
display_weather_aqi(weather, aqi)


# In[ ]:


import requests
from datetime import datetime
import time

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5"
        self.favorites = []
        self.history = []

    def get_weather(self, city):
        """Get current weather"""
        url = f"{self.base_url}/weather"
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }

        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                return response.json()
            return None
        except:
            return None

    def get_forecast(self, city):
        """Get 5-day forecast"""
        url = f"{self.base_url}/forecast"
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }

        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                return response.json()
            return None
        except:
            return None

    def get_icon(self, condition_id):
        """Get weather emoji"""
        if condition_id >= 200 and condition_id < 300:
            return "⛈️"
        elif condition_id >= 300 and condition_id < 600:
            return "🌧️"
        elif condition_id >= 600 and condition_id < 700:
            return "❄️"
        elif condition_id >= 700 and condition_id < 800:
            return "🌫️"
        elif condition_id == 800:
            return "☀️"
        else:
            return "☁️"

    def display_current(self, data):
        """Display current weather"""
        if not data:
            print("❌ City not found!")
            return

        city = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        feels = data['main']['feels_like']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        visibility = data.get('visibility', 0) / 1000
        description = data['weather'][0]['description']
        condition_id = data['weather'][0]['id']
        wind_speed = data['wind']['speed']
        wind_deg = data['wind'].get('deg', 0)
        clouds = data['clouds']['all']

        # Sunrise/Sunset
        sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M')
        sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M')

        icon = self.get_icon(condition_id)

        # Wind direction
        directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
        wind_dir = directions[int((wind_deg + 22.5) / 45) % 8]

        print()
        print("╔" + "═" * 50 + "╗")
        print(f"║  {icon} CURRENT WEATHER - {city.upper()}, {country}".ljust(51) + "║")
        print(f"║  📅 {datetime.now().strftime('%A, %d %B %Y %H:%M')}".ljust(51) + "║")
        print("╠" + "═" * 50 + "╣")
        print(f"║  🌡️  Temperature    : {temp:.1f}°C".ljust(51) + "║")
        print(f"║  📊 Min/Max        : {temp_min:.1f}°C / {temp_max:.1f}°C".ljust(51) + "║")
        print(f"║  🤔 Feels Like     : {feels:.1f}°C".ljust(51) + "║")
        print(f"║  ☁️  Condition      : {description.title()}".ljust(51) + "║")
        print("╠" + "═" * 50 + "╣")
        print(f"║  💧 Humidity       : {humidity}%".ljust(51) + "║")
        print(f"║  🔵 Pressure       : {pressure} hPa".ljust(51) + "║")
        print(f"║  👁️  Visibility     : {visibility:.1f} km".ljust(51) + "║")
        print(f"║  💨 Wind           : {wind_speed} m/s {wind_dir}".ljust(51) + "║")
        print(f"║  ☁️  Cloud Cover    : {clouds}%".ljust(51) + "║")
        print("╠" + "═" * 50 + "╣")
        print(f"║  🌅 Sunrise        : {sunrise}".ljust(51) + "║")
        print(f"║  🌇 Sunset         : {sunset}".ljust(51) + "║")
        print("╚" + "═" * 50 + "╝")

        # Add to history
        self.history.append({
            'city': city,
            'time': datetime.now().strftime('%H:%M'),
            'temp': temp
        })

    def display_forecast(self, data):
        """Display 5-day forecast"""
        if not data:
            print("❌ Could not fetch forecast!")
            return

        city = data['city']['name']
        country = data['city']['country']

        print()
        print("╔" + "═" * 60 + "╗")
        print(f"║  📅 5-DAY FORECAST - {city.upper()}, {country}".ljust(61) + "║")
        print("╠" + "═" * 60 + "╣")

        # Group by date
        daily = {}
        for item in data['list']:
            date = item['dt_txt'].split(' ')[0]
            if date not in daily:
                daily[date] = {'temps': [], 'conditions': [], 'ids': []}
            daily[date]['temps'].append(item['main']['temp'])
            daily[date]['conditions'].append(item['weather'][0]['description'])
            daily[date]['ids'].append(item['weather'][0]['id'])

        for date, info in list(daily.items())[:5]:
            min_t = min(info['temps'])
            max_t = max(info['temps'])
            condition = max(set(info['conditions']), key=info['conditions'].count)
            icon_id = max(set(info['ids']), key=info['ids'].count)
            icon = self.get_icon(icon_id)

            date_obj = datetime.strptime(date, '%Y-%m-%d')
            day = date_obj.strftime('%A')[:3]
            fmt_date = date_obj.strftime('%d %b')

            line = f"║  {icon} {day} {fmt_date}  │  🌡️ {min_t:.0f}° - {max_t:.0f}°C  │  {condition.title()[:20]}"
            print(line.ljust(61) + "║")

        print("╚" + "═" * 60 + "╝")

    def add_favorite(self, city):
        """Add city to favorites"""
        data = self.get_weather(city)
        if data:
            city_name = data['name']
            if city_name not in self.favorites:
                self.favorites.append(city_name)
                print(f"✅ {city_name} added to favorites!")
            else:
                print(f"ℹ️ {city_name} already in favorites!")
        else:
            print("❌ City not found!")

    def show_favorites(self):
        """Show favorite cities weather"""
        if not self.favorites:
            print("📭 No favorite cities yet!")
            return

        print()
        print("╔" + "═" * 55 + "╗")
        print("║" + "⭐ FAVORITE CITIES".center(55) + "║")
        print("╠" + "═" * 55 + "╣")

        for city in self.favorites:
            data = self.get_weather(city)
            if data:
                temp = data['main']['temp']
                desc = data['weather'][0]['description'].title()[:15]
                icon = self.get_icon(data['weather'][0]['id'])

                print(f"║  {icon} {city:<15} │ {temp:.1f}°C │ {desc:<15}".ljust(56) + "║")

        print("╚" + "═" * 55 + "╝")

    def show_history(self):
        """Show search history"""
        if not self.history:
            print("📭 No search history yet!")
            return

        print()
        print("╔" + "═" * 40 + "╗")
        print("║" + "📜 SEARCH HISTORY".center(40) + "║")
        print("╠" + "═" * 40 + "╣")

        for entry in self.history[-10:]:  # Last 10 searches
            print(f"║  🕐 {entry['time']} │ {entry['city']:<15} │ {entry['temp']:.1f}°C".ljust(41) + "║")

        print("╚" + "═" * 40 + "╝")

    def show_menu(self):
        """Display main menu"""
        print()
        print("╔" + "═" * 35 + "╗")
        print("║" + "🌤️ WEATHER APP".center(35) + "║")
        print("╠" + "═" * 35 + "╣")
        print("║  1. 🔍 Current Weather           ║")
        print("║  2. 📅 5-Day Forecast            ║")
        print("║  3. 🌍 Compare Cities            ║")
        print("║  4. ⭐ Add to Favorites          ║")
        print("║  5. 📋 View Favorites            ║")
        print("║  6. 📜 Search History            ║")
        print("║  7. ⚙️  Settings                  ║")
        print("║  8. 🚪 Exit                      ║")
        print("╚" + "═" * 35 + "╝")

        return input("\n👉 Choice (1-8): ")

    def 


# In[ ]:


import random

def demo_weather_app():
    """Demo version without API"""

    # Sample data
    cities_data = {
        'delhi': {'temp': 32, 'humidity': 45, 'condition': 'Clear Sky', 'icon': '☀️'},
        'mumbai': {'temp': 30, 'humidity': 75, 'condition': 'Partly Cloudy', 'icon': '⛅'},
        'bangalore': {'temp': 24, 'humidity': 65, 'condition': 'Light Rain', 'icon': '🌧️'},
        'chennai': {'temp': 33, 'humidity': 70, 'condition': 'Humid', 'icon': '☀️'},
        'kolkata': {'temp': 29, 'humidity': 80, 'condition': 'Overcast', 'icon': '☁️'},
        'jaipur': {'temp': 35, 'humidity': 30, 'condition': 'Hot & Dry', 'icon': '🔥'},
        'pune': {'temp': 26, 'humidity': 55, 'condition': 'Pleasant', 'icon': '🌤️'},
        'hyderabad': {'temp': 31, 'humidity': 50, 'condition': 'Warm', 'icon': '☀️'},
    }

    print("🌤️ WEATHER APP (Demo Mode)")
    print("=" * 40)
    print("Available cities:", ", ".join(cities_data.keys()))

    while True:
        print("\n📋 MENU")
        print("1. Get Weather")
        print("2. Compare Cities")
        print("3. Exit")

        choice = input("\nChoice: ")

        if choice == '1':
            city = input("Enter city: ").lower()

            if city in cities_data:
                data = cities_data[city]

                # Add some randomness
                temp = data['temp'] + random.randint(-2, 2)

                print()
                print("╔" + "═" * 40 + "╗")
                print(f"║  {data['icon']} Weather in {city.title()}".ljust(41) + "║")
                print("╠" + "═" * 40 + "╣")
                print(f"║  🌡️  Temperature : {temp}°C".ljust(41) + "║")
                print(f"║  💧 Humidity    : {data['humidity']}%".ljust(41) + "║")
                print(f"║  ☁️  Condition   : {data['condition']}".ljust(41) + "║")
                print("╚" + "═" * 40 + "╝")
            else:
                print("❌ City not found! Try from available cities.")

        elif choice == '2':
            print()
            print("╔" + "═" * 55 + "╗")
            print("║" + "🌍 ALL CITIES WEATHER".center(55) + "║")
            print("╠" + "═" * 55 + "╣")

            for city, data in cities_data.items():
                temp = data['temp'] + random.randint(-2, 2)
                print(f"║  {data['icon']} {city.title():<12} │ {temp}°C │ {data['condition']:<15}".ljust(56) + "║")

            print("╚" + "═" * 55 + "╝")

        elif choice == '3':
            print("👋 Goodbye!")
            break

# Run demo
demo_weather_app()


# In[ ]:




