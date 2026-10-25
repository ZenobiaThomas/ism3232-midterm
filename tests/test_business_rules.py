from business_rules import (
    calculate_bean_cost,
    calculate_shipment_total,
    format_shipment_line,
    get_bulk_discount,
    largest_shipment,
    needs_pallet,
    requires_prepayment,
    total_shipped,
)


def test_bean_cost():
    assert calculate_bean_cost(10.00, 5) == 50.00


def test_discount_below_20_bags():
    assert get_bulk_discount(19) == 0.0


def test_discount_at_20_bags():
    assert get_bulk_discount(20) == 0.09


def test_discount_at_79_bags():
    assert get_bulk_discount(79) == 0.09


def test_discount_at_80_bags():
    assert get_bulk_discount(80) == 0.14


def test_partner_discount():
    assert round(get_bulk_discount(20, True), 2) == 0.13


def test_no_shipping_fee_at_250():
    assert round(calculate_shipment_total(250.00, 1), 2) == 250.00


def test_shipping_fee_below_250():
    assert round(calculate_shipment_total(249.99, 1), 2) == 284.99


def test_shipment_with_discount():
    assert round(calculate_shipment_total(10.00, 20), 2) == 217.00


def test_prepayment_at_1500():
    assert requires_prepayment(1500.00) is True


def test_no_prepayment_below_1500():
    assert requires_prepayment(1499.99) is False


def test_no_pallet_at_60_bags():
    assert needs_pallet(60, 800.00) is False


def test_pallet_at_61_bags():
    assert needs_pallet(61, 800.00) is True


def test_no_pallet_at_700():
    assert needs_pallet(61, 700.00) is False


def test_pallet_above_700():
    assert needs_pallet(61, 700.01) is True


def test_total_shipped():
    shipments = [
        {"buyer": "A", "bag_price": 10.00, "bags": 10, "partner": False},
        {"buyer": "B", "bag_price": 20.00, "bags": 20, "partner": False},
    ]
    assert round(total_shipped(shipments), 2) == 499.00


def test_total_shipped_empty():
    assert total_shipped([]) == 0.0


def test_largest_shipment_tie():
    shipments = [
        {"buyer": "A", "bag_price": 10.00, "bags": 40, "partner": False},
        {"buyer": "B", "bag_price": 10.00, "bags": 40, "partner": False},
    ]
    assert largest_shipment(shipments) == "A"


def test_largest_shipment_empty():
    assert largest_shipment([]) == ""


def test_format_shipment_line():
    line = format_shipment_line("Coffee Shop", 1500.00, True, False)
    assert line == "Coffee Shop: $1500.00 | prepayment: yes | pallet: no"
