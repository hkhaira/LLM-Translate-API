from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
from app.translator import translate_text

app = FastAPI()

class TranslationRequest(BaseModel):
    input_str: str

    @field_validator("input_str", mode="before")
    def cast_to_str(cls, v):
        return str(v)
    
@app.post("/translate/")
async def translate(request: TranslationRequest):
    try:
        translated = translate_text(request.input_str)
        return {"translated_text": translated}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))