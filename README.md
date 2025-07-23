AI-Powered E-Commerce Agent

This project converts text based questions into SQL queries and retrieves data from a local SQLite database using an offline language model.

1. The requirements.txt file contains all the Python packages needed for the project. Install them inside a virtual environment before running the code.

2. Run the dataset_sql.py file to load CSV files into a SQLite database. It creates structured tables named ad_sales, total_sales, and eligibility.

3. Start the Llama3 model locally by using the command ollama run llama3. This enables the AI to generate SQL queries offline.

4. Launch the Flask server using main.py. It connects the web interface with the database and the language model, and handles user input.

5. Open http://127.0.0.1:5000 in your browser to ask questions in plain English. The AI will convert them into SQL, run the query, and show the result with charts if applicable.

