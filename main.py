from flask import Flask, request, render_template
import sqlite3
from llm_prog import question_to_sql
from charts import generate_chart_from_result

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    question = sql_query = ""
    response = []
    chart_url = ""

    if request.method == "POST":
        question = request.form.get("question", "").strip()
        if not question:
            response = ["Please enter a question."]
        else:
            sql_query = question_to_sql(question)

            if sql_query.startswith("-- LLM error"):
                response = [sql_query]
            else:
                try:
                    conn = sqlite3.connect("ecommerce.db")
                    cursor = conn.cursor()
                    cursor.execute(sql_query)
                    rows = cursor.fetchall()
                    cols = [desc[0] for desc in cursor.description]
                    response = [dict(zip(cols, row)) for row in rows]
                    conn.close()

                    
                    if len(cols) == 2 and all(
                        isinstance(row[1], (int, float)) and row[1] is not None
                        for row in rows[:5]
                    ):
                        data = [row[1] for row in rows]
                        labels = [str(row[0]) for row in rows]
                        chart_url = generate_chart_from_result(data, labels, "Chart Output")

                except Exception as e:
                    response = [f"SQL execution error: {str(e)}"]

    return render_template(
        "index.html",
        question=question,
        sql_query=sql_query,
        response=response,
        chart_url=chart_url
    )

if __name__ == "__main__":
    app.run(debug=True)
