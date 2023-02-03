from rosreestr2coord import Area
import json


def get_coord(number_string: str):
    area = Area(number_string)
    data = json.loads(area.to_geojson())

    coords = []
    for elem in data['features']:
        coord = elem['geometry']
        coords.append(coord['coordinates'])

    return coords
