import csv
from typing import Tuple, List

class CSV:
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath  # Store the file path for reading

    def parse(self) -> Tuple[List, List[List]]:
        try:
            with open(self.filepath, "r", newline='') as file:
                reader = csv.reader(file)
                lines = list(reader)  # Read all lines into a list of lists
        except FileNotFoundError as err:
            print(f"Error: File not found: {self.filepath}")
            raise
        except Exception as err:
            print(f"Error reading file: {err}")
            raise

        if not lines:
            print("Error: File is empty")
            raise ValueError("Empty CSV file")

        try:
            # First line is columns, rest are rows
            cols = lines[0]
            rows = lines[1:]

            # Convert numeric strings in columns
            clean_cols = self.__scheme(cols)
            # Convert numeric strings in each row
            clean_rows = [self.__scheme(row) for row in rows]

            self.__synatax_check(clean_rows,clean_cols)

            return clean_cols, clean_rows
        except Exception as err:
            print(f"Error parsing CSV data: {err}")
            raise

    def __scheme(self, my_list: List, new_list: List = None) -> List: #type: ignore
        if new_list is None:
            new_list = []
        for item in my_list:
            if isinstance(item, str):
                try:
                    new_list.append(int(item))  # Convert numeric strings to int
                except ValueError:
                    try:
                        new_list.append(float(item)) # Keep non-numeric strings as is
                    except ValueError:
                        new_list.append(item)
            else:
                new_list.append(item)  # Keep non-strings as is
        return new_list

    def __synatax_check(self,rows:list[list],cols:list):
        # check for invalid length
        for i in rows:
            if len(i) != len(cols):
                raise SyntaxError("columns and rows do not have the same length")
                exit()

                    
            

    def display(self, columns: List, rows: List[List], lines: int = 15) -> None:
        # Convert all column elements to strings for display
        print(" ".join(str(col) for col in columns))
        print("-" * lines)
        for row in rows:
            # Convert all row elements to striss for iplayrow
            print(" ".join(str(item) for item in row))

def main():
    try:
        data = CSV("/home/ark/csv_parser/Data/test.csv")
        columns, rows = data.parse()
        data.display(columns, rows)

    except Exception as err:
        print(f"Error in main: {err}")

if __name__ == "__main__":
    main()