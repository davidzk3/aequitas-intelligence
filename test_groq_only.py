import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# The models to cycle through
GROQ_MODELS = [
    "llama-3.3-70b-versatile",   # Most likely 2026 standard
    "llama-3.1-70b-versatile",   # High reliability 
    "llama3-70b-8192",           # Your current (failing) ID
    "mixtral-8x7b-32768"         # Stable alternative
]

def search_working_groq_model():
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    payload = {"price": -3039.81, "vol": -5639702.34}
    
    print("🔎 Searching for a compatible Groq model...")
    print("-" * 50)

    for model_id in GROQ_MODELS:
        try:
            print(f"Testing: {model_id}...", end=" ")
            completion = client.chat.completions.create(
                model=model_id,
                messages=[
                    {"role": "system", "content": "Return JSON only."},
                    {"role": "user", "content": f"Explain this variance as JSON: {payload}"}
                ],
                response_format={"type": "json_object"}
            )
            # If we get here, it worked!
            print("🟢 SUCCESS!")
            print(f"\n✅ USE THIS ID: {model_id}")
            return model_id
        except Exception as e:
            error_msg = str(e)
            if "does not exist" in error_msg or "Unknown model" in error_msg:
                print("❌ Not Found")
            elif "rate_limit_reached" in error_msg:
                print("⚠️ Rate Limited")
            else:
                print(f"❌ Error: {error_msg[:60]}...")
                
    print("-" * 50)
    print("❌ No working models found. Please check your Groq Dashboard for available models.")
    return None

if __name__ == "__main__":
    search_working_groq_model()