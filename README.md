# ShippingCosts

**ShippingCosts** 
Is a Python project to calculate shipping costs, select optimal drivers based on speed and salary, and calculate net profits from multiple transportation trips.


## 📦 Project Structure

ShippingCosts/ ├── costs/ │ ├── init.py │ ├── shipping_costs.py ├── UnitTest/ │ ├── init.py │ ├── Unittest.py ├── main.py ├── README.md


---

## 🚀 Features

### 1. Shipping cost calculation
The `calculate_shipping_cost()` function estimates the shipping cost between two geographic coordinates, considering the type of shipment:

```python
from main import calculate_shipping_cost

calculate_shipping_cost((0, 0), (1, 1), shipping_type='Overnight')
# → "$1.04"
```

## Available shipping types:

 * Ground
 * Priority
 * Overnight

### 2. Selecting the cheapest driver

The `calculate_driver_cost()` function determines which driver is the most economical for a given distance, based on their speed and salary:

```python
from main import calculate_driver_cost
from costs.models import Driver

driver1 = Driver(4, 10)
driver2 = Driver(7, 20)

calculate_driver_cost(80, driver1, driver2)
# → (200, driver1)
```
###  3. Calculation of money earned on trips

The `calculate_money_made()` function calculates the net earnings for one or more trips:

```python
from main import calculate_money_made
from costs.models import Driver
from costs.models import Trip

driver1 = Driver(4, 10)
driver2 = Driver(7, 20)
trip1 = Trip(200, driver1, 15)
trip2 = Trip(300, driver2, 40)

calculate_money_made(MEX=trip1, USA=trip2)
# → 445
```

## 🧪 Tests

The pytest  includes custom tests that validate:

 * The format and value of the shipping cost. 
 * The correct selection of the most economical driver. 
 * The precise calculation of profits.

Note: All can be easily validated in terminal
```terminal
pytest
```

## ⚙️ Requirements
Python 3.10+

Does not require external dependencies

##  ‍🧑‍💻 Author
Developed by `Sidhartha Manriquez`.

## 📄 License

This project is under the [License MIT](LICENSE).
