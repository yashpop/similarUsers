from app import db

class UserInterests(db.Model):

    user_handle = db.Column(db.Integer,index=True)
    interest_tag = db.Column(db.String(64),index=True)
    date_followed = db.Column(db.)

    def __init__(self,user_handle,interest_tag,date_followed):
        self.user_handle =user_handle
        self.interest_tag = interest_tag
        self.date_followed = date_followed
