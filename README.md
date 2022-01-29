# Python-Developer-Technical-task-at-disco

Python software that contains two features (Movie filter - Json parser)

## First Method : using the cmd :--

### Feature 1: Search for a movie in a csv
#### How to run the program in the cmd
```python
python moviefilter.py "Movie-Dataset-Latest (1).zip"
```
- User asked to enter the filtering parameters
- If user doesn't need this parameter just press enter

### Feature 2: parsing files to Json format
#### How to run the program
```python
python jsonparser.py type input_path output_path
python jsonparser.py csv "Movie-Dataset-Latest (1).csv" "output.json"
```

## Second Method : using Django Framework and TestCase :--

### Both features in the same project but two different apps
#### 1) Create virtual environment :

    ```python
        python -m venv env
    ```

#### 2) Activate virtual environment :
    ```python
        .\env\Scripts\activate
    ```

#### 3) Install requirements :
    ```python
        pip install -r requirements.txt
    ```

#### 4) migration(optional) :
    ```python
        python manage.py makemigrations
        python manage.py migrate
    ```

#### 5) Run the test cases :
    ```python
        python manage.py test
    ```

#### 5) Run the server :
    ```python
        python manage.py runserver
    ```
