import random


def losowanieNumerowLotto(ileLiczb, pulaLiczb):
    print(random.sample(range(pulaLiczb + 1), ileLiczb))

