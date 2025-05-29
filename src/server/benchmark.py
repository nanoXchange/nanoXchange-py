import statistics
import sys


class Benchmark:
    def __init__(self):
        self.timings = {}

    def record(self, key, duration):
        if key not in self.timings:
            self.timings[key] = []
        self.timings[key].append(duration)

    def report(self, stream=None):
        stream = stream or sys.stderr
        print("\n=== Benchmark Report ===", file=stream)
        for key, times in self.timings.items():
            avg = statistics.mean(times) * 1e6
            p99 = statistics.quantiles(times, n=100)[98] * 1e6
            print(f"{key:<12} Avg: {avg:.2f} µs | P99: {p99:.2f} µs", file=stream)
        print("=========================\n", file=stream)
