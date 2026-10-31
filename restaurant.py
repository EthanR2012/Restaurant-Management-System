import tkinter as tk
from tkinter import ttk, messagebox

# Define the RestaurantOrderManagementApp class
class RestaurantOrderManagementApp:
    # Initialize the application
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management App")

        # A dictionary to store the menu items and their prices
        self.menu_items = {
            "FRIES MEAL": 2,
            "LUNCH MEAL": 2,
            "BURGER MEAL": 3,
            "PIZZA MEAL": 4,
            "CHEESEBURGER": 2.5,
            "DRINKS": 1,
        }

        self.exchange_rate = 82 # 82 rupees = 1 dollar
        self.setup_background(root)

        # Create a frame to hold the widgets
        frame = ttk.Frame(root)    
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        frame = ttk.Label(
            frame,
            text = "Restaurant Order Management",
            font=("Arial", 20, "bold")
        ).grid(row=0, columnspan=3, padx=10, pady=10)

        self.menu_labels = {} # To store reference to menu labels
        self.menu_quantities = {} # To store reference to menu quantities

        # Create labels and entry widgets for each menu item
        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label=ttk.Label(
                frame,
                text=f"{item} (${price}):",
                font=("Arial", 12)
            )
            label.grid(row=i, column=0, padx=10, pady=5)
            self.menu_labels[item] = label

            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry

            # Currency Selection
            self.currency_var = tk.StringVar()
            ttk.Label(frame, text="Currency:", font=("Arial",12)).grid(row=len(self.menu_items) + 1, column=0, padx=10, pady= 5)

            # Dropdown for currency selection
            currency_dropdown = ttk.Combobox(frame, textvariable=self.currency_var, state="readonly", width=18, values=("USD", "INR"))
            currency_dropdown.grid(row=len(self.menu_items)+1, column=1, padx=10, pady=5)
            currency_dropdown.current(0)
            self.currency_var.trace("w", self.update_menu_prices)

            # Button to place the order
            order_button = ttk.Button(
                frame,
                text="Place Order",
                command=self.place_order
            )
            order_button.grid(
                row=len(self.menu_items)+2,
                columnspan=3
                padx=10
                pady=10
            )

            # Method to set up the background image
            def setup_background(self, root):
                bg_width, bg_height = 800,600
                canvas = tk.Canvas(root, width=bg_width, height=bg_height)
                canvas.pack()

                original_image = 