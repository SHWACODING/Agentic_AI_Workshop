from groq import Groq
import os

os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
client = Groq()

response = client.chat.completions.create(
    model='llama-3.3-70b-versatile',
    messages=[{"role":"user","content":"Exolain me Quantum Machine Learning?"}],
    temperature=0.7
)
print(response.choices[0].message.content)
