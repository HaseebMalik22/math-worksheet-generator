import tkinter as tk
from run import MathWorksheetGenerator

class MathWorksheetGUI:
    def __init__(self, master):
        self.master = master
        master.title("Math Worksheet Generator")


        master.geometry("400x250")

        # master.configure(bg="#125555")

        # Create labels and input fields

        self.type_label = tk.Label(master, text="Type of problem (+, -, x, /, mix):")
        self.type_label.pack(pady=5)
        self.type_entry = tk.Entry(master)
        self.type_entry.pack(pady=5)

        self.max_label = tk.Label(master, text="Maximum number:")
        self.max_label.pack(pady=5)
        self.max_entry = tk.Entry(master)
        self.max_entry.pack(pady=5)


        self.question_label = tk.Label(master, text="Number of questions:")
        self.question_label.pack(pady=5)
        self.question_entry = tk.Entry(master)
        self.question_entry.pack(pady=5)

        # self.file_label = tk.Label(master, text="File Name:")
        # self.file_label.pack(pady=5)
        # self.file_entry = tk.Entry(master)
        # self.file_entry.pack(pady=5)


        # Create button to generate worksheet
        self.generate_button = tk.Button(master, text="Generate Worksheet", command=self.generate_worksheet,bg="blue", fg="white")
        self.generate_button.pack(pady=5)

    def generate_worksheet(self):
        # Get input values from the user
        type_ = self.type_entry.get()
        max_number = int(self.max_entry.get())
        question_count = int(self.question_entry.get())
        # filename = str(self.file_entry.get())

        # Create MathWorksheetGenerator object and generate questions
        worksheet_generator = MathWorksheetGenerator(type_, max_number, question_count)
        questions = worksheet_generator.get_list_of_questions(question_count)

        # Create PDF of worksheet
        worksheet_generator.make_question_page(questions)
        worksheet_generator.pdf.output("worksheet.pdf")

if __name__ == '__main__':
    root = tk.Tk()
    my_gui = MathWorksheetGUI(root)
    root.mainloop()
