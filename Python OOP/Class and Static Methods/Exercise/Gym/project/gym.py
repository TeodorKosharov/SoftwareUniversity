from Exercise.Gym.project.customer import Customer
from Exercise.Gym.project.equipment import Equipment
from Exercise.Gym.project.exercise_plan import ExercisePlan
from Exercise.Gym.project.subscription import Subscription
from Exercise.Gym.project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = [subsc for subsc in self.subscriptions if subsc.id == subscription_id][0]
        customer = [customer for customer in self.customers if subscription.customer_id == subscription_id][0]
        trainer = [trainer for trainer in self.trainers if subscription.trainer_id == subscription_id][0]
        plan = [plan for plan in self.plans if plan.trainer_id == subscription_id][0]
        equipment = [equipment for equipment in self.equipment if plan.equipment_id == subscription_id][0]
        return str(subscription) + '\n' + str(customer) + '\n' + str(trainer) + '\n' + str(equipment) + '\n' + str(plan)
