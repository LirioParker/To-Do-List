import customtkinter as ctk

root_width = 300
root_height = 450
tasks = []

#Colors
yellow = "#ffce52"

#Window setup
root = ctk.CTk()
root.title("To Do List")
root.geometry(f"{root_width}x{root_height}")
ctk.set_appearance_mode("dark")

landing_frame = ctk.CTkFrame(master=root,  width=root_width, height=root_height, fg_color="#0ba7f5")
landing_frame.pack()

delete_task_frame = ctk.CTkFrame(master=landing_frame, width=root_width, height=root_height, fg_color="#0ba7f5")
delete_task_frame.pack()

add_task_frame = ctk.CTkFrame(master=landing_frame,  width=root_width, height=root_height, fg_color="#ffdb9e")
add_task_frame.pack()

def landing_screen():

    add_task_btn = ctk.CTkButton(master=landing_frame, text="Add Task", width=120, height=40, 
                                        font=("Helvetica", 17, "bold"), fg_color=yellow,
                                        text_color="#242424", hover_color="#d8aa37",
                                        corner_radius=12, command=add_task, anchor="top")
    add_task_btn.pack(padx=7, pady=7)

    delete_task_btn = ctk.CTkButton(master=landing_frame, text="Clear Tasks", width=120, height=40, 
                                        font=("Helvetica", 17, "bold"), fg_color="#f7377a",
                                        text_color="#242424", hover_color="#da2867",
                                        corner_radius=12, command=delete_task, anchor="center")
    delete_task_btn.pack(padx=7, pady=7)

    for i in tasks:
        if i == 0:
            display_task = ctk.CTkLabel(master=landing_frame, text="No tasks Yet", 
                                        font=("Helvetica", 18, "bold"))
            display_task.pack()
        else:
            display_task.pack = ctk.CTkLabel(master=landing_frame, text=tasks, 
                                        font=("Helvetica", 18, "bold"))
            display_task.pack()

def add_task():
    landing_frame.destroy()
    while True:
        task_label = ctk.CTkLabel(master=add_task_frame, text="Enter a Task: ", font=("Helvetica", 18, "bold"),
                            text_color=yellow)
        task_label.pack(padx=20, pady=20)

        task_input = ctk.CTkTextbox(master=add_task_frame, width=120, height=40, font=("Helvetica", 20, "bold"))
        task_input.pack(padx=20, pady=17)

        def get_text_content():
            task_content = task_input.get("1.0", ctk.END).strip()
            tasks.append(task_content)
            print(tasks)

        submit_task_btn = ctk.CTkButton(master=add_task_frame, text="Add Task", width=120, height=40, 
                                        font=("Helvetica", 17, "bold"), fg_color=yellow,
                                        text_color="#242424", hover_color="#d8aa37",
                                        corner_radius=12, command=get_text_content)
        submit_task_btn.pack(padx=20, pady=17)
        break

def delete_task():

    landing_frame.destroy()

    def clear_tasks():
        tasks.clear()

    delete_task_btn = ctk.CTkButton(master=delete_task_frame, text="Clear Tasks", width=120, height=40, 
                                        font=("Helvetica", 17, "bold"), fg_color="#f7377a",
                                        text_color="#242424", hover_color="#da2867",
                                        corner_radius=12, command=clear_tasks)
    delete_task_btn.pack()


    for task in tasks:
        if task == "":
            display_task = ctk.CTkLabel(master=delete_task_frame, text="No tasks Yet", 
                                        font=("Helvetica", 18, "bold"))
            display_task.pack()
        else:
            display_task.pack = ctk.CTkLabel(master=delete_task_frame, text=tasks, 
                                        font=("Helvetica", 18, "bold"))
            display_task.pack()

add_task()

root.mainloop()