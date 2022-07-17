from datetime import datetime


def tdelta(x):

    todays = datetime.now()
    sourceDate = datetime.strptime(x, '%Y-%m-%dT%H:%M:%SZ')

    delta = todays-sourceDate

    time_in_secs = round(delta.total_seconds())

    hrs, mins, seconds = time_in_secs//3600,time_in_secs//60,time_in_secs

    if hrs > 0:
        out = f'{hrs} hrs ago'
    elif mins > 0:
        out = f'{mins} mins age'
    else:
        out = f'{seconds} secs ago'

    return out