import requests


# importing custom helper functions, text and data
from helper_functions import (ask_city, 
                                ask_hours, 
                                parse_timestamp, 
                                process_passes, 
                                ask_YN, 
                                make_report)
from UK_city_data import dict as cities
from text_bits import *

# for each app session
while True:
    print(f"\n\t{welcome_txt}\n\n{instructions_txt}\n") ### welcome()

    # user input  -> ### ask_inputs()
    city = ask_city(cities)
    hours = ask_hours()

    # preparing for and making request
    latitude, longitude = cities[city]["lat"], cities[city]["lng"] 
    min_elevation = 40
    url = (f"https://api.g7vrd.co.uk/v1/satellite-passes/25544/{latitude}/{longitude}"
           f".json?minelevation={min_elevation}&hours={hours}")

    full_data = requests.get(url).json()

    request_dt = parse_timestamp(full_data['request_timestamp'])
    request_date_time = f"{request_dt['day_long']} at {request_dt['time']}"
    request_date_short = request_dt['day_short']

    # preparing text for beginning of report file -> ### part of make_txt_report()?
    file_txt = (file_title_txt +
                f"\tViewing city: \t\t{city}\n"
                f"\tReport made on: \t{request_date_time}\n"
                f"\tViewing timeframe: \t{hours} hrs\n")

    # extracting and analyzing ISS pass info from response
    all_passes = full_data['passes']
    num_all_passes = len(all_passes)

    # in case there will be no ISS passes within specifications -> ### no_passes()
    if num_all_passes == 0:
        file_txt += zero_passes_txt
        print(zero_passes_txt)
        make_report(city, hours, request_date_short, file_txt, end_txt)
        try_again = ask_YN("Would you like to try again?")
        if try_again:
            continue
        else:
            print("\nGoodbye!")
            break

    # case where there will be at least one pass
    n_passes_txt = f"\n{num_passes_txt} {num_all_passes} \n"
    file_txt += n_passes_txt + "\n"
    print(n_passes_txt)

    # processing all pass data, printing formatted results to console
    # and adding to summarised pass details to string for report file
    file_txt = process_passes(num_all_passes, all_passes, file_txt)

    # creating summary report file for this session
    make_report(city, hours, request_date_short, file_txt, end_txt)

    try_again = ask_YN("Would you like to make another request?")
    if try_again:
        continue
    else:
        print("\nGoodbye!")
        break


# def main():
#     pass


# if __name__ == "__main__":
#     main()