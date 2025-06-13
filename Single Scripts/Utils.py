from datetime import datetime as dt

def format_date(dt_, fmt="%m/%d/%Y, %H:%M:%S"):
    return f"{dt_:{fmt}}"

def now(fmt="%m/%d/%Y, %H:%M:%S"):
    return format_date(dt.now(), fmt)