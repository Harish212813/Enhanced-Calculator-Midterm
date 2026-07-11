# Enhanced Calculator Midterm Project

## About the Project

For this midterm project, I built an enhanced calculator using Python. The calculator can perform basic and advanced math operations, keep track of calculation history, save and load history from a CSV file, and support undo and redo. I also added logging, input validation, and custom error handling to make the program more reliable.

This project also uses the Factory, Memento, and Observer design patterns that we learned in class.

## Features

### Calculator Operations

* Add
* Subtract
* Multiply
* Divide
* Power
* Root
* Modulus
* Integer Division
* Percentage
* Absolute Difference

### Commands

* history
* clear
* undo
* redo
* save
* load
* help
* exit

## Project Structure

```text
enhanced-calculator-midterm/
│
├── app/
├── tests/
├── .github/
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Harish212813/Enhanced-Calculator-Midterm.git
```

Go into the project folder:

```bash
cd Enhanced-Calculator-Midterm
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the Calculator

Run the following command:

```bash
python -m app.calculator_repl
```

When the calculator starts, you can enter commands like these:

```text
add 5 3
subtract 10 4
multiply 6 2
divide 20 5
power 2 3
root 9 2
modulus 10 3
int_divide 10 3
percent 25 100
abs_diff 5 12
```

You can also use these commands:

```text
history
clear
undo
redo
save
load
help
exit
```

## Testing

To run all the tests:

```bash
pytest -v
```

To check the test coverage:

```bash
pytest --cov=app --cov-report=term-missing
```

All of my tests are passing, and the project has more than 90% test coverage.

## GitHub Actions

I set up GitHub Actions so the tests run automatically every time I push changes to the main branch. This helped me make sure everything was still working after making updates to the project.

## Error Handling

I added error handling for different situations, including:

* Division by zero
* Invalid numbers
* Invalid commands
* Missing input values
* Invalid root calculations
* Problems reading or saving the history file

Instead of crashing, the calculator prints an error message and lets the user continue.

## Logging

The calculator records calculations and important events in a log file. This makes it easier to see what operations were performed and helps with debugging if something goes wrong.

## What I Learned

This project gave me more practice working with object-oriented programming, design patterns, unit testing, GitHub Actions, and using pandas to save and load data. It also helped me get more comfortable building a larger Python project by connecting different classes and features together.
