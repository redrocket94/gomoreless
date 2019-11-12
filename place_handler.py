import googlemaps


def match_city(city):
    gmaps = googlemaps.Client(key="AIzaSyDlGbIGe2ZuoAU1hhX_KOy6nr4bc28pfBk")

    geocode_result = googlemaps.client.find_place(input=city, input_type="textquery", client=gmaps)

    candidates = geocode_result["candidates"]
    if len(candidates) == 0:
        return None
    placeid = candidates[0]["place_id"]

    placestr = googlemaps.client.place(place_id=placeid, client=gmaps)

    address_components = placestr["result"]["address_components"]
    address_city_name = address_components[0]["short_name"]
    address_components_size = len((placestr["result"]["address_components"]))

    if address_components_size >= 3:
        for line in address_components:
            if line["types"][0] == "country":
                return address_city_name + ", " + line["long_name"]
        return None

    elif 3 > address_components_size > 0:
        for line in address_components:
            if line["types"][0] == "country":
                return address_city_name + ", " + line["long_name"]
        return None
