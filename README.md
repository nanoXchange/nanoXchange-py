# ⚡ nanoXchange-py: FIX-Based Limit Order Book Simulator (Python)

`nanoXchange-py` is a **FIX-style message-driven Limit Order Book simulator**, purpose-built in Python for rapid experimentation, educational exploration, and pre-production prototyping. It emulates the core mechanics of a trading exchange — including matching limit/market orders with price-time priority, managing multiple tickers, and dynamically evolving order books.

This simulator provides a launchpad for the future high-performance system `nanoXchange` (C++), and is ideal for **quantitative developers, system designers**, and **exchange engineers** looking to sharpen their edge or build novel infrastructure.

---

## 🎯 Project Goals

- 📈 Prototype order matching algorithms using FIX-style interfaces
- 🧠 Learn realistic exchange design patterns via Python OOP
- 🔁 Provide a stepping stone toward high-performance C++ deployments
- 🛠️ Build tools for testing HFT strategies and exchange logic

---

## 🧩 Key Concepts & Design Patterns

- **FIX Protocol Emulation**: All orders are submitted, parsed, and returned using a human-readable FIX-style protocol.
- **Modular OOP Architecture**:
  - `Exchange` uses the **Singleton Pattern** for global state
  - `Command` classes follow the **Command Pattern** for encapsulated request handling
  - `Parser` handles encoding/decoding and acts as the protocol translator
- **MatchEngine** follows **Separation of Concerns**, isolating trade execution logic
- **OrderBook** uses **heap-based priority queues** for price-time management
- Clean extensibility for logging, networking, or analytics

---

## 🛠️ Features

- ✅ FIX-style order interface (e.g. `35=D|57=O1|39=AAPL|...`)
- ✅ Market and Limit order support
- ✅ Modular, extensible class-based architecture
- ✅ Matching logic based on price-time priority
- ✅ Clean separation of parsing, exchange, order book, and match engine
- ✅ Unit tests covering core command and matching components
- 🔧 Ready for integration with:
  - UDP/TCP clients and servers
  - Historical scenario replays
  - GUI / REST APIs

---

## 🚀 Dev Workflow

```bash
git clone https://github.com/nanoXchange/nanoXchange-py.git
cd nanoXchange-py
make setup        # Create & activate virtual environment
pip install -r requirements.txt
make run          # Launch interactive CLI (TODO)
```

---

## 💡 User Guide (FIX-style CLI)

Once inside the prompt, use FIX-style messages:

```
35=D|57=O1|39=AAPL|38=5|54=BUY|11=LIMIT|55=151.0
35=D|57=O2|39=AAPL|38=3|54=SELL|11=MARKET
35=8|39=AAPL
EXIT
```

- `35=D`: Place order
- `35=F`: Cancel order
- `35=8`: Display order book

---

## ✅ Running Tests

```bash
make test
```

---

## 📌 Freezing Dependencies

```bash
make freeze
# runs: pip freeze > requirements.txt
```

---

## 🛣️ Roadmap

### Near-term (Python)

- [x] FIX-based CLI with parsing + encoding
- [x] Limit and market matching via MatchEngine
- [x] Command-based architecture (Add, Cancel, Display)
- [x] CI workflow + pre-commit hooks (`black`, `ruff`)
- [ ] Add structured event logger
- [ ] Add scenario replay tool (JSON/CSV)

### Mid-term

- [ ] Add support for batch orders
- [ ] Add UDP networking interface
- [ ] Add trade log ingestion + replay

### Long-term (C++)

- [ ] Port core engine to high-performance `nanoXchange` (C++)
- [ ] Connect bots and client APIs to simulation
- [ ] Simulate real market dynamics and microstructure

---

## 🤝 Contributing

We welcome contributions from quant devs, exchange engineers, and curious hackers.

1. Fork this repo
2. Create a new feature branch
3. Submit a pull request with clear commits and passing tests

---

## 📜 License

This project is licensed under the MIT License. See [LICENSE](./LICENSE).

---

## 🙌 Acknowledgements

- Inspired by professional matching engine architecture
- Designed for education, experimentation, and performance evolution
- Built by:
  - [Julian Tay](https://github.com/juliantayyc)
  - [Nihal Ramesh](https://github.com/nihalramesh)

---

## 📬 Contact

📧 Questions or collaboration ideas?  
📂 Open an [Issue](https://github.com/nanoXchange/nanoXchange-py/issues)  
🚀 Stay tuned for the C++ version: `nanoXchange`
