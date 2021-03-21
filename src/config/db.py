import dataset
from decouple import config
con_str = config('DATABASE_URL', "")
assert con_str
# print(con_str)
db = dataset.connect(con_str)
assert db.tables
print(db.tables)