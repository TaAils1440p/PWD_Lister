# PWD Lister

This project generates 20 million random passwords of 1 to 15 characters and writes them to a CSV file.
> Canbe useful for a John the Ripper dictionnary (FOR EDUCATIONAL PURPOSES ONLY!)

## Structure

- `main.py` — Entry point
- `generator/` — Password generation and CSV writing
- `utils/` — Utility functions (e.g. execution timer)
- `config.py` — Central configuration

## Usage

```bash
python main.py
```

The file `output/passwords.csv` will be generated automatically.

## License

This project is released under the MIT License. See the [LICENSE](./LICENSE) file for more details.