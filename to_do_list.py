import customtkinter as ctk

root_width = 300
root_height = 450
tasks = []

yellow = "#ffce52"
light_yellow = "#fffd78"

root = ctk.CTk()
root.title("To Do List")
root.resizable(False, False)
root.geometry(f"{root_width}x{root_height}")
ctk.set_appearance_mode("dark")

landing_frame = ctk.CTkFrame(root, fg_color=light_yellow)
add_task_frame = ctk.CTkFrame(root, fg_color=light_yellow)
delete_task_frame = ctk.CTkFrame(root, fg_color=light_yellow)

task_container = ctk.CTkFrame(landing_frame, fg_color="transparent")
task_container.pack(fill="both", padx=20, pady=10, expand=True)

def show_frame(frame):
    landing_frame.pack_forget()
    add_task_frame.pack_forget()
    delete_task_frame.pack_forget()
    frame.pack(fill="both", expand=True)

def refresh_task_list():
    for widget in task_container.winfo_children():
        widget.destroy()

    if not tasks:
        lbl = ctk.CTkLabel(task_container, text="No tasks yet", font=("Helvetica", 18, "bold"), text_color="#242424")
        lbl.place(x=80, y= 100)
    else:
        for task in tasks:
            lbl = ctk.CTkLabel(task_container, text=task, font=("Helvetica", 18, "bold"), text_color="#242424",
                               justify="left")
            lbl.pack(fill="both", pady=2)
            

def landing_screen():
    show_frame(landing_frame)

    for widget in landing_frame.winfo_children():
        if widget not in (task_container,):
            widget.destroy()

    add_task_btn = ctk.CTkButton(landing_frame, text="Add Task", width=80, height=45,
                  font=("Helvetica", 17, "bold"), fg_color=yellow, text_color="#242424",
                  hover_color="#d8aa37", corner_radius=12, command=add_task_screen)

    add_task_btn.grid(row=0, column=0, padx=5, pady=5)

    delete_task_btn = ctk.CTkButton(landing_frame, text="Clear Tasks", width=50, height=45,
                  font=("Helvetica", 17, "bold"), fg_color="#f7377a", text_color="#242424",
                  hover_color="#da2867", corner_radius=12, command=delete_task_screen)

    refresh_task_list()
    
def add_task_screen():
    show_frame(add_task_frame)

    for widget in add_task_frame.winfo_children():
        widget.destroy()

    ctk.CTkLabel(add_task_frame, text="Enter a Task:", font=("Helvetica", 20, "bold"),
                 text_color="#2c2c2c").pack(pady=20)

    task_input = ctk.CTkTextbox(master=add_task_frame, width=120, height=40, font=("Helvetica", 20, "bold"),
                                fg_color="#363636")
    task_input.pack(padx=20, pady=12)

    def save_task():
        task_content = task_input.get("1.0", "end").strip()
        if task_content:
            tasks.append(task_content)
        landing_screen()

    submit_task_btn = ctk.CTkButton(add_task_frame, text="Add Task", width=120, height=40, 
                                    font=("Helvetica", 18, "bold"), fg_color=yellow,
                                    text_color="#242424", hover_color="#d8aa37",
                                    corner_radius=12, command=save_task).pack(pady=17)

    cancel_btn = ctk.CTkButton(add_task_frame, text="Cancel", width=120, height=40, 
                                    font=("Helvetica", 18, "bold"), fg_color="#313131",
                                    text_color="#D0D0D0", hover_color="#272727",
                                    corner_radius=12, command=landing_screen).pack(pady=17)

def delete_task_screen():
    show_frame(delete_task_frame)

    for widget in add_task_frame.winfo_children():
        widget.destroy()

    ctk.CTkLabel(delete_task_frame, text=f"You have {len(tasks)} task(s)",
                 font=("Helvetica", 18, "bold"), text_color="#242424").pack(pady=30)

    def clear_tasks():
        tasks.clear()
        landing_screen()

    delete_task_btn = ctk.CTkButton(master=delete_task_frame, text="Clear Tasks", width=120, height=40, 
                                    font=("Helvetica", 17, "bold"), fg_color="#f7377a",
                                    text_color="#242424", hover_color="#da2867",
                                    corner_radius=12, command=clear_tasks).pack(pady=20)

    cancel_btn = ctk.CTkButton(add_task_frame, text="Cancel", width=120, height=40, 
                               font=("Helvetica", 18, "bold"), fg_color="#313131",
                               text_color="#D0D0D0", hover_color="#272727",
                               corner_radius=12, command=landing_screen).pack(pady=17)

landing_screen()
root.mainloop()