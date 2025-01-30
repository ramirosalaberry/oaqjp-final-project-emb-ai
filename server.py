''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detection():
    ''' This code receives the text from the HTML interface and 
    runs sentiment analysis over it using sentiment_analysis()
    function. The output returned shows the label and its confidence 
    score for the provided text.
'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid input! Try again."
    return (
    f'For the given statement, the system response is "anger": {response["anger"]} , '
    f'"disgust": {response["disgust"]} , "fear": {response["fear"]} , '
    f'"joy": {response["joy"]} , "sadness": {response["sadness"]} , '
    f'"dominant_emotion": {response["dominant_emotion"]}.'
)

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
