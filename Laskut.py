T = 1000 # Tulot
A = 2    # Aikuisten määrä
L = 0    # Lasten määrä
v = 667  # Vakio
M = 880  # Hyväksyttävät asumismenot

Maksimit = [447, 652, 828, 981]
Maks = Maksimit[A+L-1]

Perusomavastuu = 0.42*(T-(v+111*A+246*L))

Asumistuki = 0.8*(M-Perusomavastuu)

if Asumistuki > Maks*0.8:
    Asumistuki = Maks*0.8

print("Asumistuki: ", Asumistuki, "€")