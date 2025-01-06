import tkinter as tk

# This is a code to help Americans understand the scale of the Meter and Milimeter.
# It also shows Europeans how stupidly large "AMURICAN" cars are.
# I say this as an American. WHY?????

root = tk.Tk()
root.title("Cadillactic Converter- Metric to American Units")
root.geometry("500x500")
root.state("zoomed")
root.config(bg="white")

conversion_to_frame = tk.Frame(root, bg="white")
conversion_to_frame.pack(side="top", fill="both", expand=True)

conversion_from_frame = tk.Frame(root, bg="white")

def convert_from_frame():
    conversion_to_frame.pack_forget()
    conversion_from_frame.pack(side="top", fill="both", expand=True)

def convert_to_frame():
    conversion_from_frame.pack_forget()
    conversion_to_frame.pack(side="top", fill="both", expand=True)

frame_swapper = tk.Button(conversion_to_frame, text="Swap", command=convert_from_frame)
frame_swapper.pack(side="bottom", pady=20)

frame_from_swapper = tk.Button(conversion_from_frame, text="Swap", command=convert_to_frame)
frame_from_swapper.pack(side="bottom", pady=20)

title_to = tk.Label(conversion_to_frame, text="Cadillactic Converter: Metric to American", font=("Arial", 24), bg="white", fg="black").pack(side="top", pady=50, fill=tk.X)

title_from = tk.Label(conversion_from_frame, text="Cadillactic Converter: American to Metric", font=("Arial", 24), bg="white", fg="black").pack(side="top", pady=50, fill=tk.X)

entrybox_to = tk.Entry(conversion_to_frame, font=("Arial", 12), fg="black", bg="white", width=40)
entrybox_to.pack(side="top", pady=10)

entrybox_from = tk.Entry(conversion_from_frame, font=("Arial", 12), fg="black", bg="white", width=40)
entrybox_from.pack(side="top", pady=10)

result_label_to = tk.Label(conversion_to_frame, text=" ", font=("Arial", 12), bg="white", fg="black")
result_label_to.pack(side="top", pady=10)

result_label_from = tk.Label(conversion_from_frame, text=" ", font=("Arial", 12), bg="white", fg="black")
result_label_from.pack(side="top", pady=10)

conversion_var_car_to = tk.StringVar()
conversion_var_car_to.set("Select Vehicle")

conversion_var_car_from = tk.StringVar()
conversion_var_car_from.set("Select Vehicle")

conversion_var_metric_to = tk.StringVar()
conversion_var_metric_to.set("Select Unit")

conversion_var_metric_from = tk.StringVar()
conversion_var_metric_from.set("Select Unit")

car_menu_from = tk.OptionMenu(conversion_from_frame, conversion_var_car_from, "Cadillac Escalade", "Ford F-150", "Banana")
car_menu_from.pack(side="top", pady=10)

metric_menu_to = tk.OptionMenu(conversion_to_frame, conversion_var_metric_to, "Meters", "Centimeters", "Millimeters")
metric_menu_to.pack(side="top", pady=10)

car_menu_to = tk.OptionMenu(conversion_to_frame, conversion_var_car_to, "Cadillac Escalade", "Ford F-150", "Banana")
car_menu_to.pack(side="top", pady=10)

metric_menu_from = tk.OptionMenu(conversion_from_frame, conversion_var_metric_from, "Meters", "Centimeters", "Millimeters")
metric_menu_from.pack(side="top", pady=10)

escalade_M = 5.382
escalade_CM = 538.2
escalade_MM = 5382
f150_M = 5.31114
f150_CM = 531.114
f150_MM = 5311.14
banana_MM = 178.0032
banana_CM = 17.80032
banana_M = 0.1780032

