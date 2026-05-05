Run API server (FastAPI)

Once you create your API file:

uvicorn src.api.main:app --reload

🔷  Run Streamlit UI
streamlit run src/ui/app.py

🔷 ▶️ RUN TESTS
python -m unittest tests/test_cases.py
