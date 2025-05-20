import streamlit as st
import pandas as pd
import joblib

# --- Page Configuration ---
st.set_page_config(page_title="Music Recommender", layout="centered")

# --- Title and Introduction ---
st.title("🎧 Music Genre Recommender")
st.markdown("""
This app recommends music genres based on your **MBTI personality type** and your preferred **tempo** of music.
Simply enter your preferences and get a suggestion!
""")

# --- Load Model ---
try:
    model = joblib.load("model.pkl")
except:
    st.error("❌ Could not load model. Make sure 'model.pkl' is in the same folder.")

# --- Load Dataset for Optional Visualisation ---
try:
    data = pd.read_excel("music_preferences.xlsx", sheet_name="Form Responses 1")
except:
    st.warning("📂 Could not load dataset. Charts may not work.")

# --- User Inputs ---
st.header("🧠 Your Preferences")
personality = st.selectbox("Select your MBTI personality type:", [
    'ISTJ', 'ISFJ', 'INFJ', 'INTJ',
    'ISTP', 'ISFP', 'INFP', 'INTP',
    'ESTP', 'ESFP', 'ENFP', 'ENTP',
    'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ'
])

tempo = st.radio("What kind of music tempo do you prefer?", ['Slow/Calm', 'Medium', 'Fast/Energetic'])

tempo_map = {'Slow/Calm': 1, 'Medium': 2, 'Fast/Energetic': 3}
tempo_val = tempo_map[tempo]

# --- Prediction ---
if st.button("🎵 Recommend a Genre"):
    input_df = pd.DataFrame([[personality, tempo_val]], columns=["MBTI", "Tempo_Ordinal"])
    
    try:
        prediction = model.predict(input_df)[0]
        st.success(f"✅ Recommended genre: **{prediction}**")
    except Exception as e:
        st.error(f"Prediction failed: {e}")

# --- Optional Data Visualisation ---
if 'data' in locals() and st.checkbox("📊 Show genre popularity chart"):
    genre_counts = data['What genre do you listen to most often?'].value_counts()
    st.bar_chart(genre_counts)

# --- Footer ---
st.markdown("---")
st.caption("Developed by [Your Group Name] for 297.201 Assignment 3 | Massey University")
