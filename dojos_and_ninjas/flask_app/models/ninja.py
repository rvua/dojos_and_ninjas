from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas (dojos_id, first_name, last_name, age, created_at, updated_at) VALUES (%(dojos_id)s, %(first_name)s, %(last_name)s, %(age)s, NOW(), NOW());"
        results = connectToMySQL('dojos_ninjas_schema').query_db(query, data)
        return results
    #@classmethod
    #def save(cls, data):
        #query = "INSERT INTO dojos (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW())"
        #return connectToMySQL('dojos_ninjas_schema').query_db(query, data)
