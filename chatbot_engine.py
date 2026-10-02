import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer, util

class FAQBot:
    def __init__(self, csv_path, threshold=0.4):
        self.df = pd.read_csv(csv_path)
        self.threshold = threshold
        # Small, fast, runs great on CPU/Apple Silicon
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.question_embeddings = self.model.encode(
            self.df['question'].tolist(), convert_to_tensor=True
        )

    def get_answer(self, user_query):
        query_embedding = self.model.encode(user_query, convert_to_tensor=True)
        scores = util.cos_sim(query_embedding, self.question_embeddings)[0]
        best_idx = int(scores.argmax())
        best_score = float(scores[best_idx])

        if best_score < self.threshold:
            return {
                "answer": "I'm not sure about that — could you rephrase, or ask something else about our products/policies?",
                "matched_question": None,
                "confidence": round(best_score, 3)
            }

        return {
            "answer": self.df.iloc[best_idx]['answer'],
            "matched_question": self.df.iloc[best_idx]['question'],
            "confidence": round(best_score, 3)
        }