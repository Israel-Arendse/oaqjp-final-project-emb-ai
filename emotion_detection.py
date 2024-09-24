# import the request library to handle HTTP requirements
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
    # Return the response text from the API
    return response.text

