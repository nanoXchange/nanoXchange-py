import sys
import time
from .parser import Parser
from .exchange import Exchange
from .benchmark import Benchmark


def main():
    parser = Parser()
    exchange = Exchange()
    benchmark = Benchmark()

    # Read FIX messages from stdin
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            # Record the start time for benchmarking
            start = time.perf_counter()
            # Decode FIX message and get command
            command = parser.parse_order(line)
            benchmark.record("parse", time.perf_counter() - start)

            start = time.perf_counter()
            # Decode again to extract ticker for run()
            data = parser.decode(line)
            ticker = data.get("ticker")
            benchmark.record("decode", time.perf_counter() - start)
            if ticker is None:
                raise ValueError("Missing ticker in FIX message.")

            # Add ticker if not present
            if ticker not in exchange.order_books:
                exchange.add_ticker(ticker)

            start = time.perf_counter()
            # Run command and encode response
            result = command.run(ticker)
            benchmark.record("command_run", time.perf_counter() - start)

            start = time.perf_counter()
            print(parser.encode(result))
            benchmark.record("encode", time.perf_counter() - start)
        except Exception as e:
            print(
                parser.encode({"message_type": "error", "error": str(e)}),
                file=sys.stderr,
            )

    # Print benchmark report
    benchmark.report()
