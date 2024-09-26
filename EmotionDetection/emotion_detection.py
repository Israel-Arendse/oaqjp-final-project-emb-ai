
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
    
    # Extract the emotions from the nested structure
    if 'emotionPredictions' in formatted_response and len(formatted_response['emotionPredictions']) > 0:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotions.get('anger', 0)
        disgust_score = emotions.get('disgust', 0)
        fear_score = emotions.get('fear', 0)
        joy_score = emotions.get('joy', 0)
        sadness_score = emotions.get('sadness', 0)

        # Determine the dominant emotion
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    else:
        # If the response status code is 400, the values are None
        if response.status_code == 400:
            emotions = None
            emotion_scores = None
        
        # Return the formatted response
        return {
            'anger': anger_score, 
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
      # If there are no emotion predictions in the response.
    else:
        print("No emotion predictions found in the response.")
        return {}
    
