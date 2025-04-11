import sys
from .parser import Parser
from .exchange import Exchange


def main():
    parser = Parser()
    exchange = Exchange()

    # Read FIX messages from stdin
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            # Decode FIX message and get command
            command = parser.parse_order(line)

            # Decode again to extract ticker for run()
            data = parser.decode(line)
            ticker = data.get("ticker")
            if ticker is None:
                raise ValueError("Missing ticker in FIX message.")

            # Add ticker if not present
            if ticker not in exchange.order_books:
                exchange.add_ticker(ticker)

            # Run command and encode response
            result = command.run(ticker)
            print(parser.encode(result))
        except Exception as e:
            print(
                parser.encode({"message_type": "error", "error": str(e)}),
                file=sys.stderr,
            )
