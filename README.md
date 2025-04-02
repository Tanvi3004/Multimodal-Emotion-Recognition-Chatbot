# Multimodal-Emotion-Recognition-Chatbot
A real-time emotion-aware chatbot that analyzes **text sentiment**, **facial expressions**, and **voice tone** (future scope) to deliver personalized responses. Built with **Flask**, **HuggingFace Transformers**, and **DeepFace**.

## Introduction
The rapid advancement in machine learning and artificial intelligence has paved the way for innovative applications that enhance interactive experiences. Among these innovations, the integration of multi-modal systems into chatbot technology has become increasingly prominent. This report details the development of a multi-modal chatbot application that utilizes both text and video inputs to analyze user emotions and generate responsive dialogues. The chatbot is designed to engage users by processing their textual inputs and facial expressions to understand underlying sentiments and emotions more accurately.

The primary objective of this project is to create a chatbot that can interact more intuitively with users by understanding and responding to their emotional states. This involves the analysis of text for sentiment and emotion and video for facial emotion recognition. By combining these modalities, the chatbot aims to deliver a more personalized and contextually relevant user experience.

The scope of this report includes a detailed review of the system architecture, technologies used, implementation details, and the functionalities of the multi-modal chatbot. It also addresses the challenges faced during development, testing methodologies, potential future enhancements, and the overall impact of the project.

## System Architecture
The system architecture of the multi-modal chatbot is designed to efficiently handle both text and video inputs to deliver a cohesive user experience. Below is a high-level overview of the architecture, followed by descriptions of the major components:

![Image](https://github.com/user-attachments/assets/e6fb710c-7952-4202-8a99-949ef5e4be69)

## Description of Major Components
### 1.	Web Interface:
- This component consists of the HTML, CSS, and JavaScript files that create the user interface. Users interact with the chatbot through this interface, which is responsible for capturing text and video data and displaying the chatbot's responses.
### 2. Flask Server Application:
- The Flask server acts as the backbone of the application, managing routes and interactions between the web interface and the processing modules. It handles requests from the web interface, processes them through the analysis modules, and sends responses back to the interface.
### 3. Text and Video Analysis Modules
- **Text Analysis:** Utilizes spaCy for linguistic analysis and Hugging Face's pipeline for sentiment and emotion detection.
- **Video Analysis:** Employs OpenCV for image processing and DeepFace for facial emotion recognition. This module analyzes the video frames captured from the user's webcam to identify emotional states.
### 4. Response Generator: 
- This module uses the ChatGPT API, which takes sentiment inputs from both text and video analyses to generate contextually aware responses. The API crafts responses that are sensitive to the emotional context and enhances the interaction quality.

## Technologies Used
### 1.	Flask Web Framework 
- Flask is a lightweight WSGI web application framework that is widely used to develop web applications. It provides tools, libraries, and technologies that allow building a web application. This project utilizes Flask to handle web server operations, routing, and the integration of other components.
### 2.	spaCy for NLP Tasks 
- spaCy is a powerful and efficient library for natural language processing (NLP) in Python. It is used in this project for linguistic analysis such as tokenization, part-of-speech tagging, and named entity recognition. spaCy's robust processing capabilities help in analyzing the structure and content of the user's text input.
### 3.	ChatGPT API for Chatbot Responses 
- The ChatGPT API is used to generate conversational responses. It integrates sentiment and emotional data derived from the text and video analysis to provide replies that are emotionally intelligent and contextually appropriate.
### 4.	OpenCV and DeepFace for Video and Facial Emotion Analysis 
- OpenCV (Open Source Computer Vision Library) is utilized for image processing and video handling functionalities required to analyze user's facial expressions.
- DeepFace is a deep learning facial recognition and attribute analysis framework, employed here to analyze emotions from video data by recognizing facial expressions.
### 5.	Other Supporting Technologies (JavaScript, HTML5, etc.) 
- The front end uses HTML5 and CSS for structuring and styling the user interface, while JavaScript is used for dynamic content handling, capturing video data, and communicating with the Flask backend.

## Implementation Details
### 1.	Setup and Configuration of the Flask Application 
- The Flask application is configured as the central server handling all requests and responses. It integrates various components and manages data flow between the user interface and processing modules.
### 2.	Integration of spaCy for Linguistic Analysis 
- spaCy is integrated to perform detailed linguistic analysis of user inputs. This includes extracting parts of speech, entities, and other linguistic features which are crucial for understanding the context and enhancing the chatbot's responses.
### 3.	Integration of the ChatGPT API for Response Generation 
- The ChatGPT API is configured to generate responses based on the sentiment and emotional insights gained from both text and video inputs. This approach allows for enhanced interaction by aligning the chatbot’s responses more closely with the user's emotional states.
### 4.	Implementation of Video Processing with OpenCV 
- OpenCV is used for capturing and processing video frames from the user's webcam. It handles the conversion of video data into formats suitable for facial emotion analysis.
### 5.	Facial Emotion Recognition Using DeepFace 
- DeepFace analyzes the processed video frames to identify facial emotions. This includes detecting if a face is present and analyzing various facial expressions to determine emotional states.

## Functionality
### 1. Text Analysis: Sentiment and Emotion Detection
- Text inputs are analyzed for both sentiment and emotion. Sentiment analysis categorizes the input into positive, neutral, or negative sentiments, while emotion detection identifies specific emotional states such as happiness, sadness, anger, etc.
### 2. Video Analysis: Facial Emotion Recognition
- The system processes video input to detect and analyze the user's facial expressions. This helps in understanding the emotional state of the user more comprehensively.
### 3. Combining Results from Text and Video Analysis
- The application integrates results from both text and video analysis to achieve a nuanced understanding of the user's overall emotional state. This integrated analysis helps in tailoring the chatbot's responses more effectively.
### 4. Chatbot Response Generation Based on Combined Analysis
- Based on the combined insights from text and video analyses, the chatbot generates responses that are contextually relevant and emotionally intelligent, enhancing the interaction quality and user experience.

## User Interface
### Description of the User Interface
The user interface of the multi-modal chatbot is streamlined and user-friendly, designed to facilitate easy interaction for users of varying technical abilities. It features a dual-pane layout with a chat interface on one side and a video display area on the other. The chat interface allows users to enter text and view messages, creating a conversation history that scrolls vertically. The video display captures and shows the user's facial expressions in real-time, which are essential for the emotion recognition component of the system.

- Screenshots of the Application in Use









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
