from typing import List

from fastapi import Depends, FastAPI
from pydantic import errors
from pydantic.schema import schema
from sqlalchemy.orm import Session


import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Input Data Pemasukan pada saat pembayaran menu makanan
@app.post("/postDataPembayaran/")
async def input_data_pembayaran(pembayaran : schemas.pembayaran, db: Session = Depends(get_db)):
    # try:
    addDataPesanan = crud.add_data_pesanan(db, pembayaran)
    addDataPembayaran = crud.add_data_pembayaran(db, pembayaran)
    if (addDataPembayaran == None):
        return "Adding data to database error!"
    return addDataPembayaran
    # except: 
    #     return "Error adding to database, data already exist. idPesanan, idPelanggan, and idBayar should be unique"

@app.post("/homepage")
async def get_homepage():
    return "Homepage"
# @app.post("/dataPesanan/")
# async def input_data_pesanan(pesanan : schemas.pesanan, db: Session = Depends(get_db)):
#     addDataPesanan = crud.add_data_pesanan(db, pesanan)
#     return addDataPesanan

@app.get("/getDataPembayaran/")
async def get_data_pembayaran(tanggal: str, db: Session = Depends(get_db)):
    getDataPembayaran = crud.get_data_pembayaran(db, tanggal)
    if (getDataPembayaran == []):
        return "No data available" 
    return getDataPembayaran

@app.get("/getDataPesanan/")
async def get_data_pesanan(tanggal: str, db: Session = Depends(get_db)):
    getDataPesanan = crud.get_data_pesanan(db, tanggal)
    if (getDataPesanan == []):
        return "No data available"
    return getDataPesanan
    
@app.get("/getDataPemasukan")
async def get_data_pemasukan(tanggal: str, db: Session = Depends(get_db)):
    getDataPemasukan = crud.get_data_pemasukan(db, tanggal)
    if (getDataPemasukan == []):
        return "No data available"
    return getDataPemasukan
    
    
    

