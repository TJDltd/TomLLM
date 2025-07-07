import pydantic


class InputQuery(pydantic.BaseModel):
    query: str
