from ollama import chat
from openai import OpenAI

OPENAI_KEY = "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"
OPENROUTER_KEY = "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"


# -------------------------

with open("training.txt", "r") as f:
    training = f.read()

with open("test.txt", "r") as f:
    test = f.read()

prompt = f"""
You are learning a constructed language.

Study these examples which are formatted like 

Na'vi sentence | English translation:

{training}


Now translate:

{test}

Output only your translations.
"""

# -------------------------
# GPT-4o
# -------------------------

def query_gpt(prompt):

    client = OpenAI(
        api_key=OPENAI_KEY
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


# -------------------------
# QWEN (OLLAMA)
# -------------------------

def query_qwen(prompt):

    response = chat(
        model="qwen3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


# -------------------------
# LLAMA (OLLAMA)
# -------------------------

def query_llama(prompt):

    response = chat(
        model="llama3.3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


# -------------------------
# RUN ALL MODELS
# -------------------------

models = {
    "gpt4o": query_gpt,
    "qwen": query_qwen,
    "llama": query_llama
}

for name, function in models.items():

    print(f"Running {name}...")

    output = function(prompt)

    with open(f"results/{name}.txt", "w") as f:
        f.write(output)

    print(f"Saved {name}.txt")