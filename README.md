# Moroccan Rug Assistant (Streamlit + OpenAI)

A conversational assistant built with Streamlit and OpenAI's GPT API to help users choose Moroccan rugs based on their preferences (type, size, color). The assistant replies in a helpful and friendly tone and is fully based on a local JSON catalog.

---

## ✨ Features

- Friendly chatbot UI (built with Streamlit)
- Intelligent suggestions based on user's needs
- Uses a static catalog (`rugs.json`) for product matching
- Responds politely to unrelated or off-topic requests
- Lightweight and self-contained

---

## 📚 How It Works

The assistant uses a predefined catalog stored in `rugs.json`, containing rug type, size, color, price, and shape.
It does **not** fetch or generate data beyond what's available in that file.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (for UI and interaction)
- **OpenAI API** (for GPT chat)
- **python-dotenv** (for secure API key management)

---

## 🚀 Run the App Locally

1. Clone the repo
   ```bash
   git clone https://github.com/your-username/rug-assistant.git
   cd rug-assistant
