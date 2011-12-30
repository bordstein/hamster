def humanize_mins(minutes):
    minutes = int(minutes)
    hours = minutes / 60
    minutes = minutes % 60
    if hours > 0:
        return "%02d:%02d" % (hours, minutes)
    return "%02d" % minutes
