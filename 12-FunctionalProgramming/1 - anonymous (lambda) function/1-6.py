avg_speed = lambda distance_in_km, hours_travelled, minutes_travelled : distance_in_km / (hours_travelled + (minutes_travelled/60))

distance_in_km = int(input("Enter distance in km: "))
hours_travelled = int(input("Eneter number of travel hours: "))
minutes_travelled = int(input("Enter number of travel minutes: "))

speed = avg_speed(70,1,23)
print(f"Average speed: {round(speed,1)} km/h")
