import random

# Corrected enums from utils.py
ORDER_SIDES = ["BUY", "SELL"]
ORDER_TYPES = ["LIMIT", "MARKET"]
MESSAGE_TYPES = ["D", "F", "8"]
TICKERS = ["AAPL", "TSLA", "MSFT", "NVDA", "GOOG"]

# Generate messages
message_count = 500
order_id = 1
order_ids = []  # To track valid order IDs for cancel messages
messages = []

for _ in range(message_count):
    msg_type = random.choices(MESSAGE_TYPES, weights=[80, 10, 10])[0]
    ticker = random.choice(TICKERS)

    if msg_type == "D":  # New order
        order_type = random.choice(ORDER_TYPES)
        side = random.choice(ORDER_SIDES)
        quantity = random.randint(1, 100)
        order_tag = f"O{order_id}"

        if order_type == "LIMIT":
            price = round(random.uniform(100, 300), 2)
            msg = f"35=D|11={order_type}|38={quantity}|39={ticker}|44={price}|54={side}"
        else:  # MARKET
            msg = f"35=D|11={order_type}|38={quantity}|39={ticker}|54={side}"

        order_ids.append(order_tag)
        order_id += 1

    elif msg_type == "F" and order_ids:  # Cancel order
        cancel_id = random.choice(order_ids)
        msg = f"35=F|57={cancel_id}|39={ticker}"

    else:  # Display order book
        msg = f"35=8|39={ticker}"

    messages.append(msg)

# Save to file
file_path = "test/server/integration/in/bulk_orders.in"
with open(file_path, "w") as f:
    for msg in messages:
        f.write(msg + "\n")