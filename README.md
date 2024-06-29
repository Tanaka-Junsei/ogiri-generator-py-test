# How to run

```
pip install -r requirements.txt
```

```
uvicorn main:app --reload
```

# How to test

```
curl -X POST "http://127.0.0.1:8000/add-data" -H "Content-Type: application/json" -d '{"question": "What is FastAPI?", "questionId": 1, "timestamp": "2024-06-29T12:34:56"}'
```

# How to stop

```
Ctrl + C
```