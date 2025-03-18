import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# List available models
available_models = genai.list_models()
print("✅ Available Gemini Models:")
for model in available_models:
    print(model.name)
