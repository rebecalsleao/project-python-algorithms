def study_schedule(permanence_period, target_time):
    score = 0

    for period in permanence_period:
        arrival_time = period[0]
        departure_time = period[1]
        arrival_time_inv = type(arrival_time) != int
        departure_time_inv = type(departure_time) != int
        target_time_inv = type(target_time) != int

        if arrival_time_inv or departure_time_inv or target_time_inv:
            return None

        arrived_before_or_on_time = arrival_time <= target_time
        left_after_or_on_time = departure_time >= target_time

        if arrived_before_or_on_time and left_after_or_on_time:
            score += 1

    return score
