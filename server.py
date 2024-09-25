'''Executing this function initiates the application of Emotion
   detection to be executed over the Flask channel and deployed
   on localhost:5000.
'''

# Import Flask, render_template, request
from flask import Flask, render_template, request

# Import the emotion_detector function from the EmotionDetection package
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask("Emotion_Detection")



# Renders index page
@app.route("/")
def render_index_page()
    '''This function renders the index_page of the main app
         over the flask Channel
    '''
    return render_template("index.html")

# Runs the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)