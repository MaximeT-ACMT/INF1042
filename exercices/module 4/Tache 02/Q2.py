file_path = "exemples/module4/valeurs.txt"

values = []

try:
    with open(file_path, "r") as f:
        for line in f:
            # Strip whitespace/newlines and convert to integer
            values.append(int(line.strip()))

    if values:
        v_max = max(values)
        v_min = min(values)
        average = sum(values) / len(values)

        print(f"Statistics for {file_path}:")
        print(f"- Maximum Value: {v_max}")
        print(f"- Minimum Value: {v_min}")
        print(f"- Average: {average:.2f}")

except FileNotFoundError:
    print("Error: 'valeurs.txt' not found. Please run q1.py first.")