# business_rules.py
# Author: Zenobia Thomas

def calculate_bean_cost(bag_price: float, bags: int) -> float:
    """Return the bean cost before discounts."""
    return bag_price * bags 

def get_bulk_discount(bags: int, partner: bool = False) -> float:
    """Return the discount rate as a decimal"""

def calculate_shipment_total(bag_price: float, bags: int, partner: bool = False) -> float:
    """Return the shipment total for one shipment"""

def requires_prepayment(total: float) -> bool:
    """Return True when the shipment total retquires repayment"""


def needs_pallet(bags: int, total: float) -> bool:
    """Return true when the shipment needs a freight pallet"""

def total_shipped(shipments: list) -> float:
    """Return the sum of the shipment totals for every shipment in the list"""


def largest_shipment(shipments: list) -> str:
    """Return teh buyer of the shipment with the largest shipment total"""

def format_shipment_line(buyer: str, total: float, prepayment: bool, pallet: bool) -> str:
    """Return one line of the report"
