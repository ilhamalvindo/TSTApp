from sqlalchemy import schema
from sqlalchemy.orm import Session

import models, schemas

jumlahOrang = 0

def add_data_pembayaran(db: Session, pembayaran : schemas.pembayaran):
    new_dataPembayaran = models.pembayaran(idBayar = pembayaran.idBayar, tanggal = pembayaran.tanggal, 
                                        metodePembayaran = pembayaran.metodePembayaran, totalHarga = pembayaran.totalHarga,
                                        idPesanan = pembayaran.idPesanan)
    db.add(new_dataPembayaran)
    db.commit()
    db.refresh(new_dataPembayaran)
    return new_dataPembayaran


def add_data_pesanan(db: Session, pesanan : schemas.pembayaran):
    new_dataPesanan = models.pesanan(idPelanggan = pesanan.idPelanggan, idCabang = pesanan.idCabang, totalHarga = pesanan.totalHarga,
                                    idPesanan = pesanan.idPesanan, tanggal = pesanan.tanggal)
    db.add(new_dataPesanan)
    db.commit()
    db.refresh(new_dataPesanan)
    return new_dataPesanan


def get_data_pembayaran(db: Session, Tanggal: str):
    return db.query(models.pembayaran).filter(models.pembayaran.tanggal == Tanggal).all()

def get_data_pesanan(db: Session, Tanggal: str):
    return db.query(models.pesanan).filter(models.pesanan.tanggal == Tanggal).all()


def get_data_pemasukan(db: Session, Tanggal: str):
    totalPemasukan = db.query(models.pesanan.totalHarga).filter(models.pesanan.tanggal == Tanggal).all()
    total = len(db.query(models.pesanan.totalHarga).filter(models.pesanan.tanggal == Tanggal).all())
    totalUangMasuk  = 0
    for idx in range(total):
        totalUangMasuk += totalPemasukan[idx]['totalHarga']
    # total2 = totalPemasukan[2]['totalHarga'] + totalPemasukan[1]['totalHarga']
    
    return "Total pemasukan pada " + str(Tanggal) + " adalah Rp" + str(totalUangMasuk)
