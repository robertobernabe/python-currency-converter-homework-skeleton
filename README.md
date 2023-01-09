# python-currency-converter-homework-skeleton

## Setup Dev Environment

1. Create an virtual environment 

    ```bash
    python -m venv venv
    ```

2. Activate it 
- Windows: `venv\Scripts\activate`
- Linux: `source bin/activate`

3. Install it as editable 

    ```bash
    pip install -e .[tests]
    ```

## Installation
## Usage
### Cli

```bash
currency-converter.exe 200 chf_usd

From CHF to USD
214.0
```

```bash
currency-converter.exe 200 chf_usd --reverse

From USD to CHF
186.92
```

### GUI
Running `gui-currency-converter.exe` should start the gui.