import customtkinter as ctk
from tkinter import filedialog
from core.parser import extract_text
from core.matcher import resume_score
from core.keyword_engine import missing_keywords

class ResumeTab(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.resume_path = None
        self.build_ui()

    def build_ui(self):
        # 1. Upload Button
        ctk.CTkButton(self, text="Upload Resume", command=self.upload_resume).pack(pady=10)
        
        # 2. Path Label
        self.resume_label = ctk.CTkLabel(self, text="No resume selected")
        self.resume_label.pack()

        # 3. JD Textbox
        ctk.CTkLabel(self, text="Paste Job Description").pack(pady=10)
        self.jd_box = ctk.CTkTextbox(self, height=200, width=900)
        self.jd_box.pack()

        # 4. Analyze Button
        ctk.CTkButton(self, text="Analyze", command=self.analyze).pack(pady=15)

        # 5. Results Labels
        self.score_label = ctk.CTkLabel(self, text="")
        self.score_label.pack()
        self.missing_label = ctk.CTkLabel(self, text="", wraplength=900, justify="left")
        self.missing_label.pack(pady=10)

    def upload_resume(self):
        self.resume_path = filedialog.askopenfilename(filetypes=[("PDF", "*.pdf"), ("Word", "*.docx")])
        if self.resume_path:
            self.resume_label.configure(text=self.resume_path)
        
    
    def analyze(self):
        # 1. Validation
        if not self.resume_path:
            self.score_label.configure(text="Please upload a resume first")
            return
        
        jd_text = self.jd_box.get("1.0", "end").strip()
        if not jd_text:
            self.score_label.configure(text="Please paste a job description")
            return

        # 2. Set "Loading" State
        self.score_label.configure(text="Analyzing match...", text_color="yellow")
        self.missing_label.configure(text="")
        self.update_idletasks() # Force the UI to show the "Analyzing..." text NOW

        try:
            # 3. Perform the heavy work
            resume_text = extract_text(self.resume_path)
            score = resume_score(resume_text, jd_text)
            missing = missing_keywords(resume_text, jd_text)

            # 4. Update with Results
            self.score_label.configure(text=f"Match Score: {score}%", text_color="white")
            self.missing_label.configure(text="Missing Keywords:\n" + ", ".join(missing))
            
        except Exception as e:
            self.score_label.configure(text="Analysis Failed", text_color="red")
            self.missing_label.configure(text=str(e))