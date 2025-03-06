# Data Collection System RESTful API

## Use the following steps to set up the project locally.

Clone the repository:

```bash
git clone https://github.com/Jerez-M/data_collection_backend.git
cd data_collection_backend
```

Set up a virtual environment:

```bash
python -m venv env
env/Scripts/activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Set up database:

    Use the sqlite3 db which already contains the test data.
    
Run migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

Access api on [http://127.0.0.1:8000/swagger/]
