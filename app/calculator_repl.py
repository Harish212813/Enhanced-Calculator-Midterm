from app.calculator import Calculator


def show_help():
    print("\nAvailable commands:")
    print("add <number> <number>")
    print("subtract <number> <number>")
    print("multiply <number> <number>")
    print("divide <number> <number>")
    print("power <number> <number>")
    print("root <number> <number>")
    print("modulus <number> <number>")
    print("int_divide <number> <number>")
    print("percent <number> <number>")
    print("abs_diff <number> <number>")
    print("history")
    print("clear")
    print("undo")
    print("redo")
    print("save")
    print("load")
    print("help")
    print("exit\n")


def run_calculator():
    calculator = Calculator()

    print("Enhanced Calculator")
    print("Type 'help' to view available commands.")

    while True:
        user_input = input(">>> ").strip()

        if not user_input:
            continue

        parts = user_input.split()
        command = parts[0].lower()

        if command == "exit":
            print("Goodbye!")
            break

        if command == "help":
            show_help()
            continue

        if command == "history":
            history = calculator.get_history()

            if not history:
                print("History is empty.")
            else:
                for calculation in history:
                    print(
                        f"{calculation.operation} "
                        f"{calculation.operand_a} "
                        f"{calculation.operand_b} "
                        f"= {calculation.calculate()}"
                    )
            continue

        if command == "clear":
            calculator.clear_history()
            print("History cleared.")
            continue

        if command == "undo":
            calculator.undo()
            print("Undo completed.")
            continue

        if command == "redo":
            calculator.redo()
            print("Redo completed.")
            continue

        if command == "save":
            try:
                calculator.save_history("history.csv")
                print("History saved to history.csv.")
            except Exception as error:
                print(f"Error saving history: {error}")
            continue

        if command == "load":
            try:
                calculator.load_history("history.csv")
                print("History loaded from history.csv.")
            except Exception as error:
                print(f"Error loading history: {error}")
            continue

        valid_operations = [
            "add",
            "subtract",
            "multiply",
            "divide",
            "power",
            "root",
            "modulus",
            "int_divide",
            "percent",
            "abs_diff",
        ]

        if command not in valid_operations:
            print("Unknown command. Type 'help' to view commands.")
            continue

        if len(parts) != 3:
            print("Enter a command followed by two numbers.")
            continue

        try:
            operand_a = float(parts[1])
            operand_b = float(parts[2])

            result = calculator.calculate(command, operand_a, operand_b)
            print(f"Result: {result}")

        except ValueError as error:
            print(f"Error: {error}")

        except Exception as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    run_calculator()