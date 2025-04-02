document.addEventListener("DOMContentLoaded", () => {
  const userInput = document.getElementById("user-input");
  const sendButton = document.getElementById("send-button");
  const videoPreview = document.getElementById("video-preview");
  const videoCanvas = document.getElementById("video-canvas");
  const emotionScores = document.getElementById("emotion-scores");

  let stream;

  startVideoPreview();

  sendButton.addEventListener("click", async () => {
    const text = userInput.value.trim();
    if (text !== "") {
      displayUserMessage(text);
      userInput.value = "";

      const videoFrame = captureVideoFrame();
      const response = await generateChatbotResponse(text, videoFrame);
      displayResults(response);
      displayEmotionScores(response);
    }
  });

  userInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
      sendButton.click();
    }
  });

  async function startVideoPreview() {
    try {
      stream = await navigator.mediaDevices.getUserMedia({ video: true });
      videoPreview.srcObject = stream;
    } catch (err) {
      console.error("Failed to start video preview:", err);
    }
  }

  function captureVideoFrame() {
    videoCanvas.width = videoPreview.videoWidth;
    videoCanvas.height = videoPreview.videoHeight;

    const context = videoCanvas.getContext("2d");
    context.drawImage(
      videoPreview,
      0,
      0,
      videoCanvas.width,
      videoCanvas.height,
    );

    const imageDataUrl = videoCanvas.toDataURL("image/jpeg");
    const base64Image = imageDataUrl.split(",")[1];
    return base64Image;
  }

  async function generateChatbotResponse(text, videoFrame) {
    const response = await fetch("http://127.0.0.1:5001/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        text: text,
        image: videoFrame,
      }),
    });

    const data = await response.json();
    return {
      chatbot_response: data.chatbot_response,
      text_emotions: data.text_emotions,
      video_emotions: data.video_emotions,
    };
  }

  function displayUserMessage(text) {
    const chatMessages = document.getElementById("chat-messages");
    const userMessage = document.createElement("div");
    userMessage.classList.add("user-message");
    userMessage.textContent = text;
    chatMessages.appendChild(userMessage);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  function displayResults(response) {
    const chatMessages = document.getElementById("chat-messages");
    const botMessage = document.createElement("div");
    botMessage.classList.add("bot-message");
    botMessage.textContent = response.chatbot_response;
    chatMessages.appendChild(botMessage);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  function displayEmotionScores(response) {
    const textEmotions = response.text_emotions;
    const videoEmotions = response.video_emotions;

    let emotionScoresText = "Top Text Emotion: ";
    if (textEmotions) {
      const topTextEmotion = getTopEmotion(textEmotions);
      emotionScoresText += `${topTextEmotion.emotion} (${topTextEmotion.score.toFixed(2)})`;
    } else {
      emotionScoresText += "N/A";
    }

    emotionScoresText += " | Top Video Emotion: ";
    if (videoEmotions) {
      emotionScoresText += `${videoEmotions.dominant_emotion}`;
    } else {
      emotionScoresText += "N/A";
    }

    emotionScores.textContent = emotionScoresText;
  }

  function getTopEmotion(emotions) {
    let topEmotion = "";
    let topScore = 0;
    for (const emotion in emotions) {
      if (emotions[emotion] > topScore) {
        topEmotion = emotion;
        topScore = emotions[emotion];
      }
    }
    return { emotion: topEmotion, score: topScore };
  }
});
