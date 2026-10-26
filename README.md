# ISM3232 Midterm: Copper Kettle Coffee Roasters

- **Name:** Zenobia Thomas
- **Version:** Final
- **Date:** October 25, 2026

## What This Program Does

This project prices coffee shipments. 'business_rules.py' turns the company's six business rules into eight functions, and 'main.py' runs them over four sample shipments and prints a report: totals, average cost, largest shipment, and how many shipments need prepayment.
## Business Rules

1. The bean cost is the price per bag times the number of bags.
2. The discount depends on the number of bags: Fewer than 20 bags no discount, 20 through 79 bags 9 percent discount, and 80 or more get 14 percent discount.
3. Partner cafes get an extra 4 percentage points of discount, but only on shipments of 20 bags or more. For them, 9% becomes 13% and 14% becomes 18%.
4. A $35 shipping fee is added when the discounted cost is below $250.
5. A shipment total of $1,500 or more requires prepayment.
6. A shipment needs a freight pallet when it has more than 60 bags and its shipment total is over $700.
## How to Run

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

## How to Test

```
ruff format .
ruff check .
pytest -v
```

The test file has 20 tests, including both sides of every limit.

## Files in This Repository

- `business_rules.py`: the constants and the eight functions
- `main.py`: the sample bookings and the report
- `tests/test_business_rules.py`: the pytest tests
- `tests/__init__.py`: an empty file that lets the tests import the functions
- `commands.md`: the terminal commands that built and checked the project, with their output
- `README.md`: this file
- `requirements.txt`: the packages to install
- `.gitignore`: keeps `.venv/` and `__pycache__/` out of the repository

## AI Use Statement

I did not use AI on this exam. 
