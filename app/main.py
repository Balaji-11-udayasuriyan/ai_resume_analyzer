from fastapi import FastAPI, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import Base, engine, SessionLocal
from .services.resume_parser import extract_text_from_pdf
from .services.ai_service import analyze_resume
from .crud import create_analysis
from .schemas import ResumeResponse

# Create tables automatically
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Resume Analyzer API")

# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/analyze", response_model=ResumeResponse)
async def analyze_resume_api(
    job_description: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files allowed")

    try:
        resume_text = extract_text_from_pdf(file)

        ai_result = analyze_resume(resume_text, job_description)

        saved = create_analysis(
            db=db,
            resume_text=resume_text,
            job_description=job_description,
            ats_score=ai_result["ats_score"],
            strengths=ai_result["strengths"],
            weaknesses=ai_result["weaknesses"],
            suggestions=ai_result["suggestions"],
        )

        return saved

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))