import unittest
import os
import json
from app import app
from datetime import datetime
from feedback import FEEDBACK_FILE
from utils import ensure_directory_exists, save_json, load_json

class TestApp(unittest.TestCase):
    """
    Unit tests for the Flask application (app.py).
    """

    def setUp(self):
        """
        Set up for each test: Configure Flask app for testing and clear feedback log.
        """
        app.testing = True
        self.client = app.test_client()

        # Ensure the data directory exists
        ensure_directory_exists(os.path.dirname(FEEDBACK_FILE))
        # Clear the feedback file before each test to ensure a clean state
        with open(FEEDBACK_FILE, 'w') as f:
            json.dump([], f)
        print(f"Cleared {FEEDBACK_FILE} before test in TestApp.")

    def tearDown(self):
        """
        Clean up after each test: Clear feedback log.
        """
        # Clear the feedback file after each test
        with open(FEEDBACK_FILE, 'w') as f:
            json.dump([], f)
        print(f"Cleared {FEEDBACK_FILE} after test in TestApp.")

    def test_index_page(self):
        """
        Tests that the main index page loads successfully.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"AI Assistant", response.data)
        self.assertIn(b"Choose a Function:", response.data)
        print("test_index_page passed: Index page loads.")

    def test_generate_question_answering(self):
        """
        Tests the 'answer_question' functionality.
        Note: This test currently only verifies the response page loads,
        not the actual AI-generated content due to mocking external API calls
        being outside the scope of basic Flask route tests.
        """
        with unittest.mock.patch('gemini_api.get_gemini_response', return_value="Mocked AI Answer"):
            response = self.client.post('/generate', data={
                'function_choice': 'answer_question',
                'prompt_style': 'general',
                'user_input': 'What is the capital of France?'
            })
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"AI Assistant Response", response.data)
            self.assertIn(b"Your Query: What is the capital of France?", response.data)
            self.assertIn(b"AI Response: Mocked AI Answer", response.data)
        print("test_generate_question_answering passed: Question answering route works with mock.")

    def test_generate_summarize_text(self):
        """
        Tests the 'summarize_text' functionality.
        """
        with unittest.mock.patch('gemini_api.get_gemini_response', return_value="Mocked AI Summary"):
            response = self.client.post('/generate', data={
                'function_choice': 'summarize_text',
                'prompt_style': 'standard',
                'user_input': 'This is a long text to summarize.'
            })
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"AI Response: Mocked AI Summary", response.data)
        print("test_generate_summarize_text passed: Summarization route works with mock.")

    def test_generate_creative_content(self):
        """
        Tests the 'generate_creative_content' functionality.
        """
        with unittest.mock.patch('gemini_api.get_gemini_response', return_value="Mocked AI Story"):
            response = self.client.post('/generate', data={
                'function_choice': 'generate_creative_content',
                'prompt_style': 'story_standard',
                'user_input': 'a brave knight'
            })
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"AI Response: Mocked AI Story", response.data)
        print("test_generate_creative_content passed: Creative content route works with mock.")

    def test_feedback_submission_helpful(self):
        """
        Tests that helpful feedback is correctly saved.
        """
        query = "Test query for feedback."
        response_text = "Test AI response."
        helpful_status = "yes"
        current_time = datetime.now().isoformat()

        # Mock datetime.now() to ensure consistent timestamp for verification
        with unittest.mock.patch('datetime.datetime') as mock_dt:
            mock_dt.now.return_value = datetime.fromisoformat(current_time)
            mock_dt.isoformat.return_value = current_time # For saving
            mock_dt.fromisoformat.return_value = datetime.fromisoformat(current_time) # For loading

            response = self.client.post('/feedback', data={
                'query': query,
                'response': response_text,
                'helpful': helpful_status
            }, follow_redirects=True) # Follow redirect back to index

            self.assertEqual(response.status_code, 200) # Should redirect to index page (200 OK)
            self.assertIn(b"AI Assistant", response.data) # Verify it landed on index

            feedback_data = load_json(FEEDBACK_FILE)
            self.assertEqual(len(feedback_data), 1)
            self.assertEqual(feedback_data[0]["query"], query)
            self.assertEqual(feedback_data[0]["helpful"], True)
            self.assertEqual(feedback_data[0]["timestamp"], current_time)
        print("test_feedback_submission_helpful passed: Helpful feedback saved.")


    def test_feedback_submission_not_helpful(self):
        """
        Tests that unhelpful feedback is correctly saved.
        """
        query = "Another query for feedback."
        response_text = "Another AI response."
        helpful_status = "no"
        current_time = datetime.now().isoformat()

        with unittest.mock.patch('datetime.datetime') as mock_dt:
            mock_dt.now.return_value = datetime.fromisoformat(current_time)
            mock_dt.isoformat.return_value = current_time
            mock_dt.fromisoformat.return_value = datetime.fromisoformat(current_time)

            response = self.client.post('/feedback', data={
                'query': query,
                'response': response_text,
                'helpful': helpful_status
            }, follow_redirects=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn(b"AI Assistant", response.data)

            feedback_data = load_json(FEEDBACK_FILE)
            self.assertEqual(len(feedback_data), 1)
            self.assertEqual(feedback_data[0]["query"], query)
            self.assertEqual(feedback_data[0]["helpful"], False)
            self.assertEqual(feedback_data[0]["timestamp"], current_time)
        print("test_feedback_submission_not_helpful passed: Unhelpful feedback saved.")


if __name__ == '__main__':
    # To run these tests, you might need to install 'mock' if on Python < 3.3
    # pip install mock (if needed)
    unittest.main()
