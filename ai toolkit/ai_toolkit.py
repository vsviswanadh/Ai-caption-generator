import streamlit as st
from transformers import pipeline

# Page settings
st.set_page_config(page_title="AI Productivity Assistant")

st.title("🚀 AI Productivity Assistant (Advanced AI)")

# Load FLAN-T5 model
@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="google/flan-t5-base")

generator = load_model()

# Tool selection
tool = st.selectbox(
    "Choose Tool",
    [
        "LinkedIn Post Generator",
        "Email Generator",
        "Story Generator",
        "Resume Bullet Improver",
        "Text Rewriter"
    ]
)

# Inputs
topic = st.text_area("Enter your content/topic")
tone = st.selectbox("Select Tone", ["Professional", "Casual", "Creative"])

# Prompt creation
def create_prompt(tool, topic, tone):

    if tool == "LinkedIn Post Generator":
        return f"""
Write a {tone} LinkedIn post about {topic}.
Include a strong opening, explanation, and conclusion.
"""

    elif tool == "Email Generator":
        return f"""
Write a {tone} email about {topic}.
Include subject, greeting, body, and closing.
"""

    elif tool == "Story Generator":
        return f"""
Write a {tone} short story about {topic}.
"""

    elif tool == "Resume Bullet Improver":
        return f"""
Improve this resume bullet professionally:
{topic}
"""

    elif tool == "Text Rewriter":
        return f"""
Rewrite this text in a {tone} tone:
{topic}
"""

# Generate button
if st.button("Generate"):

    if topic.strip() == "":
        st.warning("⚠️ Please enter some content")
    else:
        prompt = create_prompt(tool, topic, tone)

        with st.spinner("Generating..."):
            output = generator(prompt, max_length=200)

        result = output[0]['generated_text']

        st.subheader("✨ Generated Output")

        st.text_area("Output", result, height=250)