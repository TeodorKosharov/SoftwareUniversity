class Trainer:
    id = 1

    def __init__(self, name: str):
        self.id = Trainer.get_next_id()
        self.name = name

    @staticmethod
    def get_next_id():
        res = Trainer.id
        Trainer.id += 1
        return res

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"