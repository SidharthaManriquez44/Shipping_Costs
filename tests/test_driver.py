from src.models import Driver
from main import calculate_driver_cost

def test_least_expensive_driver():
    driver1 = Driver(4, 10)
    driver2 = Driver(7, 20)
    price, driver = calculate_driver_cost(80, driver1, driver2)
    assert price == 200
    assert driver is driver1
