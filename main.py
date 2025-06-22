from transformers import pipeline

# Load Falcon-1B (chat-friendly, works on CPU)
chatbot = pipeline(
    "text-generation",
    model="mistralai/Mistral-7B-Instruct-v0.3",
    max_new_tokens=150,
    do_sample=True,
    temperature=0.7,    
)

# # Set persona
# persona = (
#     "You are Dr. Abdul Kalam, former President of India. You are highly intelligent and a smart person, loved by all."
#     "Speak casually and confidently in your replies."
# )

print("Set the persona\n")
persona = input();

# match = re.search(r"You are (.*?),", persona)
# if match:
#     name = match.group(1)

# Named entity recognition
ner = pipeline("ner", grouped_entities=True)

for entity in ner(persona):
    if entity["entity_group"] == "PER":
        name = entity["word"]
        break

# Store chat history (optional, basic memory)
history = []

print(f"💬 Chat with {name}, (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")
    if user_input.strip().lower() in {"exit", "quit"}:
        print(f"{name}: Have a good day.")
        break

    # Combine persona and short history into prompt
    # prompt = f"{persona}\n\n"
    # for turn in history[-6:]:  # Limit to last 2 exchanges (4 lines)
    #     prompt += turn + "\n"
    # prompt += f"User: {user_input}\nDr. Abdul Kalam:"
    prompt = f"{persona}\n\nUser: {user_input}\n{name}:"
    
    # # Generate response
    # result = chatbot(prompt)[0]["generated_text"]
    
    
    # # Extract just persona's reply
    # reply = result.split("Dr. Abdul Kalam:")[-1]
    # print(f"Dr. Abdul Kalam: {result}\n")

    # # Update history
    # history.append(f"User: {user_input}")
    # history.append(f"Dr. Abdul Kalam: {reply}")

    output = chatbot(
        prompt,       
        return_full_text=False        
    )[0]["generated_text"]

    # Strip extra whitespace
    reply = output.split("User:")[0].strip()
    print(f"{name}: {reply}\n")