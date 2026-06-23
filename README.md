# CSV Parser

A Python CSV parser designed to process CSV files into structured columns and rows while handling common CSV features such as quoted fields and custom delimiters. A C++ version is planned to improve performance and scalability.

## Important Limitation

**Current Limitation:** The parser cannot compile or interpret escape sequences or special characters such as `\n`, `\t`, commas (`,`), or quotation marks (`"`) inside strings. These are treated as literal characters. For example:

* `\n` remains the two-character sequence `\n` rather than becoming a newline.
* `\t` remains the two-character sequence `\t` rather than becoming a tab.

This limitation is expected to be addressed in the future C++ implementation.

## Features

* Parses CSV files into structured columns (headers) and rows (data).
* Provides a simple API for loading, parsing, and displaying CSV data.
* Includes basic error handling for malformed rows.

## Requirements

* Python 3.6 or later.

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd csv-parser
```

## Usage

Load a CSV file, parse its contents, and display the resulting columns and rows.

### Example Code

```python
from csv_parser import CSVParser

# Load and parse the CSV file
data = CSVParser('example.csv')
col, row = data.parse()

# Display the results
display(col, row)
```

### Sample Input (`example.csv`)

```csv
name,age,description,city
John,30,"Developer, Senior",New York
Mary,,,"San Francisco"
José,25,"Line 1\nLine 2","São Paulo"
"Jane ""JD"" Doe",40,"He said ""hello""","Paris"
```

### Sample Output

```python
Columns: ['name', 'age', 'description', 'city']
Rows: [
    ['John', '30', 'Developer, Senior', 'New York'],
    ['Mary', '', '', 'San Francisco'],
    ['José', '25', 'Line 1\nLine 2', 'São Paulo'],
    ['Jane "JD" Doe', '40', 'He said "hello"', 'Paris']
]
```

## API Reference

### `CSVParser(filepath)`

Creates a parser instance using the specified CSV file path.

**Parameters:**

* `filepath` (`str`): Path to the CSV file.

### `parse()`

Parses the CSV file and returns a tuple containing columns and rows.

**Returns:**

* `columns`: List of header names.
* `rows`: List of parsed data rows.

### `display(columns, rows)`

Displays the parsed columns and rows in a readable format.

## Limitations

### Escape Sequence Handling

The parser does not interpret escape sequences. Characters such as `\n`, `\t`, commas (`,`), and quotation marks (`"`) within strings are treated as literal text.

### Large Files

Performance may be limited when processing very large files (greater than 1 GB). The planned C++ version is intended to improve performance for large datasets.

### Encoding Support

The parser currently assumes UTF-8 encoding. Other encodings, such as UTF-16, may not be fully supported.

### Error Handling

Basic validation is included, but severely malformed CSV files (such as files containing unclosed quotation marks) may still cause parsing issues.

## Future Development

The planned C++ implementation aims to provide:

* Improved performance for large files.
* Expanded encoding support.
* More robust error handling and validation.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
