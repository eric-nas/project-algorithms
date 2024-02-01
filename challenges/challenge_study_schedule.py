def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    saída = 0
    for time in permanence_period:
        if (
            time[0] is None
            or time[1] is None
            or isinstance(time[0], str)
            or isinstance(time[1], str)
        ):
            return None
        if time[0] <= target_time and time[1] >= target_time:
            saída += 1
    return saída
