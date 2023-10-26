import tkinter as tk
from tkinter import simpledialog, messagebox

def rightmost_derivation(cfg, current, target, depth=0):
    if current == target:
        return [current]

    if len(current) > len(target) or depth > len(target):
        return None

    for i in range(len(current) - 1, -1, -1):
        if current[i] in cfg:
            for prod in sorted(cfg[current[i]], key=lambda x: (len(x), x)):
                new_string = current[:i] + prod + current[i+1:]
                result = rightmost_derivation(cfg, new_string, target, depth+1)
                if result:
                    return [current] + result
            break

    return None

def main():
    root = tk.Tk()
    root.withdraw()  # Hide main window

    cfg = {}

    start_symbol = simpledialog.askstring("Input", "Enter the start symbol:", parent=root)

    n = simpledialog.askinteger("Input", "Enter the number of productions:", parent=root)
    for _ in range(n):
        production = simpledialog.askstring("Input", "Enter the production (Example: S -> aSb|bSa|ε):", parent=root)
        lhs, rhs = production.split("->")
        cfg[lhs.strip()] = [prod.strip() for prod in rhs.split("|")]

    w = simpledialog.askstring("Input", "Enter the string to derive:", parent=root)

    derivation = rightmost_derivation(cfg, start_symbol, w)

    if derivation:
        result = "\n".join(derivation)
        messagebox.showinfo("Rightmost Derivation", result)
    else:
        messagebox.showinfo("Result", f"The string {w} cannot be derived using the given CFG.")

if __name__ == "__main__":
    main()
