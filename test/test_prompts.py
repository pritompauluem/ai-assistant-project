import unittest
from prompts import get_question_answering_prompt, get_summarization_prompt, get_creative_content_prompt

class TestPrompts(unittest.TestCase):
    """
    Unit tests for the prompt generation functions in prompts.py.
    """

    def test_get_question_answering_prompt(self):
        """
        Tests the various prompt types for question answering.
        """
        query = "What is the capital of France?"

        # Test 'general' prompt type
        general_prompt = get_question_answering_prompt(query, "general")
        self.assertIn("Answer the following question clearly and concisely:", general_prompt)
        self.assertIn(query, general_prompt)

        # Test 'detailed' prompt type
        detailed_prompt = get_question_answering_prompt(query, "detailed")
        self.assertIn("Provide a comprehensive answer to the following question", detailed_prompt)
        self.assertIn("including relevant context and details", detailed_prompt)
        self.assertIn(query, detailed_prompt)

        # Test 'concise' prompt type
        concise_prompt = get_question_answering_prompt(query, "concise")
        self.assertIn("Give a brief, direct answer to:", concise_prompt)
        self.assertIn(query, concise_prompt)

        # Test default behavior
        default_prompt = get_question_answering_prompt(query)
        self.assertIn("Answer the following question clearly and concisely:", default_prompt)
        self.assertIn(query, default_prompt)

    def test_get_summarization_prompt(self):
        """
        Tests the various prompt types for text summarization.
        """
        text = "This is a long piece of text that needs to be summarized. It contains several important points about AI and machine learning, discussing their impact on various industries and future potential."

        # Test 'standard' prompt type
        standard_summary_prompt = get_summarization_prompt(text, "standard")
        self.assertIn("Summarize the following text, capturing its main ideas and important details:", standard_summary_prompt)
        self.assertIn(text, standard_summary_prompt)

        # Test 'key_points' prompt type
        key_points_summary_prompt = get_summarization_prompt(text, "key_points")
        self.assertIn("Extract the most important key points and main arguments from the following text in bullet points:", key_points_summary_prompt)
        self.assertIn(text, key_points_summary_prompt)

        # Test 'very_short' prompt type
        very_short_summary_prompt = get_summarization_prompt(text, "very_short")
        self.assertIn("Provide a very brief, one-paragraph summary of the following text:", very_short_summary_prompt)
        self.assertIn(text, very_short_summary_prompt)

        # Test default behavior
        default_summary_prompt = get_summarization_prompt(text)
        self.assertIn("Summarize the following text, capturing its main ideas and important details:", default_summary_prompt)
        self.assertIn(text, default_summary_prompt)

    def test_get_creative_content_prompt_story(self):
        """
        Tests various prompt types for creative content generation (story).
        """
        topic = "a magical forest"

        # Test 'story_standard' prompt type
        standard_story_prompt = get_creative_content_prompt(topic, content_type="story", prompt_type="standard")
        self.assertIn(f"Write a short story about: {topic}", standard_story_prompt)

        # Test 'story_imaginative' prompt type
        imaginative_story_prompt = get_creative_content_prompt(topic, content_type="story", prompt_type="imaginative")
        self.assertIn("Craft an imaginative and engaging short story", imaginative_story_prompt)
        self.assertIn(f"centered around the theme of: {topic}", imaginative_story_prompt)

        # Test 'story_structured' prompt type
        structured_story_prompt = get_creative_content_prompt(topic, content_type="story", prompt_type="structured")
        self.assertIn(f"Write a story about '{topic}' with a clear beginning", structured_story_prompt)

    def test_get_creative_content_prompt_poem(self):
        """
        Tests various prompt types for creative content generation (poem).
        """
        topic = "the sea"

        # Test 'poem_standard' prompt type
        standard_poem_prompt = get_creative_content_prompt(topic, content_type="poem", prompt_type="standard")
        self.assertIn(f"Write a poem about: {topic}", standard_poem_prompt)

        # Test 'poem_imaginative' prompt type
        imaginative_poem_prompt = get_creative_content_prompt(topic, content_type="poem", prompt_type="imaginative")
        self.assertIn("Compose an evocative and artistic poem", imaginative_poem_prompt)
        self.assertIn(f"captures the essence of: {topic}", imaginative_poem_prompt)

        # Test 'poem_structured' prompt type
        structured_poem_prompt = get_creative_content_prompt(topic, content_type="poem", prompt_type="structured")
        self.assertIn(f"Write a four-stanza poem about '{topic}' with an AABB rhyme scheme.", structured_poem_prompt)

    def test_get_creative_content_prompt_essay_idea(self):
        """
        Tests various prompt types for creative content generation (essay idea).
        """
        topic = "climate change"

        # Test 'essay_idea_standard' prompt type
        standard_essay_prompt = get_creative_content_prompt(topic, content_type="essay_idea", prompt_type="standard")
        self.assertIn(f"Generate an idea for an essay on the topic: {topic}", standard_essay_prompt)

        # Test 'essay_idea_imaginative' prompt type
        imaginative_essay_prompt = get_creative_content_prompt(topic, content_type="essay_idea", prompt_type="imaginative")
        self.assertIn("Brainstorm a unique and thought-provoking essay topic related to:", imaginative_essay_prompt)
        self.assertIn(f"{topic}", imaginative_essay_prompt)

        # Test 'essay_idea_structured' prompt type
        structured_essay_prompt = get_creative_content_prompt(topic, content_type="essay_idea", prompt_type="structured")
        self.assertIn(f"Suggest three distinct essay ideas for the topic '{topic}'", structured_essay_prompt)

    def test_get_creative_content_prompt_default(self):
        """
        Tests the default behavior for creative content prompt.
        """
        topic = "anything"
        default_creative_prompt = get_creative_content_prompt(topic)
        self.assertIn(f"Write a short story about: {topic}", default_creative_prompt)


if __name__ == '__main__':
    unittest.main()
