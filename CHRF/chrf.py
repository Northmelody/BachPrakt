from sacrebleu.metrics import CHRF

def load_english(filename):
    with open(filename, encoding="utf-8") as f:
        return [
            line.split("|", 1)[1].strip()
            for line in f
            if "|" in line
        ]

references = load_english("SolutionCHRF.txt")
qwen = load_english("qwenDEUchrf.txt")
llama = load_english("llamaDEUchrf.txt")

metric = CHRF()

print("Qwen :", metric.corpus_score(qwen, [references]).score)
print("Llama:", metric.corpus_score(llama, [references]).score)