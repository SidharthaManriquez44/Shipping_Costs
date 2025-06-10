from src.models import Driver, Trip
from main import calculate_money_made

def test_money_made():
    driver1 = Driver(4, 10)
    driver1.cost = 15
    driver2 = Driver(7, 20)
    driver2.cost = 40

    trip1 = Trip(200, driver1, 15)
    trip2 = Trip(300, driver2, 40)

    result = calculate_money_made(MEX=trip1, USA=trip2)
    assert result == 445
