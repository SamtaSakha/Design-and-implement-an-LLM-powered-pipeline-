import google.generativeai as genai
import os

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_NAME = "models/gemini-flash-latest"
model = genai.GenerativeModel(MODEL_NAME)

def analyze_feedback(text: str) -> str:
    """
    Analyze user feedback and return sentiment + summary.
    """
    prompt = f"""
    Analyze the following customer feedback.
    1. Classify sentiment as Positive, Neutral, or Negative
    2. Give a short reason

    Feedback: {text}
    """

    response = model.generate_content(prompt)
    return response.text
