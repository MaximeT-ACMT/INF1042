source_path = "exemples/module4/valeurs.txt"
low_path = "exemples/module4/bas.txt"
high_path = "exemples/module4/haut.txt"

try:
    with open(source_path, "r") as f_in, \
         open(low_path, "w") as f_low, \
         open(high_path, "w") as f_high:

        for line in f_in:
            value = int(line.strip())
            
            if value < 50000:
                f_low.write(f"{value}\n")
            else:
                f_high.write(f"{value}\n")

    print("Distribution complete: 'bas.txt' (0-49,999) and 'haut.txt' (50,000-100,000).")

except FileNotFoundError:
    print("Error: Source file not found.")