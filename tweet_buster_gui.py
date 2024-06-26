import tkinter as tk
from tkinter import messagebox
from tkinter import font
from PIL import Image, ImageTk

def on_button_click():
    a = 1
    #messagebox.showinfo("Button Clicked", "You clicked the button!")

def on_list_select(event):
    selected_item = listbox.get(listbox.curselection())
    #messagebox.showinfo("Listbox Selection", f"You selected: {selected_item}")

def on_checkbox_change():
    a = 1
    #messagebox.showinfo("Button Clicked", "You clicked the button!")

def on_checkbox_change2():
    a = 1
    #messagebox.showinfo("Button Clicked", "You clicked the button!")

def toggle_resp_classes():
    if invert_var.get() == 1:
        resp_img_label.config(image=resp_standard_photo)
    else:
        resp_img_label.config(image=resp_reverse_photo)

background_color = "#121f29"
root = tk.Tk()
root.title("Tweet Buster")
root.geometry("900x700+350+150")
root.iconbitmap('C:/Users/wutzg/Desktop/DSAI 2/Implementation/Logo/Logo_Large.ico')
root.config(bg=background_color)

# App Title
image_path = "C:/Users/wutzg/Desktop/DSAI 2/Implementation/Logo/APP_TITLE_S.png"  # Replace with the path to your image file
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo, bg=background_color)
image_label.grid(row=0, column=0, columnspan=2)

# Model List Label
label1 = tk.Label(root, text="Choose a pre-selected model:", bg=background_color, fg="white", font=("Helvetica", 11))
label1.grid(row=1, column=0)

# Model List Box
listbox = tk.Listbox(root, width=35, height=7)
listbox.grid(row=2, column=0)
items = ["albert-base-v2-fakenews-discriminator", "roberta-fake-news-classification", "TwHIN-BERT-Misinformation-Classifier", "lie_detection_distilbert",
         "distilroberta-finetuned-financial-news-sentiment-analysis", "hallucination_evaluation_model", "mix_it_up_random"]
for listbox_item  in items:
    listbox.insert(tk.END, listbox_item )
listbox.bind("<<ListboxSelect>>", on_list_select)

# Model Link Label
label2 = tk.Label(root, text="Enter a huggingface.co Link:", bg=background_color, fg="white", font=("Helvetica", 11))
label2.grid(row=1, column=1)

# Model Link Box
link_entry_frame = tk.Frame(root, bg=background_color)
link_entry = tk.Entry(link_entry_frame, width=30)
link_entry.pack(pady=5)
submit_button = tk.Button(link_entry_frame, text="Load Model")
submit_button.pack(pady=5)
link_entry_frame.grid(row=2, column=1, pady=10)

# # Model Code Label
# label2 = tk.Label(root, text="Enter your model code here:", bg=background_color, fg="white", font=("Helvetica", 11))
# label2.grid(row=1, column=2)

# # Model Code Box
# code_entry_frame = tk.Frame(root, bg=background_color)
# code_entry = tk.Text(code_entry_frame, width=25, height=6)
# code_entry.pack(pady=5)
# submit_button = tk.Button(code_entry_frame, text="Load Code")
# submit_button.pack(pady=5)
# code_entry_frame.grid(row=2, column=2, pady=10)

# Response Scale Label
resp_label = tk.Label(root, text="Response Class Order", bg=background_color, fg="white", font=("Helvetica", 11))
resp_label.grid(row=3, column=0, columnspan=2)

# Response Scale
resp_standard_img = Image.open("C:/Users/wutzg/Desktop/DSAI 2/Implementation/Logo/resp_standard.png")
resp_reverse_img = Image.open("C:/Users/wutzg/Desktop/DSAI 2/Implementation/Logo/resp_reverse.png")
resp_standard_photo = ImageTk.PhotoImage(resp_standard_img)
resp_reverse_photo = ImageTk.PhotoImage(resp_reverse_img)

# resp_image_path = "C:/Users/wutzg/Desktop/DSAI 2/Implementation/Logo/resp_standard.png"
# resp_image = Image.open(resp_image_path)
# resp_photo = ImageTk.PhotoImage(resp_image)
resp_img_label = tk.Label(root, image=resp_standard_photo, bg=background_color)
resp_img_label.grid(row=4, column=0, columnspan=2)

# Invert Response Scale
invert_var = tk.IntVar()
invert_checkbox = tk.Radiobutton(root, bg=background_color, fg="white", text="Reverse response class order", font=font.Font(family="Helvetica", size=12),
                                 value=False, variable=invert_var, command=toggle_resp_classes)
invert_checkbox.grid(row=5, column=0, columnspan=2)

# Emoji Only
emoji_checkbox = tk.Radiobutton(root, bg=background_color, fg="white", text="Emoji indicators only", font=font.Font(family="Helvetica", size=12), 
                                value=False)
emoji_checkbox.grid(row=6, column=0, columnspan=2, pady=(5, 0))

# Create and pack a button
start_model_button = tk.Button(root, text="START CLASSIFICATION", height=4, width=40)
start_model_button.grid(row=7, column=0, columnspan=2, pady=(40, 0))

# Column weights
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Run the application
root.mainloop()