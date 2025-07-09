from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, Runner
from dotenv import load_dotenv
load_dotenv()
import os
import asyncio

# Move all agent definitions here (before async def main())
spanish_agent = Agent(
    name="spanish_agent",
    instructions="You are a helpful Spanish agent who translates English, Roman Urdu and Hindi into Spanish.",
    handoff_description="A helpful Spanish agent that translates English, Roman Urdu and Hindi into Spanish.")

french_agent = Agent(
    name="french_agent",
    instructions="You are a helpful French agent who translates English, Roman Urdu and Hindi into French.",
    handoff_description="A helpful French agent that translates English, Roman Urdu and Hindi into French.")

sindhi_agent = Agent(
    name="sindhi_agent",
    instructions="You are a helpful Sindhi agent who translates English, Roman Urdu and Hindi into Sindhi.",
    handoff_description="A helpful Sindhi agent that translates English, Roman Urdu and Hindi into Sindhi.")

german_agent = Agent(
name="german_agent",
instructions="You are a helpful German agent who translates English, Roman Urdu and Hindi into German.",
handoff_description="A helpful German agent that translates English, Roman Urdu and Hindi into German.")

arabic_agent = Agent(
name="arabic_agent",
instructions="You are a helpful Arabic agent who translates English, Roman Urdu and Hindi into Arabic.",
handoff_description="A helpful Arabic agent that translates English, Roman Urdu and Hindi into Arabic.")

chinese_agent = Agent(
name="chinese_agent",
instructions="You are a helpful Chinese agent who translates English, Roman Urdu and Hindi into Chinese.",
handoff_description="A helpful Chinese agent that translates English, Roman Urdu and Hindi into Chinese."
)

japanese_agent = Agent(
name="japanese_agent",
instructions="You are a helpful Japanese agent who translates English, Roman Urdu and Hindi into Japanese.",
handoff_description="A helpful Japanese agent that translates English, Roman Urdu and Hindi into Japanese."
)

urdu_agent = Agent(
name="urdu_agent",
instructions="You are a helpful Urdu agent who translates English, Roman Urdu and Hindi into Urdu.",
handoff_description="A helpful Urdu agent that translates English, Roman Urdu and Hindi into Urdu."
)

hindi_agent = Agent(
name="hindi_agent",
instructions="You are a helpful Hindi agent who translates English, Roman Urdu and Hindi into Hindi.",
handoff_description="A helpful Hindi agent that translates English, Roman Urdu and Hindi into Hindi."
)

russian_agent = Agent(
name="russian_agent",
instructions="You are a helpful Russian agent who translates English, Roman Urdu and Hindi into Russian.",
handoff_description="A helpful Russian agent that translates English, Roman Urdu and Hindi into Russian."
)

turkish_agent = Agent(
name="turkish_agent",
instructions="You are a helpful Turkish agent who translates English, Roman Urdu and Hindi into Turkish.",
handoff_description="A helpful Turkish agent that translates English, Roman Urdu and Hindi into Turkish."
)

korean_agent = Agent(
name="korean_agent",
instructions="You are a helpful Korean agent who translates English, Roman Urdu and Hindi into Korean.",
handoff_description="A helpful Korean agent that translates English, Roman Urdu and Hindi into Korean."
)

italian_agent = Agent(
name="italian_agent",
instructions="You are a helpful Italian agent who translates English, Roman Urdu and Hindi into Italian.",
handoff_description="A helpful Italian agent that translates English, Roman Urdu and Hindi into Italian."
)

portuguese_agent = Agent(
name="portuguese_agent",
instructions="You are a helpful Portuguese agent who translates English, Roman Urdu and Hindi into Portuguese.",
handoff_description="A helpful Portuguese agent that translates English, Roman Urdu and Hindi into Portuguese."
)

bengali_agent = Agent(
name="bengali_agent",
instructions="You are a helpful Bengali agent who translates English, Roman Urdu and Hindi into Bengali.",
handoff_description="A helpful Bengali agent that translates English, Roman Urdu and Hindi into Bengali."
)

punjabi_agent = Agent(
name="punjabi_agent",
instructions="You are a helpful Punjabi agent who translates English, Roman Urdu and Hindi into Punjabi.",
handoff_description="A helpful Punjabi agent that translates English, Roman Urdu and Hindi into Punjabi."
)

