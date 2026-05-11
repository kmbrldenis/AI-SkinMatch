from dbs import engine, Base
from services.reccomendation_engine import recommend_products

Base.metadata.create_all(bind=engine)

