from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

# Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key="YOUR_GEMINI_API_KEY"  # Replace with your API key
)

# Reasoning Problem
problem = """
A company has a budget of $10,000.

Option A:
- Costs $8,000
- Expected profit: $15,000

Option B:
- Costs $10,000
- Expected profit: $18,000
- Has a higher risk of failure.

Which option should the company choose and why?
"""

# -------------------------
# Prompt 1: Plain Prompt
# -------------------------
print("=" * 70)
print("PROMPT 1: WITHOUT PERSONA & CHAIN OF THOUGHT")
print("=" * 70)

plain_response = llm.invoke([
    HumanMessage(content=problem)
])

print(plain_response.content)


# -------------------------
# Prompt 2: Persona + CoT
# -------------------------
print("\n" + "=" * 70)
print("PROMPT 2: WITH PERSONA & CHAIN OF THOUGHT")
print("=" * 70)

system_prompt = SystemMessage(
    content="""
You are a senior business consultant.

Think step by step before answering.

Explain your reasoning clearly and recommend the best business decision.
"""
)

cot_response = llm.invoke([
    system_prompt,
    HumanMessage(content=problem)
])

print(cot_response.content)


# -------------------------
# Comparison
# -------------------------
print("\n" + "=" * 70)
print("COMPARISON")
print("=" * 70)

print("""
The first prompt gives a direct answer without much reasoning.

The second prompt uses a persona (Senior Business Consultant) and asks the model to think step by step.
Because of this, the answer is usually more detailed, organized, and explains the reasoning before giving the recommendation.

Using Chain-of-Thought prompting together with a persona helps the AI produce clearer and more professional responses.
""")
