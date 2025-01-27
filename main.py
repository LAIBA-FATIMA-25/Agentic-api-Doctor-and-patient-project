from fastapi import FastAPI
from dotenv import load_dotenv
from router.doctor_router import router as doctor_router
from services.gemini_service import call_llm

load_dotenv()  # Load environment variables from .env file

app = FastAPI(
    title="Doctor-Patient Symptom Checker API",
    description="A FastAPI-based backend that lets patients input symptoms and receive diagnostic suggestions.",
    version="1.0.0",
)

# Include the doctor routes
app.include_router(doctor_router, prefix="/doctor")

@app.post("/generate-response/")
async def generate_response(prompt: str):
    try:
        response = call_llm(prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))