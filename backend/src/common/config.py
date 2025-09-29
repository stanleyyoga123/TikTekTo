from pydantic import BaseModel
from pydantic.functional_validators import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class MilvusConfig(BaseModel):
    host: str
    port: str
    db_name: str


class MongoConfig(BaseModel):
    uri: str


class QuestionModuleConfig(BaseModel):
    collection: str
    anns_field: str
    limit: int
    output_fields: list[str]
    search_params: dict


class UserPathwayController(BaseModel):
    db_name: str
    collection: str


class Config(BaseSettings):
    milvus: MilvusConfig
    mongo: MongoConfig
    question_module: QuestionModuleConfig
    user_controller: UserPathwayController

    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter=".",
        extra="ignore",
    )


CONFIG = Config()
