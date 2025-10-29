from database import *


engine = new_engine()
metadata = get_metadata()

metadata.create_all(engine)
