import time
from iss_tracker import is_iss_overhead, is_night
from notifier import send_email_notification

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        send_email_notification()
