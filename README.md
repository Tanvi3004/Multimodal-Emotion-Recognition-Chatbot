# Multimodal-Emotion-Recognition-Chatbot
A real-time emotion-aware chatbot that analyzes **text sentiment**, **facial expressions**, and **voice tone** (future scope) to deliver personalized responses. Built with **Flask**, **HuggingFace Transformers**, and **DeepFace**.

## Introduction
The rapid advancement in machine learning and artificial intelligence has paved the way for innovative applications that enhance interactive experiences. Among these innovations, the integration of multi-modal systems into chatbot technology has become increasingly prominent. This report details the development of a multi-modal chatbot application that utilizes both text and video inputs to analyze user emotions and generate responsive dialogues. The chatbot is designed to engage users by processing their textual inputs and facial expressions to understand underlying sentiments and emotions more accurately.

The primary objective of this project is to create a chatbot that can interact more intuitively with users by understanding and responding to their emotional states. This involves the analysis of text for sentiment and emotion and video for facial emotion recognition. By combining these modalities, the chatbot aims to deliver a more personalized and contextually relevant user experience.

The scope of this report includes a detailed review of the system architecture, technologies used, implementation details, and the functionalities of the multi-modal chatbot. It also addresses the challenges faced during development, testing methodologies, potential future enhancements, and the overall impact of the project.

## System Architecture
The system architecture of the multi-modal chatbot is designed to efficiently handle both text and video inputs to deliver a cohesive user experience. Below is a high-level overview of the architecture, followed by descriptions of the major components:







## Project Flow
### 1. Data Collection & Input Processing
- **Text Input:** User types a message in the chatbot.
- **Video Input:** Webcam captures facial expressions in real time.
- **(Future)** Voice input for speech emotion detection.
  
### 2. Emotion Analysis & Feature Extraction
- Text Analysis
 - Uses distilroberta-base model to detect sentiment and emotions.
 - Extracts named entities for contextual understanding (via spaCy). 

- Facial Emotion Detection
 - Captures a frame from the webcam and processes it using DeepFace.
 - Detects emotions: happy, sad, angry, neutral, etc.
  
      
### 3. Response Generation
- Uses GPT-3.5-turbo API to generate a chatbot response.
- Context-aware reply considers both text and facial emotions.
- Example:
  - User appears [happy] facially but text sounds [anxious]. Respond supportively about their exam stress.

### 4.Output Rendering
- Displays chatbot reply, text emotion scores, and detected facial emotions
  
## Technical Explanation
### 1. Text Emotion Pipeline
**Code:** analyze_text() in app.py
  - Uses Hugging Face Transformers (distilroberta-base model) for text sentiment analysis.
  - Named entity recognition (NER) via spaCy (spacy extracts entities (people, places) for contextual understanding)
Example Output:
```bash
{
  "text": "I'm excited about graduation!",
  "emotions": {"joy": 0.92, "surprise": 0.05},
  "entities": ["graduation"]
}
```
### 2. Facial Emotion Detection
**Code:** analyze_video() in app.py
- Process Flow:
  - Webcam → Canvas frame capture (app.js)
  - Base64 → OpenCV image conversion
  - DeepFace's CNN analyzes 7 emotions (angry, disgust, fear, happy, sad, surprise, neutral)
- Key Parameter: enforce_detection=False allows partial face detection

### 3. Response Generation
**Code:** generate_chatbot_response()
- Combines text + face analysis
- GPT-3.5-turbo generates context-aware replies
**Prompt Engineering Example:**
```bash
"User appears [happy] facially but text sounds [anxious]. 
Respond supportively about their exam stress."
```

## Installation Guide
**Prerequisites**
- Webcam-enabled device
- Python 3.9+
- Chrome/Firefox (for media devices API)

**Step-by-Step Setup:**
**Clone repository**
```bash
git clone https://github.com/Tanvi3004/Multimodal-Emotion-Recognition-Chatbot.git
cd Multimodal-Emotion-Recognition-Chatbot
```
**Create virtual environment (Windows)**
```bash
python -m venv venv
venv\Scripts\activate
```
**Install exact dependencies**
```bash
pip install -r requirements.txt  
```
**Download language model**
```bash
python -m spacy download en_core_web_sm
```
**Set Up OpenAI API Key**
 - Get an API Key from OpenAI.
 - Add it in app.py:
```bash
api_key = "your_openai_api_key_here"
```
**Run the Flask App**
```bash
python app.py
```
**Open in Browser**
```bash
Visit: http://127.0.0.1:5001
```

## Future Enhancements
### 1. Voice Emotion Integration
```bash
# Proposed Implementation
import librosa
from sklearn.svm import SVC  # For emotion classification

def analyze_voice(audio_clip):
    mfcc = librosa.feature.mfcc(y=audio, sr=sample_rate)
    emotion = voice_model.predict(mfcc)  # Trained model
    return {"voice_emotion": emotion}
```
### 2. Multimodal Fusion
Approach	        : Description

Early Fusion      : Combine text+face+voice raw features

Late Fusion       : Weighted average of emotion scores

Transformer-based : Use Multimodal BERT for joint analysis

### 3. Deployment Roadmap
1. Dockerize application
2. AWS EC2 deployment
3. Mobile app (Flutter) with real-time processing

### 4. Project Metrics
**Performance Benchmarks**

Model: Text Emotion	 Accuracy: 78%	Latency: 120ms

Model: Facial Recognition	Accuracy: 65%	Latency: 300ms

- Tested on 500 samples from MELD dataset

## Limitations
**Cultural Bias:** Models trained primarily on Western expressions

**Lighting Sensitivity:** Face detection fails in low light

## Usage Demo
1. Run python app.py
2. Open http://localhost:5001
3. Demo Flow:
 - Type: "I'm nervous about my presentation tomorrow"
 - Show happy facial expression
 - System detects contradiction → responds empathetically

**Context Understanding:** GPT-3.5 sometimes generates generic responses

## Contributors & Contact
- **Tanvi3004** (GitHub)
- For queries, email: tanvipatel3004@gmail.com
