import speech_recognition as sr
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
import pyttsx3

load_dotenv()

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Please say something...")
    recognizer.adjust_for_ambient_noise(source, duration=1)  # Reduce background noise
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, I could not understand your speech.")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition:", e)



prompt = ChatPromptTemplate.from_messages([

    ("system",
    """
        You are an AI Teacher.

        The user will provide speech converted to text.

        Answer the user's question clearly and accurately.
        Keep the answer short and easy to understand.
    """
    ),
    ("human",
      """
        Audio_Text:

        "{text}"

        """
    )

])


gen = prompt.format_messages(
        text=text)
model = ChatMistralAI(model="mistral-small-2506")


result = model.invoke(gen)

engine = pyttsx3.init()
print(result.content)
engine.say(result.content)

engine.runAndWait()



