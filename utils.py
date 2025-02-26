import json
import speech_recognition as sr
import streamlit as st
import pandas as pd

def get_supported_units(category):
    if category == "Length":
        return ["Meter", "Kilometer", "Centimeter", "Mile"]
    elif category == "Weight":
        return ["Kilogram", "Gram", "Pound", "Ounce"]
    elif category == "Temperature":
        return ["Celsius", "Fahrenheit"]
    elif category == "Speed":
        return ["m/s", "km/h", "mph"]

def save_history(value, from_unit, to_unit, result):
    history = load_history()
    history.append([value, from_unit, to_unit, result])
    with open("history.json", "w") as f:
        json.dump(history, f)

def load_history():
    try:
        with open("history.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def download_history(df):
    return df.to_csv(index=False).encode("utf-8")

def voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Speak the value now!")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return float(text)
    except:
        st.error("Couldn't recognize the input. Please try again.")
        return 0.0
