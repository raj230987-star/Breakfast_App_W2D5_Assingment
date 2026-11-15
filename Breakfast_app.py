import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables from .env or system environment
load_dotenv()

# Streamlit UI Setup
st.title("🥗 Healthy Breakfast Idea Generator")
st.write("Click the button below to instantly generate 5 healthy breakfast ideas using LangChain and OpenAI!")

# Create a button to trigger the generation
if st.button("Generate Breakfast Ideas"):
    # Show a loading spinner while waiting for the API response
    with st.spinner("Cooking up some healthy options..."):
        
        # 1. Initialize the Chat model
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

        # 2. Create a prompt that pins the format and constraints
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a nutrition assistant. Provide exactly 5 healthy breakfast ideas. "
                       "Format the output strictly as a numbered list (1 to 5), with exactly one line per idea, "
                       "and no preamble, intro, or outro text."),
            ("user", "Give me 5 healthy breakfast ideas.")
        ])

        # 3. Create the chain using LCEL
        chain = prompt | llm

        # 4. Invoke the chain (no input dictionary needed since the prompt is static)
        response = chain.invoke({})

        # 5. Display the cleaned text content in the web app
        st.success("Here are your breakfast ideas:")
        st.markdown(response.content)