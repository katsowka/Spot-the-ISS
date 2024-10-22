from datetime import datetime as dt


def ask_city(city_options):
    # asks for city input until a valid value is provided
    # return city as string
    # valid cities correspond to keys in 'city_options' dictionary
    # (after accounting for letter case and extra white space)
    while True:
        ans = input("Indicate the name of the city: ").strip().capitalize()
        if ans in city_options.keys():
            return ans
        else:
            print("City not found, please try again.")


def ask_hours():
    # asks for hours input until a valid is provided
    # returns number of hours as integer
    while True:
        ans = int(input("Indicate the time frame, in hours: ").strip())
        if 0 < ans <= 72:
            return ans
        else:
            print("Input not clear, please try again and choose from 1 to 72 hours.")


def ask_YN(msg):
    # asks for yes/no input until a clear answer is provided
    # returns choice as boolean
    # 'msg' is string to be printed before the 'Y/N:' input request
    while True:
        print(msg, end=" ")
        ans = input("Y / N : ").upper()
        if ('Y' in ans) and not ('N' in ans):
            return True
        elif ('N' in ans) and not ('Y' in ans):
            return False
        else:
            print("Your response is not clear, try again. ")


def parse_timestamp(time_stamp):
    # parses ISO 8601 timestamp into custom formatted date and time strings
    # returns results in dictionary
    dt_obj = dt.fromisoformat(time_stamp)
    return {'day_long': dt_obj.strftime('%A, %d %B'),
            'day_short': dt_obj.strftime('%d%b'),
            'time': dt_obj.strftime('%H:%M')}


def azimuth_to_dir(az):
    # converts azimuth value into cardinal direction
    # returns cardinal direction as string
    if 22.5 <= az < 67.5:
        return "North-East"
    elif 67.5 <= az < 112.5:
        return "East"
    elif 112.5 <= az < 157.5:
        return "South-East"
    elif 157.5 <= az < 202.5:
        return "South"
    elif 202.5 <= az < 247.5:
        return "South-West"
    elif 247.5 <= az < 292.5:
        return "West"
    elif 292.5 <= az < 337.5:
        return "North-West"
    else:
        return "North"


def process_pass(pass_response):
    # processes ISS pass data as found within API response
    # returns dictionary of custom formatted pass details
    rise = parse_timestamp(pass_response['start'])
    peak = parse_timestamp(pass_response['tca'])
    set = parse_timestamp(pass_response['end'])
    return {"day_long": f"{rise['day_long']}",
            "dir_rise": azimuth_to_dir(pass_response['aos_azimuth']),
            "dir_set": azimuth_to_dir(pass_response['los_azimuth']),
            "time_rise": f"{rise['time']}",
            "time_set": f"{set['time']}",
            "time_peak": f"{peak['time']}",
            "max_elev": str(int(pass_response['max_elevation']))}


def process_passes(num_all_passes, all_passes, file_txt):
    # processes list of ISS pass data as found within API response
    # prints all formatted pass information to console
    # returns string of all pass information to be used in report file
    for x in range(num_all_passes):
        pass_dict = process_pass(all_passes[x])
        day_long = pass_dict["day_long"]
        time_rise = pass_dict["time_rise"]
        dir_rise = pass_dict["dir_rise"]
        time_set = pass_dict["time_set"]
        dir_set = pass_dict["dir_set"]
        time_peak = pass_dict["time_peak"]
        max_elev = pass_dict["max_elev"]
        pass_txt = (f"{'-'*3} Pass {x+1}: {day_long} {'-'*15}\n"
                    f"The ISS will appear from the {dir_rise} at {time_rise}, and set in"
                    f" the {dir_set} at {time_set}. \nIt will peak at {time_peak} with a "
                    f"maximum elevation of {max_elev}\N{DEGREE SIGN}.\n")
        file_txt += pass_txt + "\n"
        print(pass_txt)
    return file_txt


def make_report(city, hours, request_date_short, file_txt, end_txt):
    # creates text file summarizing ISS pass data for
    # requested city and time frame
    file_txt += "\n" + end_txt
    report_file = f"spotISS_{city}_{request_date_short}_{hours}h.txt"
    with open(report_file, 'w') as file:
        file.write(file_txt)
    print(f"See {report_file} for a summary report of this session.\n")


