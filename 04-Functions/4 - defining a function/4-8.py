
def time_string(hours, minutes, time_format):
    if not 0 <= hours <= 23:
        return "hours must be between 0 and 23"
    if not 0 <= minutes <= 59:
        return "minutes must be between 0 and 59"
    if time_format == '24':
        return f"{hours:02}:{minutes:02}"
    elif time_format == '12':
        if hours ==12 :
            return f"{hours:02}:{minutes:02}pm"
        if hours ==0 :
            return f"{12:02}:{minutes:02}am"
        if hours < 12:
            return f"{hours:02}:{minutes:02}am"
        elif hours > 12:
            return f"{hours - 12:02}:{minutes:02}pm"
    else:
        return "incorrect time format"



print(time_string(15, 38, '24'))
print(time_string(8, 3, '24'))
print(time_string(0, 5, '24'))
print(time_string(11, 15, '12'))
print(time_string(0, 7, '12'))
print(time_string(7, 30, '12'))
print(time_string(12, 46, '12'))
print(time_string(13, 10, '12'))
print(time_string(19, 2, '12'))