import sqlite3
import json

class DB:
    '''
    Databse class for the Apothecary Project.
    '''
    def __init__(self):
        self._DB_PATH = "apoth_database.db"
        self._table_names = ["ingredients", "herbs", "potions"]
                
        self.init_database()

    def get_connection(self):
        conn = sqlite3.connect(self._DB_PATH)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        return conn
        
    def fetch_all_rows(self, table_name='herbs'):
        if table_name not in self._table_names: return []
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        items = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return items

    def init_database(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        # Create the ingredients table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ingredients (
                ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                quantity INTEGER DEFAULT 100
            )
        ''')

        # Create the herbs table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS herbs (
                herb_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                quantity INTEGER DEFAULT 100
            )
        ''')
        
        # Create the potions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS potions (
                potion_id INTEGER PRIMARY KEY AUTOINCREMENT,
                ingredient_id INTEGER NOT NULL,
                herb_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                effect TEXT NOT NULL,
                quantity INTEGER DEFAULT 100,
                FOREIGN KEY (ingredient_id) REFERENCES ingredients(ingredient_id)
                FOREIGN KEY (herb_id) REFERENCES herbs(herb_id)
            )        
        ''')
        
        conn.close()
        
    def seed_db(self):
        with open("seed.json", 'r') as f:
            potions_data = json.load(f)
        
        conn = self.get_connection()
        cursor = conn.cursor()
        
        for potion in potions_data:
            # Add the herb
            herb_name = potion.get("herb")
            cursor.execute("SELECT herb_id FROM herbs WHERE name = ?", (herb_name,))
            herb_row = cursor.fetchone()
            
            if herb_row:
                herb_id = herb_row[0]
            else:
                cursor.execute("INSERT INTO herbs (name) VALUES (?)", (herb_name,))
                herb_id = cursor.lastrowid
        
            # Add the ingredient
            ingredient_name = potion.get("ingredient")
            cursor.execute("SELECT ingredient_id FROM ingredients WHERE name = ?", (ingredient_name,))
            ingredient_row = cursor.fetchone()
            
            if ingredient_row:
                ingredient_id = ingredient_row[0]
            else:
                cursor.execute("INSERT INTO ingredients (name) VALUES (?)", (ingredient_name,))
                ingredient_id = cursor.lastrowid
            
            # Add the potion
            potion_name = potion.get("name")
            potion_effect = potion.get("effect")
            
            cursor.execute("SELECT potion_id FROM potions WHERE name = ?", (potion_name,))
            potion_row = cursor.fetchone()
            
            if not potion_row:
                cursor.execute('''
                    INSERT INTO potions (ingredient_id, herb_id, name, effect) VALUES (?, ?, ?, ?)
                ''', (ingredient_id, herb_id, potion_name, potion_effect))
                
            conn.commit()
        
        conn.close()
        
if __name__ == "__main__":
    db = DB()
    db.seed_db()