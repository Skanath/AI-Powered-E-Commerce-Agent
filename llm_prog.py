import requests

def question_to_sql(question):
    prompt = f"""
You are an assistant that writes SQL SELECT queries for an e-commerce SQLite database.

Available tables and columns:

1. ad_sales
   - date, item_id, ad_sales, impressions, ad_spend, clicks, units_sold

2. total_sales
   - date, item_id, total_sales, total_units_ordered

3. eligibility
   - eligibility_datetime_utc, item_id, eligibility, message

Write only valid SQL SELECT queries using these columns.
Avoid JOINs unless necessary.
Return only the SQL. Do not explain.

Question: {question}
"""



    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": prompt, "stream": False}
    )
    return response.json()["response"].strip()
