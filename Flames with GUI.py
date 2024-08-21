import tkinter as tk
from tkinter import messagebox

def flames_count(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    
    count1 = {char: name1.count(char) for char in set(name1)}
    count2 = {char: name2.count(char) for char in set(name2)}

    total_count = sum(count1.values()) + sum(count2.values())
    common_count = sum(min(count1.get(char, 0), count2.get(char, 0)) for char in set(name1) | set(name2))
    remaining_count = total_count - (2 * common_count)

    return remaining_count

def flames_result(remaining_count):
    flames_words = ["Friends", "Lovers", "Affection", "Marriage", "Enemies", "Sibling"]
    index = remaining_count % len(flames_words)
    return flames_words[index - 1]

def calculate_flames():
    name1 = entry_name1.get()
    name2 = entry_name2.get()

    count = flames_count(name1, name2)
    result = flames_result(count)

    messagebox.showinfo("FLAMES Result", f"{name1} and {name2} are {result}!")

# GUI Setup
root = tk.Tk()
root.geometry("450x150")
root["bg"] = "lightgreen"
root.title("FLAMES Game")

label_name1 = tk.Label(root, text="Enter Name 1:", width=15, bg="white", fg="black")
entry_name1 = tk.Entry(root, width=30, bg="white", fg="black", font=("Arial", 12))

label_name2 = tk.Label(root, text="Enter Name 2:", width=15, bg="white", fg="black")
entry_name2 = tk.Entry(root, width=30, bg="white", fg="black", font=("Arial", 12))

calculate_button = tk.Button(root, bg="lightblue", text="Calculate FLAMES", command=calculate_flames)

# Layout
label_name1.grid(row=0, column=0, padx=10, pady=5)
entry_name1.grid(row=0, column=1, padx=10, pady=5)

label_name2.grid(row=1, column=0, padx=10, pady=5)
entry_name2.grid(row=1, column=1, padx=10, pady=5)

calculate_button.grid(row=2, columnspan=2, pady=10)

root.mainloop()
