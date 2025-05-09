import sys
from random import random, Random, randint

from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        #self.ui.generujButton.clicked.connect(self.generuj)
        self.ui.losujButton.clicked.connect(self.losuj)
        self.show()

    def losuj(self):
        obstawione_liczby = self.ui.obstawiamEdit.text()
        if len(obstawione_liczby) != 6:
            informacja = QMessageBox()
            informacja.setText("Wprowadz poprawne liczby!")
            informacja.exec()

        lista = []
        while len(lista) < 6:
            wynik_losowania = randint(1, 49)
            lista.append(wynik_losowania)
        self.ui.losowanieEdit.setText(str(lista))

        trafienia = 0
        for i in str(wynik_losowania):
            if i in str(obstawione_liczby):
                trafienia += 1
        self.ui.trafieniaButton.setText(str(trafienia))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())