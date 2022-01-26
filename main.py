class Voiture():
    def __init__(self, marque, prix, couleur):
        self.marque = marque
        self.prix = prix
        self.couleur = couleur

    def __str__(self):
        return f"Votre voiture est une {self.marque} {self.couleur} et coûte {self.prix}"

    def __repr__(self):
        return f"Votre voiture est une {self.marque} {self.couleur} et coûte {self.prix}"

    @property
    def prix_euros(self):
        return int(self.prix * 1.5)

    @classmethod
    def lamborghini(cls):
        return cls("Lamborghini", 150000, "rouge")

    @classmethod
    def porsche(cls):
        return cls("porsche", 200000, "noir")

super_voiture = Voiture("Lamborghini", 150000, "rouge")
print(super_voiture)
print(super_voiture.prix_euros)

lamborghini = Voiture.lamborghini()
print(lamborghini.prix)
print(lamborghini.prix_euros)
porsche = Voiture.porsche()
print(porsche.prix)