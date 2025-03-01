# FastAPI Chatbot with SQL Query Generation

This project provides a FastAPI-based chatbot application that integrates with OpenAI to generate SQL queries from user inputs. The chatbot then retrieves product information from a database and provides answers to the user. The project also includes a simple UI for interacting with the chatbot.

## Features

- **Chatbot Interface**: A simple web-based UI where users can type their queries and receive answers.
- **SQL Query Generation**: Translates user input into SQL queries using OpenAI's GPT model.
- **Database Integration**: Retrieves data from the database based on the generated SQL query.
- **Product Embeddings**: Stores product embeddings to provide better responses for queries related to product data.

## Project Structure

.
├── app.py                 # Main FastAPI app entry point
├── database.py            # Handles database connection and queries
├── embeddings.py          # Handles product embeddings and storing them
├── query_generator.py     # Handles SQL query generation using OpenAI
├── models.py              # Defines data models for FastAPI (e.g., Pydantic models)
├── config.py              # Configuration and constants (e.g., DB connection, OpenAI API key)
└── chat_bot_ui.py         # Handles chatbot user interface interactions


## Requirements

To run this project, you need the following dependencies:

- Python 3.8+
- OpenAI API Key
- PostgreSQL or other SQL database (depending on your setup)

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/fastapi-chatbot.git
    cd fastapi-chatbot
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:
    - **Windows**:
      ```bash
      venv\Scripts\activate
      ```
    - **Linux/Mac**:
      ```bash
      source venv/bin/activate
      ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Set up your **OpenAI API key** and **database configurations** in the `config.py` file.

6. Run the FastAPI application:
    ```bash
    uvicorn app:app --reload
    ```

7. Open your browser and visit `http://127.0.0.1:8000` to interact with the chatbot UI.

## Endpoints

- **GET `/`**: Returns the chatbot UI HTML page.
- **POST `/search/`**: Receives a user query, generates an SQL query, and retrieves results from the database.
- **POST `/store_embeddings/`**: Stores product embeddings in the database.

## Contributing

Feel free to fork this repository, submit issues, or create pull requests for any improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
