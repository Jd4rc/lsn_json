import pytest

@pytest.fixture
def data():
       return {
           "first_names" : [
           "Alex",
           "John",
           "Mike",
           "Egor",
           "Daniel",
           "Chris",
           "Andrew",
           "Max",
           "Leo",
           "Ryan"
       ],
       "last_names" : [
           "Smith",
           "Johnson",
           "Brown",
           "Miller",
           "Davis",
           "Wilson",
           "Taylor",
           "Anderson",
           "Thomas",
           "Jackson"
       ],
       "cities" : [
           "New York",
           "London",
           "Berlin",
           "Warsaw",
           "Stockholm",
           "Minsk",
           "Tokyo",
           "Prague",
           "Toronto",
           "Amsterdam"
       ]
       }