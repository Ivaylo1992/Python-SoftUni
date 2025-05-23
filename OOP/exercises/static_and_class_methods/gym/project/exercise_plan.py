class ExercisePlan:
    id = 1
    def __init__(self, trainer_id: int, equipment_id: int, duration: int) -> None:
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = self.__class__.id
        self.__class__.id += 1

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int) -> 'ExercisePlan':
        duration = hours * 60
        return cls(trainer_id, equipment_id, duration)

    @staticmethod
    def get_next_id() -> int:
        return ExercisePlan.id

    def __repr__(self) -> str:
        return f"Plan <{self.id}> with duration {self.duration} minutes"

