import streamlit as st
import asyncio
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, Runner
from dotenv import load_dotenv
import os

load_dotenv()

# Load model & agent setup
MODEL_NAME = "gemini-2.0-flash"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
external_client = AsyncOpenAI(api_key=GEMINI_API_KEY, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
model = OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=external_client)
config = RunConfig(model=model, model_provider=external_client, tracing_disabled=True)

# Import your agents setup
from main import manager_agent

# Language list for dropdown
language_list = [
    "Spanish", "French", "Sindhi", "German", "Arabic", "Chinese", "Japanese", "Urdu", "Hindi", "Russian",
    "Turkish", "Korean", "Italian", "Portuguese", "Bengali", "Punjabi", "Persian", "Pashto", "Gujarati", "Tamil",
    "Telugu", "Malay", "Swahili", "Greek", "Thai", "Romanian", "Hebrew", "Indonesian", "Hungarian", "Polish", "Dutch",
    "Czech", "Ukrainian", "Filipino", "Nepali", "Burmese", "Lao", "Amharic", "Somali", "Zulu", "Kurdish",
    "Azerbaijani", "Kazakh", "UK English", "Swedish", "Norwegian", "Finnish", "Mongolian", "Slovak", "Serbian"
]

# Streamlit UI setup
st.set_page_config(page_title="Multi-Language Translator", page_icon="🌍", layout="centered")
# st.title("🌐 Multi-Language Translator (50 lang included)")
st.title("🌐 50-Language Translator")
st.write("This app translates text into various languages using AI agents.")
st.markdown("Translate English, Roman Urdu, or Hindi into any supported language.")

with st.form("translate_form"):
    input_text = st.text_area("✍️ Enter text to translate", height=150)
    selected_language = st.selectbox("🌎 Select target language", language_list)
    submitted = st.form_submit_button("Translate")

if submitted:
    if not input_text.strip():
        st.error("Please enter text to translate.")
    else:
        prompt = f"Translate this to {selected_language.lower()}: {input_text}"

        with st.spinner("Translating..."):
            try:
                result = asyncio.run(Runner.run(manager_agent, prompt, run_config=config))
                st.success("✅ Translation Complete")
                st.text_area("📝 Translated Text", result.final_output, height=150)
                st.markdown(f"🤖 Translated by: **{result.last_agent.name.replace('_', ' ').title()}**")
            except Exception as e:
                st.error(f"❌ Error: {e}")