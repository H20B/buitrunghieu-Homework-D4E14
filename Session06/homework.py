import pymysql
from pymongo import MongoClient
# connect mongo
mongo_client = MongoClient()
mongo_database = mongo_client.get_database('cakes_ex')
mongo_collection = mongo_database.get_collection('cakes')
# connect mysql
client = pymysql.connect(
    host = "localhost",
    user = 'root',
    password = "buitrunghieu201199",
    cursorclass = pymysql.cursors.DictCursor)
database = client.cursor()
database.execute("CREATE DATABASE cakes")

database.execute('''
    CREATE TABLE `cakes`.cakes(
        id VARCHAR(255),
        type VARCHAR(255),
        name VARCHAR(255),
        ppu DECIMAL(10,2),
        PRIMARY KEY(id)
    )
''')
database.execute('''
    CREATE TABLE `cakes`.topping(
    id INT,
    type VARCHAR(255)
    PRIMARY KEY (type)
    )
''')

database.execute('''
    CREATE TABLE `cakes`.batter(
    id INT,
    type VARCHAR(255)
    PRIMARY KEY (type)
    )
''')

database.execute('''
    CREATE TABLE `cakes`.filling(
    id INT,
    type VARCHAR(255)
    PRIMARY KEY (type)
    )
''')

database.execute('''
    CREATE TABLE `cakes`.cake_batter(
    cake_id VARCHAR(255)
    batter_id INT
    PRIMARY KEY (cake_id, batter_id)
    )
''')

database.execute('''
    CREATE TABLE `cakes`.cake_topping(
    cake_id VARCHAR(255)
    topping_id VARCHAR(255)
    PRIMARY KEY (cake_id, topping_id)
    )
''')

database.execute('''
    CREATE TABLE `cakes`.cake_filling(
    cake_id VARCHAR(255)
    filling_id VARCHAR(255)
    PRIMARY KEY (cake_id, filling_id)
    )
''')


query = {
    'type':{'$ne':None},
    'name':{'$ne':None},
    'ppu':{'$ne':None},
    'batter':{'$ne':None},
    'filling':{'$ne':None},
    'topping':{'$ne':None},
}

cakes_database = mongo_collection.find({})
for cake in cakes_database:
                                   # Transform    
    cake_id = str(cake['_id'])
                                    #load
    database.execute(f'''
        INSERT INTO `cakes`.cake(`id`, `type`, `name`, `ppu`)
        VALUES("{cake_id}", "{cake['type']}",  "{cake['name']}",  "{cake['ppu']}")
    ''')


# Topping table

query = [
  {
    '$unwind':'$topping'
  },
  {
    '$group':{
      '_id':'$topping'
    }
  }
]

topping_database = mongo_collection.aggregate(query)

for topping in topping_database:
    database.execute(f'''
        INSERT INTO `cakes`.topping(`type`)
        VALUES("{topping['_id']}")
    ''')
# Cake_topping table
query = [
  {
    '$unwind':'$topping'
  }
]

cake_topping_database = mongo_collection.aggregate(query)

for cake_topping in cake_topping_database:
    cake_topping_id = str(cake_topping["_id"])
    database.execute(f'''
        INSERT INTO `cakes`.cake_topping(`cake_id`,`topping_id`)
        VALUES("{cake_topping_id}")
    ''')

# Batter Table
query = [
  {
    '$unwind':'$batter'
  },
  {
    '$group':{
      '_id':'$batter'
    }
  }
]
batter_database = mongo_collection.aggregate(query)
for batter in batter_database:
    database.execute(f'''
        INSERT INTO `cakes`.batter(`type`)
        VALUES("{topping['_id']}")
    ''')


# Cake_batter table 

query = [
  {
    '$unwind':'$batter'
  }
]
cake_batter_database = mongo_collection.aggregate(query)

for cake_batter in cake_batter_database:
    cake_batter_id = str(cake_batter["_id"])
    database.execute(f'''
        INSERT INTO `cakes`.cake_batter(`cake_id`,`batter_id`)
        VALUES("{cake_batter_id}")
    ''')

#Filling table
query = [
  {
    '$unwind':'$filling'
  },
  {
    '$group':{
      '_id':'$filling'
    }
  }
]
batter_database = mongo_collection.aggregate(query)
for batter in batter_database:
    database.execute(f'''
        INSERT INTO `cakes`.filling(`type`)
        VALUES("{filling['_id']}")
    ''')

# Cake_filling table
query = [
  {
    '$unwind':'$filling'
  }
]
cake_filling_database = mongo_collection.aggregate(query)

for cake_filling in cake_filling_database:
    cake_filling_id = str(cake_filling["_id"])
    database.execute(f'''
        INSERT INTO `cakes`.cake_filling(`cake_id`,`batter_id`)
        VALUES("{cake_batter_id}")
    ''')

client.commit()    
