import datetime
from vj4 import db
from vj4.util import argmethod


async def add(ip: str):
  coll = db.coll('blacklist')
  expire_at = datetime.datetime.utcnow() + datetime.timedelta(days=365)
  await coll.insert_one({'_id': ip, 'expire_at': expire_at})


async def query(ip: str):
  coll = db.coll('blacklist')
  return await coll.find_one({'_id': ip})


@argmethod.wrap
async def ensure_indexes():
  coll = db.coll('blacklist')
  await coll.create_index('expire_at', expireAfterSeconds=0)


if __name__ == '__main__':
  argmethod.invoke_by_args()