import customtkinter as Ctk
from customtkinter import *

class GoldenRatioApp:

    def __init__(self, root):
        # Configure the appearance and theme
        Ctk.set_appearance_mode("System")
        Ctk.set_default_color_theme("blue")

        # Set up the root window
        self.root = root
        self.root.title("Golden Ratio")
        self.make_app_widgets()

    def make_app_widgets(self):
        # Input label
        label = Ctk.CTkLabel(self.root, text="Enter your value:", font=("Arial", 36))
        label.grid(column=0, row=0, sticky=Ctk.W, pady=3, padx=(10,0))

        # Entry field for user input
        self.entry = Ctk.CTkEntry(self.root, width=250, height=40, font=("Arial", 36))
        self.entry.grid(column=1, row=0, sticky=Ctk.W, pady=3)

        # Button to calculate the golden ratio
        button = Ctk.CTkButton(self.root, text="Calculate", width=525, height=45, command=self.golden_number)
        button.grid(column=0, row=1, columnspan=2, sticky=Ctk.N, pady=3)

        # Textbox to display results
        self.text = Ctk.CTkTextbox(self.root, state='disabled', width=550, height=400)
        self.text.grid(column=0, row=2, columnspan=2, pady=3, padx=3)

    def golden_number(self):
        try:
            number = int(self.entry.get())  # Get the input as an integer
            if number <= 0:
                self.update_text("Please enter a positive integer.")
                return

            # Generate golden ratio sequence
            a, b = 1, 1
            results = ["Golden Ratio\n"]

            for i in range(1, number + 1):
                c = a + b
                a, b = b, c
                v = b / a
                results.append(f"V{i} = {round(v, 5)} = {b} / {a}\n")

            # Update the text with the results
            self.update_text("".join(results))
        except ValueError:
            self.update_text("Please enter a valid integer.")

    def update_text(self, content):
        self.text.configure(state="normal")  # Enable the text widget
        self.text.delete("1.0", "end")  # Clear previous text
        self.text.insert("1.0", content)  # Insert the new content
        self.text.configure(state="disabled")  # Disable the text widget again


if __name__ == "__main__":
    root = Ctk.CTk()
    app = GoldenRatioApp(root)
    root.mainloop()