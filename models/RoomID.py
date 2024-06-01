#!/usr/bin/env python3
# by dongchao <cookie@maxcale.cn>


from sqlalchemy import Column,VARCHAR


class RoomID:
    __tablename__ = 'china_open_room_id'

    Name = Column("Name", VARCHAR(255), nullable=False, unique=False)
    CardNo = Column(VARCHAR(255), nullable=False, unique=False)
    Descriot = Column(VARCHAR(255), nullable=False, unique=False)
    CtfTp = Column(VARCHAR(255), nullable=False, unique=False)
    CtfId = Column(VARCHAR(255), nullable=False, unique=False)
    Gender = Column(VARCHAR(255), nullable=False, unique=False)
    Birthday = Column(VARCHAR(255), nullable=False, unique=False)
    Address = Column(VARCHAR(255), nullable=False, unique=False)
    Zip = Column(VARCHAR(255), nullable=False, unique=False)
    Dirty = Column(VARCHAR(255), nullable=False, unique=False)
    District1 = Column(VARCHAR(255), nullable=False, unique=False)
    District2 = Column(VARCHAR(255), nullable=False, unique=False)
    District3 = Column(VARCHAR(255), nullable=False, unique=False)
    District4 = Column(VARCHAR(255), nullable=False, unique=False)
    District5 = Column(VARCHAR(255), nullable=False, unique=False)
    District6 = Column(VARCHAR(255), nullable=False, unique=False)
    FirstNm = Column(VARCHAR(255), nullable=False, unique=False)
    LastNm = Column(VARCHAR(255), nullable=False, unique=False)
    Duty = Column(VARCHAR(255), nullable=False, unique=False)
    Mobile = Column(VARCHAR(255), nullable=False, unique=False)
    Tel = Column(VARCHAR(255), nullable=False, unique=False)
    Fax = Column(VARCHAR(255), nullable=False, unique=False)
    EMail = Column(VARCHAR(255), nullable=False, unique=False)
    Nation = Column(VARCHAR(255), nullable=False, unique=False)
    Taste = Column(VARCHAR(255), nullable=False, unique=False)
    Education = Column(VARCHAR(255), nullable=False, unique=False)
    Company = Column(VARCHAR(255), nullable=False, unique=False)
    CTel = Column(VARCHAR(255), nullable=False, unique=False)
    CAddress = Column(VARCHAR(255), nullable=False, unique=False)
    CZip = Column(VARCHAR(255), nullable=False, unique=False)
    Family = Column(VARCHAR(255), nullable=False, unique=False)
    Version = Column(VARCHAR(255), nullable=False, unique=False)

