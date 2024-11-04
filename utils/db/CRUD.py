from aiogram import types

from .models import *
from . import s


def craete_user(user_id, is_user=True):
    db = s()
    try:

        user = db.query(User).where(User.user_id == user_id).first()
        if user:
            return False
        user = User()
        user.user_id = user_id
        user.is_user = is_user
        db.add(user)
        db.commit()
        return True
    except:
        db.rollback()
    finally:
        db.close()

def update_user(user_id, user_name=None, full_name=None, is_user=True):
    db = s()
    try:

        user = db.query(User).where(User.user_id == user_id).first()
        if not user:
            return False
        user.user_name = user_name
        user.full_name = u"{full_name}".format(full_name=full_name).encode('unicode_escape')
        user.is_user = is_user
        db.commit()
        return True
    except:
        db.rollback()
    finally:
        db.close()

def get_user(user_id=None, all=None):
    db = s()
    try:

        if all:
            users = db.query(User).where(User.is_user == True).all()
            return users
        user = db.query(User).where(User.user_id == user_id).first()
        if not user:
            return False
        return user
    except:
        db.rollback()
    finally:
        db.close()
