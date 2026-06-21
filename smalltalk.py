import os
from groq import Groq

from dotenv import load_dotenv
load_dotenv()
groq_client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def small_talk_chain(query, history=[]):
    prompt = f'''You are a helpful and friendly e-commerce chatbot designed for small talk. You can answer normal conversational questions like greetings, your name, your purpose, and more. 
    If the user asks a complex or out-of-domain question that is completely unrelated to e-commerce or small talk, politely inform them that you don't have knowledge about it and ask them to ask relevant questions (like about Flipkart products).

    QUESTION: {query}
    '''
    
    messages = []
    for msg in history:
        role = "assistant" if msg["role"].lower() == "assistant" else "user"
        messages.append({"role": role, "content": msg["content"]})
        
    messages.append({
        "role": "user",
        "content": prompt
    })

    completion = groq_client.chat.completions.create(
        model=os.environ['GROQ_MODEL'],
        messages=messages
    )
    return completion.choices[0].message.content