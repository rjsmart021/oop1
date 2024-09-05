def mood_response(mood):
    responses = {
        'happy': "you're feeling happy today!",
        'sad': "FEEL BETTER SOON.",
        'okay': "okay? BETTER ANSWERS ARE OUT THERE.",
        'excited': "That's great! What are you excited about?",
        'angry': "Relax.",
        'energetic': "Sounds like you have a lot of energy today!",
        'tired': "Take it easy and get some rest if you're feeling tired.",
    }
    return responses.get(mood.lower(), "I'm not sure how to respond to that.")
