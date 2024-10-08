'''Executing this function initiates the application of Emotion
   detection to be executed over the Flask channel and deployed
   on localhost:5000.
'''

# Import Flask, render_template, request.
from flask import Flask, render_template, request

# Import the emotion_detector function from the EmotionDetection package.
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask("Emotion Detection")

# App route to call the emotion_detector function
# Sends a GET request to the HTML interface to receive the input text.
@app.route("/emotionDetector")
def emotion_detector_path():
    ''' This code receives the text from the HTML interface and
        runs emotion detection over it via emotion_detection()
        function. The output shows the emotions, "anger", "disgust",
        "fear", "joy" and "sadness" along with their respective scores, 
        as well as the "dominant emotion. If there is a blank entry, 
        the message "Invalid input! Try again." is return.
    '''
    # Retrieve the detected emotion from the text in the request argument.
    detect_emotion = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response.
    response = emotion_detector(detect_emotion)

    # Extract the emotional scores and dominant emotion from the response.
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Check if there is dominant_emotion is None.
    if dominant_emotion is None:
        return "Invalid input! Try again."

    # Returns a formatted string with the emotional_scores and dominant emotion.
    return (f"For the given statement, the system response is:\n"
            f"'anger': {anger_score}, 'disgust': {disgust_score}, \n" 
            f"'fear': {fear_score}, 'joy': {joy_score}, 'sadness': {sadness_score}.\n" 
            f"The dominant emotion is {dominant_emotion}.")

# Renders index page
@app.route("/")
def render_index_page(): # Runs the 'render_template' function in the 'index.html' template.
    '''This function renders the index_page of the main app
         over the flask Channel
    '''
    return render_template("index.html")

# Runs the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) # Hosts the app on the port:5000.
