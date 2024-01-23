# Python API Data Fetching and Processing

This script is designed to demonstrate the process of fetching data from an API, extracting specific information from the data, and performing type checks on the extracted information. The script is written in Python and utilizes the `requests` library to make HTTP requests.

## Features

- Fetches data from the JSONPlaceholder API.
- Extracts titles from the fetched data.
- Filters titles that contain the substring 'qui'.
- Checks if any title is of integer type.
- Prints out all filtered titles and the result of the type check.

## Requirements

- Python 3.x
- `requests` library

## Usage

1. Ensure Python 3.x is installed on your system.
2. Install the `requests` library using pip:
    `pip install requests`
3. Run the script:
    `python trail_task.py`


## Code Description

The script performs the following steps:

1. **Data Fetching**:
- Makes a GET request to 'https://jsonplaceholder.typicode.com/todos' to fetch data.

2. **Data Processing**:
- Parses the JSON response into a Python list of dictionaries.

3. **Title Extraction**:
- Iterates over each dictionary (representing a to-do item).
- Checks if the dictionary contains the key 'title' and if the associated value is a string.
- Further filters titles that contain the substring 'qui'.

4. **Printing Titles**:
- Prints each filtered title using f-strings for formatted output.

5. **Type Checking**:
- Checks if any of the extracted titles is of type `int`.
- Prints a message indicating whether at least one title is of integer type.

## Note

This script is for demonstration purposes and uses a publicly available API that returns placeholder data.
