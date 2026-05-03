import os
import json
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

# The exact mathematical data from your successful runs
MOCK_MATH = {"price_variance": -3039.81, "volume_variance": -5639702.34, "mix_variance": -1653.73}

class VarianceAnalysis(BaseModel):
    price_variance: float
    volume_variance: float
    mix_variance: float
    strategic_narrative: str
    confidence_score: float

def test_gemini():
    try:
        from google import genai
        client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
        # Using the model that worked for you in the support agent
        client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Analyze as JSON: {MOCK_MATH}",
            config={'response_mime_type': 'application/json', 'response_schema': VarianceAnalysis}
        )
        return "🟢 SUCCESS"
    except Exception as e:
        return f"🔴 FAILED: {type(e).__name__}"

def test_groq():
    try:
        from groq import Groq
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        # FIX: Explicitly forcing the model to see 'JSON' in both system and user prompts
        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You are a financial analyst. Return ONLY a valid JSON object."},
                {"role": "user", "content": f"Analyze these variances and return a JSON object: {MOCK_MATH}"}
            ],
            response_format={"type": "json_object"}
        )
        # Verify it can be parsed
        json.loads(completion.choices[0].message.content)
        return "🟢 SUCCESS"
    except Exception as e:
        # If this still fails, it may be a specific rate limit or model access issue on your key
        return f"🔴 FAILED: {type(e).__name__} - {str(e)[:50]}"

def test_mistral():
    try:
        try:
            from mistralai import Mistral
        except ImportError:
            from mistralai.client import Mistral
            
        client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
        client.chat.complete(
            model="mistral-large-latest",
            messages=[{"role": "user", "content": f"Analyze as JSON: {MOCK_MATH}"}],
            response_format={"type": "json_object"}
        )
        return "🟢 SUCCESS"
    except Exception as e:
        return f"🔴 FAILED: {type(e).__name__}"

if __name__ == "__main__":
    print("🧪 RUNNING REFINED 3-TIER STACK...")
    print(f"Gemini  | {test_gemini()}")
    print(f"Groq    | {test_groq()}")
    print(f"Mistral | {test_mistral()}")