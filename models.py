from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Date

from database import Base

class pembayaran(Base):
    __tablename__ = "pembayaran"

    idBayar = Column(Integer, primary_key=True)
    tanggal = Column(Date)
    metodePembayaran = Column(String)
    totalHarga = Column(Integer)
    idPesanan = Column(Integer)


class pesanan(Base):
    __tablename__ = "pesanan"

    idPesanan = Column(Integer, primary_key=True)
    tanggal = Column(Date)
    idPelanggan = Column(Integer, unique=True)
    idCabang = Column(Integer)
    totalHarga = Column(Integer)


