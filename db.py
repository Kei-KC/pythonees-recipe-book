import pymysql as sql
import pymysql.cursors
conn = sql.connect(host='127.0.0.1',
                   user='root',
                   password='',
                   db='Recipe_Book',
                   unix_socket='/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock',
                   charset='utf8mb4',
                   cursorclass=pymysql.cursors.DictCursor)

def search_recipe(name=None):
    cursor = conn.cursor()
    if name:  
        query = """ select * from recipe where name = %s
            """
        cursor.execute(query, (name))
        data = cursor.fetchall()
        cursor.close()
        return data['name'], data['description'], data['ingredients']
    else:
        query = """ select * from recipe
            """
        cursor.execute(query)
        data = cursor.fetchall()
        name = []
        desc = []
        ing = []
        for line in data:
            n, d, i = data['name'], data['description'], data['ingredients']
            name.append(n)
            desc.append(d)
            ing.append(i)
        cursor.close()
        return name,desc, ing
    
def create_recipe(name, description, ingredients, steps):
    i = 0
    cursor = conn.cursor()
    query = """ INSERT INTO `recipe` (`name`, `description`, `ingredients`) VALUES (%s, %s, %s)
        """
    cursor.execute(query, (name, description, ingredients))
    query_steps = """INSERT INTO `instructions` (`step_number`, `name`, `instruction`) VALUES (%s, %s, %s)"""
    for step in steps:
        i+=1
        cursor.execute(query_steps, (i, name, step))
    conn.commit()
    cursor.close()
   
def view_instructions(name):
    cursor = conn.cursor()
    query = """select * from recipe where name = %s
    """
    cursor.execute(query, (name))
    data = cursor.fetchall()
    if not data:
        print(f"No recipe found with name {name}")
        return
    query_instructions = """SELECT * FROM `instructions` WHERE name = %s order by step_number ASC
    """
    cursor.execute(query_instructions, (name))
    data = cursor.fetchall()
    instructions = []
    for instruction in data:
        instructions.append(instruction['instruction'])
    return instructions 

def export_db():
    
        
    
    

    
