import json


class Venues():
    ''' Gets the venues information, from the name to the location or urls'''

    def __init__(self, venue_id, venue_name, city_name, state, venue_address, venue_url, performer_name = None):
        self.venue_id = venue_id
        self.venue_name = venue_name
        self.city_name = city_name
        self.state = state
        self.venue_address = venue_address
        self.url = venue_url
        self.performer_name = performer_name


def get_venues_data():
        # Open the file that hold the json data.
    with open('MN_venues_data.json', mode='r') as f:
        try:
            s = json.load(f)
        except Exception as e:
            print('Problem loading file', e)

    # This line is to pull items on the event list only.
    raw_event_list = s['events']

    venues_list = []

        # This is a good code to get just the name that we want.
    for venue in raw_event_list['event']:
        # This is to see if name is in the list first.
        # if venue['venue_name'] == 'First Avenue':
        if venue['performers'] != None:
            venue_perfomers = venue['performers']['performer']
            if isinstance(venue_perfomers, dict):
                # Wrap in a list
                venue_perfomers = [venue_perfomers]
            # Now loop in the new list format
            for inside_performer in venue_perfomers:
                # This will store the name on the list of items for Venues.
                venues_data = Venues(venue_id = str(venue['venue_id']), venue_name = str(venue['venue_name']), city_name = str(venue['city_name']), state = str(venue['region_name']), venue_address = str(venue['venue_address']), venue_url = str(venue['venue_url']), performer_name = str(inside_performer['name']))
        else:
            # This is to make sure that dosen't get a duplicate.
            venues_data = Venues(venue_id = str(venue['venue_id']), venue_name = str(venue['venue_name']), city_name = str(venue['city_name']), state = str(venue['region_name']), venue_address = str(venue['venue_address']), venue_url = str(venue['venue_url']))

        venues_list.append(venues_data)

    return venues_list

def main():
    # Create an instance to print the list.
    venue_list = get_venues_data()

    for venue in venue_list:  # Run the script to see the results.
        print('{}  {} performer : {}'.format(venue.venue_name, venue.venue_id, venue.performer_name))

if __name__ == '__main__':
    main()
