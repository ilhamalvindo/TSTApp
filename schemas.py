from typing import List, Optional

from pydantic import BaseModel


class pembayaran(BaseModel):
    idBayar : int
    tanggal : str
    metodePembayaran : str
    totalHarga : int
    idPesanan : int
    idPelanggan : int
    idCabang : int


# class pesanan(BaseModel):
#     idPelanggan : str
#     idCabang : str

