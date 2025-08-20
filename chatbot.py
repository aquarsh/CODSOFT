import datetime
import requests

API_KEY = "a9651ac5273115d369fca93cafdf479e"
API_URL = "http://api.openweathermap.org/data/2.5/weather"

def fetch_weather(location):
    try:
        api_link = f"{API_URL}?q={location}&appid={API_KEY}&units=metric"
        result = requests.get(api_link).json()

        if result.get("cod") != 200:
            return f"Sorry, I couldn't find weather data for '{location}'."

        city_name = result["name"]
        temp_now = result["main"]["temp"]
        feels = result["main"]["feels_like"]
        condition = result["weather"][0]["description"]

        return f"In {city_name}, it's currently {temp_now}°C (feels like {feels}°C) with {condition}."
    
    except:
        return "There was an error for getting the weather. Please try again."

print("Jarvis: Hello Sir! Ready to assist you.")

while True:
    query = input("You: ").lower().strip()
    hour = datetime.datetime.now().hour
     
    if any(word in query for word in ["hello", "hey"]):
        if 5 <= hour < 12:
            print("Jarvis: Good morning! How may I help you today?")
        elif 12 <= hour < 17:
            print("Jarvis: Good afternoon! How can I assist?")
        elif 17 <= hour < 21:
            print("Jarvis: Good evening! How’s your day going?")
        else:
            print("Jarvis: Hello! What can I do for you?")
    elif "namaste" in query:
        print("Jarvis: Namste sir!") 
    elif "greet me" in query or "greetings" in query:
        if 5 <= hour < 12:
            print("Jarvis: Wishing you a great morning, sir!")
        elif 12 <= hour < 17:
            print("Jarvis: Good afternoon, sir!")
        elif 17 <= hour < 21:
            print("Jarvis: Good evening, sir!")
        else:
            print("Jarvis: Good night, sir! Sleep well.")

    elif "weather" in query:
        if "of" in query:
            city = query.split("of")[-1].strip()
            print("Jarvis:", fetch_weather(city))
        else:
            print("Jarvis: Could you tell me which city? For example: 'weather in Delhi'.")

    elif "time" in query:
        print(f"Jarvis: It's {datetime.datetime.now().strftime('%I:%M %p')} right now.")
    elif "date" in query:
        print(f"Jarvis: Today is {datetime.datetime.now().strftime('%B %d, %Y')}.")
    elif "year" in query:
        print(f"Jarvis: The year is {datetime.datetime.now().year}.")
    elif "month" in query:
        print(f"Jarvis: It's {datetime.datetime.now().strftime('%B')}.")
    elif "day" in query:
        print(f"Jarvis: Today is {datetime.datetime.now().strftime('%A')}.")

    elif "your name" in query:
        print("Jarvis: I'm Jarvis, your personal assistant.")
    elif "how are you" in query:
        print("Jarvis: I am good ready, for use! And you?")
    elif "what are you doing"in query:
        print("Jarvis: Staying updated for correct time, date and weather forecast!")
    elif "who made you" in query:
        print("Jarvis: You did, sir.")

    elif "bye" in query:
        if 21 <= hour or hour < 5:
            print("Jarvis: Good night, sir. Take care!")
        else:
            print("Jarvis: Goodbye, sir. Have an amazing day!")
        break
    else:
        print("Jarvis: Sorry, I’m not sure how to respond to that.")
        