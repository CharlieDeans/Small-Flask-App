### Small-Flask-App README

# Small-Flask-App

A little Flask app with two API endpoints. Using this space almost like a diary for my Flask learning.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Small-Flask-App is a simple web application built using the Flask framework. The primary purpose of this project is to provide a basic understanding of how to create API endpoints using Flask. This app includes two API endpoints and is structured in a way that is easy to understand and extend.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/Small-Flask-App.git
    cd Small-Flask-App
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the application, use the following command:
```bash
python main.py
```

By default, the application will be available at `http://127.0.0.1:55055/`.

## API Endpoints

The application includes the following API endpoints:

1. **GET /hello**
    - Description: Returns a "Hello, World!" message.
    - Example Response:
        ```json
        {
            "message": "Hello, World!"
        }
        ```

2. **GET /goodbye**
    - Description: Returns a "Goodbye, World!" message.
    - Example Response:
        ```json
        {
            "message": "Goodbye, World!"
        }
        ```

## Project Structure

```
Small-Flask-App/
│
├── templates/
│   └── index.html
├── .gitignore
├── README.md
├── main.py
├── requirements.txt
└── README.md
```

- `templates/`: Directory containing HTML templates.
- `.gitignore`: Specifies intentionally untracked files to ignore.
- `README.md`: Project documentation.
- `main.py`: The main Python file containing the Flask application.
- `requirements.txt`: List of dependencies required for the project.

## Contributing

Contributions will not even be looked it. This is just for me.

## License

This project does not have a LICENSE. Feel free to use anything from this repo, although I doubt there is anything of value for anyone else. Thanks.
