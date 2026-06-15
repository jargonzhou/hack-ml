"""
This handles the logging of all user interactions with the app. 
Writes descriptive log statements with timestamps to track the user’s actions throughout the app. 
Stores and retrieves application logs locally – and eventually in the cloud
"""


from datetime import datetime
from app.pits.global_settings import LOG_FILE


def log_action(action, action_type):
  timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  log_entry = f"{timestamp}: {action_type} : {action}\n"
  with open(LOG_FILE, 'a') as file:
    file.write(log_entry)


def reset_log():
  with open(LOG_FILE, 'w') as file:
    file.truncate(0)
