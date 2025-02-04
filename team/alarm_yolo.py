# security_alarm.py
from ultralytics import solutions

def create_security_alarm(model_path, from_email, password, to_email, records=0):
    security_alarm = solutions.SecurityAlarm(
        # show=True,
        model=model_path,
        records=records
    )
    security_alarm.authenticate(from_email, password, to_email)
    return security_alarm

def monitor_security(security_alarm, frame):
    return security_alarm.monitor(frame)
