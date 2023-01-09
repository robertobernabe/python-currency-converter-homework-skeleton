# python-currency-converter-homework-skeleton

# Tasks

1. Fix all bugs or missing code pieces.
2. 

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
4. Install nox, if you want to run your tests via nox
    ```bash
    pip install nox
    ```


## Usage

### Run the tests
You either can run them:
 - In your Python virtual env, via: `pytest tests/`
 - Or by executing `nox -s tests`



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
Running `gui-currency-converter.exe` within your python virtual environment should start the gui.
