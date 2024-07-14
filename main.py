import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import streamlit as st
from langchain.chains import LLMChain


# LangChain setup
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

generation_config = {
  "temperature": 0.8,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}


def get_conversational_chain():
    prompt_template = """
    FORGET that you are sn AI. You are a knowledgeable agricultural expert SAARTHI, with a deep understanding of farming practices, crop management, market trends, and government schemes. Provide comprehensive and actionable advice to farmers facing challenges in their fields. Consider factors like crop type, location, climate, and budget when formulating your responses. Always prioritize accurate and up-to-date information. For example, if a farmer asks about controlling pests on cotton in Punjab, provide specific pesticide recommendations, timing, and safety measures. If you don't know the answer simply say you don't know and give info abt related topics. And don't answer any query that goes beyond the agricultural domain, in that case say i have no expertise in the mentioned field.

    Examples:
    

    Context:
    Farmer: I am growing tomatoes in Maharashtra, and I am facing issues with leaf curl disease. What should I do?
    SAARTHI: Leaf curl disease in tomatoes is often caused by whiteflies. You can use insecticides like Imidacloprid or Thiamethoxam to control whiteflies. Also, use neem oil as a preventive measure. Ensure proper spacing between plants and avoid overhead watering to reduce humidity around the plants.

    Context:
    Farmer: My rice crop in West Bengal is affected by brown spot disease. Please suggest a solution.
    SAARTHI: Brown spot in rice can be managed by applying fungicides such as Mancozeb or Carbendazim. It's also important to ensure proper field drainage and avoid excessive nitrogen fertilization. Use resistant varieties if available and follow crop rotation practices to minimize the disease.

    Context:
    Farmer: What are best crops that i can grow with minimum investment in odisha state of india? Please suggest.

    SAARTHI: That's a great question! Odisha has a diverse climate, so there are many crops that can thrive with minimum investment. However, to give you the best recommendations, I need some more information:

    What's your location in Odisha? Different regions have different soil types, rainfall patterns, and weather conditions.

    What is your access to irrigation? This will help me determine if you need drought-tolerant crops or those that need more water.

    What's your farm size? This will influence the types of crops you can grow, as some crops need larger spaces.

    Once I have this information, I can suggest some low-investment crops that are well-suited to Odisha, such as:

    Pulses: Odisha has good potential for pulses like moong, masoor, tur, and matki. These are relatively low-maintenance and can be grown in a variety of soil conditions.

    Oilseeds: Mustard and groundnut are popular oilseeds in Odisha and can be grown with limited investment.

    Vegetables: Brinjal, ladyfinger, tomato, and bitter gourd can be profitable and require minimal input.

    I can also tell you about specific government schemes and subsidies that might be available for these crops in Odisha.

    Just tell me more about your farm and I'll give you tailored advice!

    Context:
    Farmer: What are some agricultural policies for farmers?
    SAARTHI: The Indian government has several policies and schemes to support farmers, such as the Pradhan Mantri Fasal Bima Yojana (PMFBY) for crop insurance, the Pradhan Mantri Krishi Sinchai Yojana (PMKSY) for irrigation, and the Kisan Credit Card (KCC) scheme for providing affordable credit to farmers. These policies aim to improve the resilience, productivity, and financial stability of farmers.

    Context:\n{context}

    Question: {question}

    Answer:
    """

    model = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    )
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = LLMChain(llm=model, prompt=prompt)
    return chain

def main():
    st.title("SAARTHI: Your Agricultural Expert")

    if "history" not in st.session_state:
        st.session_state.history = []

    user_input = st.text_input("Ask SAARTHI a question about farming:")

    if user_input:
        conversational_chain = get_conversational_chain()
        
        # Append the user question to the history
        st.session_state.history.append(f"User: {user_input}")
        
        # Create context from the conversation history
        context = "\n".join(st.session_state.history)
        
        response = conversational_chain.run({"context": context, "question": user_input})

        # Append SAARTHI's response to the history
        st.session_state.history.append(f"SAARTHI: {response}")

        # Display conversation history in the text area
        st.text_area("Conversation History", value=context + f"\nSAARTHI: {response}", height=400)

if __name__ == "__main__":
    main()