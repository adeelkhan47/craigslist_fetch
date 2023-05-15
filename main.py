import logging

logging.basicConfig(level=logging.INFO)

state_to_url = {
    "Alabama": "https://auburn.craigslist.org/",
    "Alaska": "https://anchorage.craigslist.org/",
    "Arizona": "https://phoenix.craigslist.org/",
    "Arkansas": "https://fayar.craigslist.org/",
    "California": "https://sfbay.craigslist.org/",
    "Colorado": "https://denver.craigslist.org/",
    "Connecticut": "https://newhaven.craigslist.org/",
    "Delaware": "https://delaware.craigslist.org/",
    "Florida": "https://miami.craigslist.org/",
    "Georgia": "https://atlanta.craigslist.org/",
    "Hawaii": "https://honolulu.craigslist.org/",
    "Idaho": "https://boise.craigslist.org/",
    "Illinois": "https://chicago.craigslist.org/",
    "Indiana": "https://indianapolis.craigslist.org/",
    "Iowa": "https://desmoines.craigslist.org/",
    "Kansas": "https://wichita.craigslist.org/",
    "Kentucky": "https://lexington.craigslist.org/",
    "Louisiana": "https://neworleans.craigslist.org/",
    "Maine": "https://maine.craigslist.org/",
    "Maryland": "https://baltimore.craigslist.org/",
    "Massachusetts": "https://boston.craigslist.org/",
    "Michigan": "https://detroit.craigslist.org/",
    "Minnesota": "https://minneapolis.craigslist.org/",
    "Mississippi": "https://jackson.craigslist.org/",
    "Missouri": "https://stlouis.craigslist.org/",
    "Montana": "https://montana.craigslist.org/",
    "Nebraska": "https://omaha.craigslist.org/",
    "Nevada": "https://lasvegas.craigslist.org/",
    "New Hampshire": "https://nh.craigslist.org/",
    "New Jersey": "https://cnj.craigslist.org/",
    "New Mexico": "https://albuquerque.craigslist.org/",
    "New York": "https://newyork.craigslist.org/",
    "North Carolina": "https://raleigh.craigslist.org/",
    "North Dakota": "https://nd.craigslist.org/",
    "Ohio": "https://columbus.craigslist.org/",
    "Oklahoma": "https://tulsa.craigslist.org/",
    "Oregon": "https://portland.craigslist.org/",
    "Pennsylvania": "https://pittsburgh.craigslist.org/",
    "Rhode Island": "https://providence.craigslist.org/",
    "South Carolina": "https://greenville.craigslist.org/",
    "South Dakota": "https://sd.craigslist.org/",
    "Tennessee": "https://nashville.craigslist.org/",
    "Texas": "https://austin.craigslist.org/",
    "Utah": "https://saltlakecity.craigslist.org/",
    "Vermont": "https://vermont.craigslist.org/",
    "Virginia": "https://richmond.craigslist.org/",
    "Washington": "https://seattle.craigslist.org/",
    "West Virginia": "https://charlestonwv.craigslist.org/",
    "Wisconsin": "https://madison.craigslist.org/",
    "Wyoming": "https://wyoming.craigslist.org/",
}
numbers_to_states = {
    "0": "All",
    "1": "Alabama",
    "2": "Alaska",
    "3": "Arizona",
    "4": "Arkansas",
    "5": "California",
    "6": "Colorado",
    "7": "Connecticut",
    "8": "Delaware",
    "9": "Florida",
    "10": "Georgia",
    "11": "Hawaii",
    "12": "Idaho",
    "13": "Illinois",
    "14": "Indiana",
    "15": "Iowa",
    "16": "Kansas",
    "17": "Kentucky",
    "18": "Louisiana",
    "19": "Maine",
    "20": "Maryland",
    "21": "Massachusetts",
    "22": "Michigan",
    "23": "Minnesota",
    "24": "Mississippi",
    "25": "Missouri",
    "26": "Montana",
    "27": "Nebraska",
    "28": "Nevada",
    "29": "New Hampshire",
    "30": "New Jersey",
    "31": "New Mexico",
    "32": "New York",
    "33": "North Carolina",
    "34": "North Dakota",
    "35": "Ohio",
    "36": "Oklahoma",
    "37": "Oregon",
    "38": "Pennsylvania",
    "39": "Rhode Island",
    "40": "South Carolina",
    "41": "South Dakota",
    "42": "Tennessee",
    "43": "Texas",
    "44": "Utah",
    "45": "Vermont",
    "46": "Virginia",
    "47": "Washington",
    "48": "West Virginia",
    "49": "Wisconsin",
    "50": "Wyoming"
}

print("Craigslist Bot is Here.")

for a, b in numbers_to_states.items():
    print(f"{a} => {b}")
choose_state = input("Choose state number : ")
if choose_state in numbers_to_states.keys():
    if choose_state == "0":
        for state, state_url in state_to_url.items():
            print(state, state_url)
    else:
        selected_state = numbers_to_states[choose_state]
        selected_state_url = state_to_url[selected_state]
else:
    print("--------------------------------- Invalid Entry ---------------------------------")

