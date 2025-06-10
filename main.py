from src.shipping_costs import get_distance, format_price, SHIPPING_PRICES
from math import inf

def calculate_shipping_cost(from_coords, to_coords, shipping_type='Overnight'):
    distance = get_distance(*from_coords, *to_coords)
    shipping_rate = SHIPPING_PRICES[shipping_type]
    price = distance * shipping_rate
    price = format_price(price)
    return price


def calculate_driver_cost(distance, *drivers):
    cheapest_driver = None
    cheapest_driver_price = inf

    for driver in drivers:
        driver_time = distance / driver.speed
        price_for_driver = driver_time * driver.salary

        if price_for_driver < cheapest_driver_price:
            cheapest_driver = driver
            cheapest_driver_price = price_for_driver

    return cheapest_driver_price, cheapest_driver


def calculate_money_made(**trips):
    total_money_made = 0
    for trip_id, trip in trips.items():
        trip_revenue = trip.cost - trip.driver_cost
        total_money_made += trip_revenue
    return total_money_made
