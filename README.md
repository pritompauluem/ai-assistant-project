# AI Assistant Development Project

This project implements a basic web-based AI Assistant using Flask and the Google Gemini API. It demonstrates prompt engineering principles by allowing users to choose different functions and prompt styles to guide the AI's responses. The AI's responses are formatted using Markdown, which is then rendered into HTML for a visually appealing presentation.

## Features

- **Three Core Functions:**
  - **Answer Questions:** Get factual information.
  - **Summarize Text:** Condense given articles or blocks of text.
  - **Generate Creative Content:** Create stories, poems, or essay ideas.
- **Flexible Prompt Design:** Each function offers multiple prompt styles (e.g., General, Detailed, Concise for questions; Standard, Key Points, Very Short for summaries; various creative styles).
- **User-Friendly Web Interface:** Simple HTML forms for input and clear display of AI responses.
- **Formatted AI Responses:** AI-generated text, initially in Markdown, is converted to HTML for enhanced readability and presentation.
- **Feedback Mechanism:** Users can provide feedback (helpful/not helpful) on AI responses, which is logged for potential analysis and improvement.

## File Structure

The project's file structure is organized as follows, listing key files and directories with brief descriptions:
''' bash
├── venv/ # Virtual environment folder
├── app.py # Main Flask application
├── prompts.py # Custom prompt designs for each function
├── gemini_api.py # Functions to interact with Google Gemini API
├── feedback.py # Manages user feedback (save, read)
├── utils.py # Helper functions (e.g., ensure directory, log events)
├── requirements.txt # List of project dependencies
├── README.md # This file
├── .env # Optional: For setting GOOGLE_API_KEY locally
├── templates/ # HTML templates for web UI
│ ├── base.html # Common layout template
│ ├── index.html # Input page (choose function + input)
│ └── result.html # Output page (shows response + feedback)
├── static/ # Static assets (CSS)
│ └── style.css # Basic styling
└── data/ # Stores persistent data
├── feedback_log.json # Collected feedback in JSON
└── logs.txt # Application logs
'''
## Setup Instructions

1.  **Clone the Repository (if applicable):**

    ```bash
    # If this were a real repository
    # git clone <repository_url>
    # cd ai-assistant
    ```

2.  **Create a Virtual Environment:**
    It's highly recommended to use a virtual environment to manage dependencies.

    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**

    - **On Windows:**
      ```bash
      venv\Scripts\activate
      ```
    - **On macOS/Linux:**
      ```bash
      source venv/bin/activate
      ```

4.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    This command will install Flask, `google-generativeai`, and `markdown` as specified in `requirements.txt`.

5.  **Set up Google Gemini API Key:**
    The application needs a Google Gemini API key. **Do NOT hardcode your API key directly in `gemini_api.py` or any other source file.** For local development, you can set it as an environment variable.

    - **Obtain your API Key:** Visit [Google AI Studio](https://aistudio.google.com/app/apikey) to generate an API key.
    - **Using Environment Variable (Temporary for current session):**
      - **On Windows:**
        ```bash
        set GOOGLE_API_KEY="YOUR_API_KEY"
        ```
      - **On macOS/Linux:**
        ```bash
        export GOOGLE_API_KEY="YOUR_API_KEY"
        ```
      - Replace `YOUR_API_KEY` with the actual key you obtained.
    - **Using a `.env` file (Optional for local development):**
      - If you prefer to use a `.env` file (you would need `pip install python-dotenv` if it's not already installed), create a file named `.env` in the root directory and add:
        ```
        GOOGLE_API_KEY="YOUR_API_KEY"
        ```
      - The `gemini_api.py` file is configured to attempt to read from environment variables.

6.  **Run the Flask Application:**
    It is generally recommended to use `flask run` for Flask applications as it properly initializes the Flask environment.

    ```bash
    flask run
    ```

    You can also run `app.py` directly, though `flask run` is preferred for development:

    ```bash
    python app.py
    ```

    The application will typically run on `http://127.0.0.1:5000/`. Open this URL in your web browser.

## How to Use the AI Assistant

1.  **Access the Application:** Open your web browser and navigate to `http://127.0.0.1:5000/` (or the address shown in your terminal after running `flask run`).

2.  **Choose a Function:**

    - Select "Answer Questions," "Summarize Text," or "Generate Creative Content" from the "Choose a Function" dropdown.

3.  **Select a Prompt Style:**

    - Based on your chosen function, the "Choose a Prompt Style" dropdown will update. Select the style that best suits the kind of response you want (e.g., "Detailed" for questions, "Key Points" for summaries, "Imaginative" for stories).

4.  **Enter Your Query/Text:**

    - In the large text area, type your question, paste the text you want to summarize, or enter the topic for your creative content.

5.  **Generate Response:**

    - Click the "Generate Response" button. The AI's formatted response will be displayed on a new page.

6.  **Provide Feedback:**

    - After viewing the response, you can indicate whether it was "Helpful" or "Not Helpful" by clicking the respective buttons. This feedback is logged for future improvements.

7.  **Go Back:**
    - Click "Go Back" to return to the main input page and try another query.

## Documentation (user_guide.pptx)

A separate PowerPoint file named `user_guide.pptx` would contain a user guide explaining how to use the AI Assistant and detailing its different functions. This file is designed as a standalone visual guide for end-users, simplifying complex setup and usage details into an accessible format for presentations or quick reference. It covers the same ground as this README but in a more visual, step-by-step manner.

---

Feel free to explore the code, modify prompts, and expand the functionality!
