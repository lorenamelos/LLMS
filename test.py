import random

# Define templates and keywords
templates = [
    "Complete the sentence: [sentence]",
    "What do you think about [topic]?",
    "Provide a response to [scenario]"
]

topics = ["artificial intelligence", "climate change", "space exploration"]
scenarios = ["meeting a new person", "encountering a problem at work", "planning a vacation"]

# Function to generate a random prompt
def generate_prompt():
    # Choose a random template
    template = random.choice(templates)

    # Generate prompt based on selected template
    if "[sentence]" in template:
        prompt = template.replace("[sentence]", input("Enter a sentence: "))
    elif "[topic]" in template:
        prompt = template.replace("[topic]", random.choice(topics))
    elif "[scenario]" in template:
        prompt = template.replace("[scenario]", random.choice(scenarios))

    return prompt

# Generate and print a prompt
prompt = generate_prompt()
print("Generated Prompt:", prompt)
