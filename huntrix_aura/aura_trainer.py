class HuntrixAuraTrainer:
    def __init__(self, bless_count=0.5):
        self.aura = 0
        self.bless_count = bless_count  # 0.5

    def listen_funk(self, times=1):
        self.aura += int(10000 * self.bless_count) * times

    def listen_song(self, times=1):
        self.aura += int(120000 * self.bless_count) * times

    def mythical_combo(self, times=1):
        self.aura += int(130000 * self.bless_count) * times

    def reset(self):
        self.aura = 0

    def status(self):
        return f"Current Aura: {self.aura} (Bless x{self.bless_count})"

def main():
    trainer = HuntrixAuraTrainer(bless_count=0.5)

    while True:
        print(" --- Huntrix Aura Trainer ---")
        print("Bless Count:", trainer.bless_count)
        print("1) Listen to funk (+10,000 base)")
        print("2) Listen to their song (+120,000 base)")
        print("3) Mythical aura combo (+130,000 base)")
        print("4) Show aura")
        print("5) Reset aura")
        print("0) Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            trainer.listen_funk()
        elif choice == "2":
            trainer.listen_song()
        elif choice == "3":
            trainer.mythical_combo()
        elif choice == "4":
            print(trainer.status())
        elif choice == "5":
            trainer.reset()
            print("Aura reset to 0.")
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
