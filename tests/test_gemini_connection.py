from ai.gemini_client import get_gemini_client, get_model_name


def test_connection():
    """
    Test the Gemini API connection.
    """

    client = get_gemini_client()

    response = client.models.generate_content(
        model=get_model_name(),
        contents="Reply with exactly: Gemini connection successful!"
    )

    print("\nGemini Response:\n")
    print(response.text)


if __name__ == "__main__":
    test_connection()