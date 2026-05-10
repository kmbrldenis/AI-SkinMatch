from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

DATABASE_URL = "postgresql://postgres:12345678@localhost/ai_skinmatch"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class UserData (Base):

    __tablename__ = "user_data"

    id = Column(Integer, primary_key = True, index = True)
    email = Column(String (255), unique = True, index = True)
    hash_password = Column(String (255), nullable = False)
    skin_type = Column(String (50))
    sens_level = Column(String (50))
    budget_range = Column(String (50))

class Product (Base):

    __tablename__ = "products"

    product_id = Column(Integer, primary_key = True, index = True)
    name = Column(String (255), unique = True, index = True)
    category = Column(String (50))
    price = Column(DECIMAL (10, 2))

class Ingredients (Base):

    __tablename__ = "ingredients"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String (255), unique = True, index = True)
    comedogenic_grade = Column(Integer)
    irritation_grade = Column(Integer)

class ProductIngredient(Base):
    __tablename__ = "product_ingredients"

    product_id = Column(Integer, ForeignKey("products.product_id"), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"), primary_key=True)
