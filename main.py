from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google.cloud import firestore
import os
from datetime import datetime

# Firestoreのクライアントを初期化
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service.json"
db = firestore.Client()

app = FastAPI()

# リクエストボディのモデルを定義
class Question(BaseModel):
    question: str
    questionId: int
    timestamp: str

@app.post("/add-data")
async def add_data():
    try:
        # Question型のデータを生成
        data = Question(
            question="Sample question",
            questionId=123,
            timestamp=datetime.utcnow().isoformat()
        )
        # Firestoreのコレクションにデータを書き込む
        doc_ref = db.collection('question').document()
        doc_ref.set(data.dict())
        return {"message": "Data added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to add data: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
