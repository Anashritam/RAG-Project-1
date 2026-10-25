# RAG-Project-1
## start
```
knowledgebase-ai/
├── src/
│   └── knowledgebase_ai/
│       ├── __init__.py
│       ├── main.py
│       ├── api/
│       │   ├── __init__.py
│       │   └── routes.py
│       ├── core/
│       │   ├── __init__.py
│       │   └── config.py
│       ├── domain/
│       │   ├── __init__.py
│       │   └── models.py
│       ├── ingestion/
│       │   ├── __init__.py
│       │   ├── loader.py
│       │   └── chunker.py
│       ├── retrieval/
│       │   ├── __init__.py
│       │   ├── embeddings.py
│       │   └── retriever.py
│       ├── generation/
│       │   ├── __init__.py
│       │   ├── llm_client.py
│       │   └── prompts.py
│       └── services/
│           ├── __init__.py
│           ├── ingestion_service.py
│           └── qa_service.py
├── tests/
│   ├── unit/
│   └── integration/
├── data/
│   └── documents/
├── .env.example
├── .gitignore
├── pyproject.toml
└── README.md
```