import re
from datetime import datetime, date


def name_validator(name, message):
    if isinstance(name, str) and re.match(r"^[a-zA-Z\s]{2,30}$", name):
        return name
    else:
        raise ValueError(message)


def mobile_validator(mobile, message):
    if isinstance(mobile, str) and re.match(r"^\d{11}$", mobile):
        return mobile
    else:
        raise ValueError(message)


def positive_int_validator(int_value, message):
    if isinstance(int_value, int) and int_value >= 0:
        return int_value
    else:
        raise ValueError(message)


def boolean_validator(bool_value, message):
    if isinstance(bool_value, bool):
        return bool_value
    else:
        raise ValueError(message)


def date_validator(date_value, message):
    if isinstance(date_value, date):
        return date_value
    else:
        raise ValueError(message)


def date_time_validator(date_time_value, message):
    if isinstance(date_time_value, datetime):
        return date_time_value
    else:
        raise ValueError(message)

def description_validator(description_value, message):
    if isinstance(description_value, str):
        return description_value
    else:
        raise ValueError(message)