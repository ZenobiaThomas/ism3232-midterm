# Terminal Record: [Copper Kettle Coffee Roasters]

## 1. Building the project
```
mkdir ism3232_midterm
cd ~/ism3232/ism_midterm
cd ism3232
mkdir ism3232_midterm
touch business.py main.py commands.md README.md requirements.txt .gitignore
mkdir tests 
touch tests/__init__.py tests/test_business_rules.py
python3 -m venv .venv
source .venv/bin/activate
tree
mv business_rules.py main.py commands.md README.md requirements.txt .gitignore tests ism_midterm/
mv ism3232_midterm ~/ism3232/
cd ~/ism3232
mv ism3232_midterm ism3232-midterm
cd ism3232-midterm
echo '.venv/' > .gitignore
echo '__pycache__/' >> .gitignore
echo '.pytest_cache/' >> .gitignore
echo '.ruff_cache/' >> .gitignore

## 2. The virtual environment
```
which python3
```

```text
/home/zenobia18/ism3232/ism3232-midterm/.venv/bin/python3
```
The path ends in '.venv/bin/python3', so the projects virtual environment is active.
## 3. The project structure
``` 
tree -L 2
```

```
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files
```
The files in ism3232-midterm/ are shown but .venv folder is hidden
## 4. Every function and test
```
rg 'def '
``` 

```
business_rules.py
15:def calculate_bean_cost(bag_price: float, bags: int) -> float:
19:def get_bulk_discount(bags: int, partner: bool = False) -> float:
33:def calculate_shipment_total(bag_price: float, bags: int, partner: bool = False) -> float:
43:def requires_prepayment(total: float) -> bool:
49:def needs_pallet(bags: int, total: float) -> bool:
54:def total_shipped(shipments: list) -> float:
66:def largest_shipment(shipments: list) -> str:
80:def format_shipment_line(buyer: str, total: float, prepayment: bool, pallet: bool) -> str:

tests/test_business_rules.py
12:def test_bean_cost():
15:def test_discount_below_20_bags():
18:def test_discount_at_20_bags():
21:def test_discount_at_79_bags():
24:def test_discount_at_80_bags():
27:def test_partner_discount():
30:def test_no_shipping_fee_at_250():
33:def test_shipping_fee_below_250():
36:def test_shipment_with_discount():
39:def test_prepayment_at_1500():
42:def test_no_prepayment_below_1500():
45:def test_no_pallet_at_60_bags():
48:def test_pallet_at_61_bags():
51:def test_no_pallet_at_700():
54:def test_pallet_above_700():
57:def test_total_shipped():
65:def test_total_shipped_empty():
68:def test_largest_shipment_tie():
74:def test_largest_shipment_empty():
77:def test_format_shipment_line():
```
Business_rules.py has 8 functions and test_business_rules.py has 20 tests.
## 5. Which files print
```
rg -l 'print'
```
```
commands.md
main.py
```
Shows files with the word "print".
## 6. The commit history
```
git log --oneline
```
```
f8eab1c (HEAD -> main, origin/main) Add pytest tests and fix largest shipment
5c411b4 Add shipment report loop and summary counts
7b21736 Copy in shipments
5744a3f Add last three functions and update rules
eda6c7a Add two complete functions
cfccb53 first three complete functions
aceabe2 Add eight function definitions
b2e5435 Midterm project files setup
```
Shows my commits starting with the newest one first.