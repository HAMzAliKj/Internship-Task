import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY")   # Store your API key in an environment variable
)


def writer_agent(topic):
    writer_prompt = PromptTemplate.from_template(
        """
You are a professional essay writer.

Write a concise, well-structured essay (3–5 paragraphs) on the following topic.

Requirements:
- Formal tone
- Introduction
- Body
- Conclusion

Topic:
{topic}
"""
    )

    chain = writer_prompt | llm
    return chain.invoke({"topic": topic}).content


def editor_agent(draft):
    editor_prompt = PromptTemplate.from_template(
        """
You are an expert editor and critic.

Review the essay below.

First, provide a section titled:
### Improvements Made

List the improvements you made as bullet points.

Then provide another section titled:
### Revised Essay

Rewrite the essay by improving:
- Grammar
- Clarity
- Flow
- Structure
- Word choice

Do not change the original meaning.

Essay:
{draft}
"""
    )

    chain = editor_prompt | llm
    return chain.invoke({"draft": draft}).content

topics = [
    "The impact of artificial intelligence on modern education.",
    "The importance of renewable energy for the future."
]


for i, topic in enumerate(topics, start=1):

    print("=" * 80)
    print(f"TOPIC {i}: {topic}")
    print("=" * 80)

    
    draft = writer_agent(topic)

    print("\nWRITER AGENT OUTPUT")
    print("-" * 80)
    print(draft)

    edited = editor_agent(draft)

    print("\nEDITOR AGENT OUTPUT")
    print("-" * 80)
    print(edited)

    print("\n\n")
