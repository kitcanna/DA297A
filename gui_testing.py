import tkinter as tk
import admin_functionalities as af
import doctor_functionalitites as df
import patient_functionalities as pf

# A work in progress. 
# Phase 2 of project if completed.

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome to the MAU Health Center Database")
        self.root.configure(bg="darkslategray")

        self.text_panel = tk.Text(root, width=120, height=30, background="#698E8E", highlightbackground="darkslategray", foreground="white", font=("Courier", 12))
        self.text_panel.config(state="normal") 
        self.text_panel.insert(tk.END, "Welcome! Are you an admin, doctor or a patient?\n")
        self.text_panel.pack()
        self.text_panel.config(state="disabled") 

        self.text_field = tk.Entry(root, width=100, background="white", font=("Calibri", 12))
        self.text_field.pack()
        self.text_field.bind("<Return>", self.add_text)

        self.add_button = tk.Button(root, text="Submit", command=self.add_text, highlightbackground = "darkslategray", font=("Calibri", 12), bg="darkslategray")
        self.add_button.pack()

    def add_text(self, event=None):
        text = self.text_field.get().lower()
        self.text_panel.config(state="normal")
        self.text_panel.insert(tk.END, "You: " + text + "\n")
        self.text_panel.insert(tk.END, "******************************************* \n")
        self.text_panel.config(state="disabled")
        self.text_field.delete(0, tk.END)
        self.text_panel.see(tk.END)
        self.text_field.delete(0, tk.END)

        if text in ["admin", "doctor", "patient"]:
            self.user_type = text
            self.text_panel.config(state="normal")
            self.text_panel.insert(tk.END, "Hello, {}.\n".format(text))
            self.text_panel.insert(tk.END, "Please enter your ID number:\n")
            self.text_panel.config(state="disabled")

        elif self.user_type:

            if self.user_type == "doctor":
                self.doctor_id = text
                self.text_panel.config(state="normal")
                self.text_panel.insert(tk.END, "Welcome Doctor with ID: {}\n".format(self.doctor_id))
                self.text_panel.insert(tk.END, "What would you like to do? Choose a number.\n")
                self.text_panel.insert(tk.END, "1. Define availabilities\n")
                self.text_panel.insert(tk.END, "2. See upcoming appointments\n")
                self.text_panel.insert(tk.END, "3. See list of patients and add medical records\n")
                self.text_panel.config(state="disabled")

                if self.doctor_id:
                    self.function = text   
                    self.text_panel.config(state="normal")
                    self.text_panel.insert(tk.END, "Listing all your appointments...\n")

                    apps = df.list_all_upcoming_app(self.doctor_id)
                    for i in apps: 
                            self.text_panel.insert(tk.END,"---------------------")
                            self.text_panel.insert(tk.END,i[0])
                            self.text_panel.insert(tk.END,"\n")
                    print(apps)
                    self.text_panel.config(state="disabled")

            elif self.user_type == "patient":
                self.patient_id = text
                self.text_panel.config(state="normal")
                self.text_panel.insert(tk.END, "Welcome Patient with ID: {}\n".format(self.patient_id))
                self.text_panel.config(state="disabled")

            elif self.user_type == "admin":
                self.admin_id = text
                self.text_panel.config(state="normal")
                self.text_panel.insert(tk.END, "Welcome Admin with ID: {}\n".format(self.admin_id))
                self.text_panel.config(state="disabled")
        else:
            self.text_panel.config(state="normal")
            self.text_panel.insert(tk.END, "Invalid input. Please try again.\n")
            self.text_panel.config(state="disabled")

        self.text_panel.see(tk.END)


root = tk.Tk()
app = LoginPage(root)
root.mainloop()
