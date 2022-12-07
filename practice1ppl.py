class  siswa:
    def __init__(self, nama):
        self.nama = nama

perkenalan = siswa('Euroski')

print(f'siswa Kami Bernama {perkenalan.nama} Ganteng')

class guru:
    def __init__(self, nama):
        self.nama = nama

class guruotkp:
    def __ini__(self, nama, cantik):
        super().__init__()
        self._cantik = cantik

    def perkenalan(self):
        print(f'Guru Kami Bernama {self._nama} yang {self._cantik}')

BuAnita = guruotkp('Bu Anita','Cantik')
BuAnita.pamer()

class kepsek:
    def __init__(self, nama):
        self._nama = nama

    def lilik(self):
         print(f'kepsek kami bernama {self._nama}')

l = kepsek('King Lilik')
l.lilk()