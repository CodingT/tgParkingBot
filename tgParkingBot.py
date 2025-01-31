import os
import requests
import asyncio
from dotenv import load_dotenv
from datetime import datetime, timedelta
from telegram import Bot

# Loading environment variables from .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')  # https://api-portal.nyc.gov/

BOT_TOKEN = os.getenv('BOT_TOKEN')  # https://core.telegram.org/api
CHAT_ID = os.getenv('CHAT_ID') 

today = datetime.now()
one_week_ahead = today + timedelta(days=7)
#print(f"Current date and time: {today}")


from_date = today.strftime('%Y-%m-%d')
to_date = one_week_ahead.strftime('%Y-%m-%d')


def get_calendar_data(from_date, to_date, API_KEY):
    api_url = f"https://api.nyc.gov/public/api/GetCalendar?fromDate={from_date}&toDate={to_date}&subscription-key={API_KEY}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code, response.text


response_data = get_calendar_data(from_date, to_date, API_KEY)
#print(response_data)
#print(f"Type of response_data: {type(response_data)}")


def get_not_in_affect_days(data):
    results = []
    for day in data['days']:
        date = datetime.strptime(day['today_id'], '%Y%m%d')
        day_of_week = date.strftime('%A')
        for item in day['items']:
            if item['type'] == 'Alternate Side Parking' and (item['status'] == 'NOT IN AFFECT' or item['status'] == 'SUSPENDED'):
                results.append(f"{date.strftime('%Y-%m-%d')} ({day_of_week}): {item['status']} - {item['details']}")
    return results


formated_output = get_not_in_affect_days(response_data)
#print(formated_output)
#print(f"Type of formated_output: {type(formated_output)}")

# Send the message if ASP is suspended
if formated_output:
    try:
        bot = Bot(token=BOT_TOKEN)
        asyncio.run(bot.send_message(chat_id=CHAT_ID, text=formated_output))
        print("Message sent successfully!")
    except Exception as e:
        print(f"Failed to send message: {e}")
else:
    print(f"ASP is in Effect the week of {from_date} - no message was sent to Telegram.")
