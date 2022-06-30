from datetime import datetime

from bcrypt import checkpw
from sqlalchemy import delete, or_, and_, update
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func
from sqlalchemy.exc import DataError
from app.database import models, schemas


def test(db: Session):
    pass
