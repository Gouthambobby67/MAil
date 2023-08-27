import tkinter as tk
from tkinter import messagebox

class MailApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Mail Application")
        
        self.setup_ui()
    
    def setup_ui(self):
        
        self.from_entry = tk.Entry(self.root)
        self.from_entry.pack()

        self.to_label = tk.Label(self.root, text="To:")
        self.to_label.pack()

        self.to_entry = tk.Entry(self.root)
        self.to_entry.pack()

        self.subject_label = tk.Label(self.root, text="Subject:")
        self.subject_label.pack()

        self.subject_entry = tk.Entry(self.root)
        self.subject_entry.pack()

        self.message_label = tk.Label(self.root, text="Message:")
        self.message_label.pack()

        self.message_text = tk.Text(self.root)
        self.message_text.pack()

        self.send_button = tk.Button(self.root, text="Send", command=self.send_mail)
        self.send_button.pack()
    
    def send_mail(self):
        from_address = self.from_entry.get()
        to_address = self.to_entry.get()
        subject = self.subject_entry.get()
        message = self.message_text.get("1.0", tk.END)

        # You would typically integrate with a mail sending library here
        # For example: send_mail(from_address, to_address, subject, message)
        
        messagebox.showinfo("Success", "Mail sent successfully!")

def main():
    root = tk.Tk()
    app = MailApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()
