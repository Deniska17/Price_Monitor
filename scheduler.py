import schedule,time 
from main import ruleaza

schedule.every().day.at("09:00").do(ruleaza)

while True:
    schedule.run_pending()
    time.sleep(1)