import streamlit as st
from openai import OpenAI
import os
import json
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("rugs.json", "r", encoding="utf-8") as f:
    rugs_data = json.load(f)

def format_rugs_for_prompt(rugs):
    lignes = []
    for r in rugs:
        ligne = f"- Type: {r['type']}, Dimensions: {r['dimensions']}, Color: {r['color']}, Price: {r['price_euros']}€, Shape: {r['shape']}"
        lignes.append(ligne)
    texte = "\n".join(lignes)
    return texte

rugs_text = format_rugs_for_prompt(rugs_data)

system_pres = f"""
You are a friendly and witty assistant for an online store selling Moroccan rugs.
You help customers choose rugs based on their preferences (type, size, color).
Here is the catalog of available rugs in triple backticks: ```{rugs_text}```

Always make suggestions from this list.

If the customer seems unsure, help guide them with gentle, friendly questions.

If the customer asks how you're doing, always answer warmly and return the question.

If they mention something unrelated to Moroccan rugs, acknowledge it kindly with a bit of humor or charm,
and bring the topic back to rugs, but only do this once unless they insist. If it's clearly a joke or said once,
respond naturally and move on.
"""

#start formatting streamlit interface
st.set_page_config(page_title="Moroccan Rug Assistant", layout="centered")
st.title("🧵 BRAND - Moroccan Rug Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_pres}]

user_input = st.chat_input("Ask your question here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("Thinking..."):
        reply = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages,
            temperature=1,
        ).choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})

for msg in st.session_state.messages[1:]:
    avatar = "👤" if msg["role"] == "user" else "🤖"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])