def convert_from():
    if conversion_var_car_from.get() == "Cadillac Escalade" and conversion_var_metric_from.get() == "Meters":
        convert_M_escalade()
    if conversion_var_car_from.get() == "Cadillac Escalade" and conversion_var_metric_from.get() == "Millimeters":
        convert_MM_escalade()
    if conversion_var_car_from.get() == "Ford F-150" and conversion_var_metric_from.get() == "Meters":
        convert_M_f150()
    if conversion_var_car_from.get() == "Ford F-150" and conversion_var_metric_from.get() == "Millimeters":
        convert_MM_f150()
    if conversion_var_car_from.get() == "Banana" and conversion_var_metric_from.get() == "Meters":
        convert_M_banana()
    if conversion_var_car_from.get() == "Banana" and conversion_var_metric_from.get() == "Millimeters":
        convert_MM_banana()
    if conversion_var_car_from.get() == "Banana" and conversion_var_metric_from.get() == "Centimeters":
        convert_CM_banana()
    if conversion_var_car_from.get() == "Ford F-150" and conversion_var_metric_from.get() == "Centimeters":
        convert_CM_f150()
    if conversion_var_car_from.get() == "Cadillac Escalade" and conversion_var_metric_from.get() == "Centimeters":
        convert_CM_escalade()

def convert():
    if conversion_var_car_to.get() == "Cadillac Escalade" and conversion_var_metric_to.get() == "Meters":
        convert_escalade_M()
    if conversion_var_car_to.get() == "Cadillac Escalade" and conversion_var_metric_to.get() == "Millimeters":
        convert_escalade_MM()
    if conversion_var_car_to.get() == "Ford F-150" and conversion_var_metric_to.get() == "Meters":
        convert_f150_M()
    if conversion_var_car_to.get() == "Ford F-150" and conversion_var_metric_to.get() == "Millimeters":
        convert_f150_MM()
    if conversion_var_car_to.get() == "Banana" and conversion_var_metric_to.get() == "Meters":
        convert_banana_M()
    if conversion_var_car_to.get() == "Banana" and conversion_var_metric_to.get() == "Millimeters":
        convert_banana_MM()
    if conversion_var_car_to.get() == "Banana" and conversion_var_metric_to.get() == "Centimeters":
        convert_banana_CM()
    if conversion_var_car_to.get() == "Cadillac Escalade" and conversion_var_metric_to.get() == "Centimeters":
        convert_escalade_CM()
    if conversion_var_car_to.get() == "Ford F-150" and conversion_var_metric_to.get() == "Centimeters":
        convert_f150_CM()

def convert_escalade_M():
    try:
        entry = float(entrybox_to.get())
        result = entry / escalade_M
        result_label_to.config(text=f"{entry} meters is equal to {result:.2f} Cadillac Escalades")
    except ValueError:
        result_label_to.config(text="Please enter a valid number")

def convert_escalade_CM():
    try:
        entry = float(entrybox_to.get())
        result = entry / escalade_CM
        result_label_to.config(text=f"{entry} centimeters is equal to {result:.2f} Cadillac Escalades")
    except ValueError:
        result_label_to.config(text="Please enter a valid number")

def convert_escalade_MM():
    try:
        entry = float(entrybox_to.get())
        result = entry / escalade_MM
        result_label_to.config(text=f"{entry} milimeters is equal to {result:.2f} Cadillac Escalades")
    except ValueError:
        result_label_to.config(text="Please enter a valid number")

def convert_f150_MM():
    try:
        entry = float(entrybox_to.get())
        result = entry / f150_MM
        result_label_to.config(text=f"{entry} milimeters is equal to {result:.2f} Ford F-150s")
    except ValueError:
        result_label_to.config(text="Please enter a valid number")

def convert_f150_CM():
    try:
        entry = float(entrybox_to.get())
        result = entry / f150_CM
        result_label_to.config(text=f"{entry} centimeters is equal to {result:.2f} Ford F-150s")
    except ValueError:
        result_label_to.config(text="Please enter a valid number")

