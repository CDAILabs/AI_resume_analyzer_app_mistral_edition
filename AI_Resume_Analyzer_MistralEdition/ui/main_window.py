import customtkinter as ctk
from ui.resume_tab import ResumeTab
from ui.cover_letter_tab import CoverLetterTab

class ResumeAnalyzerApp(ctk.CTk):
    def __init__(self, llm_client):
        super().__init__()

        # --- Window Configuration ---
        self.title("Resume Analyzer AI - Mistral Edition")
        self.geometry("1000x800")

        # --- Create Tabview Container ---
        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(fill="both", expand=True, padx=10, pady=10)

        # 1. Add the physical tabs to the widget
        tab_match_container = self.tabview.add("Resume Match")
        tab_cover_container = self.tabview.add("Cover Letter")

        # 2. Initialize and Place the Resume Tab
        # We pass tab_match_container as the 'master'
        self.resume_view = ResumeTab(master=tab_match_container)
        self.resume_view.pack(fill="both", expand=True)

        # 3. Initialize and Place the Cover Letter Tab
        # We pass functions (lambdas) so this tab can access data from the other tab
        self.cover_view = CoverLetterTab(
            master=tab_cover_container,
            llm_client=llm_client,
            get_resume_path=lambda: self.resume_view.resume_path,
            get_jd_text=lambda: self.resume_view.jd_box.get("1.0", "end").strip()
        )
        self.cover_view.pack(fill="both", expand=True)

if __name__ == "__main__":
    # This part is just for solo testing; usually app.py handles this.
    print("Please run app.py to start the application.")