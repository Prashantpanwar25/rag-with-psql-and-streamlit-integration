from fastapi import FastAPI
from models import SearchQuery
from query_generator import generate_sql_query
from embeddings import store_product_embeddings
from database import execute_query

app = FastAPI()

@app.post("/search/")
async def search(search_query: SearchQuery):
    print(f"Received search query: {search_query.query}")
    user_query = search_query.query
    sql_query = generate_sql_query(user_query)

    # Check if the generated SQL query is a string
    if isinstance(sql_query, dict) and "error" in sql_query:
        print(f"Error in generated SQL query: {sql_query}")
        return sql_query  # Return error if query generation failed

    conn = get_db_connection()
    cur = conn.cursor()

    try:
        print(f"Executing SQL query: {sql_query}")
        cur.execute(sql_query)
        rows = cur.fetchall()
        columns = [desc[0] for desc in cur.description]
        print(f"Fetched {len(rows)} rows from the database.")

        # Generate readable answer dynamically based on query results
        readable_answer = []
        for row in rows:
            answer_parts = []  # To hold parts of the dynamic answer
            for idx, column in enumerate(columns):
                answer_parts.append(f"{column}: {row[idx]}")  # Create a dynamic sentence based on column names and values
            readable_answer.append(" | ".join(answer_parts))  # Join all column values to make a readable sentence
            print(f"Row data: {answer_parts}")

        return {
            "sql_query": sql_query,
            "results": rows,
            "columns": columns,
            "answer": "\n".join(readable_answer)  # Combine the readable answers into a response
        }
    except Exception as e:
        print(f"Error while executing query: {e}")
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()


@app.post("/store_embeddings/")
async def store_embeddings():
    store_product_embeddings()
    return {"message": "Product embeddings stored successfully"}
