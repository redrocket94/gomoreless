import datetime

import csv_handler
import rides_handler


def input_prompt():
    user_input = input("Please input your command: ").split(" ")
    cmd = user_input[0].upper()
    del user_input[0]

    if cmd == "C":
        if not has_minimum_input(user_input, 4,
                                 " If you have a city name with a space in the name e.g São Paulo, replace with "
                                 "a dash like so: São-Paulo and try again!"):
            return  # restart process if user did not input sufficient data

        setup_ride(user_input)

    elif cmd == "R":
        last_ride = csv_handler.get_last_created_ride_from_csv()
        if last_ride is None:
            print("There are no rides to create a return from!")
            return
        else:
            if len(user_input) > 1 or user_input == []:
                print("Incorrect input, please follow the templare R [date] (without square brackets)")
                return

            if is_compatible_return_date(last_ride[2], user_input[0]):
                last_ride[2] = user_input[0]  # replace date in last created ride with new date input
                last_ride[0], last_ride[1] = last_ride[1], last_ride[0]  # swap destinations
                setup_ride(last_ride)

    elif cmd == "S":
        if has_minimum_input(user_input, 5, " Note you have to write 'none' if you have no data for a given input!"):
            csv_handler.find_ride(user_input[0], user_input[1], user_input[2], user_input[3], user_input[4])

    else:
        print("Your input was invalid!")


def has_minimum_input(user_input, minimum_num, extra_msg=""):
    if len(user_input) < minimum_num:
        print("Your input lacked sufficient data, please try again!{}".format(extra_msg))
        return False
    elif len(user_input) > minimum_num:
        print("You have too many inputs!{}".format(extra_msg))
        return False
    else:
        return True


def ride_verified_by_user(ride_data):
    is_confirmed = False
    user_input = input("You are about to create a ride with this data:\n"
                       "From City: {}\n"
                       "To City: {}\n"
                       "Date: {}\n"
                       "Seats: {}\n"
                       "Input 'Y' to confirm this, input 'N' to cancel: ".format(ride_data[0], ride_data[1],
                                                                                 ride_data[2], ride_data[3])).upper()
    while is_confirmed is False:
        if user_input == "Y":
            return True
        elif user_input == "N":
            return False
        else:
            user_input = input(
                "Invalid input, please input either 'Y' to confirm or 'N' to cancel (no apostrophes): ").upper()


def setup_ride(user_input):
    ride_createable = rides_handler.create_ride(user_input)

    if ride_createable is not None:
        if not ride_verified_by_user(user_input):
            print("Ride was cancelled!")
            return
        csv_handler.write_created_ride_to_csv(user_input)
        print("Your ride was created!")

    else:
        print("Your ride could not be created!")
        return


def is_compatible_return_date(initial_date, returning_date):
    initial_year, initial_month, initial_day = map(int, initial_date.split("-"))
    returning_year, returning_month, returning_day = map(int, returning_date.split("-"))

    if datetime.datetime(returning_year, returning_month, returning_day) < datetime.datetime(initial_year,
                                                                                             initial_month,
                                                                                             initial_day):
        print("You cannot make a return date at an earlier date than your departure!")
        return False
    return True


if __name__ == "__main__":
    while True:
        input_prompt()
