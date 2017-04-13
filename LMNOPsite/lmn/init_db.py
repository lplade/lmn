from models import Venue, Note, Artist, Show
import datetime


def add_artists():
    artists = [
        Artist(name="David Bowie"),
        Artist(name="Prince"),
        Artist(name="Biggy Smalls"),
        Artist(name="Tupac Shakur"),
        Artist(name="Keith Emerson"),
        Artist(name="Phife Dawg"),
        Artist(name="Greg Lake"),
        Artist(name="George Michael"),
        Artist(name="Chuck Berry")
    ]
    for a in artists:
        Artist.objects.create(a)


def add_venues():
    venues = [
        Venue(name="El Taquito", city="West Saint Paul", state="MN"),
        Venue(name="The dumpster behind the 7-11", city="Teaneck", state="NJ"),
        Venue(name="The Olive Garden", city="Eugene", state="OR"),
        Venue(name="Red Lobster", city="Bend", state="OR"),
        Venue(name="Nordski Nook", city="Spooner", state="WI"),
        Venue(name="Perkins", city="Saint Cloud", state="MN"),
        Venue(name="Denny's", city="River Falls", state="WI"),
        Venue(name="White Castle", city="Denton Farmpark", state="NC"),
        Venue(name="The abandoned Freemason lodge across from the disused Freemason Lodge",
              city="Unincorporated", state="MT")
    ]
    for v in venues:
        Venue.objects.create(v)


def add_shows():
    shows = [
        Show(show_date=datetime.today, artist="Keith Emerson", venue="Red Lobster"),
        Show(show_date=datetime.today, artist="Price", venue="El Taquito")
    ]
    for s in shows:
        Show.objects.create(s)


def main():
    add_artists()
    add_venues()
    add_shows()


if __name__ == '__main__':
    main()
