Python Script that checking NYC 311 API for Street cleaning schedule for one week (+7 days) ahead,
and will send to your Telegram notification if there is a Street Cleaning Suspended, ex.:

["2025-01-01 (Wednesday): SUSPENDED - Alternate side parking and meters are suspended for New Year's Day.",  
 "2025-01-06 (Monday): SUSPENDED - Alternate side parking is suspended for Three Kings' Day. Meters are in effect."]

How to run:  
 1.Create local Python Env: python -m venv tgParkingBotEnv  
 2.Activate it : source /home/user/tgParkingBot/tgParkingBotEnv/bin/activate  
 3.Install pip packages:  pip instal -r requirements.txt  
 4.In same directory create a new '.env' file with your secrets values for NYC 311 and Telegram   
    ( API_KEY from https://api-portal.nyc.gov/ ; BOT_TOKEN and CHAT_ID from  https://core.telegram.org/api )  
 5.Run: python tgParkingBot.py

 can be scheduled to run with crontab ex. every Saturday 7 Pm:

 0 19 * * sat /bin/bash -c 'source /home/user/tgParkingBot/tgParkingBotEnv/bin/activate && python /home/user/tgParkingBot/tgParkingBot.py' >> /var/log/parkingBot.log 2>&1




DOCKER

1.Download docker image locally: docker pull abocman/tg-parking-bot  
2.In same directory create '.env' file with your secrets values of NYC 311 api and Telegram tokens  
3.Run container: docker run --rm --env-file .env abocman/tg-parking-bot  

Or schedule with crontab:  
0 19 * * sat /usr/bin/docker run --rm --env-file .env abocman/tg-parking-bot >> /var/log/parkingBot.log 2>&1

