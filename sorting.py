from collections import Counter
import re

# --------load sentences from training.
with open("Na'vi Files/training.txt", "r", encoding="utf-8") as f:
    training = [line.strip() for line in f if line.strip()]

with open("Na'vi Files/test.txt", "r", encoding="utf-8") as f:
    test = [line.strip() for line in f if line.strip()]

training_navi = [line.split("|")[0].strip() for line in training]
# --------- helper: tokenize ----------
def tokenize(text):
    return re.findall(r"\w+", text.lower())

# --------- precompute tokens ----------
training_tokens = [tokenize(s) for s in training]
test_tokens = [tokenize(s) for s in test]

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

for i in range(len(training)):
    scores = []

    for j in range(len(test)):
        score = similarity(training_tokens[i], test_tokens[j])

        # Ignore completely unrelated sentences
        if score > 0:
            scores.append((score, test[j]))

    scores.sort(reverse=True, key=lambda x: x[0])

    top30 = [sentence for _, sentence in scores[:30]]
    all_selected.update(top30)

# ---------- Save unique selected test sentences ----------
with open("distinct_sentences.txt", "w", encoding="utf-8") as f:
    for sentence in sorted(all_selected):
        f.write(sentence + "\n")

print(f"Saved {len(all_selected)} unique sentences to distinct_sentences.txt")
