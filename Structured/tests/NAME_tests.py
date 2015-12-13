from nose.tools import *
from NAME.appcode import Room


def setup():
    print("SetUp")


def teardown():
    print("Tear Down")


def test_basic():
    panic = Room("Panic Room", "Hide here when attacked")
    assert_equal(panic.name, "Panic Room")
    assert_equal(panic.description, "Hide here when attacked")


def test_room_paths():
    center = Room("Center", "Room in the center")
    north = Room("North", "Room in the north")
    south = Room("South", "Room in the south")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)


def test_map():
    start = Room("Start", "You start your journey from here.")
    west = Room("West", "You have moved westwards. Turn East for greener pastures!!")
    bottom = Room("Bottom", "You just hit rock bottom. Nowhere to go but up!!")

    start.add_paths({'west': west, 'down': bottom})
    west.add_paths({'east': start})
    bottom.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)
