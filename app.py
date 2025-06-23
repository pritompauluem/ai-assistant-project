import os
from flask import Flask, request, render_template, redirect, url_for
from datetime import datetime
from utils import log_event, ensure_directory_exists
from prompts import get_question_answering_prompt, get_summarization_prompt, get_creative_content_prompt
from gemini_api import get_gemini_response
import markdown

app = Flask(__name__)

# Ensure the data directory exists on startup
DATA_DIR = 'data'
ensure_directory_exists(DATA_DIR)
log_event("Application started and data directory ensured.")

@app.route('/')
def index():
    """
    Renders the main input page for the AI Assistant.
    """
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    """
    Handles the user's request, generates a response using the AI model,
    converts markdown to HTML, and displays the result.
    """
    function_choice = request.form['function_choice']
    prompt_style = request.form['prompt_style']
    user_input = request.form['user_input']

    prompt = ""
    ai_response = "Error: Could not generate a response."
    original_ai_response = "" # Store the original, raw AI response
    ai_response_html = "" # Store the HTML converted response

    if function_choice == 'answer_question':
        prompt = get_question_answering_prompt(user_input, prompt_type=prompt_style)
    elif function_choice == 'summarize_text':
        prompt = get_summarization_prompt(user_input, prompt_type=prompt_style)
    elif function_choice == 'generate_creative_content':
        if '_' in prompt_style:
            parts = prompt_style.split('_', 1)
            content_type = parts[0]
            creative_prompt_type = parts[1]
        else:
            content_type = "story"
            creative_prompt_type = prompt_style
        prompt = get_creative_content_prompt(user_input, content_type=content_type, prompt_type=creative_prompt_type)
    else:
        log_event(f"Invalid function choice received: {function_choice}", "data/errors.log")
        ai_response = "Invalid function selected."

    if prompt:
        log_event(f"Generating response for function: {function_choice}, style: {prompt_style}, input: '{user_input[:50]}...' using Gemini.")
        original_ai_response = get_gemini_response(prompt) # Get the raw response
        log_event(f"AI Response generated: '{original_ai_response[:50]}...'")

        # Convert Markdown response to HTML for proper rendering
        ai_response_html = markdown.markdown(original_ai_response)

    # Pass both the HTML for display and the original raw text for feedback logging
    return render_template('result.html', query=user_input, response=ai_response_html, original_ai_response=original_ai_response)

@app.route('/feedback', methods=['POST'])
def feedback():
    """
    Collects user feedback on the AI's response.
    """
    query = request.form['query']
    response = request.form['response'] # This will now be the original raw response
    helpful = request.form['helpful'] == 'yes'
    timestamp = datetime.now().isoformat()

    save_feedback(query, response, helpful, timestamp)
    log_event(f"User feedback received: Query='{query[:50]}...', Helpful={helpful}")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

