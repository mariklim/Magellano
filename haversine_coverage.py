import math   
#function haversine returns the distance between the coordinates of two given geographic point
def haversine(lat1,lon1,lat2,lon2):
    #Earth radius
    R = 6373.0
  

    # change in coordinates
    dlon = math.radians(lon2) - math.radians(lon1)
    dlat = math.radians(lat2) - math.radians(lat1)

    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c
     #function  countCoverage calculates the percentage of the zone covered by enabled shoppers. One shopper covers a zone if the distance among the coordinates is less than  inserted parameter.
def countCoverage(distance):
    locations = [
    {'id': 1000, 'zip_code': '37069', 'lat': 45.35, 'lng': 10.84},
    {'id': 1001, 'zip_code': '37121', 'lat': 45.44, 'lng': 10.99},
    {'id': 1001, 'zip_code': '37129', 'lat': 45.44, 'lng': 11.00},
    {'id': 1001, 'zip_code': '37133', 'lat': 45.43, 'lng': 11.02},
    ]

    shoppers = [
    {'id': 'S1', 'lat': 45.46, 'lng': 11.03, 'enabled': 1},
    {'id': 'S2', 'lat': 45.46, 'lng': 10.12, 'enabled': 1},
    {'id': 'S3', 'lat': 45.34, 'lng': 10.81, 'enabled': 1},
    {'id': 'S4', 'lat': 45.76, 'lng': 10.57, 'enabled': 1},
    {'id': 'S5', 'lat': 45.34, 'lng': 10.63, 'enabled': 1},
    {'id': 'S6', 'lat': 45.42, 'lng': 10.81, 'enabled': 1},
    {'id': 'S7', 'lat': 45.34, 'lng': 10.94, 'enabled': 1},
    ]



    shoppers_count = len(shoppers)
    locations_count = len(locations)
    # Loop through the arrays for find the distance of each shopper and location
    for i in range(shoppers_count):
        filtered_locations_count = 0
        for j in range(locations_count):
            if haversine(locations[j]['lat'], locations[j]['lng'], shoppers[i]['lat'], shoppers[i]['lng']) < distance:
                filtered_locations_count = filtered_locations_count + 1
                #I save these elements with id and the percentage of the coverage in the array
        sorted_shoppers = []
        items = {'id': shoppers[i]['id'], 'coverage': (filtered_locations_count/locations_count*100)}
        sorted_shoppers.append(items)
    
        print(sorted_shoppers)

def main():
    countCoverage(10)
if __name__ == "__main__":
  main()
    