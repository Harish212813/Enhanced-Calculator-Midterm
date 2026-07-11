from datetime import datetime

from app.operations import OperationFactory


class Calculation:
    def __init__(self, operation, operand_a, operand_b):
        self.operation = operation
        self.operand_a = operand_a
        self.operand_b = operand_b
        self.result = None
        self.timestamp = datetime.now()

    def calculate(self):
        operation = OperationFactory.create_operation(self.operation)
        self.result = operation.execute(self.operand_a, self.operand_b)
        return self.result

    def to_dict(self):
        return {
            "operation": self.operation,
            "operand_a": self.operand_a,
            "operand_b": self.operand_b,
            "result": self.result,
            "timestamp": self.timestamp.isoformat(),
        }