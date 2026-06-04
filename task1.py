import os
import tkinter as tk
from tkinter import messagebox, ttk

FILE_NAME = "students.txt"


def load_data():
    """Файлдан деректерді қауіпсіз оқу"""
    students = []
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        students.append({
                            "name": parts[0],
                            "id": parts[1],
                            "gpa": float(parts[2])
                        })
        except Exception as e:
            messagebox.showerror("⚠️ Қате", f"Деректерді оқу кезінде қате туындады: {e}")
    return students


def save_data(students):
    """Деректерді файлға сенімді сақтау"""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            for student in students:
                file.write(f"{student['name']},{student['id']},{student['gpa']}\n")
    except Exception as e:
        messagebox.showerror("⚠️ Қате", f"Деректерді сақтау сәтсіз аяқталды: {e}")


class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Студенттерді басқару жүйесі v2.0 ✨")
        self.root.geometry("650x500")
        self.root.configure(bg="#f0f4f8")

        # Деректерді жүктеу
        self.students = load_data()

        # --- ЖОҒАРҒЫ БӨЛІМ: Деректер енгізу панелі ---
        input_frame = tk.LabelFrame(root, text=" Жаңа студент қосу ", font=("Arial", 10, "bold"), bg="#f0f4f8",
                                    fg="#1a365d")
        input_frame.pack(fill="x", padx=15, pady=10)

        tk.Label(input_frame, text="Аты-жөні:", bg="#f0f4f8").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.ent_name = tk.Entry(input_frame, width=25)
        self.ent_name.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="ID (Тек сан):", bg="#f0f4f8").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.ent_id = tk.Entry(input_frame, width=15)
        self.ent_id.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(input_frame, text="GPA (0.0 - 4.0):", bg="#f0f4f8").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.ent_gpa = tk.Entry(input_frame, width=10)
        self.ent_gpa.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        btn_add = tk.Button(input_frame, text="➕ Қосу және Сақтау", bg="#2b6cb0", fg="white", font=("Arial", 9, "bold"),
                            command=self.add_student_gui)
        btn_add.grid(row=1, column=2, columnspan=2, padx=5, pady=5, sticky="e")

        # --- ОРТАҢҒЫ БӨЛІМ: Іздеу және Сұрыптау панелі ---
        action_frame = tk.Frame(root, bg="#f0f4f8")
        action_frame.pack(fill="x", padx=15, pady=5)

        tk.Label(action_frame, text="🔍 Іздеу:", bg="#f0f4f8").pack(side="left", padx=2)
        self.ent_search = tk.Entry(action_frame, width=20)
        self.ent_search.pack(side="left", padx=5)

        btn_search = tk.Button(action_frame, text="Табу", bg="#4a5568", fg="white", command=self.search_student_gui)
        btn_search.pack(side="left", padx=2)

        btn_reset = tk.Button(action_frame, text="🔄 Жаңарту", bg="#718096", fg="white", command=self.update_table)
        btn_reset.pack(side="left", padx=15)

        btn_sort = tk.Button(action_frame, text="🔤 Алфавитпен сұрыптау", bg="#2f855a", fg="white",
                             font=("Arial", 9, "bold"), command=self.sort_students_gui)
        btn_sort.pack(side="right", padx=5)

        # --- ТӨМЕНГІ БӨЛІМ: Деректер кестесі (Treeview) ---
        table_frame = tk.Frame(root)
        table_frame.pack(fill="both", expand=True, padx=15, pady=10)

        columns = ("name", "id", "gpa")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        self.tree.heading("name", text="Студенттің аты-жөні")
        self.tree.heading("id", text="ID Нөмірі")
        self.tree.heading("gpa", text="GPA")

        self.tree.column("name", width=300)
        self.tree.column("id", width=150, anchor="center")
        self.tree.column("gpa", width=100, anchor="center")

        # Тігінен айналдыру жолағы (Scrollbar)
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Кестені алғашқы деректермен толтыру
        self.update_table()

    def update_table(self, data_list=None):
        """Кестедегі мәліметтерді жаңартып отыратын ішкі функция"""
        # Ескі жолдарды тазалау
        for item in self.tree.get_children():
            self.tree.delete(item)

        display_list = data_list if data_list is not None else self.students

        # Жаңа жолдарды қосу
        for s in display_list:
            self.tree.insert("", "end", values=(s["name"], s["id"], f"{s['gpa']:.2f}"))

    def add_student_gui(self):
        """Жаңа студент қосудың графикалық логикасы"""
        name = self.ent_name.get().strip()
        student_id = self.ent_id.get().strip()
        gpa_str = self.ent_gpa.get().strip()

        # Валидациялық тексерістер
        if not name:
            messagebox.showwarning("Қате", "❌ Аты-жөні бос болмауы керек!")
            return

        if not student_id.isdigit():
            messagebox.showwarning("Қате", "❌ ID тек сандардан тұруы тиіс!")
            return

        try:
            gpa = float(gpa_str)
            if gpa < 0.0 or gpa > 4.0:
                messagebox.showwarning("Қате", "❌ GPA 0.0 мен 4.0 аралығында болуы керек!")
                return
        except ValueError:
            messagebox.showwarning("Логикалық қате", "❌ GPA үшін тек ондық сандарды енгізіңіз (Мысалы: 3.67)!")
            return

        # Егер барлық тексерістен сәтті өтсе:
        self.students.append({"name": name, "id": student_id, "gpa": gpa})
        save_data(self.students)
        self.update_table()

        # Енгізу өрістерін тазалау
        self.ent_name.delete(0, tk.END)
        self.ent_id.delete(0, tk.END)
        self.ent_gpa.delete(0, tk.END)
        messagebox.showinfo("Сәтті", "🎉 Студент сәтті қосылды және файлға сақталды!")

    def search_student_gui(self):
        """Аты-жөні бойынша ішінара іздеу"""
        search_name = self.ent_search.get().strip().lower()
        if not search_name:
            messagebox.showwarning("Ескерту", "❌ Іздеу өрісі бос!")
            self.update_table()
            return

        found = [s for s in self.students if search_name in s['name'].lower()]
        if found:
            self.update_table(found)
        else:
            messagebox.showinfo("Нәтиже", "❌ Кешіріңіз, мұндай студент табылмады.")
            self.update_table([])

    def sort_students_gui(self):
        """Алфавит бойынша сұрыптап көрсету"""
        if not self.students:
            messagebox.showinfo("Ақпарат", "📭 Сұрыптайтын дерек жоқ, тізім бос.")
            return
        sorted_list = sorted(self.students, key=lambda x: x['name'])
        self.update_table(sorted_list)
        messagebox.showinfo("Сұрыптау", "🔤 Кестедегі студенттер аты бойынша сұрыпталды!")


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()