from typing import Optional, List
from flaskr import login_manager
import sqlalchemy.orm as so
from sqlalchemy import Boolean, String, Integer, ForeignKey
from datetime import datetime, timezone
from flaskr import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(userId):
    return db.session.get(User, int(userId))

class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True, autoincrement=True)
    full_name: so.Mapped[str] = so.mapped_column(String(75), default='blank')
    email: so.Mapped[str] = so.mapped_column(unique=True, index=True)
    email_verified: so.Mapped[Boolean] = so.mapped_column(Boolean(), default=False)
    password_hash: so.Mapped[str] = so.mapped_column(String(256))
    permission_level: so.Mapped[int] = so.mapped_column(Integer, default=0)
    created_at: so.Mapped[datetime] = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))

    tickets: so.Mapped[List["Ticket"]] = so.relationship(back_populates="owner") #owner is column defined in Ticket model

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return '<User {}>'.format(self.email)

class Ticket(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True, autoincrement=True)
    validated: so.Mapped[Boolean] = so.mapped_column(Boolean, default=False)
    created_at: so.Mapped[datetime] = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))
    comments: so.Mapped[Optional[str]] = so.mapped_column(String(300))

    owner: so.Mapped["User"] = so.relationship(back_populates="tickets") #tickets is column defined in User model
    owner_id: so.Mapped[int] = so.mapped_column(ForeignKey('user.id'))
