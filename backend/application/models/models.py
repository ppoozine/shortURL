import sqlalchemy
from ..database import metadata

UrlModel = sqlalchemy.Table(
    "url",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("old_url", sqlalchemy.Text),
    sqlalchemy.Column("new_url", sqlalchemy.Text),
)