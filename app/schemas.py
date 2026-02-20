from pydantic import BaseModel

class ResumeResponse(BaseModel):
    ats_score: int
    strengths: str
    weaknesses: str
    suggestions: str

    class Config:
        from_attributes = True