"""Language Model Module involving model integrations and calls."""

from langchain_google_genai import ChatGoogleGenerativeAI


class Model:
    def __init__(
        self,
        model_name="gemini-2.5-pro",
        temperature=1.0,
        max_tokens=None,
        timeout=None,
        max_retries=1,
    ):
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.timeout = timeout
        self.max_retries = max_retries

    def _initialize_language_model(self):
        """Initialize and return a language model instance."""
        return ChatGoogleGenerativeAI(
            model=self.model_name,
            temperature=self.temperature,  # Gemini 3.0+ defaults to 1.0
            max_tokens=self.max_tokens,
            timeout=self.timeout,
            max_retries=self.max_retries,
            # other params...
        )

    def call_model(self, prompt):
        """Simulate a model call with a given prompt."""
        model = self._initialize_language_model()
        response = model.invoke(prompt)
        return response

    def call_model_with_structured_output(self, prompt, response_schema):
        """Simulate a model call with structured output."""
        model = self._initialize_language_model()
        model_with_structured_output = model.with_structured_output(
            schema=response_schema.model_json_schema(), method="json_schema"
        )
        return model_with_structured_output.invoke(prompt)
