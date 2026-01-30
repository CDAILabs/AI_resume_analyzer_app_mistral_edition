🤖 AI Resume Analyzer App — Mistral Edition
An AI-powered desktop application that analyzes resumes, matches them against job descriptions, extracts key skills, and generates personalized cover letters — all powered by Mistral 7B, running fully locally on CPU.
No cloud. No API keys. No GPU required.
________________________________________
✨ Features
•	📄 Resume parsing and keyword extraction
•	🎯 Resume vs Job Description matching
•	✍️ AI-generated, job-specific cover letters
•	🧠 Powered by Mistral-7B-Instruct (GGUF)
•	🪟 Windows-friendly desktop UI
•	🔒 Fully offline & secure
________________________________________
🌟 Unique Selling Points (USP)
•	🖥 Runs 100% locally — no internet required after setup
•	⚙️ CPU-only execution — no high-end GPU needed
•	🔐 Privacy-first & secure — resumes never leave your machine
•	💸 No API costs — completely free to run
•	📦 Lightweight GGUF model support
Ideal for users who care about data privacy, offline usage, and low hardware requirements.

🧠 LLM Requirement (Important)
This application requires Mistral 7B (GGUF format) to run locally.
🔽 Step 1: Download Mistral Model
Download the model from Hugging Face:
👉 Mistral 7B Instruct GGUF
https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF
Recommended file (example):
mistral-7b-instruct-v0.2.Q4_K_M.gguf
💡 Smaller quantized models (Q4 / Q5) are recommended for most systems.
________________________________________
📂 Step 2: Place the Model File
Save the downloaded .gguf file anywhere on your system, for example:
C:\models\mistral\mistral-7b-instruct-v0.2.Q4_K_M.gguf
________________________________________
🛠 Step 3: Set Model Path in app.py
Open app.py and update the model path:
MISTRAL_MODEL_PATH = r"C:\models\mistral\mistral-7b-instruct-v0.2.Q4_K_M.gguf"
⚠️ Make sure:
•	The path is correct
•	You use r"" (raw string) on Windows
________________________________________
▶️ How to Run the App
1.	Clone the repository:
git clone https://github.com/your-username/AI_resume_analyzer_app_mistral_edition.git
cd resume_ai_app
2.	(Optional but recommended) Create a virtual environment:
python -m venv venv
venv\Scripts\activate
3.	Install dependencies:
pip install -r requirements.txt
4.	Run the app:
python app.py


🚀 Stay tuned! More powerful features are on the way.
