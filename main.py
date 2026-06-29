from ollama import chat
from openai import OpenAI

OPENAI_KEY = "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"
OPENROUTER_KEY = "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"


# -------------------------ask in german / french ->>english translation!

with open("training.txt", "r") as f:
    training = f.read()

with open("test2.txt", "r") as f:
    test = f.read()


#You are learning a constructed language.
#Study these examples which are formatted like 
#Na'vi sentence | English translation
#Now look at these multiple choice questions and choose the correct translation.
#Format your answer like 1A, 2B, 3C, ... in one line.

#Du lernst eine konstruierte Sprache.
#Lerne von diesen Beispielen mit der Formattierung Na'vi Satz | Englische Übersetzung :
#Jetzt betrachte diese Multiple-Choice Fragen und wähle die richtige Übersetzung.
#Formattiere deine Antwort in einer Zeile Und halte dich an das Muster 1A, 2B, 3C, ...

#Tu apprends une langue construite.
#Apprends à partir de ces exemples présentés sous la forme Phrase en Na'vi | Traduction en anglais :
#Regarde maintenant ces questions à choix multiples et choisis la bonne traduction.
#Formule ta réponse sur une seule ligne en respectant le schéma 1A, 2B, 3C, ...

#Here are some simple rules of the language:
#fì- indicates proximal deixis. When used as a plural, it becomes fay+
#tsa- indicates distal dexis. When used as a plural, it becomes tsay+
#-o marks the noun as indefinite
#the ergative case is -l on nouns ending with vowels and -ìl on nouns ending with consonants


prompt = f"""

You are learning a constructed language.


Study these examples which are formatted like Na'vi sentence | English translation :
{training}

Now look at this file with Na'vi sentences, and translate ALL of them.
Do not give explanations, ONLY your translations.
{test}


"""
#{test}
# GPT-4o--------------------------------------------------------------------disabled bc api


#def query_gpt(prompt):
#
 #   client = OpenAI(
 #       api_key=OPENAI_KEY
 #   )
#
 #   response = client.chat.completions.create(
  #      model="gpt-4o",
   #     messages=[
    #        {"role": "user", "content": prompt}
     #   ]
    #)

 #   return response.choices[0].message.content

# QWEN--------------------------------------------------------------------

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


# LLAMA --------------------------------------------------------

def query_llama(prompt):

    response = chat(
    model="llama3.1:8b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    options={
    "temperature": 0
    }
)

    return response["message"]["content"]




models = {
    #"gpt4o": query_gpt,
    "qwen": query_qwen,
    "llama": query_llama
}

for name, function in models.items():

    print(f"Running {name}...")

    output = function(prompt)

    with open(f"results/{name}.txt", "w") as f:
        f.write(output)

    print(f"Saved {name}.txt")