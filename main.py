from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
from intent_recognition.classification_api import IntentClassification
from offers.chatbot_api import Chatbot

print("App Started")
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
api = Api(app)

intent: IntentClassification = IntentClassification()
offers: Chatbot = Chatbot()

@app.route("/nlp/demo", methods=['POST'])
def nlp_demo():
    text = request.args.get('text', None)
    result = decide_and_return(text)
    return result

def decide_and_return(text: str):
    category = intent.predict(text)
    if(category == 1 or category == 2 or category == 3):
        return offers.chat(text)
    else:
        return "smalltalk"

app.run(host= '0.0.0.0', port=5000, debug=True)