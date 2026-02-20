from sqlalchemy.orm import Session
from .models import ResumeAnalysis

def create_analysis(
    db: Session,
    resume_text: str,
    job_description: str,
    ats_score: int,
    strengths: str,
    weaknesses: str,
    suggestions: str,
):
    analysis = ResumeAnalysis(
        resume_text=resume_text,
        job_description=job_description,
        ats_score=ats_score,
        strengths=strengths,
        weaknesses=weaknesses,
        suggestions=suggestions,
    )

    db.add(analysis)
    db.commit()
    db.refresh(analysis)

    return analysis