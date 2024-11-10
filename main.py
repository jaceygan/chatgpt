from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["OPENAI"])
model = "gpt-4o-mini"

user_prompts = [
"How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
"Where is the Arc de Triomphe?",
"What are the must-see artworks at the Louvre Museum?"
]

system_prompt = "You are a travel planning expert for Peterman Reality Tours. \
                    You will provide valuable insights into the iconic landmarks and hidden treasures of Paris. \
                    You will respond intelligently and provide an engaging and immersive travel planning experience for the user."

system_message = {"role":"system", "content":system_prompt}

conversation = [system_message]

def get_response (conv) :
    response = client.chat.completions.create(
    model = model,
    messages = conv,
    temperature = 0, max_tokens=100)
    return response.choices [0].message.content


for prompt in user_prompts:
    print("")
    print("Question:", prompt)
    conversation.append({"role": "user", "content": prompt})
    response = get_response(conversation)
    conversation.append({"role": "assistant", "content": response})
    print("Answer:", response)
