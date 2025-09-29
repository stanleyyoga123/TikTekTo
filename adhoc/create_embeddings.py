import os
import pickle
from google import genai
import pandas as pd

out = {}

# NOTE: uncomment this if you have checkpoint file
# out = pickle.load(open("out/embeddings.pkl", "rb"))

path = "out/data.csv"
df = pd.read_csv(path, encoding="cp1252")

PROMPT = """Question: {question}
Answer: {answer}
Category: {category}
Tags: {tags}
Difficulty: {difficulty}"""

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

model = "gemini-embedding-001"


for i, row in df.iterrows():
    _id = row["Question Number"]
    if _id in out:
        continue
    content = PROMPT.format(
        question=row["Question"],
        answer=row["Answer"],
        category=row["Category"],
        tags=row["Tags"],
        difficulty=row["Difficulty"],
    )
    print(_id)
    print(content)
    embedding = client.models.embed_content(model=model, contents=content).embeddings
    out[_id] = embedding

    pickle.dump(out, open("out/embeddings.pkl", "wb"))
