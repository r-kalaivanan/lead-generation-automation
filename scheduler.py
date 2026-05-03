import schedule
import time
from main import main 

def job():
    print("Running scheduled lead generation...")
    main()

schedule.every().day.at("10:00").do(job)

print("📅 Scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(1)