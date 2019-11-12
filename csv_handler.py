# function to write created ride to csv file, with default 1 seat
import csv
import datetime


def write_created_ride_to_csv(ride_data):
    with open("rides.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(ride_data)


def get_last_created_ride_from_csv():  # not optimal for large files
    with open("rides.csv", "r") as csvfile:
        try:
            last_entry = list(csv.reader(csvfile))[-1]
            return last_entry
        except IndexError:
            return None


def find_ride(from_city, to_city, from_date, to_date, minimum_free_seats):
    with open("rides.csv", "r") as csvfile:

        if not minimum_free_seats.isdigit():
            minimum_free_seats = 1

        for ride_entry in list(csv.reader(csvfile)):
            has_from_city = has_to_city = has_from_date = has_to_date = has_minimum_free_seats = False

            if from_city == ride_entry[0].split(",")[0] or from_city == "none":
                has_from_city = True
            if to_city == ride_entry[1].split(",")[0] or to_city == "none":
                has_to_city = True
            if from_date != "none":
                has_from_date = True
            if to_date != "none":
                has_to_date = True
            if int(minimum_free_seats) <= int(ride_entry[3]):
                has_minimum_free_seats = True

            if has_from_city and has_to_city and has_minimum_free_seats:
                if has_from_date and not has_to_date:
                    if datetime.datetime.strptime(ride_entry[2], "%Y-%m-%d").date() == datetime.datetime.strptime(
                            from_date, "%Y-%m-%d").date():
                        print(", ".join(ride_entry))
                if has_to_date and not has_from_date:
                    if datetime.datetime.strptime(ride_entry[2], "%Y-%m-%d").date() == datetime.datetime.strptime(
                            to_date, "%Y-%m-%d").date():
                        print(", ".join(ride_entry))
                if not has_to_date and not has_from_date:
                    print(", ".join(ride_entry))
                if has_from_date and from_date != "none" and has_to_date and to_date != "none":
                    if datetime.datetime.strptime(from_date, "%Y-%m-%d").date() <= datetime.datetime.strptime(
                            ride_entry[2], "%Y-%m-%d").date() <= datetime.datetime.strptime(to_date, "%Y-%m-%d").date():
                        print(", ".join(ride_entry))
