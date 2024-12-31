import requests
import asyncio
from datetime import datetime, timedelta
from telegram import Bot


api_key = 'YOUR_311_NYC_API_KEY_HERE'  # https://api-portal.nyc.gov/
today = datetime.now()
one_week_ahed = today + timedelta(days=7)

BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"  # https://core.telegram.org/api
CHAT_ID = "YOUR_TELEGRAM_CHAT_ID_HERE" 


from_date = today.strftime('%Y-%m-%d')
to_date = one_week_ahed.strftime('%Y-%m-%d')


def get_calendar_data(from_date, to_date, api_key):
    api_url = f"https://api.nyc.gov/public/api/GetCalendar?fromDate={from_date}&toDate={to_date}&subscription-key={api_key}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code, response.text


response_data = get_calendar_data(from_date, to_date, api_key)
#print(response_data)


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
print(formated_output)


# Send the message
try:
    bot = Bot(token=BOT_TOKEN)
    asyncio.run(bot.send_message(chat_id=CHAT_ID, text=formated_output))
    print("Message sent successfully!")
except Exception as e:
    print(f"Failed to send message: {e}")
