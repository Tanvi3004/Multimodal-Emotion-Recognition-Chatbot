from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import spacy
from transformers import pipeline
import base64
import numpy as np
import requests
import json
from deepface import DeepFace
import cv2

# Initialize the Flask application
app = Flask(__name__)
CORS(app)

# Load pre-trained models and pipelines
try:
    sentiment_analyzer = pipeline("sentiment-analysis")
    emotion_detector = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)
    nlp = spacy.load("en_core_web_sm")
except Exception as e:
    print("Error loading pre-trained models:", str(e))
    raise

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        print("Request data:", request.json)
        text_result = None
        video_result = None

        if 'text' in request.json:
            text = request.json['text']
            text_result = analyze_text(text)

        if 'image' in request.json:
            image_data = request.json['image']
            video_result = analyze_video(image_data)

        chatbot_response = generate_chatbot_response(text_result, video_result)

        response = {
            'chatbot_response': chatbot_response,
            'text_emotions': text_result["emotions"] if text_result else None,
            'video_emotions': video_result
        }

        return jsonify(response)
    except Exception as e:
        print("Error occurred during analysis:", str(e))
        return jsonify({'error': str(e)}), 500

def analyze_text(text):
    try:
        sentiment_result = sentiment_analyzer(text)[0]
        emotion_result = emotion_detector(text)[0]
        emotions = {emotion["label"]: emotion["score"] for emotion in emotion_result}

        doc = nlp(text)
        pos_tags = [token.pos_ for token in doc]
        named_entities = [ent.text for ent in doc.ents]

        print("Sentiment Result:", sentiment_result)
        print("Emotion Result:", emotion_result)
        print("POS Tags:", pos_tags)
        print("Named Entities:", named_entities)

        return {
            "text": text,
            "sentiment": {
                "label": sentiment_result["label"],
                "score": sentiment_result["score"]
            },
            "emotions": emotions,
            "pos_tags": pos_tags,
            "named_entities": named_entities
        }
    except Exception as e:
        print("Error occurred during text analysis:", str(e))
        raise

def analyze_video(image_data):
    # Convert the base64-encoded image data to a NumPy array
    image_data = base64.b64decode(image_data)
    image_np = np.frombuffer(image_data, np.uint8)
    image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

    # Perform facial emotion analysis using DeepFace
    try:
        emotions = DeepFace.analyze(image, actions=['emotion'], enforce_detection=False)
        dominant_emotion = emotions[0]['dominant_emotion']
        emotion_scores = emotions[0]['emotion']

        # Normalize the emotion scores to a range between 0 and 1
        total_score = sum(emotion_scores.values())
        normalized_scores = {emotion: score / total_score for emotion, score in emotion_scores.items()}

        return {
            'dominant_emotion': dominant_emotion,
            'emotion_scores': normalized_scores
        }

    except ValueError as e:
        print(f"No face detected in the image. Error: {str(e)}")
        return None

def generate_chatbot_response(text_result, video_result):
    try:
        api_endpoint = "https://api.openai.com/v1/chat/completions"
        api_key = "yourkey"

        prompt = "Based on the sentiment and emotion analysis results, provide an appropriate response as if you were engaging in a human-like conversation:\n\n"

        if text_result:
            text_sentiment = text_result["sentiment"]
            prompt += f"Text: {text_result['text']}\n"
            prompt += f"Text sentiment: {text_sentiment['label']} (score: {text_sentiment['score']:.2f})\n"
            dominant_text_emotion = max(text_result["emotions"], key=text_result["emotions"].get)
            prompt += f"Dominant text emotion: {dominant_text_emotion}\n"

        if video_result:
            dominant_video_emotion = video_result['dominant_emotion']
            prompt += f"Dominant video emotion: {dominant_video_emotion}\n"

        prompt += "Respond in a way that acknowledges the sentiment and emotions detected in the text and video, and engage in a conversational manner.\n"

        print("Prompt:", prompt)

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(api_endpoint, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            response_data = response.json()
            chatbot_response = response_data["choices"][0]["message"]["content"]
            print("Chatbot Response:", chatbot_response)
            return chatbot_response
        else:
            print("Error occurred during API request:", response.status_code, response.text)
            raise Exception("Failed to generate chatbot response")
    except Exception as e:
        print("Error occurred during chatbot response generation:", str(e))
        raise

if __name__ == '__main__':
    app.run(debug=True, port=5001)
