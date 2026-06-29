from collections import Counter
import re

# --------load sentences from training.
with open("training.txt", "r", encoding="utf-8") as f:
    sentences = [line.strip() for line in f if line.strip()]

# --------- helper: tokenize ----------
def tokenize(text):
    return re.findall(r"\w+", text.lower())

# --------- precompute tokens ----------
tokenized = [tokenize(s) for s in sentences]

# --------- similarity (word overlap score) ----------
def similarity(a_tokens, b_tokens):
    a = Counter(a_tokens)
    b = Counter(b_tokens)

    # intersection size (shared words count)
    common = set(a.keys()) & set(b.keys())
    score = sum(min(a[w], b[w]) for w in common)

    return score

# --------- find top 3 for each sentence ----------
all_selected = set()

for i, sent_i in enumerate(sentences):
    scores = []

    for j, sent_j in enumerate(sentences):
        if i == j:
            continue

        score = similarity(tokenized[i], tokenized[j])
        scores.append((score, sent_j))

    # sort by best match
    scores.sort(reverse=True, key=lambda x: x[0])

    top3 = [s for _, s in scores[:30]]
    all_selected.update(top3)


# --------- write unique results ----------
with open("distinct_sentences.txt", "w", encoding="utf-8") as f:
    for s in sorted(all_selected):
        f.write(s + "\n")

print("Done. Saved to distinct_sentences.txt")
#--------------------------
input_file = "distinct_sentences.txt"
output_file = "test3.txt"

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

cleaned = []

for line in lines:
    line = line.strip()

    if "|" in line:
        line = line.split("|")[0]   # keep only part before |

    cleaned.append(line)

with open(output_file, "w", encoding="utf-8") as f:
    for line in cleaned:
        f.write(line + "\n")

print("Done. Saved cleaned file.")