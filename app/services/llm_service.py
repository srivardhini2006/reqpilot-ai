import json

from google import genai

from config.settings import GEMINI_API_KEY, MODEL_NAME


class LLMService:
    """
    Central service responsible for communication with Gemini.
    """

    def __init__(self):

        if not GEMINI_API_KEY:
            raise ValueError(
                "Gemini API key not found. Check your .env file."
            )

        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate_text(self, prompt: str) -> str:
        """
        Generate a normal text response.
        """

        response = self.client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )

        return response.text

    def generate_json(self, prompt: str) -> dict:
        """
        Generate and return a JSON response.
        """

        response = self.client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config={
                "response_mime_type": "application/json"
            }
        )

        return json.loads(response.text)