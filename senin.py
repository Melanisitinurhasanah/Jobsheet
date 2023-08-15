class CekTebakan:
    def __init__(self, tebakan, jawaban):
        self.tebakan = tebakan
        self.jawaban = jawaban

    def cek(self):
        if self.tebakan == self.jawaban:
            return True
        return False
        
tebakan = "some_guess"
jawaban = "some_answer"

checker = CekTebakan(tebakan, jawaban)
result = checker.cek()
print(result) # True or False