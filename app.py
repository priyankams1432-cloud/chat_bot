import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = "https://models.github.ai/inference"
model = "gpt-4o-mini"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

system_prompt = "You are a helpful assistant. Answer questions clearly and concisely in English."
conversation_history = [SystemMessage(system_prompt)]

print("Chatbot: Hello! I'm your assistant. Type 'quit' or 'exit' to end.")
print("-" * 50)

while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() in ['quit', 'exit']:
        print("Chatbot: Goodbye! Have a nice day!")
        break
    
    if not user_input:
        continue
    
    conversation_history.append(UserMessage(user_input))
    
    response = client.complete(
        messages=conversation_history,
        temperature=1.0,
        top_p=1.0,
        max_tokens=1000,
        model=model
    )
    
    assistant_message = response.choices[0].message.content
    conversation_history.append(SystemMessage(assistant_message))
    
    print(f"Chatbot: {assistant_message}")
    print("-" * 50)

                                      