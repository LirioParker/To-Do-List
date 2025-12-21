import customtkinter as ctk

# Set appearance and theme
ctk.set_appearance_mode("System")  # "Light" or "Dark"
ctk.set_default_color_theme("blue")

# Create main window
app = ctk.CTk()
app.title("CTk Button Positioning")
app.geometry("400x300")

# -------- 1. Using pack() --------
btn_pack = ctk.CTkButton(app, text="Pack (Top)", command=lambda: print("Pack clicked"))
btn_pack.pack(side="top", pady=10)  # pady adds vertical spacing

# -------- 2. Using grid() --------
frame_grid = ctk.CTkFrame(app)
frame_grid.pack(pady=10)

btn_grid1 = ctk.CTkButton(frame_grid, text="Grid (0,0)")
btn_grid1.grid(row=0, column=0, padx=5, pady=5)

btn_grid2 = ctk.CTkButton(frame_grid, text="Grid (0,1)")
btn_grid2.grid(row=0, column=1, padx=5, pady=5)

# -------- 3. Using place() --------
btn_place = ctk.CTkButton(app, text="Place (x=150, y=200)")
btn_place.place(x=150, y=200)  # Absolute positioning

# Run the app
app.mainloop()
