from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        results = connectToMySQL('dojos_ninjas_schema').query_db(query, data)
        return results
    
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_ninjas_schema').query_db(query)
        dojos = []
        for one_dojo in results:
            dojos.append(cls(one_dojo))
        return dojos
    
    @classmethod 
    def get_dojos_with_ninjas(cls):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojos_id;"
        results = connectToMySQL('dojos_ninjas_schema').query_db(query)
        dojos = []
        for row in results:
            dojo = cls(row) 
            ninja_data = {
                "id":row['ninjas.id'],
                "first_name":row['first_name'],
                "last_name":row['last_name'],
                "age":row['age'],
                "created_at":row['ninjas.created_at'],
                "updated_at":row['ninjas.updated_at']
            }
            dojo.ninjas = (ninja.Ninja(ninja_data))
            dojos.append(dojo) 
        return dojos   

    @classmethod
    def get_dojo(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos_id = dojos.id WHERE dojos.id = %(dojos_id)s;"
        results = connectToMySQL('dojos_ninjas_schema').query_db(query, data)
        dojo = cls(results[0])
        for row in results:
            ninja_data = {
                "id":row['ninjas.id'],
                "first_name":row['first_name'],
                "last_name":row['last_name'],
                "age":row['age'],
                "created_at":row['ninjas.created_at'],
                "updated_at":row['ninjas.updated_at']
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo


    #@classmethod
    #def save(cls, data):
        #query = "INSERT INTO restaurants (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW())"
        #return connectToMySQL('dojos_ninjas_schema').query_db(query, data)
    
    #@classmethod 
    #def get_dojo_with_ninjas(cls, data):
        #query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s"
        #results = connectToMySQL('dojos_ninjas_schema').query_db(query, data)
        #dojo = cls(results[0])
        #for row_from_db in results:
            #ninja_data = {
                #"id":row_from_db['ninjas.id'],
                #"first_name":row_from_db['ninjas.first_name'],
                #"last_name":row_from_db['ninjas.last_name'],
                #"age":row_from_db['ninjas.age'],
                #"created_at":row_from_db['ninjas.created_at'],
                #"updated_at":row_from_db['ninjas.updated_at']
            #}
            #dojo.ninjas.append(ninja.Ninja(ninja_data))