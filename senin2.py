import random
from guess import cek

class Game:
    def __init__(self):
        self.jawaban = random.randint(1, 10)

    def main(self):
        tebakan = int(input('Tebak angka dari 1 s.d 10:'))
        if cek(tebakan, self.jawaban):
            print("Jawaban kamu benar!")
        else:
            print("Jawaban kamu salah!")

if __name__ == "__main__":
    game = Game()
    game.main()
