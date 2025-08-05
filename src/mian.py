def parser(filepath: str,) -> list: # type: ignore

    try:
        with open(filepath, "r") as file:
            unformated_data = file.read()
    except Exception as err:
        print(f"error: {err}    args:{filepath}")
        exit()

    lines = unformated_data.splitlines()
    col = lines[0]
    rows = lines[1:]

    cols = col.split(',')
    row = []

    for i in rows:
        index = i.split(",")
        row.append(index)

    return cols,row # type: ignore


def display(columns, rows, lines=15):
    print(" ".join(columns))
    print("-" * lines)
    for row in rows:
        print(" ".join(row))

        
    
    

def main():
    columns,rows = parser("./test.csv")
    display(columns,rows)

if __name__ == "__main__":
    main()