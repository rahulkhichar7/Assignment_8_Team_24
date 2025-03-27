from fastapi import FastAPI
from elasticsearch import Elasticsearch

app = FastAPI()

# Connect to Elasticsearch running inside Docker
es = Elasticsearch("http://elasticsearch:9200")


INDEX_NAME = "documents"

@app.get("/get_best_document")
async def get_best_document():
    query = {
        "size": 1,
        "query": {
            "match_all": {}
        },
        "sort": [
            {"_score": "desc"}
        ]
    }
    response = es.search(index=INDEX_NAME, body=query)
    if response["hits"]["hits"]:
        return response["hits"]["hits"][0]["_source"]
    return {"message": "No documents found"}

@app.post("/insert_large_document")
async def insert_large_document():
    document = {
        "id": 5,
        "text": "This is a the document which is newly inserted in Elasticsearch."
    }
    es.index(index=INDEX_NAME, id=document["id"], document=document)
    return {"message": "Document insertion successful"}


