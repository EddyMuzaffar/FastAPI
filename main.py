from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
def read_items(q: str, item_id: int = Path(title="The ID of the item to get")):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results