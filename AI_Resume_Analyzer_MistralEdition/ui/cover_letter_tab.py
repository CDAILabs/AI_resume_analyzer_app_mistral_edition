import customtkinter as ctk
import threading
from tkinter import filedialog, messagebox
from core.parser import extract_text
from docx import Document
from fpdf import FPDF

class CoverLetterTab(ctk.CTkFrame):
    def __init__(self, master, llm_client, get_resume_path, get_jd_text, **kwargs):
        super().__init__(master, **kwargs)
        self.llm = llm_client.get_llm()
        self.get_resume_path = get_resume_path
        self.get_jd_text = get_jd_text
        self.build_ui()

    def build_ui(self):
        # 1. Store the button as self.gen_button so we can disable it
        self.gen_button = ctk.CTkButton(
            self, 
            text="Generate Cover Letter", 
            command=self.generate
        )
        self.gen_button.pack(pady=10)

        # 2. Output Textbox
        self.cover_text = ctk.CTkTextbox(self, height=450, width=900)
        self.cover_text.pack(pady=10)

        # 3. Export Button
        ctk.CTkButton(self, text="Save Cover Letter", command=self.save_letter).pack(pady=10)
    
    def generate(self):
        path = self.get_resume_path()
        jd = self.get_jd_text()
        
        if not path or not jd:
            messagebox.showwarning("Warning", "Upload resume and paste JD first!")
            return
        
        # Disable button and set loading state
        self.gen_button.configure(state="disabled", text="Generation in Progress...")
        self.cover_text.configure(text_color="white") # Reset color if it was red from an error
        self.cover_text.delete("1.0", "end")
        self.cover_text.insert("1.0", "Generating cover letter... Please wait...")
        
        threading.Thread(target=self._run_gen, args=(path, jd), daemon=True).start()

    def _run_gen(self, path, jd):
        try:
            first_token = True
            resume_text = extract_text(path)
            
            prompt = f"[INST] Write a cover letter using this Resume:\n{resume_text[:1200]}\n\nFor this Job:\n{jd[:1200]} [/INST]"
            
            stream = self.llm(prompt, max_tokens=800, stream=True)
            
            for chunk in stream:
                token = chunk["choices"][0].get("text", "")
                
                if first_token:
                    # Clear "Please wait" only when the first word arrives
                    self.after(0, lambda: self.cover_text.delete("1.0", "end"))
                    first_token = False
                
                self.after(0, lambda t=token: self._append_text(t))

        except Exception as e:
            error_display = f"\n\n{'='*30}\n[AI ERROR]: {str(e)}\n{'='*30}"
            self.after(0, lambda: self.cover_text.insert("end", error_display))
            self.after(0, lambda: self.cover_text.configure(text_color="red"))

        finally:
            # Re-enable the button
            self.after(0, lambda: self.gen_button.configure(
                state="normal", 
                text="Generate Cover Letter"
            ))

    def _append_text(self, t):
        self.cover_text.insert("end", t)
        self.cover_text.see("end")

    def save_letter(self):
        letter = self.cover_text.get("1.0", "end").strip()
        if not letter or "Please wait" in letter:
            messagebox.showwarning("Warning", "No cover letter content to save!")
            return
            
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text File", "*.txt"), ("Word Doc", "*.docx"), ("PDF", "*.pdf")]
        )
        
        if file_path:
            try:
                if file_path.endswith(".txt"):
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(letter)
                elif file_path.endswith(".docx"):
                    doc = Document()
                    doc.add_paragraph(letter)
                    doc.save(file_path)
                elif file_path.endswith(".pdf"):
                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_font("Arial", size=12)
                    for line in letter.split('\n'):
                        pdf.multi_cell(0, 10, line)
                    pdf.output(file_path)
                
                messagebox.showinfo("Saved", "File saved successfully!")
            except Exception as e:
                messagebox.showerror("Save Error", f"Could not save file: {e}")
                def _run_gen(self, path, jd):
                    resume_text = extract_text(path)
                    prompt = f"[INST] Write a cover letter for this Resume:\n{resume_text[:1000]}\n\nJD:\n{jd[:1000]} [/INST]"
                    stream = self.llm(prompt, max_tokens=600, stream=True)
                    for chunk in stream:
                        token = chunk["choices"][0]["text"]
                        self.after(0, lambda t=token: self.cover_text.insert("end", t))
      