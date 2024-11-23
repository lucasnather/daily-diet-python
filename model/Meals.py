from config.database import db
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime 

class Meals(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    datetime: Mapped[datetime] =  mapped_column(default=datetime.now(), nullable=False)
    isOnDiet: Mapped[bool] = mapped_column(nullable=False)