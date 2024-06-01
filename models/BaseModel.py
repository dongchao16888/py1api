#!/usr/bin/env python3
# by dongchao <cookie@maxcale.cn>


from sqlalchemy import VARCHAR, Column, Integer, TIMESTAMP, CHAR, text


class BaseModel:
    __abstract__ = True
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    valid = Column(CHAR(1), server_default='1')
    description = Column(VARCHAR(255), nullable=True, unique=False)
    created_at = Column(TIMESTAMP(True), server_default=text('CURRENT_TIMESTAMP'), doc='创建时间')
    updated_at = Column(TIMESTAMP(True), server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), doc='更新时间')

