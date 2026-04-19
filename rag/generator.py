from groq import Groq
from dotenv import load_dotenv
load_dotenv()
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_answer(query, chunks):

    context = "\n\n".join([chunk["text"] for chunk in chunks])

    prompt = f"""
Answer the question using ONLY the context below.

Context:
{context}

Question:
{query}

If the answer is not in the context, say "I don't know".

Answer:
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content