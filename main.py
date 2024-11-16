import tkinter as tk
import random
import datetime

class KelimeTahminApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kelime Tahmin Oyunu")

        self.kelimelerListesi = ["apaçık", "güpegündüz", "sırılsıklam", "çepeçevre", "darmaduman", "karmakarışık"]
        self.soruSirasi = 1
        self.toplamPuan = 0

        self.soru_label = tk.Label(root, text="Karışık Kelime: ", font=("Helvetica", 16))
        self.soru_label.pack(pady=10)

        self.karisik_kelime_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.karisik_kelime_label.pack(pady=10)

        self.cevap_entry = tk.Entry(root, font=("Helvetica", 16))
        self.cevap_entry.pack(pady=10)

        self.sonuc_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.sonuc_label.pack(pady=10)

        self.devam_button = tk.Button(root, text="Cevapla", command=self.cevapla, font=("Helvetica", 16))
        self.devam_button.pack(pady=10)

        self.devamEt_button = tk.Button(root, text="Devam Et", command=self.devam_et, font=("Helvetica", 16), state="disabled")
        self.devamEt_button.pack(pady=10)

        self.bitir_button = tk.Button(root, text="Bitir", command=self.bitir, font=("Helvetica", 16), state="disabled")
        self.bitir_button.pack(pady=10)

        self.yeniden_basla_button = tk.Button(root, text="Yeniden Başla", command=self.yeniden_basla, font=("Helvetica", 16))
        self.yeniden_basla_button.pack(pady=10)
        self.yeniden_basla_button.pack_forget()

        self.sonraki_soru()

    def sonraki_soru(self):
        if self.soruSirasi > len(self.kelimelerListesi):
            self.soru_label.config(text="Oyun Bitti! Toplam Puanınız: " + str(self.toplamPuan))
            self.karisik_kelime_label.config(text="")
            self.cevap_entry.config(state="disabled")
            self.devam_button.config(state="disabled")
            self.devamEt_button.config(state="disabled")
            self.bitir_button.config(state="disabled")
            self.yeniden_basla_button.pack()
            return

        self.anahtar = self.kelimelerListesi[self.soruSirasi - 1]
        self.karisikKelime = ''.join(random.sample(self.anahtar, len(self.anahtar)))

        self.soru_label.config(text=f"Toplam süre: 20sn\nSoru No: {self.soruSirasi}")
        self.karisik_kelime_label.config(text=self.karisikKelime)
        self.cevap_entry.delete(0, tk.END)
        self.cevap_entry.config(state="normal")
        self.devam_button.config(state="normal")
        self.devamEt_button.config(state="disabled")
        self.bitir_button.config(state="disabled")

        self.baslangicZamani = datetime.datetime.now()

    def cevapla(self):
        cevap = self.cevap_entry.get()
        bitisZamani = datetime.datetime.now()
        fark = bitisZamani - self.baslangicZamani

        if fark.seconds > 20:
            self.sonuc_label.config(text=f"Maalesef süreniz doldu. Kullandığınız süre: {fark.seconds} saniye\nToplam puan: {self.toplamPuan}")
        elif cevap == self.anahtar:
            self.toplamPuan += 1
            self.sonuc_label.config(text=f"Tebrikler doğru bildiniz.\nAktif soru puanı: 1\nToplam puan: {self.toplamPuan}\nKullandığınız süre: {fark.seconds} saniye")
        else:
            self.sonuc_label.config(text=f"Üzgünüz yanlış cevap. Doğru cevap: {self.anahtar}\nKullandığınız süre: {fark.seconds} saniye\nToplam puan: {self.toplamPuan}")

        self.soruSirasi += 1
        self.cevap_entry.config(state="disabled")
        self.devam_button.config(state="disabled")
        self.devamEt_button.config(state="normal")
        self.bitir_button.config(state="normal")

    def devam_et(self):
        self.sonuc_label.config(text="")
        self.sonraki_soru()

    def bitir(self):
        self.soru_label.config(text=f"Oyun Bitti! Toplam Puanınız: {self.toplamPuan}")
        self.karisik_kelime_label.config(text="")
        self.cevap_entry.config(state="disabled")
        self.devam_button.config(state="disabled")
        self.devamEt_button.config(state="disabled")
        self.bitir_button.config(state="disabled")
        self.yeniden_basla_button.pack()

    def yeniden_basla(self):
        self.soruSirasi = 1
        self.toplamPuan = 0
        self.yeniden_basla_button.pack_forget()
        self.sonraki_soru()

root = tk.Tk()
app = KelimeTahminApp(root)
root.mainloop()
