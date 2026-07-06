import streamlit as st
import speech_recognition as sr
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
import pyttsx3

load_dotenv()

st.set_page_config(page_title="AI Teacher", page_icon="🎓")

st.title("🎓 AI Teacher")
st.write("Click the button below and ask your question using your microphone.")

if st.button("🎤 Ask Question"):

    recognizer = sr.Recognizer()

    with st.spinner("Listening..."):
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        st.success("Speech Recognized")
        st.write("**You said:**")
        st.write(text)

    except sr.UnknownValueError:
        st.error("Sorry, I could not understand your speech.")
        st.stop()

    except sr.RequestError as e:
        st.error(f"Could not request results from Google Speech Recognition: {e}")
        st.stop()

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
            You are an AI Teacher.

            The user will provide speech converted to text.

            Answer the user's question clearly and accurately.
            Keep the answer short and easy to understand.
            """
        ),
        (
            "human",
            """
            Audio_Text:

            "{text}"
            """
        )
    ])

    gen = prompt.format_messages(text=text)

    model = ChatMistralAI(model="mistral-small-2506")

    with st.spinner("Generating answer..."):
        result = model.invoke(gen)

    st.subheader("📖 AI Teacher Answer")
    st.write(result.content)

    engine = pyttsx3.init()
    engine.say(result.content)
    engine.runAndWait()