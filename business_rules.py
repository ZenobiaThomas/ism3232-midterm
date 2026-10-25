# business_rules.py
# Author: Zenobia Thomas

def calculate_bean_cost(bag_price: float, bags: int) -> float:
    




def get_bulk_discount(bags: int, partner: bool = False) -> float:

def calculate_shipment_total(bag_price: float, bags: int, partner: bool = False) -> float:

def requires_prepayment(total: float) -> bool:

def needs_pallet(bags: int, total: float) -> bool:

def total_shipped(shipments: list) -> float:

def largest_shipment(shipments: list) -> str:

def format_shipment_line(buyer: str, total: float, prepayment: bool, pallet: bool) -> str:
