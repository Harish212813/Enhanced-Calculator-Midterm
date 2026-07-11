import pytest

from app.calculator_config import CalculatorConfig


def test_config_loads_values(monkeypatch, tmp_path):
    log_dir = tmp_path / "logs"
    history_dir = tmp_path / "data"

    monkeypatch.setenv("CALCULATOR_LOG_DIR", str(log_dir))
    monkeypatch.setenv("CALCULATOR_HISTORY_DIR", str(history_dir))
    monkeypatch.setenv("CALCULATOR_LOG_FILE", "test.log")
    monkeypatch.setenv("CALCULATOR_HISTORY_FILE", "test_history.csv")
    monkeypatch.setenv("CALCULATOR_MAX_HISTORY_SIZE", "50")
    monkeypatch.setenv("CALCULATOR_AUTO_SAVE", "false")
    monkeypatch.setenv("CALCULATOR_PRECISION", "3")
    monkeypatch.setenv("CALCULATOR_MAX_INPUT_VALUE", "5000")
    monkeypatch.setenv("CALCULATOR_DEFAULT_ENCODING", "utf-8")

    config = CalculatorConfig()

    assert config.log_dir == log_dir
    assert config.history_dir == history_dir
    assert config.log_file == "test.log"
    assert config.history_file == "test_history.csv"
    assert config.max_history_size == 50
    assert config.auto_save is False
    assert config.precision == 3
    assert config.max_input_value == 5000
    assert config.default_encoding == "utf-8"

    assert log_dir.exists()
    assert history_dir.exists()


def test_config_file_paths(monkeypatch, tmp_path):
    monkeypatch.setenv("CALCULATOR_LOG_DIR", str(tmp_path / "logs"))
    monkeypatch.setenv("CALCULATOR_HISTORY_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("CALCULATOR_LOG_FILE", "calculator.log")
    monkeypatch.setenv("CALCULATOR_HISTORY_FILE", "history.csv")

    config = CalculatorConfig()

    assert config.log_file_path == tmp_path / "logs" / "calculator.log"
    assert config.history_file_path == tmp_path / "data" / "history.csv"


def test_invalid_max_history_size(monkeypatch, tmp_path):
    monkeypatch.setenv("CALCULATOR_LOG_DIR", str(tmp_path / "logs"))
    monkeypatch.setenv("CALCULATOR_HISTORY_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("CALCULATOR_MAX_HISTORY_SIZE", "0")

    with pytest.raises(
        ValueError,
        match="Maximum history size must be greater than zero",
    ):
        CalculatorConfig()


def test_invalid_precision(monkeypatch, tmp_path):
    monkeypatch.setenv("CALCULATOR_LOG_DIR", str(tmp_path / "logs"))
    monkeypatch.setenv("CALCULATOR_HISTORY_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("CALCULATOR_PRECISION", "-1")

    with pytest.raises(
        ValueError,
        match="Precision cannot be negative",
    ):
        CalculatorConfig()


def test_invalid_max_input_value(monkeypatch, tmp_path):
    monkeypatch.setenv("CALCULATOR_LOG_DIR", str(tmp_path / "logs"))
    monkeypatch.setenv("CALCULATOR_HISTORY_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("CALCULATOR_MAX_INPUT_VALUE", "0")

    with pytest.raises(
        ValueError,
        match="Maximum input value must be greater than zero",
    ):
        CalculatorConfig()