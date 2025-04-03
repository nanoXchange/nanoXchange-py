# ⚡ nanoXchange-py: Limit Order Book Simulator (Python)

`nanoXchange-py` is a modular, interactive **Limit Order Book (LOB)** simulator written in Python. It simulates core mechanics of a financial exchange — including placing limit/market orders, executing trades, and maintaining a dynamic order book with price-time priority.

This project serves as a **precursor to `nanoXchange`**, a high-performance C++ implementation. `nanoXchange-py` allows developers to **prototype ideas, learn trading system design**, and validate algorithms quickly in Python before porting them to a lower-level production-grade environment.

---

## 🎯 Project Goals

- 🔍 Rapid prototyping of order matching logic and microstructure features
- 🧠 Learn and explore exchange system design in Python
- 🚀 Prepare for performance-critical implementation in C++

---

## 🛠️ Features

- ✅ Limit and Market order support
- ✅ Price-time priority matching algorithm
- ✅ Modular object-oriented design
- ✅ Interactive CLI for manual order placement
- ✅ Unit tests for core components
- ⚙️ Clean architecture for easy extension to:
  - Networking (e.g. UDP client/server)
  - Analytics and trade logging
  - GUI or REST APIs

---

---

## 🚀 Getting Started (Development Workflow)

### 1. Clone the repo

```bash
git clone https://github.com/nanoXchange/nanoXchange-py.git
cd nanoXchange-py
```

### 2. Create and activate a virtual environment

```bash
make setup
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the CLI

```bash
make run
```

You’ll enter an interactive prompt where you can:

```
PLACE,LIMIT,BUY,100.0,5,order1
PLACE,MARKET,SELL,0,3,order2
SHOW
EXIT
```

## Running Tests

```bash
make test
```

## Freezing Dependencies

If you install a new package (e.g., black, pytest), freeze it:

```bash
make freeze
```

This performs `pip freeze > requirements.txt`

---

## 🛣️ Roadmap

We plan to extend `nanoXchange-py` to serve both as a robust simulation platform and a stepping stone toward a C++ implementation.

### ✅ Near-term goals (Python)

- [x] CLI-based limit order book
- [x] Market and limit order matching
- [x] Unit test coverage with `pytest`
- [x] Clean, testable modular architecture
- [ ] Implement `EventLogger` for structured trade logs
- [ ] Add CSV-based or JSON-based scenario replay
- [ ] Pre-commit hooks for formatting, linting (`black`, `ruff`)
- [ ] Add CI workflow with GitHub Actions

### 🔄 Intermediate goals

- [ ] Add UDP-based client-server networking interface
- [ ] Implement in-memory metrics (order volume, latency stats)
- [ ] Benchmark core engine under stress test conditions
- [ ] Add support for iceberg/hidden orders (POC)

### 🚀 Long-term goals

- [ ] Port to high-performance C++ version (`nanoXchange`)
- [ ] Integrate with C++ trading bot simulator
- [ ] Allow external interaction with nanoXchange for simulated market data and matching

---

## 📜 License

This project is licensed under the **MIT License**. See [LICENSE](./LICENSE) for details.

---

## 🤝 Contributing

We welcome contributions! To contribute:

1. Fork the repo
2. Create a new branch (`git checkout -b feature/awesome-feature`)
3. Commit your changes
4. Push to the branch (`git push origin feature/awesome-feature`)
5. Open a Pull Request

Please follow the existing code style and ensure all tests pass before submitting.

---

## 🙌 Acknowledgements

- Inspired by real-world exchange architecture and matching engines
- Developed as part of a learning and prototyping initiative by:
  - [Julian Tay](https://github.com/juliantayyc)
  - [Nihal Ramesh](https://github.com/nihalramesh)

---

## 💬 Contact

For questions, feedback, or collaboration:

📧 Email us  
📂 Open an [Issue](https://github.com/nanoXchange/nanoXchange-py/issues)

<!-- 🌐 Visit our [main nanoXchange repo (C++)](https://github.com/nanoXchange/nanoXchange) when released -->
