import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# App UI Title and Description
st.title("💡 My First LangChain GenAI App")
st.write("Type any programming topic below and let AI generate a fun fact for you!")

# Create a text input box for the user
topic = st.text_input("Enter a topic (e.g., Python, JavaScript, Rust):", "Python")

# Create a submit button
if st.button("Generate Fun Fact"):
    if topic:
        # Show a loading spinner while waiting for OpenAI
        with st.spinner("Generating..."):
            # 1. Initialize the Chat model
            llm = ChatOpenAI(model="gpt-4o-mini")

            # 2. Create the Prompt Template
            prompt = ChatPromptTemplate.from_messages([
                ("system", "You are a helpful and concise programming assistant."),
                ("user", "Give me a one-sentence fun fact about {topic}.")
            ])

            # 3. Create the Chain
            chain = prompt | llm

            # 4. Invoke the chain using the dynamic user input from Streamlit
            response = chain.invoke({"topic": topic})

            # Display the result in the web app
            st.success("Here is your fun fact:")
            st.write(response.content)
    else:
        st.warning("Please enter a topic first!")