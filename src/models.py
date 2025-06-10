class Driver:
    def __init__(self, speed, salary):
        self.speed = speed
        self.salary = salary

    def __repr__(self):
        return "Nile Driver speed {} salary {}".format(self.speed, self.salary)


class Trip:
    def __init__(self, cost, driver, driver_cost):
        self.cost = cost
        self.driver = driver
        self.driver_cost = driver_cost
