from datetime import datetime, timedelta

today = datetime.now()
print(f"today : {today.strftime('%d/%m/%Y')}")

meeting_time = today + timedelta(hours=2 , minutes=30)
print(f"Meeting in 2.5 hours: {meeting_time.strftime('%I:%M %p')}")

