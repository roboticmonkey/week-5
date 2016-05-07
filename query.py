"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
db.session.query(Brand).get(8)
# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter( (Model.name == 'Corvette') & (Model.brand_name == 'Chevrolet')).all()
# Get all models that are older than 1960.
Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()
# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like( 'Cor%')).all()
# Get all brands that were founded in 1903 and that are not yet discontinued.
Brand.query.filter((Brand.founded == 1903)& (Brand.discontinued == None)).all()
# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.
Brand.query.filter((Brand.founded < 1950)| (Brand.discontinued != None)).all()

# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name !='Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''
    models = Model.query.options(db.joinedload(brand)).all()

    for model in models:
        if model.year == year:
            if model.brand is not None:
                
                print "Brand name: %s, Model Name: %s, Headquarters: %s" % (
                                                        model.brand_name,
                                                        model.name,
                                                        model.headquarters)
            else:
                print "Brand name: %s, Model Name: %s, --" % (
                                                        model.brand_name,
                                                        model.name)



def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    models = Model.query.all()

    for model in models:
        print model.name, model.brand_name

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# the data type is a flask-sqlaclhemy baseQuery type object
# the value is, i dont know. if you exicute the query you get the brand object
# that the query returns. but if you dont exicute the query then you are just
# getting the memory location of the query object you created. I am not sure what
# answer you are looking for as I am not sure I understand the question.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
# an association table manages a many to many relationship. Ie. in the example
# given in the lecture. a book can have many genres and a genre can have many 
# books. therefore you put an association table "between" the book and genre
# tables to keep track of just book_ids and genre_ids that match. 
# association tables just hold ids. 

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    #I dont get it. I have tried looking at the notes, flask-sqlalchemy docs,
    # sqlalchemy docs and I have not been able to find out what i am doing wrong
    # I have no idea how to get the .like() to work with a variable.

    #i seemed to have figured it out
    
    brands = Brand.query.filter((Brand.name.like('%'+mystr+'%'))|(Brand.name == mystr)).all()
    
    return brands


def get_models_between(start_year, end_year):
    models = Model.query.filter((Model.year >= start_year) & (Model.year < end_year)).all()

    return models
    