def convert_f150_M():
    try:
        entry = float(entrybox_to.get())
        result = entry / f150_M
        result_label_to.config(text=f"{entry} meters is equal to {result:.2f} Ford F-150s")
    except ValueError:
        result_label_to.config(text="Please enter a valid number")

def convert_M_f150():
    try:
        entry = float(entrybox_from.get())
        result = entry * f150_M
        result_label_from.config(text=f"{entry} Ford F-150s is equal to {result:.2f} meters")
    except ValueError:
        result_label_from.config(text="Please enter a valid number")

def convert_CM_f150():
    try:
        entry = float(entrybox_from.get())
        result = entry * f150_CM
        result_label_from.config(text=f"{entry} Ford F-150s is equal to {result:.2f} centimeters")
    except ValueError:
        result_label_from.config(text="Please enter a valid number")

def convert_MM_f150():
    try:
        entry = float(entrybox_from.get())
        result = entry * f150_MM
        result_label_from.config(text=f"{entry} Ford F-150s is equal to {result:.2f} milimeters")
    except ValueError:
        result_label_from.config(text="Please enter a valid number")

def convert_M_escalade():
    try:
        entry = float(entrybox_from.get())
        result = entry * escalade_M
        result_label_from.config(text=f"{entry} Cadillac Escalades is equal to {result:.2f} meters")
    except ValueError:
        result_label_from.config(text="Please enter a valid number")

def convert_CM_escalade():
    try:
        entry = float(entrybox_from.get())
        result = entry * escalade_CM
        result_label_from.config(text=f"{entry} Cadillac Escalades is equal to {result:.2f} centimeters")
    except ValueError:
        result_label_from.config(text="Please enter a valid number")

def convert_MM_escalade():
    try:
        entry = float(entrybox_from.get())
        result = entry * escalade_MM
        result_label_from.config(text=f"{entry} Cadillac Escalades is equal to {result:.2f} milimeters")
    except ValueError:
        result_label_from.config(text="Please enter a valid number")

def convert_MM_banana():
    try:
        entry = float(entrybox_from.get())
        result = entry * banana_MM
        result_label_from.config(text=f"{entry} Bananas is equal to {result:.2f} milimeters")
    except ValueError:
        result_label_from.config(text="Please enter a valid number")

def convert_M_banana():
    try:
        entry = float(entrybox_from.get())
        result = entry * banana_M
        result_label_from.config(text=f"{entry} Bananas is equal to {result:.2f} meters")
    except ValueError:
        result_label_from.config(text="Please enter a valid number")

def convert_banana_MM():
    try:
        entry = float(entrybox_to.get())
        result = entry / banana_MM
        result_label_to.config(text=f"{entry} milimeters is equal to {result:.2f} Bananas")
    except ValueError:
        result_label_to.config(text="Please enter a valid number")

def convert_banana_M():
    try:
        entry = float(entrybox_to.get())
        result = entry / banana_M
        result_label_to.config(text=f"{entry} meters is equal to {result:.2f} Bananas")
    except ValueError:
        result_label_to.config(text="Please enter a valid number")

def convert_CM_banana():
    try:
        entry = float(entrybox_from.get())
        result = entry * banana_CM
        result_label_from.config(text=f"{entry} Bananas is equal to {result:.2f} centimeters")
    except ValueError:
        result_label_from.config(text="Please enter a valid number")

def convert_banana_CM():
    try:
        entry = float(entrybox_to.get())
        result = entry / banana_CM
        result_label_to.config(text=f"{entry} centimeters is equal to {result:.2f} Bananas")
    except ValueError:
        result_label_to.config(text="Please enter a valid number")

convertbutton_to = tk.Button(conversion_to_frame, text="Convert", command=convert)
convertbutton_to.pack(side="top", pady=10)

convert_button_from = tk.Button(conversion_from_frame, text="Convert", command=convert_from)
convert_button_from.pack(side="top", pady=10)

root.mainloop()
