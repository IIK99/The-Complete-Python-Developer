class Kucing:
    def bersuara(self):
        return "Meow"


class Anjing:
    def bersuara(self):
        return "Woof"


def hewan_bersuara(hewan):
    print(hewan.bersuara())


kucing = Kucing()
anjing = Anjing()

hewan_bersuara(kucing)  # Output: Meow
hewan_bersuara(anjing)  # Output: Woof
