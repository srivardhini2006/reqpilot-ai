from google import genai
from config.settings import GEMINI_API_KEY, MODEL_NAME


class LLMService:
    """
    Handles all communication with the configured LLM.
    """

    def __init__(self):
        if not GEMINI_API_KEY:
            raise ValueError("Gemini API key not found. Check your .env file.")

        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate_text(self, prompt: str) -> str:
        """
        Generate a text response from the LLM.
        """

        response = self.client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )

        return response.text