import datetime
from os import environ

# hour=24, minute=0 would result in 12:00:00 AM
# hour=10, minute=10 would result in 10:10:00 AM
# hour=12, minute=30, second=50 would result in 12:30:50 PM

hour = int(environ['BOT_HOUR'])
minute = int(environ['BOT_MINUTE'])
second = int(environ['BOT_SECOND'])
TASK_DATE = datetime.time(hour=hour, minute=minute, second=second) # Timezone is UTC
DAY = environ['BOT_DAY'] # Set this to whatever day you want it to run, Monday, Tuesday, etc...
NOTIFY_CHANNEL = int(environ['BOT_CHANNEL']) # The ID of the channel you want the message to be sent to
DATABASE = environ['PG_CONNECT_STRING'] # "postgresql://user:password@host/database" # PostgreSQL database connection URL
BOT_TOKEN = environ['BOT_TOKEN'] # Your bot's token
