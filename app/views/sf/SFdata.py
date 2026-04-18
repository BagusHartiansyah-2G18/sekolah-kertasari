from app.models import Informasi
import pandas as pd
from deep_translator import GoogleTranslator

import json

def dataFrameToJson(df):
    data_json = df.to_dict(orient='records')  # list of dicts
    return json.dumps(data_json) 

# Dinformasi(kategori=['tagline', 'alamat'])
# qs = qs.filter(kategori='tagline', judul='judul tertentu')

class Dinformasi:
    def __init__(self, kategori=None):
        # ambil data
        qs = Informasi.objects.all()
        if kategori:
            qs = qs.filter(kategori=kategori)

        if not qs.exists():
            self.dt = pd.DataFrame()
        else:
            self.dt = pd.DataFrame(qs.values(
                'id', 'judul', 'keterangan', 'kategori','gambar'
            ))

            # convert tanggal
            # if 'tgl_bayar' in self.dt.columns:
            #     self.dt['tgl_bayar'] = pd.to_datetime(self.dt['tgl_bayar'], errors='coerce')
            #     self.dt['periode'] = self.dt['tgl_bayar'].dt.to_period('M')

            # 🔥 translate (aman)
            # self.dt['judulE'] = self.dt['judul'].apply(self.translate_to_english)
            # self.dt['keteranganE'] = self.dt['keterangan'].apply(self.translate_to_english)

    # 🔥 fungsi translate (fix)
    def translate_to_english(self, text):
        try:
            if not text:
                return ""
            return GoogleTranslator(source='en', target='id').translate(text)
        except:
            return text  # fallback kalau error

    def get_by_kategori(self, kategori):
        return self.dt[self.dt['kategori'] == kategori]
        
        # return Informasi.objects.filter(kategori=kategori).values(
        #     'id', 'judul', 'kategori', 'keterangan','gambar'
        # )
    # def images(self):
    #     return  self.dt[self.dt['gambar'] !='']
    def images(self):
        kategori=['brandcontent', 'program']
        judul=None
        qs = Informasi.objects.all()

        # 🔥 filter kategori
        if kategori:
            if isinstance(kategori, str):
                kategori = [k.strip() for k in kategori.split(',')]
            qs = qs.filter(kategori__in=kategori)

        # 🔥 filter judul
        if judul:
            qs = qs.filter(judul=judul)

        data = list(qs.values(
            'id', 'judul', 'keterangan', 'kategori', 'gambar'
        ))

        return pd.DataFrame(data)

    def get_df(self):
        return self.dt

    def to_json(self):
        if self.dt.empty:
            return []
        return self.dt.to_dict(orient='records')
    def updKategori(self,id,kategori):
        data = Informasi.objects.get(id=id)
        data.kategori = kategori
        # data.judul = "Judul Baru"
        # data.keterangan = "Deskripsi baru"
        data.save() 
        # Informasi.objects.filter(kategori='faq').update(
        #     keterangan="FAQ sudah diperbarui"
        # )