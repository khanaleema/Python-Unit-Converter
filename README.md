# Unit Converter App

## Overview

This is a simple **Unit Converter App** built using **Python and Streamlit**. It allows users to convert between different units of **length, weight, temperature, speed, and currency**.

## Features

- Convert units for **Length, Weight, Temperature, Speed, and Currency**
- **Conversion History** saved and downloadable as a CSV or JSON file
- **Data Visualization** with interactive charts
- User-friendly **Streamlit UI**

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/khanaleema/Python-Unit-Converter.git
   cd Python-Unit-Converter
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

## Dependencies

- `streamlit`
- `pandas`
- `requests`
- `json`
- `altair`

## File Structure

```
Python-Unit-Converter/
│── app.py          # Main application file
│── requirements.txt # Dependencies
│── history.json    # Stores conversion history
│── currency_rates.json # Stores cached currency rates
│── README.md       # Project documentation
```

## Contributing

Feel free to fork this repository and contribute by submitting pull requests!

## License

This project is for educational purposes and does not have a specific license.
