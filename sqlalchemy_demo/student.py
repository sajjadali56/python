from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

from sqlalchemy.sql import text


def add_column(engine, table_name, column, default=None):
    """Add a column to a table in the database.

    Args:
        engine (sqlalchemy.engine.Engine): The database engine.
        table_name (str): The name of the table to add the column to.
        column (sqlalchemy.sql.schema.Column): The column to add.
        default (str, optional): The default value for the column. Defaults to None.

    Returns:
        None
    """

    column_name = column.name
    column_type = column.type.compile(dialect=engine.dialect)
    query = text(
        f'ALTER TABLE {table_name} ADD COLUMN {column_name} {
            column_type} DEFAULT {default}'
    )

    # Use engine.connect() to execute the query
    with engine.connect() as connection:
        connection.execute(query)


engine = create_engine("sqlite:///database.db")

BASE = declarative_base()


class Student(BASE):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer, default=18)
    gender = Column(String(50), default="Male", name="gender")

    def __repr__(self):
        """Provide a helpful representation when printed."""
        return f"User(id={self.id!r}, name={self.name!r}, age={self.age!r}, gender={self.gender!r})"

    def __str__(self):
        return f"User(id={self.id!r}, name={self.name!r}, age={self.age!r}, gender={self.gender!r})"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
        }


BASE.metadata.create_all(engine)
