response = requests.post(
    "http://localhost:8000/generate",
    json={
        "document_type": document_type,
        "parties": parties,
        "terms": terms,
        "dates": dates
    }
)