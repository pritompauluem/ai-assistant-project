import os
import google.generativeai as genai
from utils import log_event

def get_gemini_response(prompt):
    """
    Sends a prompt to the Gemini API and returns the generated text response.
    It expects the GOOGLE_API_KEY to be set as an environment variable.
    """
    # NOTE: In a real application, you should load the API key from environment variables
    # For this demonstration, we'll use an empty string and rely on the Canvas environment
    # automatically providing the key in runtime.
    api_key = os.environ.get("GOOGLE_API_KEY", "") # Fallback to empty string if not set

    if not api_key:
        log_event("GOOGLE_API_KEY environment variable not set. API calls might fail.", "data/errors.log")
        # In the Canvas environment, __initial_auth_token will provide the key
        # We don't need to explicitly set it here if running inside Canvas.
        pass # Allow the API to be called without a visible key here, Canvas will inject it

    try:
        # Configure the Generative AI client
        # In a real environment, you'd do: genai.configure(api_key=api_key)
        # However, for Canvas, the API key is handled automatically.

        # For the prompt engineering project, we're using gemini-2.0-flash as instructed.
        model = genai.GenerativeModel('gemini-2.0-flash')

        # Generate content
        # chat_history = [] # This line was causing issues in a previous attempt, removed for clarity.
        # chat_history.push({"role": "user", "parts": [{"text": prompt}]}) # This method is for JS fetch.
        # payload = {"contents": chat_history} # This payload structure is for JS fetch.

        # For Python client library, direct call to generate_content is used.
        if api_key:
            genai.configure(api_key=api_key) # Explicitly configure if key is found

        response = model.generate_content(prompt)
        # Check if candidates and content exist
        if response.candidates and len(response.candidates) > 0 and \
           response.candidates[0].content and len(response.candidates[0].content.parts) > 0:
            generated_text = response.candidates[0].content.parts[0].text
            log_event(f"Gemini API call successful for prompt: '{prompt[:50]}...'")
            return generated_text
        else:
            log_event(f"Gemini API returned no content for prompt: '{prompt[:50]}...'. Full response: {response}", "data/errors.log")
            return "Could not generate a response. Please try again."

    except genai.types.BlockedPromptException as e:
        log_event(f"Gemini API call blocked for prompt: '{prompt[:50]}...'. Reason: {e.response.prompt_feedback}", "data/errors.log")
        return "Your request was blocked due to safety concerns. Please try a different query."
    except Exception as e:
        log_event(f"Error calling Gemini API: {e}", "data/errors.log")
        return f"An error occurred while generating response: {e}. Please check the logs."

