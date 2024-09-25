
# Import the JSON library
import json 

# import the request library to handle HTTP requests
import requests 

# Define the function 'emotion_detector' to take the string input (text_to_analyse)
def emotion_detector(text_to_analyze):
    #  Define the URL for the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Set the headers required for the API request.
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Create the dictionary 'textobj' with the text to be analyzed under the variable 'text'
    textobj = { "raw_document": { "text": text_to_analyze} }
    # Send a POST request to the API with the text and headers
    response = requests.post(url, headers=header, json = textobj)

    # Parse the JSON response
    formatted_response = json.loads(response.text)
    print(formatted_response) # Print the entire response
    
    # Extract the emotions from the dictionary
    anger_score = document_emotion.get('anger', 0)
    disgust_score = document_emotion.get('disgust', 0)
    fear_score = document_emotion.get('fear', 0)
    joy_score = document_emotion.get('joy', 0)
    sadness_score = document_emotion.get('sadness', 0)

    # Determine the dominant emotion
    # by returning the highest value
    emotions = {
        'anger': anger_score,
        'disgust': digust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotions, key=emotions.get)

    # Return the response text from the API
    return {
        'anger': anger_score, 
        'disgust': disgust_score,
        'fear': fear_score,
        'sadness': sadness_score,
        'dominant_emotion_': dominant_emotion
    }
    
