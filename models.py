from db import db
import datetime


class Table1(db.Model):
    """定义数据模型"""
    __tablename__ = 'Table1'
    Id = db.Column(db.String(240), primary_key=True)
    Name = db.Column(db.String(80))
    Ops = db.Column(db.String(120))
    Time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    Check = db.Column(db.Boolean, nullable=True, default=None)
    def __init__(self, Id, Name, Ops, Time, Check):
        self.Id = Id
        self.Name = Name
        self.Ops = Ops
        self.Time = Time
        self.Check = Check
    def __repr__(self):
        return f'{self.Id} {self.Ops} {self.Time}'