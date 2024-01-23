import sheetsaccess
import googlemaps

API_KEY = 'Insert API Key here'
map_client = googlemaps.Client(API_KEY)
def CalculateDistances():
    data = sheetsaccess.RetrieveData()
    sheetsData = [] #list to house information in sheets
    # Iterate through the information of an entry
    for person in data:
        index = data.index(person)
        dest = f"{person[3]}"
        home_address = '1156 High St, Santa Cruz' #Location of UCSC to compute commute time from house to campus.
        
        distanceCell = 'I' + str(index + 2)
        if sheetsaccess.CheckCell(distanceCell) == True: #If the cell is empty, update the information of this cell, and every other cell
            distance = map_client.distance_matrix(dest, home_address, mode = 'driving')['rows'][0]['elements'][0]['distance']['value']/1000
            sheetsaccess.AddData(distanceCell, distance) 
        
            timeDrivingCell = 'J' + str(index + 2)
            timeDriving = round((map_client.distance_matrix(dest, home_address, mode = "driving")['rows'][0]['elements'][0]['duration']['value'])/60)
            sheetsaccess.AddData(timeDrivingCell, timeDriving)

            timeTransitCell = 'K' + str(index+2)
            timeTransit = round((map_client.distance_matrix(dest, home_address, mode = "transit")['rows'][0]['elements'][0]['duration']['value'])/60)
            sheetsaccess.AddData(timeTransitCell, timeTransit)
        
            timeWalkCell = 'L' + str(index+2)
            timeWalk = round((map_client.distance_matrix(dest, home_address, mode = "walking")['rows'][0]['elements'][0]['duration']['value'])/60)
            sheetsaccess.AddData(timeWalkCell, timeWalk)
        sheetsData.append(sheetsaccess.GetRowVals(index+2))

    # Add the last 4 column data to the sheetsData list
    for residence in sheetsData:
        residence[8] = float(residence[8])
        residence[9] = int(residence[9])
        residence[10] = int(residence[10])
        residence[11] = int(residence[11])
    return sheetsData
        
# Retrives the data in a given category
def RetrieveCategories(userdata, category):
    data = []
    categories = {
        'address' : 4,
        'vacancies': 5,
        'estimated rent': 6,
        'time until vacancy': 7,
        'distance': 8,
        'driving time': 9,
        'bus time': 10,
        'walking time': 11
    }
    for residence in userdata:
        data.append(residence[categories[category]])
    return data

# One-time call to populate all the columns with their relevant information
userData = CalculateDistances()
addressList = RetrieveCategories(userData, 'address')
vacancyList = RetrieveCategories(userData, 'vacancies')
rentList = RetrieveCategories(userData, 'estimated rent')
vacancyTimesList = RetrieveCategories(userData, 'time until vacancy')
distanceList = RetrieveCategories(userData, 'distance')
drivetimeList = RetrieveCategories(userData, 'driving time')
bustimeList = RetrieveCategories(userData, 'bus time')
walktimeList = RetrieveCategories(userData, 'walking time')

# User interface to run in terminal. This was our original idea, until we realized we could code a website in Python with Streamlit, so we no longer have use for it.
'''

print("\nWelcome to HomelessNoMore: A program that allows you to easily search for available off-campus housing based on your needs, without the hassle and unreliability of word-of-mouth!"\
"You can also be educated on Santa Cruz housing through our chatbot!\n")
print("Please select an option from 1-3:\n1: See local available housing in SC\n2: Speak with an informed SC housing chatbot\n3:Quit")

while True:
    try:
        user_prompt = int(input())
    except ValueError:
        print("Please enter a valid number from 1-3")
        continue
    if user_prompt < 1 or user_prompt > 3:
        print("Please enter a valid number from 1-3")
        continue
    break

if user_prompt == 1:
    print("Below are available (or soon to be available) off-campus housing. Please enter a category from vacancies to walking time to sort them accordingly")
    while True:
        sheetsData = CalculateDistances()
        graph.CreateGraph(sheetsData)
        print('Please enter a sortable category to sort the residences accordingly (Vacancies/Estimated Rent/Time Until Vacancy/Distance/Driving Time/Bus Time/Walking Time)')
        print('If there is a residence you would like more info on, type in the corresponding row number')
        print('If you would like to exit the program, type q')
        try:
            user_selection = input()
            if user_selection == 'q':
                print("Have a nice day!")
                exit()
            elif user_selection.isdigit():
                user_selection = int(user_selection)
                index = user_selection-1
                print(f"Looks like you're interested in this property! The name of the vacating resident is {sheetsData[index][2]}."\
                        f" You can contact them by emailing them at {sheetsData[index][1]}, or calling them at {sheetsData[index][3]}!")
                while True:
                    user_choice = input('Would you like to keep browsing properties? (y/n)\n')
                    if user_choice == 'y' or user_choice == 'yes':
                        break
                    elif user_choice == 'n' or user_choice == 'no':
                        print("Have a nice day!")
                        exit()
                    else:
                        continue
                continue
            else:
                user_selection = user_selection.lower()
                sheetsData = graph.SortData(sheetsData, user_selection)
                continue
        
        except KeyError:
                print('Please enter a sortable category to sort the residences accordingly (Vacancies/Estimated Rent/Time Until Vacancy/Distance/Driving Time/Bus Time/Walking Time) (Case Sensitive)')
                print('If there is a residence you would like more info on, type in the corresponding row number')
                print('If you would like to exit the program, type q')
                continue
else:
    exit()

'''

