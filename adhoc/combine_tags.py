import json
import pandas as pd


df = pd.read_csv("data/questions.csv", encoding="cp1252")
tags = json.load(open("out/tags.json"))

df["Tags"] = tags
df.to_csv("out/data.csv", index=False)
