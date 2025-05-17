from pydantic import BaseModel, Field, HttpUrl


class CreateSourceSchema(BaseModel):
    title: str = Field(description="Название источника")
    url: HttpUrl = Field(description="Ссылка на сайт источник")
    xpath: str = Field(description="Путь к элементу с ценой")
