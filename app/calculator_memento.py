class CalculatorMemento:
    def __init__(self, calculations):
        self.calculations = calculations.copy()

    def get_state(self):
        return self.calculations.copy()


class HistoryCaretaker:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def save(self, calculations):
        memento = CalculatorMemento(calculations)
        self.undo_stack.append(memento)
        self.redo_stack.clear()

    def undo(self, current_calculations):
        if not self.undo_stack:
            raise ValueError("Nothing to undo")

        current_memento = CalculatorMemento(current_calculations)
        self.redo_stack.append(current_memento)

        previous_memento = self.undo_stack.pop()
        return previous_memento.get_state()

    def redo(self, current_calculations):
        if not self.redo_stack:
            raise ValueError("Nothing to redo")

        current_memento = CalculatorMemento(current_calculations)
        self.undo_stack.append(current_memento)

        next_memento = self.redo_stack.pop()
        return next_memento.get_state()