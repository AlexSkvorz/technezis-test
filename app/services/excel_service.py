import pandas as pd

from app.schemes.source_schemes import CreateSourceSchema


async def parse_excel(file_path: str) -> list[CreateSourceSchema]:
    df = pd.read_excel(file_path, engine="openpyxl")
    df = df.astype(str).fillna("")

    sources = []
    for _, row in df.iterrows():
        sources.append(
            CreateSourceSchema(title=row["title"].strip(), url=row["url"].strip(), xpath=row["xpath"].strip())
        )

    return sources
