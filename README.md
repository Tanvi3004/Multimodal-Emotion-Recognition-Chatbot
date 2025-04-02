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
![Image](https://github.com/user-attachments/assets/2294f8d1-b4c7-481f-a1c0-6f7bdcad9c68)

- **Chat Interface:** This screenshot should show a typical interaction with several exchanged messages between the user and the chatbot.
- **Video Display:** This should capture the video interface during an active session, highlighting the facial emotion recognition feature.

## Explanation of User Interactions and Flow
Users interact with the chatbot by typing their message into a text box. They can submit their message by clicking a 'Send' button or pressing 'Enter.' As they communicate, the system simultaneously captures video to analyze facial expressions. The backend processes both text and video inputs for emotional and sentiment analysis, then the chatbot crafts a response based on this multi-modal data. The conversation appears in real-time within the chat interface, providing an engaging and interactive user experience.

## Challenges Faced
**Technical Challenges and Their Solutions**
- **Multi-Modal Data Handling:** Initially, synchronizing text and video data processing was challenging due to their differing data handling needs. Solution: Implemented a queue system to manage data processing in a synchronized manner, ensuring that both text and video analyses are completed before generating responses.
**Performance Issues and Optimizations**
- **Response Time:** Early versions of the chatbot experienced slow response times due to the heavy processing requirements of video data. Solution: Optimized video processing algorithms and introduced lower resolution processing for faster analysis without significant loss of accuracy.
**Handling Asynchronous Tasks in JavaScript**
- **RAsynchronous API Calls:** The frontend needed to manage simultaneous API calls for sending text and video data efficiently. Solution: Utilized JavaScript's async and await features along with Promise objects to handle these operations smoothly, improving UI responsiveness and preventing freeze-ups during data transmission.

## Testing and Validation
- **Unit Testing:** Each module, from sentiment analysis to facial recognition, was tested independently to ensure it functions correctly in isolation.
- **Integration Testing:** After unit testing, modules were integrated step by step, with tests conducted at each step to verify that the modules interact correctly.
- **User Acceptance Testing (UAT):** Conducted with potential end-users to ensure the system met their needs and was intuitive to use.

## Test Cases and Results
- **Sentiment Analysis:** Tested with a diverse set of input texts to cover various emotional tones and contexts. The system demonstrated high accuracy in classifying sentiments as positive, negative, or neutral.
- **Facial Emotion Recognition:** Evaluated using standard datasets like the Facial Expression Recognition 2013 (FER-2013) dataset. Adjustments were made to improve accuracy based on these results.

## Validation of Sentiment and Emotion Analysis Accuracy
The accuracy of sentiment and emotion analysis was validated through:
- **Continuous Learning:** The system is periodically retrained on updated datasets to adapt to new linguistic usages and facial expression trends.
- **Feedback Loops:** User feedback is solicited and analyzed to refine the models continually, ensuring that the system evolves based on actual user interactions and preferences.

## Future Enhancements
Potential Improvements and New Features
- **Personalization Features:** Introducing user profiles that allow the chatbot to remember past interactions, thereby personalizing responses and enhancing user engagement.
- **Multilingual Support:** Expanding the chatbot's capabilities to include multiple languages to cater to a global audience, enhancing accessibility and usability.
- **Enhanced Security Measures:** Implementing advanced security protocols to protect sensitive user data, especially in interactions involving personal topics.

## Scalability Options
- **Cloud-Based Deployment:** Migrating to cloud services can offer more robust scalability, allowing the system to adjust resources dynamically based on user demand and reduce operational costs.
- **Microservices Architecture:** Adopting a microservices architecture to improve the modularity of the application, making it easier to scale specific components of the system independently as needed.

## Integration with Additional Modalities
- **Audio Analysis:** Integrating voice tone and speech pattern analysis to complement the existing text and video inputs, offering a more comprehensive understanding of user emotions and intentions.
- **Gesture Recognition:** Incorporating gesture recognition technologies to analyze body language, further enriching the emotional analysis and making the system more intuitive.

## Conclusion
**Summary of Achievements**
The project successfully delivered a multi-modal chatbot that integrates text and video analysis to detect user emotions, significantly enhancing the interactive experience. It demonstrated high accuracy in sentiment and emotion recognition, thanks to the sophisticated integration of AI technologies.

**Impact of the Project on the Target Audience**
The chatbot has proven to be a valuable tool for users seeking interactive, empathetic communication. It has enhanced user experience by providing more accurate, context-aware responses, making digital interactions more engaging and human-like.

**Reflections on the Project**
Developing this chatbot was a challenging yet rewarding endeavor. It offered insights into the practical applications of AI in everyday technology and underscored the importance of emotional intelligence in digital interactions. The project also highlighted the critical role of continuous improvement and adaptation in technology projects to keep pace with user expectations and technological advancements.

### References
Citations of Technologies and Frameworks Used
- Flask: Flask Documentation
- spaCy: spaCy 2.0: Natural Language Understanding with Bloom embeddings, convolutional neural networks and incremental parsing
- Hugging Face Transformers: Hugging Face's Transformers: State-of-the-art Natural Language Processing
- OpenCV: Open Source Computer Vision Library
- DeepFace: DeepFace: Closing the Gap to Human-Level Performance in Face Verification

## Research Papers or Articles Referenced
-  Loper, Edward, and Bird, Steven, "NLTK: The Natural Language Toolkit." Proceedings of the ACL Workshop on Effective Tools and Methodologies for Teaching Natural Language Processing and Computational Linguistics. Vol. 1. 2002.
-  Goodfellow, Ian J., et al. "Challenges in representation learning: A report on three machine learning contests." Neural Networks (2013): 117-124.
