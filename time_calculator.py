def add_time(current_time_string, time_to_add_string, current_day_name=None):
    result_string = ""

    def convert_time_string_to_minutes_num(time_string):  # rewrite
        result = None
        stringElements = time_string.split(":")
        hours = int(stringElements[0])
        if stringElements[1][-2:] == "PM":
            hours += 12
        minutes = int(stringElements[1][0:2])
        result = hours*60 + minutes
        return result

    def convert_minutes_to_days_hours_minutes(mins_number):
        days = mins_number // (24*60)
        hours = (mins_number - 24*60*days) // 60
        minutes = mins_number % 60
        return [days, hours, minutes]

    def calculate_week_day_name(starting_day_name, days_added_number):
        position_to_dayname = {0: "sunday", 1: "monday", 2: "tuesday",
                               3: "wednesday", 4: "thursday", 5: "friday", 6: "saturday"}
        day_name_to_position = {value: key for key,
                                value in position_to_dayname.items()}
        return position_to_dayname[(day_name_to_position[starting_day_name.lower()]+days_added_number) % 7].capitalize()

    def describe_days_passed(days_passed_number):
        if days_passed_number == 0:
            return ""
        elif days_passed_number == 1:
            return f"(next day)"
        elif days_passed_number > 1:
            return f"({days_passed_number} days later)"
        else:
            raise value_error()

    def convert_military_time_to_12_base_string(hours, minutes):
        if (hours > 23 or hours < 0 or minutes < 0 or minutes > 59):
            raise ValueError()
        result = ""
        minutes_str = str(minutes)
        if minutes < 10:
            minutes_str = minutes_str.rjust(2, "0")

        temp_hours = hours
        designator = ""
        if hours > 12:
            temp_hours = hours-12
        elif hours == 0:
            temp_hours = hours+12
        else:
            temp_hours = hours

        if hours > 11:
            designator = "PM"
        else:
            designator = "AM"

        result = f"{temp_hours}:{minutes_str} {designator}"
        return result

    def format_result_string(days, hours, minutes, day_name=None):
        hours_minutes_formatted = convert_military_time_to_12_base_string(
            hours, minutes)

        day_name_formatted = ""
        if (day_name is not None):
            day_name_formatted = f", {day_name}"

        days_passed_formatted = ""
        if days > 0:
            days_passed_formatted = f" {describe_days_passed(days)}"

        return f"{hours_minutes_formatted}{day_name_formatted}{days_passed_formatted}"

    current_time_in_minutes = convert_time_string_to_minutes_num(
        current_time_string)
    time_to_add_in_minutes = convert_time_string_to_minutes_num(
        time_to_add_string)
    final_time_in_minutes = current_time_in_minutes+time_to_add_in_minutes
    final_time_array = convert_minutes_to_days_hours_minutes(
        final_time_in_minutes)
    result_day_name = None
    if (current_day_name is not None):
        result_day_name = calculate_week_day_name(
            current_day_name, final_time_array[0])

    result_string = format_result_string(
        final_time_array[0], final_time_array[1], final_time_array[2], result_day_name)
    return result_string
