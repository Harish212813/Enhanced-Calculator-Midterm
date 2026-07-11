import logging


class CalculationObserver:
    def update(self, calculation, history):
        raise NotImplementedError


class LoggingObserver(CalculationObserver):
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)

    def update(self, calculation, history):
        self.logger.info(
            "Calculation completed: %s %s %s = %s",
            calculation.operation,
            calculation.operand_a,
            calculation.operand_b,
            calculation.result,
        )


class AutoSaveObserver(CalculationObserver):
    def __init__(self, file_path):
        self.file_path = file_path

    def update(self, calculation, history):
        history.save_to_csv(self.file_path)