from prettytable import PrettyTable, DOUBLE_BORDER
table = PrettyTable()
table.add_column("names", ["Sonya", "Plamen", "Mishi", "Teo"])
table.add_column("age", [35, 40, 6, 1])
table.align["names"] = "l"
table.align["age"] = "c"
table.set_style(DOUBLE_BORDER)
print(table)