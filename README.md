# Flask Rest API with CRUD Operations

This project showcases a simple Flask Rest API with CRUD operations, utilizing a SQLite database to manage drinks. The API allows users to perform basic operations such as retrieving a list of drinks, getting information about a specific drink, adding a new drink, and deleting a drink.

## Getting Started

### Prerequisites

- Python (version 3.6 or higher)
- Flask
- Flask-SQLAlchemy

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ced87/flask-rest-api.git
    ```

2. Navigate to the project directory:

    ```bash
    cd flask-rest-api
    ```

3. Create a virtual environment (optional but highly recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source venv/bin/activate
        ```

5. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

6. Run the application:

    ```bash
    flask run
    ```

    The API will be accessible at [http://localhost:5000](http://localhost:5000).

### Included Database

This project includes an instance of a SQLite database (`data.db`) with a few pre-populated entries. You can explore the API's functionality with these initial entries.

## API Endpoints

- **GET /drinks:** Retrieve a list of all drinks.
- **GET /drinks/{id}:** Retrieve information about a specific drink by ID.
- **POST /drinks:** Add a new drink to the database.
- **DELETE /drinks/{id}:** Delete a drink from the database by ID.

## Contributing

Contributions are welcome! If you have suggestions or find issues, please create a GitHub issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
