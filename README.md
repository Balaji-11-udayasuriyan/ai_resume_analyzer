# 🚀 AI Resume Analyzer API

An AI-powered Resume Analyzer built using **FastAPI, PostgreSQL, and Groq (OpenAI-compatible models)**.

This API extracts text from uploaded resumes (PDF), compares it with a job description using a Large Language Model, calculates an ATS score, identifies strengths & weaknesses, and stores the analysis in PostgreSQL.

---

## 📌 Features

- 📄 Upload Resume (PDF)
- 🧠 AI-based ATS Score Calculation
- 💪 Strength & Weakness Analysis
- 📊 Improvement Suggestions
- 🐘 PostgreSQL Database Storage
- 📖 Swagger API Documentation
- ⚡ Clean Modular FastAPI Architecture

---

## 🛠️ Tech Stack

- **Backend:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **AI Model:** openai/gpt-oss-120b (Groq OpenAI-compatible endpoint)
- **PDF Parsing:** PyMuPDF
- **Environment Management:** python-dotenv

---

## 📂 Project Structure

```bash
ai_resume_analyzer/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── services/
│   │   ├── ai_service.py
│   │   └── resume_parser.py
│
├── .env
├── requirements.txt
└── README.md
```

## 🐘 PostgreSQL Setup

1. Install PostgreSQL
2. Open SQL Shell (psql)
3. Create database:

```sql
CREATE DATABASE resume_db;
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/resume_db
GROQ_API_KEY=your_groq_api_key
```

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/ai_resume_analyzer.git
cd ai_resume_analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 📬 API Endpoint

### POST `/analyze`

Form Data:

| Key | Type | Description |
|------|------|-------------|
| job_description | Text | Job description content |
| file | File | Resume (PDF only) |

---

## 📥 Sample Response

```json
{
  "ats_score": 84,
  "strengths": "Strong FastAPI and PostgreSQL experience with clean API design.",
  "weaknesses": "Limited cloud deployment exposure.",
  "suggestions": "Add AWS/GCP deployment projects and quantify impact with metrics."
}
```

---

## 🗄 Database Table

Table Name: `resume_analysis`

| Column | Type |
|--------|------|
| id | Integer |
| resume_text | Text |
| job_description | Text |
| ats_score | Integer |
| strengths | Text |
| weaknesses | Text |
| suggestions | Text |

---

## output 
<img width="1920" height="1080" alt="Screenshot (63)" src="https://github.com/user-attachments/assets/f9d6e435-b1ea-4886-9151-26fb589500ef" />
<img width="1920" height="1080" alt="Screenshot (64)" src="https://github.com/user-attachments/assets/f9d6e435-b1ea-4886-9151-26fb589500ef" />



---
## ⚙️ How It Works

1. Upload PDF Resume
2. Extract text using PyMuPDF
3. Send resume + JD to LLM
4. Receive structured JSON output
5. Store analysis in PostgreSQL
6. Return structured response

---

## 🚀 Future Improvements

- JWT Authentication
- User Accounts
- Dashboard Analytics
- Docker Support
- Cloud Deployment
- Skill Matching Percentage Scoring
- Keyword Extraction Engine

---

## 👨‍💻 Author

Balaji U  
Python Backend Developer | FastAPI | PostgreSQL | AI Integration

---

## 📜 License

MIT License
