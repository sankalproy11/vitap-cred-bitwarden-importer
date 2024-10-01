# VIT-AP Credential Importer

This Python script converts a CSV file containing `Username` and `Password` into a structured `login.json` file. The JSON follows a predefined format where the username and password are populated for each entry, and unique IDs are assigned starting from `random-id-1`. This `login.json` can be imported into your bitwarden vault.

# Note

If you're from a different VIT, change the uri accordingly in line-24 of `script.py`.

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sankalproy11/vitap-cred-bitwarden-importer
   cd vitap-cred-bitwarden-importer
   ```

## Usage

1. Create a `data.csv` file is in the following format, refer the `sample_data.csv`:

   ```csv
   Username,Password
   21BCEXXXX,pazs5uW1
   21BCEXXXY,pazs5uW2
   21BCEXXXZ,pazs5uW3
   21BCEXXXA,pazs5uW4
   ```

2. Run the script to generate the `login.json` file:

   ```bash
   python script.py
   ```

3. The generated `login.json` file will have entries with the username, password, and other predefined fields.

## License

This project is licensed under the MIT License.
