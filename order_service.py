import uuid

PARTS_DATA = {
    "A": {"price": 10.28, "name": "LED Screen"},
    "B": {"price": 24.07, "name": "OLED Screen"},
    "C": {"price": 33.30, "name": "AMOLED Screen"},
    "D": {"price": 25.94, "name": "Wide-Angle Camera"},
    "E": {"price": 32.39, "name": "Ultra-Wide-Angle Camera"},
    "F": {"price": 18.77, "name": "USB-C Port"},
    "G": {"price": 15.13, "name": "Micro-USB Port"},
    "H": {"price": 20.00, "name": "Lightning Port"},
    "I": {"price": 42.31, "name": "Android OS"},
    "J": {"price": 45.00, "name": "iOS OS"},
    "K": {"price": 45.00, "name": "Metallic Body"},
    "L": {"price": 30.00, "name": "Plastic Body"}
}

def validate_order(components):
    component_types = set(PARTS_DATA[code]["name"].split(" ")[0] for code in components)
    return len(component_types) == len(set(["Screen", "Camera", "Port", "OS", "Body"]))

def calculate_total_price(components):
    total_price = sum(PARTS_DATA[code]["price"] for code in components)
    return total_price

def create_order(components):
    if not validate_order(components):
        return None

    total_price = calculate_total_price(components)
    order_id = str(uuid.uuid4())
    parts = [PARTS_DATA[code]["name"] for code in components]

    return {
        "order_id": order_id,
        "total": total_price,
        "parts": parts
    }