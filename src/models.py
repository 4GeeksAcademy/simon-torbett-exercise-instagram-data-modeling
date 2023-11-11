import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    posts = relationship('Post', back_populates='user')
    comments = relationship('Comment', back_populates='user')
    stories = relationship('Story', back_populates='user')

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    caption = Column(String)
    image_url = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='posts')
    comments = relationship('Comment', back_populates='post')
    views = Column(Integer, default=0)

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    user = relationship('User', back_populates='comments')
    post = relationship('Post', back_populates='comments')

class Story(Base):
    __tablename__ = 'stories'
    id = Column(Integer, primary_key=True)
    image_url = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='stories')

    def to_dict(self):
        return {}

# Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e
