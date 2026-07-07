from ollama import chat
from openai import OpenAI

with open("Na'vi Files/training.txt", "r") as f:
    training = f.read()

with open("test3.txt", "r") as f:
    test = f.read()


#You are learning a constructed language.
#Study these examples which are formatted like 
#Na'vi sentence | English translation :
#Now look at these multiple choice questions and choose the correct translation.
#Format your answer like 1A, 2B, 3C, ... in one line.
#/////
#Now accurately translate the following sentences.
#Give your response in the same format as the training sentences, Na'vi Sentence | Your english translation.
#Do not explain, only give the translations.

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
Study these examples which are formatted like 
Na'vi sentence | English translation :
{training}
Now accurately translate the following sentences.
Give your response in the same format as the training sentences, Na'vi Sentence | Your english translation.
Do not explain, only give the translations.

Aylì’ufa awngeyä ’eylanä a’ewan. 
Ayngari fìkem feyä ’e’ala topur kangay sìyi nì’aw.
Ayngengaru oheyä tsmukit alu Newey te Tskaha Sorewn’ite.



"""
# QWEN--------------------------------------------------------------------
#Ayngeyä tìftusia ’o’ livu nì’aw!
#Ayoe ke wasyem.
#Eltu si! Tsatstal afwem lu litx nìtxan.
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
    "qwen": query_qwen,
    "llama": query_llama
}

for name, function in models.items():

    print(f"Running {name}...")

    output = function(prompt)

    with open(f"results/{name}.txt", "w") as f:
        f.write(output)

    print(f"Saved {name}.txt")