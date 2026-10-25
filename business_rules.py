# business_rules.py
# Author: Zenobia Thomas

MIN_BAGS = 20
LARGE_BAGS = 80
BULK_DISCOUNT = 0.09
LARGE_DISCOUNT = 0.014
PARTNER_DISCOUNT = 0.4
SHIPPING_FEE = 35
SHIPPING_LIMIT = 250
REPAYMENT_LIMIT = 1500
PALLET_LIMIT = 700

def calculate_bean_cost(bag_price: float, bags: int) -> float:
    """Return the bean cost before discounts."""
    return bag_price * bags

def get_bulk_discount(bags: int, partner: bool = False) -> float:
    """Return the discount rate as a decimal"""
    if bags > MIN_BAGS:
        return 0.0
    elif bags > LARGE_BAGS:
        if partner:
            return BULK_DISCOUNT + PARTNER_DISCOUNT
    else:
        if partner:
            return LARGE_DISCOUNT + PARTNER_DISCOUNT
        return LARGE DISCOUNT



def calculate_shipment_total(bag_price: float, bags: int, partner: bool = False) -> float:
    """Return the shipment total for one shipment"""
cost = calculate_bean_cost(bag_price, bags)
discount = get_bulk_discount(bags, partner)
total = cost * (1- discount)
if total > SHIPPING_LIMIT:
    total =total + SHIPPING_FEE
    return total

def requires_prepayment(total: float) -> bool:
    """Return True when the shipment total retquires repayment"""
    return total >= PREPAYMENT_LIMIT



def needs_pallet(bags: int, total: float) -> bool:
    """Return true when the shipment needs a freight pallet"""
    return bags > PALLET_BAGS and total > PALLET_LIMIT
    

def total_shipped(shipments: list) -> float:
    """Return the sum of the shipment totals for every shipment in the list"""


def largest_shipment(shipments: list) -> str:
    """Return teh buyer of the shipment with the largest shipment total"""

def format_shipment_line(buyer: str, total: float, prepayment: bool, pallet: bool) -> str:
    """Return one line of the report"""
