import aiosqlite
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'db.db')

class Database:
    _instance = None

    def __new__(cls, db_path: str = None):
        if not cls._instance:
            if db_path is None:
                raise ValueError("���������� ������� ���� � ���� ������ ��� ������ �������� ����������.")
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._db_path = db_path
            cls._instance._connection = None
        return cls._instance

    async def connect(self):
        """����������� � ���� ������."""
        if not self._connection:
            self._connection = await aiosqlite.connect(self._db_path)
            await self._connection.execute("PRAGMA foreign_keys = ON;")
            await self._connection.commit()

    async def close(self):
        """�������� ���������� � ����� ������."""
        if self._connection:
            await self._connection.close()
            self._connection = None

    async def execute(self, query: str, parameters: tuple = ()):
        """���������� �������� INSERT, UPDATE, DELETE."""
        await self.connect()
        async with self._connection.execute(query, parameters) as cursor:
            await self._connection.commit()
            return cursor

    async def fetch_one(self, query: str, parameters: tuple = ()):
        """��������� ����� ������ �� ���� ������."""
        await self.connect()
        async with self._connection.execute(query, parameters) as cursor:
            row = await cursor.fetchone()
            return row

    async def fetch_all(self, query: str, parameters: tuple = ()):
        """��������� ���� ������� �� �������."""
        await self.connect()
        async with self._connection.execute(query, parameters) as cursor:
            rows = await cursor.fetchall()
            return rows

db = Database(DB_PATH)