persian_agent = Agent(
name="persian_agent",
instructions="You are a helpful Persian agent who translates English, Roman Urdu and Hindi into Persian.",
handoff_description="A helpful Persian agent that translates English, Roman Urdu and Hindi into Persian."
)

pashto_agent = Agent(
name="pashto_agent",
instructions="You are a helpful Pashto agent who translates English, Roman Urdu and Hindi into Pashto.",
handoff_description="A helpful Pashto agent that translates English, Roman Urdu and Hindi into Pashto."
)

gujarati_agent = Agent(
name="gujarati_agent",
instructions="You are a helpful Gujarati agent who translates English, Roman Urdu and Hindi into Gujarati.",
handoff_description="A helpful Gujarati agent that translates English, Roman Urdu and Hindi into Gujarati."
)

tamil_agent = Agent(
name="tamil_agent",
instructions="You are a helpful Tamil agent who translates English, Roman Urdu and Hindi into Tamil.",
handoff_description="A helpful Tamil agent that translates English, Roman Urdu and Hindi into Tamil."
)

telugu_agent = Agent(
name="telugu_agent",
instructions="You are a helpful Telugu agent who translates English, Roman Urdu and Hindi into Telugu.",
handoff_description="A helpful Telugu agent that translates English, Roman Urdu and Hindi into Telugu."
)

malay_agent = Agent(
name="malay_agent",
instructions="You are a helpful Malay agent who translates English, Roman Urdu and Hindi into Malay.",
handoff_description="A helpful Malay agent that translates English, Roman Urdu and Hindi into Malay."
)

swahili_agent = Agent(
name="swahili_agent",
instructions="You are a helpful Swahili agent who translates English, Roman Urdu and Hindi into Swahili.",
handoff_description="A helpful Swahili agent that translates English, Roman Urdu and Hindi into Swahili."
)

greek_agent = Agent(
name="greek_agent",
instructions="You are a helpful Greek agent who translates English, Roman Urdu and Hindi into Greek.",
handoff_description="A helpful Greek agent that translates English, Roman Urdu and Hindi into Greek."
)

thai_agent = Agent(
name="thai_agent",
instructions="You are a helpful Thai agent who translates English, Roman Urdu and Hindi into Thai.",
handoff_description="A helpful Thai agent that translates English, Roman Urdu and Hindi into Thai."
)

romanian_agent = Agent(
name="romanian_agent",
instructions="You are a helpful Romanian agent who translates English, Roman Urdu and Hindi into Romanian.",
handoff_description="A helpful Romanian agent that translates English, Roman Urdu and Hindi into Romanian."
)

hebrew_agent = Agent(
name="hebrew_agent",
instructions="You are a helpful Hebrew agent who translates English, Roman Urdu and Hindi into Hebrew.",
handoff_description="A helpful Hebrew agent that translates English, Roman Urdu and Hindi into Hebrew."
)

indonesian_agent = Agent(
name="indonesian_agent",
instructions="You are a helpful Indonesian agent who translates English, Roman Urdu and Hindi into Indonesian.",
handoff_description="A helpful Indonesian agent that translates English, Roman Urdu and Hindi into Indonesian."
)

hungarian_agent = Agent(
name="hungarian_agent",
instructions="You are a helpful Hungarian agent who translates English, Roman Urdu and Hindi into Hungarian.",
handoff_description="A helpful Hungarian agent that translates English, Roman Urdu and Hindi into Hungarian."
)

polish_agent = Agent(
name="polish_agent",
instructions="You are a helpful Polish agent who translates English, Roman Urdu and Hindi into Polish.",
handoff_description="A helpful Polish agent that translates English, Roman Urdu and Hindi into Polish."
)

dutch_agent = Agent(
name="dutch_agent",
instructions="You are a helpful Dutch agent who translates English, Roman Urdu and Hindi into Dutch.",
handoff_description="A helpful Dutch agent that translates English, Roman Urdu and Hindi into Dutch."
)

czech_agent = Agent(
name="czech_agent",
instructions="You are a helpful Czech agent who translates English, Roman Urdu and Hindi into Czech.",
handoff_description="A helpful Czech agent that translates English, Roman Urdu and Hindi into Czech."
)

