from config.database import db
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime 

class Meals(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    datetime: Mapped[datetime] =  mapped_column(default=datetime.now())
    isOnDiet: Mapped[bool] = mapped_column()