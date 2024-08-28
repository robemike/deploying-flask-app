from app import app
from models import db, Bird 

with app.app_context():

    print('Deleting the existing Birds in the Database...')
    Bird.query.delete()

    print('Creating nes Birds for the Database...')
    chickadee = Bird(name='Black-Capped Chickadee', species='Poecile Atricapillus')
    grackle = Bird(name='Grackle', species='Quiscalus Quiscula')
    starling = Bird(name='Common Starling', species='Sturnus Vulgaris')
    dove = Bird(name='Mourning Dove', species='Zenaida Macroura')

    print('Adding Bird objects to Transaction')
    db.session.add_all([chickadee, grackle, starling, dove])

    print('Commiting Transaction...')
    db.session.commit()

    print('All Birds have been added to the database.')