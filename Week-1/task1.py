from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

# Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key="YOUR_GEMINI_API_KEY"  # Replace with your API key
)

# System Prompt (Persona)
system_prompt = SystemMessage(
    content="""
You are PyBuddy, a friendly Python programming mentor.

Rules:
- Only answer Python programming questions.
- Explain concepts in simple English.
- Give examples when helpful.
- If the user asks something unrelated to Python, politely tell them you only help with Python programming.
- Always be friendly and encouraging.
"""
)

# Test Messages (5 required)
test_messages = [
    "Write a Python function to reverse a string.",
    "Explain the difference between a list and a tuple.",
    "Find the bug in this code:\nfor i in range(5)\n    print(i)",
    "How can I improve this function?\ndef add(a,b): return a+b",
    "Who won the FIFA World Cup?"  # Off-topic question
]

print("=" * 60)
print("Python Mentor Chatbot")
print("=" * 60)

for i, message in enumerate(test_messages, start=1):
    print(f"\nTest {i}")
    print("User:")
    print(message)

    response = llm.invoke([
        system_prompt,
        HumanMessage(content=message)
    ])

    print("\nBot:")
    print(response.content)
    print("-" * 60)
