Python Script that checking NYC 311 API for Street cleaning schedule for one week (+7 days) ahead,
and will send to your Telegram notification if there is a Street Cleaning Suspended, ex.:

["2025-01-01 (Wednesday): SUSPENDED - Alternate side parking and meters are suspended for New Year's Day.",
 "2025-01-06 (Monday): SUSPENDED - Alternate side parking is suspended for Three Kings' Day. Meters are in effect."]

 can be run scheduled to run with crontab ex. every Saturday 7 Pm:

 0 19 * * sat /bin/bash -c 'source /home/user/tgParkingBot/tgParkingBotEnv/bin/activate && python /home/user/tgParkingBot/tgParkingBot.py' >> /var/log/parkingBot.log 2>&1
