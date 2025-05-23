from typing import List

from project.trainer import Trainer
from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription


class Gym:
    def __init__(self) -> None:
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer) -> None:
        if not self.is_instance_found(self.customers, customer):
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer) -> None:
        if not self.is_instance_found(self.trainers, trainer):
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment) -> None:
        if not self.is_instance_found(self.equipment, equipment):
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan) -> None:
        if not self.is_instance_found(self.plans, plan):
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription) -> None:
        if not self.is_instance_found(self.subscriptions, subscription):
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int) -> str:
        subscription = next((s for s in self.subscriptions if s.id == subscription_id), None)
        customer = next((c for c in self.customers if c.id == subscription.customer_id), None)
        trainer = next((t for t in self.trainers if t.id == subscription.trainer_id), None)
        plan = next((p for p in self.plans if p.trainer_id == trainer.id), None)
        equipment = next((e for e in self.equipment if e.id == plan.equipment_id), None)

        result = [
            subscription.__repr__(),
            customer.__repr__(),
            trainer.__repr__(),
            equipment.__repr__(),
            plan.__repr__(),
        ]

        return '\n'.join(result)


    # Helper method
    @staticmethod
    def is_instance_found(array, inst):
        return inst in array