ukrainian_agent = Agent(
name="ukrainian_agent",
instructions="You are a helpful Ukrainian agent who translates English, Roman Urdu and Hindi into Ukrainian.",
handoff_description="A helpful Ukrainian agent that translates English, Roman Urdu and Hindi into Ukrainian."
)

filipino_agent = Agent(
name="filipino_agent",
instructions="You are a helpful Filipino agent who translates English, Roman Urdu and Hindi into Filipino.",
handoff_description="A helpful Filipino agent that translates English, Roman Urdu and Hindi into Filipino."
)

nepali_agent = Agent(
name="nepali_agent",
instructions="You are a helpful Nepali agent who translates English, Roman Urdu and Hindi into Nepali.",
handoff_description="A helpful Nepali agent that translates English, Roman Urdu and Hindi into Nepali."
)

burmese_agent = Agent(
name="burmese_agent",
instructions="You are a helpful Burmese agent who translates English, Roman Urdu and Hindi into Burmese.",
handoff_description="A helpful Burmese agent that translates English, Roman Urdu and Hindi into Burmese."
)

lao_agent = Agent(
name="lao_agent",
instructions="You are a helpful Lao agent who translates English, Roman Urdu and Hindi into Lao.",
handoff_description="A helpful Lao agent that translates English, Roman Urdu and Hindi into Lao."
)

amharic_agent = Agent(
name="amharic_agent",
instructions="You are a helpful Amharic agent who translates English, Roman Urdu and Hindi into Amharic.",
handoff_description="A helpful Amharic agent that translates English, Roman Urdu and Hindi into Amharic."
)

somali_agent = Agent(
name="somali_agent",
instructions="You are a helpful Somali agent who translates English, Roman Urdu and Hindi into Somali.",
handoff_description="A helpful Somali agent that translates English, Roman Urdu and Hindi into Somali."
)

zulu_agent = Agent(
name="zulu_agent",
instructions="You are a helpful Zulu agent who translates English, Roman Urdu and Hindi into Zulu.",
handoff_description="A helpful Zulu agent that translates English, Roman Urdu and Hindi into Zulu."
)

kurdish_agent = Agent(
name="kurdish_agent",
instructions="You are a helpful Kurdish agent who translates English, Roman Urdu and Hindi into Kurdish.",
handoff_description="A helpful Kurdish agent that translates English, Roman Urdu and Hindi into Kurdish."
)

azerbaijani_agent = Agent(
name="azerbaijani_agent",
instructions="You are a helpful Azerbaijani agent who translates English, Roman Urdu and Hindi into Azerbaijani.",
handoff_description="A helpful Azerbaijani agent that translates English, Roman Urdu and Hindi into Azerbaijani."
)

kazakh_agent = Agent(
name="kazakh_agent",
instructions="You are a helpful Kazakh agent who translates English, Roman Urdu and Hindi into Kazakh.",
handoff_description="A helpful Kazakh agent that translates English, Roman Urdu and Hindi into Kazakh."
)

uk_english_agent = Agent(
name="uk_english_agent",
instructions="You are a helpful UK English agent who converts American English, Roman Urdu and Hindi into British English.",
handoff_description="A helpful UK English agent that converts American English, Roman Urdu and Hindi into British English."
)

swedish_agent = Agent(
name="swedish_agent",
instructions="You are a helpful Swedish agent who translates English, Roman Urdu and Hindi into Swedish.",
handoff_description="A helpful Swedish agent that translates English, Roman Urdu and Hindi into Swedish."
)

norwegian_agent = Agent(
name="norwegian_agent",
instructions="You are a helpful Norwegian agent who translates English, Roman Urdu and Hindi into Norwegian.",
handoff_description="A helpful Norwegian agent that translates English, Roman Urdu and Hindi into Norwegian."
)

finnish_agent = Agent(
name="finnish_agent",
instructions="You are a helpful Finnish agent who translates English, Roman Urdu and Hindi into Finnish.",
handoff_description="A helpful Finnish agent that translates English, Roman Urdu and Hindi into Finnish."
)

