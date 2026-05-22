from typing import Optional
from sqlalchemy import select
from sqlalchemy.orm import Session
from database.models import User
from database.database import sql_engine


def get_by_spotify_id(spotify_id: str) -> Optional[User]:
    with Session(sql_engine) as session:
        return session.execute(select(User).where(User.spotify_id == spotify_id)).scalars().first()


def update_user(spotify_id: str, name: str, image_url: Optional[str]) -> User:
    with Session(sql_engine) as session:
        user: Optional[User] = session.execute(select(User).where(User.spotify_id == spotify_id)).scalars().first()

        if not user:
            user: User = User(
                spotify_id=spotify_id,
                name=name,
                image_url=image_url
            )

            session.add(user)
        else:
            user.name = name
            user.image_url = image_url

        session.commit()

        session.refresh(user)

        return user
