from datetime import datetime


def sanitize_dt(dt):
    utc_date = datetime.utcfromtimestamp(dt)
    # formato de la fecha mas humana
    formatted_date = utc_date.strftime("%a %d %b %y")
    return formatted_date


def sanitize_temp(temp):
    return f"{temp} °C"