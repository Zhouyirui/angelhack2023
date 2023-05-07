final_time = 1234
def calculate_dist(speed, time, rest):
    rounds = final_time // (time + rest)
    remainder = final_time % (time + rest)
    distance = rounds * speed * time
    distance += min(remainder, time) * speed
    print(distance)

calculate_dist(5, 9, 18)

"""
John = 2880
James = 2432
Jenna = 3540
Josh = 2037
Jacob = 1260
Jerry = 2070
"""