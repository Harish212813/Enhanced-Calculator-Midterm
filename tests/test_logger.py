import logging

from app.logger import setup_logger


def test_setup_logger(monkeypatch, tmp_path):
    log_dir = tmp_path / "logs"

    monkeypatch.setenv("CALCULATOR_LOG_DIR", str(log_dir))
    monkeypatch.setenv("CALCULATOR_LOG_FILE", "test.log")

    logger = setup_logger("test_logger")

    logger.info("Test log message")

    log_file = log_dir / "test.log"

    assert log_file.exists()

    for handler in logger.handlers:
        handler.flush()

    content = log_file.read_text(encoding="utf-8")

    assert "Test log message" in content
    assert "INFO" in content


def test_logger_does_not_add_duplicate_handlers(monkeypatch, tmp_path):
    monkeypatch.setenv(
        "CALCULATOR_LOG_DIR",
        str(tmp_path / "logs"),
    )
    monkeypatch.setenv("CALCULATOR_LOG_FILE", "duplicate.log")

    logger = setup_logger("duplicate_logger")
    original_handler_count = len(logger.handlers)

    same_logger = setup_logger("duplicate_logger")

    assert same_logger is logger
    assert len(same_logger.handlers) == original_handler_count


def test_logger_level(monkeypatch, tmp_path):
    monkeypatch.setenv(
        "CALCULATOR_LOG_DIR",
        str(tmp_path / "logs"),
    )

    logger = setup_logger("level_logger")

    assert logger.level == logging.INFO