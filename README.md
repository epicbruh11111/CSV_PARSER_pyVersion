🌟 CSV Parser Extravaganza 🐍
Welcome to the ultimate Python CSV parser! 🎉 This bad boy slices and dices CSV files into neat columns and rows, handling all the tricky stuff like quoted fields and custom delimiters. A C++ version is in the works to make it lightning-fast! ⚡️
⚠️ HEADS UP: We CANNOT compile or interpret \n, \t, commas (,), or quotes (") inside strings. They’re treated as literal characters (e.g., \n stays \n, not a newline; " inside strings is just "). This is a hard limit for now, but we’ll tackle it in the C++ version. 😎
🚀 Features

Turns CSV files into tidy columns (headers) and rows (data). 📋

Simple API to load, parse, and display CSVs. 🛠️
Basic error handling for wonky rows. 🚨

🛠️ Setup

Make sure you’ve got Python 3.6+ ready to roll. 🐍
Clone the repo:git clone <repository-url>


Jump into the project folder:cd csv-parser




🎯 How to Use It
Load a CSV, parse it into columns and rows, and show off the results.
Example Code
from csv_parser import CSVParser

# Load and parse your CSV
data = CSVParser('example.csv')
col, row = data.parse()

# Show the goods
display(col, row)

Sample Input (example.csv)
name,age,description,city
John,30,"Developer, Senior",New York
Mary,,,"San Francisco"
José,25,"Line 1\nLine 2","São Paulo"
"Jane ""JD"" Doe",40,"He said ""hello""","Paris"

Sample Output
Columns: ['name', 'age', 'description', 'city']
Rows: [
    ['John', '30', 'Developer, Senior', 'New York'],
    ['Mary', '', '', 'San Francisco'],
    ['José', '25', 'Line 1\nLine 2', 'São Paulo'],
    ['Jane "JD" Doe', '40', 'He said "hello"', 'Paris']
]

API Breakdown

CSVParser(filepath): Kicks things off with your CSV file path. 📂
parse(): Returns (columns, rows) where:
columns: List of header names. 📌
rows: List of data rows. 📑


display(columns, rows): Prints everything in a nice, readable format. 🖨️

Limitations

No Escape Sequence Magic: \n, \t, commas (,), and quotes (") in strings are kept as literal characters. We CANNOT compile them (e.g., \n won’t turn into a newline).
Big Files: Not great for massive CSVs (>1GB). The C++ version will handle these like a champ. 💪
Encoding: Sticks to UTF-8 for now. Other encodings (e.g., UTF-16) might trip it up. 🌐
Error Handling: Catches basic errors, but super messy CSVs (e.g., unclosed quotes) can still cause havoc. 🚧

🔮 What’s Next?

C++ Version: Coming soon to crush it with:
Speedy performance for huge files. ⚡️
Better encoding support. 🌍
Tougher error handling. 🛡️


📜 License
MIT License. Check out LICENSE for the deets. 📄
