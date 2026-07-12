# 🎓 AI-Voice-Tutor

An AI-powered voice assistant that acts as a virtual teacher. The application listens to a user's spoken question, converts it into text using Speech Recognition, sends it to the Mistral Large Language Model through LangChain, and speaks the generated answer back to the user.

---

## 🚀 Features

* 🎤 Voice-based question input
* 📝 Speech-to-Text using Google Speech Recognition
* 🤖 AI-generated answers using Mistral AI
* 🔗 LangChain prompt management
* 🔊 Text-to-Speech response using Pyttsx3
* 🌐 Simple Streamlit web interface
* ⚡ Fast and interactive learning experience

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Mistral AI
* SpeechRecognition
* Pyttsx3
* Python Dotenv

---

## 📂 Project Structure

```text
AI-Audio-Teacher/
│
├── app.py                
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables
├── run.py                 # Streamlit application
                
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Akshaykompally/AI-Voice-Tutor.git
cd AI-Voice-Tutor
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
MISTRAL_API_KEY=your_mistral_api_key
```

Get your API key from the Mistral AI developer portal.

---

## ▶️ Run the Application

```bash
streamlit run run.py
```

The application will open automatically in your browser.

---

## 🖥️ How It Works

1. Click the **Ask Question** button.
2. Speak your question into the microphone.
3. The application converts your speech into text.
4. The text is sent to the Mistral AI model.
5. The AI generates a concise educational answer.
6. The answer is displayed on the screen.
7. The answer is also spoken aloud using Text-to-Speech.

---

## 📚 Dependencies

* langchain
* langchain-community
* langchain-mistralai
* streamlit
* SpeechRecognition
* python-dotenv
* pyttsx3
* pyaudio
* sounddevice
* soundfile
* requests
* tiktoken
* chromadb
* faiss-cpu
* sentence-transformers
* faster-whisper
* piper-tts
* fastapi
* uvicorn
* pydantic

---


## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Akshay Kompally**

GitHub: https://github.com/Akshaykompally

---

⭐ If you found this project useful, consider giving it a star on GitHub!
