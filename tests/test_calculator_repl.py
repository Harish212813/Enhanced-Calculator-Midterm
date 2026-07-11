from app.calculator_repl import run_calculator


def test_add_and_exit(monkeypatch, capsys):
    inputs = iter(["add 5 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run_calculator()

    output = capsys.readouterr().out

    assert "Result: 8.0" in output
    assert "Goodbye!" in output


def test_history(monkeypatch, capsys):
    inputs = iter(["add 5 3", "history", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run_calculator()

    output = capsys.readouterr().out

    assert "add 5.0 3.0 = 8.0" in output


def test_clear_history(monkeypatch, capsys):
    inputs = iter(["add 5 3", "clear", "history", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run_calculator()

    output = capsys.readouterr().out

    assert "History cleared." in output
    assert "History is empty." in output


def test_invalid_command(monkeypatch, capsys):
    inputs = iter(["randomcommand", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run_calculator()

    output = capsys.readouterr().out

    assert "Unknown command." in output


def test_invalid_number(monkeypatch, capsys):
    inputs = iter(["add hello 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run_calculator()

    output = capsys.readouterr().out

    assert "Error:" in output


def test_divide_by_zero(monkeypatch, capsys):
    inputs = iter(["divide 10 0", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run_calculator()

    output = capsys.readouterr().out

    assert "Cannot divide by zero" in output


def test_help(monkeypatch, capsys):
    inputs = iter(["help", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run_calculator()

    output = capsys.readouterr().out

    assert "Available commands:" in output
    assert "add <number> <number>" in output


def test_undo_and_redo(monkeypatch, capsys):
    inputs = iter(
        [
            "add 5 3",
            "multiply 4 6",
            "undo",
            "redo",
            "history",
            "exit",
        ]
    )
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run_calculator()

    output = capsys.readouterr().out

    assert "Undo completed." in output
    assert "Redo completed." in output
    assert "multiply 4.0 6.0 = 24.0" in output