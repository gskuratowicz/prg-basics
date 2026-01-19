ms_to_kmh = lambda ms : int(ms * 3.6)

speed = 35
result = ms_to_kmh(speed)
print(f"{speed} m/s = {result} km/h")