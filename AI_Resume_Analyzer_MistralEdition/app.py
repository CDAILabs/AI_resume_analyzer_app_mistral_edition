import customtkinter as ctk
import os
import sys
from llm.llama_mistral_client import LLMClient
from ui.main_window import ResumeAnalyzerApp


def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def main():
    # 1️⃣ UI theme
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # 2️⃣ Load model using relative path
    model_path = r"D:\llama\models\tinyllama-1.1b-1t-openorca.Q4_K_M.gguf"

    llm_client = LLMClient(model_path=model_path)

    # 3️⃣ Start App
    app = ResumeAnalyzerApp(llm_client)
    app.mainloop()


if __name__ == "__main__":
    main()
