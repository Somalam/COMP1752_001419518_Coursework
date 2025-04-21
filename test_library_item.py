import pytest
from library_item import LibraryItem


def test_initialization():

    item = LibraryItem("Test Track", "Test Artist")
    assert item.name == "Test Track"
    assert item.artist == "Test Artist"
    assert item.rating == 0
    assert item.play_count == 0

    item2 = LibraryItem("Test Track 2", "Test Artist 2")
    assert item2.name == "Test Track 2"
    assert item2.artist == "Test Artist 2"
    assert item2.rating == 0
    assert item2.play_count == 0

def test_info_method():

    item = LibraryItem("Another Brick in the Wall", "Pink Floyd", 4)
    assert item.info() == "Another Brick in the Wall - Pink Floyd ****"

    item2 = LibraryItem("Another track", "Another artist", 2)
    assert item2.info() == "Another track - Another artist **"

def test_stars_method():

    item0 = LibraryItem("Track", "Artist", 0)
    assert item0.stars() == ""
    
    item1 = LibraryItem("Track", "Artist", 1)
    assert item1.stars() == "*"
    
    item3 = LibraryItem("Track", "Artist", 3)
    assert item3.stars() == "***"
    
    item5 = LibraryItem("Track", "Artist", 5)
    assert item5.stars() == "*****"

if __name__ == "__main__":
    test_initialization()
    test_info_method()
    test_stars_method()