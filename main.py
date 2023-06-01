class Animal:
    def __init__(self, name, sound):
        self.name=name
        self.sound=sound
    def soound(self):
        print(f"Тварина: {self.name}, звук: {self.sound}")

a=Animal("Kow", "moo")
a.soound()

