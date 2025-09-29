from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection

connections.connect(alias="default", host="localhost", port="19530")

fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema(name="username", dtype=DataType.VARCHAR, max_length=500),
    FieldSchema(name="role", dtype=DataType.VARCHAR, max_length=500),
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=3072),
]
schema = CollectionSchema(fields, description="User database")

collection_name = "user_collection"
collection = Collection(
    name=collection_name,
    schema=schema,
    using="default",
    shards_num=1,
)

index_params = {"metric_type": "L2", "index_type": "IVF_FLAT", "params": {"nlist": 64}}
collection.create_index(field_name="embedding", index_params=index_params)
