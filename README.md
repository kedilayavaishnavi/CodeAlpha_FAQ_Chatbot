# FAQ Chatbot — Semantic Search with Sentence Transformers

A chatbot that answers FAQs using sentence-embedding semantic search instead of
keyword matching, so it understands paraphrased questions.

## Features
- Semantic matching via `all-MiniLM-L6-v2` sentence embeddings
- Confidence threshold with graceful fallback for out-of-scope queries
- Interactive chat UI built with Streamlit
- Real-time confidence score

## Why semantic search over keyword matching
Keyword-based FAQ bots fail on paraphrases ("get my money back" vs "return policy").
This bot embeds both the user query and all FAQ questions into a shared vector space
and ranks by cosine similarity, so meaning — not exact words — drives the match.

## Tech Stack
Python, Sentence-Transformers, Streamlit, scikit-learn, pandas

## Setup
```bash
pip install -r requirements.txt
streamlit run app.py