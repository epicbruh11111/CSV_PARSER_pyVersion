CSV Parser
A lightweight Python-based CSV parser for reading and processing CSV files, handling common edge cases such as quoted fields, empty fields, and custom delimiters. The next version of this parser is planned to be implemented in C++ for improved performance.
Features

Parses CSV files into a structured format with columns (headers) and rows (data).
Supports common CSV edge cases:
Quoted fields with commas (e.g., "Developer, Senior")
Empty fields (e.g., ,, or ,"",)
Line breaks within quoted fields (e.g., "Line 1\nLine 2")
Custom delimiters (e.g., ,, ;, \t)
Various line endings (\n, \r, \r\n)


Simple API for loading and parsing CSV files.
Error handling for malformed CSV rows.

Warning: The current version does not compile escape sequences like \n, \t, or commas (,) inside strings as literal characters. These are treated as part of the string content. For example, \n in a quoted field will be preserved as the characters \ and n, not interpreted as a newline. This limitation will be addressed in future versions.
Installation

Ensure Python 3.6+ is installed.
Clone the repository:git clone <repository-url>


Navigate to the project directory:cd csv-parser


(Optional) Install dependencies for development or testing:pip install -r requirements.txt



Usage
The parser provides a simple interface to load a CSV file, parse it into columns and rows, and display the results.
Example
from csv_parser import CSVParser

# Load and parse a CSV file
data = CSVParser('example.csv')
col, row = data.parse()

# Display the parsed data
display(col, row)

Example Input (example.csv)
name,age,description,city
John,30,"Developer, Senior",New York
Mary,,,"San Francisco"
José,25,"Line 1\nLine 2","São Paulo"
"Jane ""JD"" Doe",40,"He said ""hello""","Paris"

Example Output
Columns: ['name', 'age', 'description', 'city']
Rows: [
    ['John', '30', 'Developer, Senior', 'New York'],
    ['Mary', '', '', 'San Francisco'],
    ['José', '25', 'Line 1\nLine 2', 'São Paulo'],
    ['Jane "JD" Doe', '40', 'He said "hello"', 'Paris']
]

API

CSVParser(filepath): Initialize the parser with the path to a CSV file.
parse(): Parse the CSV file and return a tuple (columns, rows) where:
columns: List of header names (first row).
rows: List of lists containing the data rows.


display(columns, rows): Utility function to print the parsed columns and rows in a readable format.

Limitations

Escape Sequences: Special characters like \n, \t, or commas (,) within quoted strings are not compiled/interpreted (e.g., \n is treated as literal \n, not a newline). This is by design to preserve raw string content but may be enhanced in the C++ version.
Performance: The Python version may not be optimized for very large CSV files (>1GB). The upcoming C++ version will address this with better memory management and performance.
Encoding: Currently assumes UTF-8 encoding. Support for other encodings (e.g., UTF-16, ISO-8859-1) is limited.
Error Handling: Basic error handling is implemented, but complex recovery from malformed CSVs (e.g., unclosed quotes) is not fully supported.

Future Work

C++ Version: The next version will be rewritten in C++ for better performance, especially for large files, and will include:
Support for compiling escape sequences (e.g., \n as a newline).
Enhanced error recovery for malformed CSVs.
Broader encoding support.
Streaming parsing for memory efficiency.


Additional features like custom delimiter detection and validation of header uniqueness.

Contributing
Contributions are welcome! Please submit a pull request or open an issue for bug reports or feature suggestions.

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m "Add feature").
Push to the branch (git push origin feature-branch).
Open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
