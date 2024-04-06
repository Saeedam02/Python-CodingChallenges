import tkinter as tk
from tkinter import filedialog

class Notepad:
    def __init__(self, root):
        # Initialize the Notepad application
        self.root = root
        self.root.title("Notepad")
        
        # Create a text area widget for user input
        self.textarea = tk.Text(self.root, wrap='word', undo=True)
        self.textarea.pack(expand=True, fill='both')
        
        # Create a menu bar
        self.menubar = tk.Menu(self.root)
        
        # File menu
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New", command=self.new_file)
        self.filemenu.add_command(label="Open", command=self.open_file)
        self.filemenu.add_command(label="Save", command=self.save_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.root.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        
        # Edit menu
        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Undo", command=self.textarea.edit_undo)
        self.editmenu.add_command(label="Redo", command=self.textarea.edit_redo)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        
        # Configure the root window with the menu bar
        self.root.config(menu=self.menubar)

    def new_file(self):
        # Clear the text area when creating a new file
        self.textarea.delete(1.0, tk.END)
    
    def open_file(self):
        # Prompt the user to select a file and load its content
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                self.textarea.delete(1.0, tk.END)
                self.textarea.insert(1.0, file.read())

    def save_file(self):
        # Prompt the user to choose a file path and save the content
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.textarea.get(1.0, tk.END))

if __name__ == "__main__":
    root = tk.Tk()
    app = Notepad(root)
    root.mainloop()
