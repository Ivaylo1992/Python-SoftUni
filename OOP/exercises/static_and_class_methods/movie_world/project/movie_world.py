from typing import List

from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name) -> None:
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity() -> int:
        return 15

    @staticmethod
    def customer_capacity() -> int:
        return 10

    def add_customer(self, customer: Customer) -> None:
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id) -> str:
        current_customer = [c for c in self.customers if c.id == customer_id][0]
        current_dvd = [d for d in self.dvds if d.id == dvd_id][0]

        if current_dvd in current_customer.rented_dvds:
            return f"{current_customer.name} has already rented {current_dvd.name}"

        if current_dvd.is_rented:
            return "DVD is already rented"

        if current_customer.age < current_dvd.age_restriction:
            return (f"{current_customer.name} should be at least {current_dvd.age_restriction}"
                    f" to rent this movie")

        current_dvd.is_rented = True
        current_customer.rented_dvds.append(current_dvd)
        return f"{current_customer.name} has successfully rented {current_dvd.name}"

    def return_dvd(self, customer_id, dvd_id) -> str:
        current_customer = [c for c in self.customers if c.id == customer_id][0]
        current_dvd = [d for d in self.dvds if d.id == dvd_id][0]

        if current_dvd in current_customer.rented_dvds:
            current_dvd.is_rented = False
            current_customer.rented_dvds.remove(current_dvd)
            return f"{current_customer.name} has successfully returned {current_dvd.name}"

        return f"{current_customer.name} does not have that DVD"

    def __repr__(self) -> str:
        result = []
        for customer in self.customers:
            result.append(customer.__repr__())

        for dvd in self.dvds:
            result.append(dvd.__repr__())

        return "\n".join(result)