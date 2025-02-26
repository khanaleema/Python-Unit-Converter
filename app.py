import streamlit as st
import pandas as pd
from converter import convert_units
from utils import get_supported_units, save_history, load_history, download_history, voice_input

st.set_page_config(page_title="Advanced Unit Converter", layout="wide")

# Load history
history = load_history()

st.title("🔄 Advanced Unit Converter with Extra Features")

# Sidebar
st.sidebar.header("⚙️ Settings")
theme = st.sidebar.radio("Select Theme", ["Light", "Dark"])
st.markdown(
    """
    <style>
    body {background-color: #f0f2f6;}
    """ if theme == "Light" else """
    <style>
    body {background-color: #0e1117; color: white;}
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown("## 🎙️ Voice Input")
if st.sidebar.button("Use Microphone"):
    value = voice_input()
    st.sidebar.success(f"Recognized Value: {value}")
else:
    value = st.sidebar.number_input("Enter Value", min_value=0.0, step=1.0)

category = st.selectbox("Select Category", ["Length", "Weight", "Temperature", "Speed"])
units = get_supported_units(category)
from_unit = st.selectbox("From Unit", units)
to_unit = st.selectbox("To Unit", units)

if st.button("Convert"):
    result = convert_units(category, from_unit, to_unit, value)
    st.success(f"{value} {from_unit} = {result} {to_unit}")
    save_history(value, from_unit, to_unit, result)
    history = load_history()

# Show History
st.subheader("📜 Conversion History")
history_df = pd.DataFrame(history, columns=["Value", "From", "To", "Result"])
st.table(history_df)

st.download_button("⬇️ Download History as CSV", download_history(history_df), file_name="history.csv", mime="text/csv")
