import unittest
import os
import json
from datetime import datetime
from feedback import save_feedback, get_all_feedback, FEEDBACK_FILE
from utils import ensure_directory_exists, save_json, load_json

class TestFeedback(unittest.TestCase):
    """
    Unit tests for the feedback management functions in feedback.py.
    """

    def setUp(self):
        """
        Set up for each test: ensure data directory exists and clear feedback log.
        """
        ensure_directory_exists(os.path.dirname(FEEDBACK_FILE))
        # Clear the feedback file before each test to ensure a clean state
        with open(FEEDBACK_FILE, 'w') as f:
            json.dump([], f)
        print(f"Cleared {FEEDBACK_FILE} before test.")

    def tearDown(self):
        """
        Clean up after each test: ensure data directory exists and clear feedback log.
        """
        ensure_directory_exists(os.path.dirname(FEEDBACK_FILE))
        # Clear the feedback file after each test
        with open(FEEDBACK_FILE, 'w') as f:
            json.dump([], f)
        print(f"Cleared {FEEDBACK_FILE} after test.")

    def test_save_feedback(self):
        """
        Tests that feedback is correctly saved to the JSON file.
        """
        query = "Test query for saving."
        response = "Test response."
        helpful = True
        timestamp = datetime.now().isoformat()

        save_feedback(query, response, helpful, timestamp)

        # Verify the content of the feedback file
        feedback_data = load_json(FEEDBACK_FILE)

        self.assertIsInstance(feedback_data, list)
        self.assertEqual(len(feedback_data), 1)

        saved_entry = feedback_data[0]
        self.assertEqual(saved_entry["query"], query)
        self.assertEqual(saved_entry["response"], response)
        self.assertEqual(saved_entry["helpful"], helpful)
        self.assertEqual(saved_entry["timestamp"], timestamp)
        print("test_save_feedback passed: Feedback saved correctly.")

    def test_get_all_feedback_empty(self):
        """
        Tests retrieving feedback when the file is empty.
        """
        feedback_data = get_all_feedback()
        self.assertIsInstance(feedback_data, list)
        self.assertEqual(len(feedback_data), 0)
        print("test_get_all_feedback_empty passed: Returns empty list for empty file.")

    def test_get_all_feedback_with_data(self):
        """
        Tests retrieving multiple feedback entries.
        """
        # Manually add some data to the feedback file
        initial_data = [
            {
                "query": "Q1",
                "response": "R1",
                "helpful": True,
                "timestamp": datetime.now().isoformat()
            },
            {
                "query": "Q2",
                "response": "R2",
                "helpful": False,
                "timestamp": datetime.now().isoformat()
            }
        ]
        save_json(FEEDBACK_FILE, initial_data)

        feedback_data = get_all_feedback()
        self.assertIsInstance(feedback_data, list)
        self.assertEqual(len(feedback_data), 2)
        self.assertEqual(feedback_data[0]["query"], "Q1")
        self.assertEqual(feedback_data[1]["response"], "R2")
        print("test_get_all_feedback_with_data passed: Retrieves all feedback entries.")

    def test_save_multiple_feedbacks(self):
        """
        Tests saving multiple feedback entries sequentially.
        """
        save_feedback("Query A", "Response A", True, datetime.now().isoformat())
        save_feedback("Query B", "Response B", False, datetime.now().isoformat())

        feedback_data = get_all_feedback()
        self.assertEqual(len(feedback_data), 2)
        self.assertEqual(feedback_data[0]["query"], "Query A")
        self.assertEqual(feedback_data[1]["query"], "Query B")
        self.assertEqual(feedback_data[1]["helpful"], False)
        print("test_save_multiple_feedbacks passed: Multiple feedbacks saved correctly.")

if __name__ == '__main__':
    unittest.main()
