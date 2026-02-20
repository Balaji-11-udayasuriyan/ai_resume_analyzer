import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def analyze_resume(resume_text: str, job_description: str):

    prompt = f"""
You are an ATS Resume Analyzer.

Return STRICT JSON:

{{
  "ats_score": number between 0-100,
  "strengths": "string",
  "weaknesses": "string",
  "suggestions": "string"
}}

Resume:
{resume_text}

Job Description:
{job_description}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    content = response.choices[0].message.content.strip()

    try:
        return json.loads(content)
    except:
        raise Exception("AI did not return valid JSON")