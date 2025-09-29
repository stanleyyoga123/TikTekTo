from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection

connections.connect(alias="default", host="localhost", port="19530")

fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema(name="question", dtype=DataType.VARCHAR, max_length=500),
    FieldSchema(name="answer", dtype=DataType.VARCHAR, max_length=500),
    FieldSchema(name="category", dtype=DataType.VARCHAR, max_length=500),
    FieldSchema(name="tags", dtype=DataType.VARCHAR, max_length=500),
    FieldSchema(name="difficulty", dtype=DataType.VARCHAR, max_length=500),
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=3072),
]
schema = CollectionSchema(fields, description="Questions and Answers RAG")

collection_name = "questions_collection"
collection = Collection(
    name=collection_name, schema=schema, using="default", shards_num=1
)

import pandas as pd
import pickle

df = pd.read_csv("out/data.csv")
embeddings = pickle.load(open("out/embeddings.pkl", "rb"))

entities = [[], [], [], [], [], []]
for _, row in df.iterrows():
    _id = row["Question Number"]
    question = row["Question"]
    answer = row["Answer"]
    category = row["Category"]
    tags = row["Tags"]
    difficulty = row["Difficulty"]
    embedding = embeddings[_id][0].values
    entities[0].append(question)
    entities[1].append(answer)
    entities[2].append(category)
    entities[3].append(tags)
    entities[4].append(difficulty)
    entities[5].append(embedding)

result = collection.insert(entities)

index_params = {"metric_type": "L2", "index_type": "IVF_FLAT", "params": {"nlist": 64}}

collection.create_index(field_name="embedding", index_params=index_params)

print(result)
