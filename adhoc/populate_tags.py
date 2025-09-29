import time
import json
import os

import pandas as pd
from google import genai

PROMPT = """
Extract tags that are related with this question and answer

Category: {category}
Question: {question}
Answer: {answer}

Just answer with the tags with comma separated for each
"""

MODEL = "gemini-2.5-flash"
output = []
# NOTE: Uncomment this if you have checkpoint file
# output = json.load(open(os.path.join("out", "tags.json")))


path = os.path.join("data", "questions.csv")
df = pd.read_csv(path, encoding="cp1252")

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

for i, row in df.iterrows():
    if i < len(output):
        continue
    print(i)
    print(row["Question"])
    prompt = PROMPT.format(
        category=row["Category"], question=row["Question"], answer=row["Answer"]
    )
    out = client.models.generate_content(model=MODEL, contents=prompt).text
    output.append(out.lower())
    json.dump(output, open(os.path.join("out", "tags.json"), "w"))
    time.sleep(6)
