"""
This module contains various prompt designs for the AI Assistant's different functionalities.
Each function provides multiple prompt variations to guide the AI's response.
"""

def get_question_answering_prompt(query, prompt_type="general"):
    """
    Returns a prompt for answering factual questions.
    :param query: The question asked by the user.
    :param prompt_type: Specifies the type of prompt (general, detailed, concise).
    """
    if prompt_type == "general":
        return f"Answer the following question clearly and concisely: {query}"
    elif prompt_type == "detailed":
        return f"Provide a comprehensive answer to the following question, including relevant context and details: {query}"
    elif prompt_type == "concise":
        return f"Give a brief, direct answer to: {query}"
    else:
        return f"Answer the question: {query}"

def get_summarization_prompt(text, prompt_type="standard"):
    """
    Returns a prompt for summarizing text.
    :param text: The text to be summarized.
    :param prompt_type: Specifies the type of summary (standard, key_points, very_short).
    """
    if prompt_type == "standard":
        return f"Summarize the following text, capturing its main ideas and important details:\n\n{text}"
    elif prompt_type == "key_points":
        return f"Extract the most important key points and main arguments from the following text in bullet points:\n\n{text}"
    elif prompt_type == "very_short":
        return f"Provide a very brief, one-paragraph summary of the following text:\n\n{text}"
    else:
        return f"Summarize this text: {text}"

def get_creative_content_prompt(topic, content_type="story", prompt_type="standard"):
    """
    Returns a prompt for generating creative content.
    :param topic: The topic or theme for the creative content.
    :param content_type: The type of content to generate (story, poem, essay_idea).
    :param prompt_type: Specifies the style/length (standard, imaginative, structured).
    """
    if content_type == "story":
        if prompt_type == "standard":
            return f"Write a short story about: {topic}"
        elif prompt_type == "imaginative":
            return f"Craft an imaginative and engaging short story, full of vivid descriptions, centered around the theme of: {topic}"
        elif prompt_type == "structured":
            return f"Write a story about '{topic}' with a clear beginning, rising action, climax, falling action, and resolution. Aim for about 3-4 paragraphs."
    elif content_type == "poem":
        if prompt_type == "standard":
            return f"Write a poem about: {topic}"
        elif prompt_type == "imaginative":
            return f"Compose an evocative and artistic poem that captures the essence of: {topic}. Use metaphors and imagery."
        elif prompt_type == "structured":
            return f"Write a four-stanza poem about '{topic}' with an AABB rhyme scheme."
    elif content_type == "essay_idea":
        if prompt_type == "standard":
            return f"Generate an idea for an essay on the topic: {topic}"
        elif prompt_type == "imaginative":
            return f"Brainstorm a unique and thought-provoking essay topic related to: {topic}, including a potential thesis statement."
        elif prompt_type == "structured":
            return f"Suggest three distinct essay ideas for the topic '{topic}', each with a brief outline of key arguments."
    return f"Generate creative content based on: {topic}"

