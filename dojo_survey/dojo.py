from flask import flash
from mysqlconection import connectToMySQL

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos (name, location, language, comment) VALUES ( %(name)s , %(location)s , %(language)s, %(comment)s);"
        return connectToMySQL('dojo_survey_schema').query_db( query, data )
    
    @classmethod
    def show_last_user(cls):
        query = "SELECT * FROM dojos ORDER BY created_at DESC LIMIT 1 "
        results = connectToMySQL('dojo_survey_schema').query_db( query)
        return (results[0])
    
    @staticmethod
    def validate_dojo(dojo):
        is_valid = True # we assume this is true
        if len(dojo['name']) < 1:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if (dojo['location'] == "Choose a location"):
            flash("You must choose a location.")
            is_valid = False
        if (dojo['language'] == "Choose a language"):
            flash("You must choose a language.")
            is_valid = False
        if len(dojo['comment']) < 10:
            flash("Your comment must be at least 10 characters.")
            is_valid = False
        return is_valid