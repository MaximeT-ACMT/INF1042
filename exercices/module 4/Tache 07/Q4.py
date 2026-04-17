notes = {"math": 78, "Français": 85, "science": 91}

notes["history"] = 88
notes["math"] = 82

for matière, note in notes.items():
    
    print(f"Matière: {matière} | Note: {note}")