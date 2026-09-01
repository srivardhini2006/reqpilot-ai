import json
import time

from google import genai

from config.settings import GEMINI_API_KEY, MODEL_NAME


class LLMService:
    """
    Central service responsible for communication with Gemini.
    Handles temporary API availability failures with retries.
    """

    def __init__(self):

        if not GEMINI_API_KEY:
            raise ValueError(
                "Gemini API key not found. Check your .env file."
            )

        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def _generate_content(self, prompt: str, config=None):
        """
        Send a request to Gemini with retry handling for
        temporary server availability errors.
        """

        max_retries = 3

        for attempt in range(max_retries):

            try:

                return self.client.models.generate_content(
                    model=MODEL_NAME,
                    contents=prompt,
                    config=config,
                )

            except Exception as error:

                error_message = str(error)

                if "503" not in error_message:
                    raise

                if attempt == max_retries - 1:
                    raise

                wait_time = 2 ** attempt

                print(
                    f"Gemini temporarily unavailable. "
                    f"Retrying in {wait_time} seconds..."
                )

                time.sleep(wait_time)

    def generate_text(self, prompt: str) -> str:
        """
        Generate a normal text response.
        """

        response = self._generate_content(prompt)

        return response.text

    def generate_json(self, prompt: str) -> dict:
        """
        Generate and return a JSON response.
        """

        response = self._generate_content(
            prompt,
            config={
                "response_mime_type": "application/json"
            }
        )

        return json.loads(response.text)