from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class pembayaran(Base):
    __tablename__ = "pembayaran"

    idBayar = Column(String, primary_key=True)
    tanggal = Column(String)
    MetodePembayaran = Column(String)
    TotalHarga = Column(Integer)
    idPesanan = Column(String)


class pesanan(Base):
    __tablename__ = "pesanan"

    idPesanan = Column(String, primary_key=True)
    tanggal = Column(String)
    idPelanggan = Column(String, unique=True)
    idCabang = Column(String)
    totalHarga = Column(Integer)


