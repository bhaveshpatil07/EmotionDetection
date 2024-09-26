'''Emotion Detector Flask application.'''

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect() -> str:
    '''This code receives the text from the HTML interface and 
    runs sentiment analysis over it using emotion_detection() 
    function. The output returned shows the label and its confidence 
    score for the provided text.'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    response_text = "For the given statement, the system response is "
    for emotion_type, value in response.items():
        if emotion_type in ("anger", "disgust", "fear", "joy", "sadness"):
            response_text += f"{emotion_type}: {value}, "

    response_text += f"The dominant emotion is {response['dominant_emotion']}."

    return response_text

@app.route("/")
def render_index_page() -> str:
    '''This function initiates the rendering of the main application 
    page over the Flask channel'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
