import requests
import math

URL_PATH = "https://nominatim.openstreetmap.org/search"

def get_lat_lon(location):
    PARAMS = {'q': location, 'format':'jsonv2'}
    headers = {
        'User-Agent': 'DistanceCalc/1.0'
    }
    r = requests.get(url=URL_PATH, params=PARAMS, headers=headers)
    data = r.json()

    latitude = float(data[0]['lat'])
    longitude = float(data[0]['lon'])
    return [latitude, longitude]


def calculate_distance(orig, dest):
    dlon = dest[1] - orig[1]
    dlat = dest[0] - orig[0]
    a = (math.sin(math.radians(dlat / 2)))**2 + \
        math.cos(math.radians(orig[0]))* \
        math.cos(math.radians(dest[0]))* \
        (math.sin(math.radians(dlon/2)))**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    R = 3961
    d = R * c
    return d

def selection_sort(array):
    # step 1: loop from the beginning of the array to the second to last item
    currentIndex = 0
    while (currentIndex < len(array) - 1):
        # step 2: save a copy of the currentIndex
        minIndex = currentIndex
        # step 3: loop through all indexes that proceed the currentIndex
        i = currentIndex + 1
        while (i < len(array)):
            # step 4:   if the value of the index of the current loop is less
            #           than the value of the item at minIndex, update minIndex
            #           with the new lowest value index
            if (array[i] < array[minIndex]):
                # update minIndex with the new lowest value index
                minIndex = i
            i += 1
        # step 5: if minIndex has been updated, swap the values at minIndex and currentIndex
        if (minIndex != currentIndex):
            temp = array[currentIndex]
            array[currentIndex] = array[minIndex]
            array[minIndex] = temp
        currentIndex += 1
    return array


def main():
    origin_name = "New Mexico Museum of Natural History & Science"
    origin_loc = get_lat_lon(origin_name)

    # 5 other locations
    places = [
        "New Mexico Highlands University",
        "Gene Torres Golf Course",
        "Sandia Peak Tramway",
        "Santa Fe Plaza",
        "Las Vegas Municipal Airport"
    ]

    distances = []
    for place in places:
        loc = get_lat_lon(place)
        d = calculate_distance(origin_loc, loc)
        distances.append((d, place))

    # sort by distance using selection sort
    sort_places = selection_sort(distances)

    print(f"Distances from {origin_name}:\n")
    for dist, name in sort_places:
        print(f"{name}: {dist:.2f} miles")




if __name__ == '__main__':
    main()
