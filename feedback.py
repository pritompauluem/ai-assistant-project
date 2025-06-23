import os
from utils import ensure_directory_exists, load_json, save_json, log_event

FEEDBACK_FILE = "data/feedback_log.json"

def get_all_feedback():
    """
    Retrieves all feedback entries from the feedback log file.
    Ensures the data directory exists before attempting to read.
    """
    ensure_directory_exists(os.path.dirname(FEEDBACK_FILE))
    return load_json(FEEDBACK_FILE, default_value=[])

def save_feedback(query, response, helpful, timestamp):
    """
    Saves a new feedback entry to the feedback log file.
    :param query: The original user query.
    :param response: The AI's response.
    :param helpful: Boolean indicating if the response was helpful.
    :param timestamp: Timestamp of the feedback.
    """
    feedback_data = get_all_feedback()
    feedback_entry = {
        "query": query,
        "response": response,
        "helpful": helpful,
        "timestamp": timestamp
    }
    feedback_data.append(feedback_entry)
    save_json(FEEDBACK_FILE, feedback_data)
    log_event(f"Feedback saved: Query='{query[:50]}...', Helpful={helpful}")

