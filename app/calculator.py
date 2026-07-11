from app.calculation import Calculation
from app.calculator_memento import HistoryCaretaker
from app.history import CalculationHistory


class Calculator:
    def __init__(self):
        self.history = CalculationHistory()
        self.caretaker = HistoryCaretaker()
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self, calculation):
        for observer in self.observers:
            observer.update(calculation, self.history)

    def calculate(self, operation, operand_a, operand_b):
        self.caretaker.save(self.history.get_all())

        calculation = Calculation(operation, operand_a, operand_b)
        result = calculation.calculate()

        self.history.add(calculation)
        self.notify_observers(calculation)

        return result

    def get_history(self):
        return self.history.get_all()

    def clear_history(self):
        self.caretaker.save(self.history.get_all())
        self.history.clear()

    def undo(self):
        restored_history = self.caretaker.undo(self.history.get_all())
        self.history.calculations = restored_history

    def redo(self):
        restored_history = self.caretaker.redo(self.history.get_all())
        self.history.calculations = restored_history

    def save_history(self, file_path):
        self.history.save_to_csv(file_path)

    def load_history(self, file_path):
        self.caretaker.save(self.history.get_all())
        self.history.load_from_csv(file_path)