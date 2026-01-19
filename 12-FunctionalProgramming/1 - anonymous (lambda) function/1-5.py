def find_average_speed(distance_in_km,hours_travelled,minutes_travelled):
    total_time = hours_travelled + minutes_travelled / 60
    return distance_in_km / total_time

distance_in_km = int(input("Enter distance in km: "))
hours_travelled = int(input("Eneter number of travel hours: "))
minutes_travelled = int(input("Enter number of travel minutes: "))

speed = find_average_speed(distance_in_km,hours_travelled,minutes_travelled)

print(f"Average speed: {round(speed,1)} km/h")