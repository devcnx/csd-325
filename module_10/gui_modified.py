"""
Name: Brittaney Perry-Morgan
Date: Sunday, July 13th, 2025
Assignment: Module 10.2 GUI To-Do

Purpose: The modified code from 2.2 Scrolling and Deleting in the Tkinter by Example PDF.

This is the modified GUI application for the Module 10.2 assignment.

Imports:
    - tkinter: The main GUI library for Python.
    - tkinter.messagebox: A module for creating message boxes.
"""

import tkinter as tk
import tkinter.messagebox as msg
from tkinter import ttk


class ToDo(tk.Tk):
    """
    Representation of a to-do list.

    Fields:
        - tasks: A list of tasks.
        :type tasks: list[tk.Label]

        - tasks_canvas: The canvas for the tasks.
        :type tasks_canvas: tk.Canvas

        - tasks_frame: The frame for the tasks.
        :type tasks_frame: tk.Frame

        - text_frame: The frame for the text.
        :type text_frame: tk.Frame

        - scrollbar: The scrollbar for the tasks.
        :type scrollbar: tk.Scrollbar

        - canvas_frame: The frame for the canvas.
        :type canvas_frame: tk.Frame

        - task_create: The entry widget for creating tasks.
        :type task_create: ttk.Entry
    """

    def __init__(self, tasks=None):
        """Initialize the Todo GUI."""
        super().__init__()

        self.tasks = tasks if tasks is not None else []

        # Configure styles
        style = ttk.Style(self)
        style.theme_use("clam")  # Use the native macOS theme
        style.configure(
            "Color1.TLabel",
            background="#eaf2f8",
            foreground="black",
            padding=10,
            font=("Helvetica", 12),
        )
        style.configure(
            "Color2.TLabel",
            background="#fdfefe",
            foreground="black",
            padding=10,
            font=("Helvetica", 12),
        )
        style.configure(
            "Header.TLabel",
            background="lightgrey",
            foreground="black",
            padding=10,
            font=("Helvetica", 12),
        )

        # Add title, size, and frames
        self.title("Perry-Morgan-ToDo")
        self.geometry("600x500")

        # Add File menu
        menu = tk.Menu(self)
        self.config(menu=menu)
        file_menu = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.destroy)

        # Main frame
        main_frame = ttk.Frame(self, padding="10 10 10 10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Input frame
        input_frame = ttk.Frame(main_frame, padding="10 0 10 10")
        input_frame.pack(fill=tk.X)

        self.task_create = ttk.Entry(input_frame, width=40, font=("Helvetica", 12))
        self.task_create.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.task_create.focus_set()

        add_button = ttk.Button(input_frame, text="Add Task", command=self.add_task)
        add_button.pack(side=tk.RIGHT, padx=(10, 0))

        # Canvas and Scrollbar frame
        canvas_frame = ttk.Frame(main_frame)
        canvas_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))

        self.tasks_canvas = tk.Canvas(canvas_frame)
        self.tasks_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        self.scrollbar = ttk.Scrollbar(
            canvas_frame, orient="vertical", command=self.tasks_canvas.yview
        )
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tasks_frame = ttk.Frame(self.tasks_canvas)
        self.tasks_frame.columnconfigure(0, weight=1)
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        # Add initial task/instruction label
        todo1 = ttk.Label(
            self.tasks_frame,
            text="--- Right Click Item to Delete ---",
            style="Header.TLabel",
            width=55,
            anchor="center",
        )
        todo1.bind("<Button-3>", self.remove_task)

        self.tasks.append(todo1)

        for index, task in enumerate(self.tasks):
            task.grid(row=index, column=0, sticky="ew", pady=(0, 5))

        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

        self.canvas_frame = self.tasks_canvas.create_window(
            (0, 0), window=self.tasks_frame, anchor="n"
        )

    def add_task(self, _event=None):
        """
        Add new tasks.

        Parameters:
            - event: The event that triggered the function.
            :type event: Event
        """
        task_text = self.task_create.get().strip()

        if len(task_text) > 0:
            new_task = ttk.Label(self.tasks_frame, text=task_text)

            self.set_task_color(len(self.tasks), new_task)

            new_task.bind("<Button-3>", self.remove_task)
            new_task.grid(row=len(self.tasks), column=0, sticky="ew", pady=(0, 5))

            self.tasks.append(new_task)

        self.task_create.delete(0, tk.END)

    def remove_task(self, _event):
        """
        Remove a task.

        Parameters:
            - event: The event that triggered the function.
            :type event: Event
        """
        task = _event.widget
        if (
            msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?")
            and task.winfo_exists()
        ):
            self.tasks.remove(task)
            task.destroy()
            self.recolor_tasks()

    def recolor_tasks(self):
        """
        Recolor the tasks.
        """
        for index, task in enumerate(self.tasks):
            self.set_task_color(index, task)

    def set_task_color(self, position, task):
        """
        Set the colour of a task.

        Parameters:
            - position: The position of the task.
            :type position: int

            - task: The task to set the colour of.
            :type task: ttk.Label
        """
        _, task_style_choice = divmod(position, 2)

        if task_style_choice == 0:
            task.configure(style="Color1.TLabel")
        else:
            task.configure(style="Color2.TLabel")

    def on_frame_configure(self, _event=None):
        """
        Configure the frame.

        Parameters:
            - event: The event that triggered the function.
            :type event: Event
        """
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

        self.canvas_frame = self.tasks_canvas.create_window(
            (0, 0), window=self.tasks_frame, anchor="n"
        )

    def task_width(self, _event=None):
        """
        Set the width of the task.

        Parameters:
            - event: The event that triggered the function.
            :type event: Event
        """
        canvas_width = _event.width if _event else 600
        self.tasks_canvas.itemconfig(self.canvas_frame, width=canvas_width)

    def mouse_scroll(self, _event):
        """
        Scroll the canvas.

        Parameters:
            - event: The event that triggered the function.
            :type event: Event
        """
        if _event.delta:
            self.tasks_canvas.yview_scroll(int(-1 * (_event.delta / 120)), "units")
        else:
            move = 1 if _event.num == 5 else -1
            self.tasks_canvas.yview_scroll(move, "units")

    def exit(self):
        self.destroy()


if __name__ == "__main__":
    todo = ToDo()
    todo.mainloop()