mongolian_agent = Agent(
name="mongolian_agent",
instructions="You are a helpful Mongolian agent who translates English, Roman Urdu and Hindi into Mongolian.",
handoff_description="A helpful Mongolian agent that translates English, Roman Urdu and Hindi into Mongolian."
)

slovak_agent = Agent(
name="slovak_agent",
instructions="You are a helpful Slovak agent who translates English, Roman Urdu and Hindi into Slovak.",
handoff_description="A helpful Slovak agent that translates English, Roman Urdu and Hindi into Slovak."
)

serbian_agent = Agent(
name="serbian_agent",
instructions="You are a helpful Serbian agent who translates English, Roman Urdu and Hindi into Serbian.",
handoff_description="A helpful Serbian agent that translates English, Roman Urdu and Hindi into Serbian."
)



manager_agent = Agent(
name="manager_agent",
instructions=(
"You are a helpful manager agent. "
"Your task is to route translation requests to the appropriate language agent based on the target language. "
"The input may be in English, broken English, Roman Urdu, or Hindi-style Roman script. "
"Even if the input is in Roman Urdu, broken English, or a mix, still route it properly. "
"Only return the translated sentence in short form unless the user asks for more."
),
handoffs=[
spanish_agent,
french_agent,
sindhi_agent,
german_agent,
arabic_agent,
chinese_agent,
japanese_agent,
urdu_agent,
hindi_agent,
russian_agent,
turkish_agent,
korean_agent,
italian_agent,
portuguese_agent,
bengali_agent,
punjabi_agent,
persian_agent,
pashto_agent,
gujarati_agent,
tamil_agent,
telugu_agent,
malay_agent,
swahili_agent,
greek_agent,
thai_agent,
romanian_agent,
hebrew_agent,
indonesian_agent,
hungarian_agent,
polish_agent,
dutch_agent,
czech_agent,
ukrainian_agent,
filipino_agent,
nepali_agent,
burmese_agent,
lao_agent,
amharic_agent,
somali_agent,
zulu_agent,
kurdish_agent,
azerbaijani_agent,
kazakh_agent,
uk_english_agent,
swedish_agent,
norwegian_agent,
finnish_agent,
mongolian_agent,
slovak_agent,
serbian_agent
]
)

async def main():
    MODEL_NAME = "gemini-2.0-flash"
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")




    external_client = AsyncOpenAI(
        api_key=GEMINI_API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/") 
    # ye url jo hum AsynOpenAI ke through hum jo client bana rahe hein wo use kare ga.. hum ye url is liye use ker rahe ke pata chale ke hum gemini use ker rahe hein 

    model = OpenAIChatCompletionsModel(
        model=MODEL_NAME, 
        openai_client=external_client)



    #     To Remove this error : 
    # OPENAI_API_KEY is not set, skipping trace export
    
    config  = RunConfig(
        model = model,
        model_provider=external_client,
        tracing_disabled=True
        )
    

    # user_input = input("Enter your query: ")  

    print("Welcome to the Multi-Language Translator!")
    text = input("Enter the English text to translate: ")
    print("Available Languages:\n")
    language_list = [
        "Spanish", "French", "Sindhi", "German", "Arabic", "Chinese", "Japanese", "Urdu", "Hindi", "Russian",
        "Turkish", "Korean", "Italian", "Portuguese", "Bengali", "Punjabi", "Persian", "Pashto", "Gujarati", "Tamil",
        "Telugu", "Malay", "Swahili", "Greek", "Thai", "Romanian", "Hebrew", "Indonesian", "Hungarian", "Polish", "Dutch",
        "Czech", "Ukrainian", "Filipino", "Nepali", "Burmese", "Lao", "Amharic", "Somali", "Zulu", "Kurdish",
        "Azerbaijani", "Kazakh", "UK English", "Swedish", "Norwegian", "Finnish", "Mongolian", "Slovak", "Serbian"
    ]
    print("\n".join(language_list))

    language_input = input("Enter the language to translate into: ").strip().lower()
    user_input = f"Translate this to {language_input}: {text}"

    result = await Runner.run(manager_agent,user_input,run_config=config)

    print(result.final_output)
    print("last_agent:", result.last_agent.name)

if __name__ == "__main__":
    asyncio.run(main())