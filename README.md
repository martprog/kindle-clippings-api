# Kindle Clippings API

This API allows querying Kindle clippings by author or book.

## Routes

- **All Clippings:**
  - Endpoint: `/api/all`

- **Clippings by Author:**
  - Endpoint: `/api/author?name=...`

- **Clippings by Book:**
  - Endpoint: `/api/book?name=...`

## Getting Started

Follow these steps to set up and run the Kindle Clippings API:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/martprog/kindle-clippings-api.git
    cd kindle-clippings-api
    ```

2. **Setting Up Virtual Environment and Installing Dependencies:**
    - For Unix/Linux:
        ```bash
        python -m venv env
        source env/bin/activate
        pip install -r requirements.txt
        ```

    - For Windows:
        ```bash
        python -m venv env
        .\env\Scripts\activate
        pip install -r requirements.txt
        ```

3. **Run the API:**
    ```bash
    python run.py
    ```

## Usage

- Use the provided routes to query Kindle clippings based on author or book.
