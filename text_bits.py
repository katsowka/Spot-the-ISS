# bits of test to be used in the console print statements and within summary report file

welcome_txt = "* WELCOME to Spot the International Space Station! *"

instructions_txt = ("Enter a viewing city (in the UK, population over 50 000) and a time frame (72 hrs max)\n"
                    "and I'll tell you if, when and how you could view the ISS flying above you! Please note that\n"
                    "these passes are predictions, and become less accurate when forecast further into the future.")

zero_passes_txt = (f"\nUnfortunately the ISS will not be viewable from the requested city in the requested timeframe.\n"
                   f"Please choose another city or come back another day.\n")

num_passes_txt = "Number of ISS passes within stated timeframe:"

file_title_txt = f"{' '*10}* Spot the ISS: SUMMARY REPORT *\n\n"

happy_spotting_txt = "* Happy ISS spotting! *"

end_txt = ("Note: ISS data obtained from G7VRD's public satellite pass API, found at\n"
           "https://g7vrd.co.uk/public-satellite-pass-rest-api")