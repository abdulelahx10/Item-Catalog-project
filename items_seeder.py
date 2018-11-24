from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, Item, User

engine = create_engine('sqlite:///catalogitems.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create dummy user
user1 = User(name="ex ex", email="ex@ex.com")
session.add(user1)
session.commit()

# Create Catagory
catagory1 = Category(name="Soccer")

session.add(catagory1)
session.commit()

# Create item
item1 = Item(title="ball", description="round object that is hit or thrown or kicked in soccer games",
             category_id=catagory1.id, user_id=user1.id)

session.add(item1)
session.commit()

# Create Catagory2
catagory2 = Category(name="BaseBall")

session.add(catagory2)
session.commit()

# Create item2
item2 = Item(title="Bat", description="A baseball bat is a smooth wooden or metal club used in the sport of baseball to hit the ball after it is thrown by the pitcher.",
             category_id=catagory2.id, user_id=user1.id)

session.add(item2)
session.commit()

#
catagory = Category(name="BasketBall")

session.add(catagory)
session.commit()

catagory = Category(name="Frisbee")

session.add(catagory)
session.commit()

catagory = Category(name="Snowboarding")

session.add(catagory)
session.commit()

catagory = Category(name="Rock Climbing")

session.add(catagory)
session.commit()

catagory = Category(name="FoosBall")

session.add(catagory)
session.commit()

catagory = Category(name="Skating")

session.add(catagory)
session.commit()

catagory = Category(name="Hockey")

session.add(catagory)
session.commit()


print("added menu items!")
