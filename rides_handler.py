import datetime

import place_handler


def create_ride(ride_data):
    try:
        seats = int(ride_data[-1])
    except ValueError:
        print("Invalid seat input, must be numbers!")
        return

    if __verify_date(ride_data[-2]) is None:
        return

    from_city = place_handler.match_city(ride_data[0])
    to_city = place_handler.match_city(ride_data[1])

    if from_city is None:
        print("Could not find destination {}".format(ride_data[0]))
    if to_city is None:
        print("Could not find destination {}".format(ride_data[1]))
    elif seats > 10:
        print("Seats are limited to a maximum of 10, please try again.")
    else:
        ride_data[0] = from_city
        ride_data[1] = to_city
        return ride_data
    return None


def __verify_date(date):
    try:
        year, month, day = date.split("-")
        valid_date = datetime.date(int(year), int(month), int(day))
        return valid_date
    except ValueError:
        print("Incorrect date: {}! Please follow template YYYY-MM-DD".format(date))
        return None
    except:
        print("Your date is incorrect! Please try again and follow the template YYYY-MM-DD")
        return None
