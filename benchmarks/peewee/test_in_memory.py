import os
import time
from random import choice, randrange, randint

from peewee import SqliteDatabase

from models import Journal

db = SqliteDatabase(":memory:")
try:
    db.drop_tables([Journal])
except Exception as e:
    print(f"Error dropping tables: {e}")

db.create_tables([Journal])
print("Database in use: in memory")

LEVEL_CHOICE = [10, 20, 30, 40, 50]
count = int(os.environ.get("ITERATIONS", "1000"))

# Test A
start = now = time.time()
for i in range(count):
    Journal(level=choice(LEVEL_CHOICE), text=f"Insert from A, item {i}").save()
now = time.time()

print(f"{count / (now - start): 10.2f}")

count = int(os.environ.get("ITERATIONS", "1000"))

# Test B
start = now = time.time()
with db.atomic():
    for i in range(count):
        Journal(level=choice(LEVEL_CHOICE), text=f"Insert from B, item {i}").save()
now = time.time()

print(f"{count / (now - start): 10.2f}")

# Test C
CHUNK_SIZE = 100
count = int(os.environ.get("ITERATIONS", "1000"))

# Work around peewee bulk-insert limitation that is total of 2000 values
test = int(os.environ.get("TEST", "1"))
if test == 3:
    CHUNK_SIZE = 50

chunks = count // CHUNK_SIZE
start = now = time.time()
for _ in range(chunks):
    Journal.insert_many(
        [(choice(LEVEL_CHOICE), f"Insert from C, item {i}") for i in range(CHUNK_SIZE)],
        [Journal.level, Journal.text],
    ).execute()
now = time.time()

print(f"{count / (now - start): 10.2f}")

# Test D
start = time.time()

count = 0

for _ in range(10):
    for level in LEVEL_CHOICE:
        res = list(Journal.select().where(Journal.level == level))
        count += len(res)

now = time.time()

print(f"{count / (now - start): 10.2f}")

# Test E
iters = int(os.environ.get("ITERATIONS", "1000"))
start = time.time()


count = 0

for _ in range(iters // 10):
    for level in LEVEL_CHOICE:
        res = list(
            Journal.select().where(Journal.level == level).limit(20).offset(randrange(iters - 20))
        )
        count += len(res)

now = time.time()

print(f"{count / (now - start): 10.2f}")

#Test F
count = int(os.environ.get("ITERATIONS", "1000"))
maxval = count - 1
count *= 2
start = time.time()


for _ in range(count):
    val = randint(1, maxval)
    Journal.get(Journal.id == val)

now = time.time()

print(f"{count / (now - start): 10.2f}")

# Test G
start = time.time()


count = 0

for _ in range(10):
    for level in LEVEL_CHOICE:
        res = list(Journal.select().where(Journal.level == level).dicts())
        count += len(res)

now = time.time()

print(f"{count / (now - start): 10.2f}")

# Test H
start = time.time()


count = 0

for _ in range(10):
    for level in LEVEL_CHOICE:
        res = list(Journal.select().where(Journal.level == level).tuples())
        count += len(res)

now = time.time()

print(f"{count / (now - start): 10.2f}")

# Test I
objs = list(Journal.select())
count = len(objs)

start = time.time()

with db.atomic():
    for obj in objs:
        obj.level = choice(LEVEL_CHOICE)
        obj.text = f"{obj.text} Update"
        obj.save()

now = time.time()

print(f"{count / (now - start): 10.2f}")

# Test J
objs = list(Journal.select())
count = len(objs)

start = time.time()

with db.atomic():
    for obj in objs:
        obj.level = choice(LEVEL_CHOICE)
        obj.save(only=["level"])

now = time.time()

print(f"{count / (now - start): 10.2f}")

# Test K
objs = list(Journal.select())
count = len(objs)

start = time.time()

with db.atomic():
    for obj in objs:
        obj.delete_instance()

now = time.time()

print(f"{count / (now - start): 10.2f}")

db.close()
