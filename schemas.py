from typing import List, Optional

from pydantic import BaseModel


class pembayaran(BaseModel):
    idBayar : str
    tanggal : str
    MetodePembayaran : str
    TotalHarga : int
    idPesanan : str
    idPelanggan : str
    idCabang : str


# class pesanan(BaseModel):
#     idPelanggan : str
#     idCabang : str

