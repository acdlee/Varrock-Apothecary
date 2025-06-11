<p align="center">
  <img src="https://github.com/user-attachments/assets/7a06cd8b-1f82-4456-97c7-e6e8246e55c0" alt="wbg1t12osrf81" width="400"/>
</p>

<div align="center">
  <h1>Varrock Apothecary</h1>
  <strong>CLI interface powered by Questionary, FastAPI, and SQLite3</strong>
</div>

## About
The <strong>Varrock Apothecary</strong> is an interactive storefront inspired from a store
from the game Old School Runescape. The final version of this project will include an interactive CLI with Questionary,
FastAPI backend handling API requests, and SQLite3 for data storage.

## Features
- Interactive CLI for navigating the storefront
- RESTful FastAPI backend handling CRUD operations
- Persistent, idempotent database with SQLite3
- Inspired by OSRS lore for a fun, nostalgic experience

## Installation
1. Clone this repository:
```bash
git clone https://github.com/acdlee/Varrock-Apothecary.git
cd Varrock-Apothecary
```
2. Create and activate a virtual environment:
```bash
python -m venv .va-venv
source .va-venv/Scripts/activate # On Linux: source .va-venv/bin/activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
<strong>Frontend-Backend currently unconnected</strong>
1. Setup the database by navigating to '/backend/app/ and running:
```python
python ./database.py
```
2. Run the server by navigating to /backend/ and running:
```python
uvicorn main:app --reload
```
3. Run the frontend by navigating to /frontend/ and running:
```python
python ./store.py
```

## Screenshots

## Contributing & Contact
Open issues or submit pull requests; reach out on GitHub.
