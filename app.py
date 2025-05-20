import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

# Title
st.title("🎧 Music Genre Recommender")
st.markdown("Discover music genres based on your **MBTI type** and **tempo preference**.")

# User input
personality = st.selectbox("Select your MBTI type:", ['E', 'I'])
tempo = st.radio("Choose your preferred tempo:", ['Slow/Calm', 'Medium', 'Fast/Energetic'])

# Map tempo to ordinal
tempo_map = {'Slow/Calm': 1, 'Medium': 2, 'Fast/Energetic': 3}
tempo_val = tempo_map[tempo]

# Create input DataFrame
input_dict = {'MBTI_E': 0, 'MBTI_I': 0}
input_dict[f'MBTI_{personality}'] = 1
input_dict['Tempo_Ordinal'] = tempo_val
input_df = pd.DataFrame([input_dict])

# Predict
if st.button("🎵 Recommend Genre"):
    prediction = model.predict(input_df)[0]
    st.success(f"🎶 Your recommended genre label is: **{prediction}**")
    st.caption("Note: To see genre names, decoding with genre_encoder.pkl is needed.")
