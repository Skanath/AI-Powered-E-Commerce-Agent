import requests

def question_to_sql(question):
    prompt = f"""
You are an AI assistant that converts natural language into safe SQL SELECT queries for an e-commerce SQLite database.

Use only the following tables and their columns:

1. ad_sales
   - date, item_id, ad_sales, impressions, ad_spend, clicks, units_sold

2. total_sales
   - date, item_id, total_sales, total_units_ordered

3. eligibility
   - eligibility_datetime_utc, item_id, eligibility, message

Rules:
- Output only a valid SQL SELECT query.
- Always use COALESCE(column, 0) to handle NULL values.
- Always use NULLIF(x, 0) in divisions to avoid division by zero.
- Avoid JOINs unless necessary.
- If the question asks for the "highest", "maximum", or "top" record, use ORDER BY and LIMIT 1.
- Never explain the SQL or add comments. Only output the SQL code.

Question: {question}
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except Exception as e:
        return f"-- LLM error: {e}"
