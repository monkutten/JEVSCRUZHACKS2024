# Used to create user interface in terminal when running script
def CreateGraph(userdata):
    print(f"{'Address' : <60}{'Vacancies' : ^9}{'Estimated Rent' : ^20}{'Time Until Vacancy' : ^22}{'Distance (km)' : ^22}{'Driving Time (mins)' : ^18}{'Bus Time (mins)' : ^18}{'Walking Time (mins)' : >18}\n")
    for index in range(len(userdata)):
        print(f"{index+1}. {userdata[index][4] : <60}{userdata[index][5] : ^6}{userdata[index][6] : ^17}{userdata[index][7] : ^22}{userdata[index][8] : ^22}{userdata[index][9] : ^18}{userdata[index][10] : ^18}{userdata[index][11] : >18}")

# Enable a user to sort by size in a given category
def SortData(userdata, category):
    categories = {
        'vacancies': 5,
        'estimated rent': 6,
        'time until vacancy': 7,
        'distance': 8,
        'driving time': 9,
        'bus time': 10,
        'walking time': 11
    }
    userdata = sorted(userdata, key=lambda x: x[categories[category]])
    return userdata