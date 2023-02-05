from copy import copy

from rosreestr2coord import Area
import json
import folium


def get_coord(number_string):
    if type(number_string) != str or 18 < len(number_string) or len(number_string) < 12:
        return False

    check_number = number_string.split(':')
    for x in check_number:
        if x.isalpha() is True:
            return False

    area = Area(number_string)
    row_data = area.to_geojson()
    if isinstance(row_data, (str, bytes, bytearray)):
        data = json.loads(row_data)

        coords = []
        for elem in data['features']:
            coord = elem['geometry']
            coords.append(coord['coordinates'])

        return coords
    return False


def markup_to_map(coords):
    if coords is False:
        return False
    check = []
    for x in coords:
        check.append([x[1], x[0]])

    check.append([check[0][0], check[0][1]])

    coords_location = [check[0][0], check[0][1]]
    m = folium.Map(location=coords_location, zoom_start=17)

    folium.PolyLine(check).add_to(m)
    m.save('markup/templates/markup/map_folium.html')
    return True


def output(number_string):
    return markup_to_map(get_coord(number_string))


# start_map = folium.Map(location=[55.7522200, 37.6155600], zoom_start=8)
# start_map.save('markup/templates/markup/map_start.html')