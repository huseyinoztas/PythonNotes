import sys
from PyQt5 import QtWidgets as qtw
from PyQt5.QtCore import Qt
from Designer import Ui_MainWindow

class Uygulama(qtw.QMainWindow): ## hesap makinesindeki işlevselliğin temel classıdır
    sayi=None
    sayi2=False
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.sifir.clicked.connect(self.basmak)
        self.ui.bir.clicked.connect(self.basmak)
        self.ui.iki.clicked.connect(self.basmak)
        self.ui.uc.clicked.connect(self.basmak)
        self.ui.dort.clicked.connect(self.basmak)
        self.ui.bes.clicked.connect(self.basmak)
        self.ui.alti.clicked.connect(self.basmak)
        self.ui.yedi.clicked.connect(self.basmak)
        self.ui.sekiz.clicked.connect(self.basmak)
        self.ui.dokuz.clicked.connect(self.basmak)
        self.ui.yuzde.clicked.connect(self.yuzde)
        self.ui.toplama.clicked.connect(self.matematik)
        self.ui.cikarma.clicked.connect(self.matematik)
        self.ui.carpma.clicked.connect(self.matematik)
        self.ui.bolme.clicked.connect(self.matematik)
        self.ui.silme.clicked.connect(self.temizle)
        self.ui.geri.clicked.connect(self.basmak)
        self.ui.nokta.clicked.connect(self.ondalik)
        self.ui.esittir.clicked.connect(self.hesapla)
        self.ui.isaret.clicked.connect(self.isaret)

        self.ui.toplama.setCheckable(True)
        self.ui.cikarma.setCheckable(True)
        self.ui.carpma.setCheckable(True)
        self.ui.bolme.setCheckable(True)
        self.ui.esittir.setCheckable(True)

    def basmak(self):
        button=self.sender()
        if((self.sayi2) and (self.ui.esittir.isChecked())):
            self.ui.sonuc.setText(str(button.text()))
            self.sayi2=True
            self.ui.esittir.setChecked(False)
        elif((self.ui.toplama.isChecked() or self.ui.cikarma.isChecked() or self.ui.carpma.isChecked() or self.ui.bolme.isChecked()) and (not self.sayi2)):
            self.ui.sonuc.setText(format(float(button.text()),'.15g'))
            self.sayi2=True
        else:
            if(("." in self.ui.sonuc.text() and button.text()=="0")):
                self.ui.sonuc.setText(format(float(self.ui.sonuc.text() + button.text())))
            else:
                self.ui.sonuc.setText(format(float(self.ui.sonuc.text() + button.text()),'.15g'))

    def ondalik(self):

        if "." not in  self.ui.sonuc.text():
            self.ui.sonuc.setText(self.ui.sonuc.text() + '.')

    def isaret(self):
        deger=float(self.ui.sonuc.text())*-1
        self.ui.sonuc.setText(format(deger,'.15g'))
    
    def yuzde(self):
        deger=float(self.ui.sonuc.text())*0.01
        self.ui.sonuc.setText(format(deger,'.15g'))
    
    def temizle(self):
        self.sayi=0
        self.sayi2=False
        self.ui.sonuc.setText("0")
        self.ui.toplama.setChecked(False)
        self.ui.cikarma.setChecked(False)
        self.ui.carpma.setChecked(False)
        self.ui.bolme.setChecked(False)
        self.ui.esittir.setChecked(False)

    def matematik(self):
        button=self.sender()
        self.sayi=float(self.ui.sonuc.text())
        button.setChecked(True)

    def hesapla(self):
        self.sayi2=float(self.ui.sonuc.text())
        if self.ui.toplama.isChecked():
            yenideger=self.sayi+self.sayi2
            self.ui.sonuc.setText(format(yenideger,".15g"))
            self.ui.toplama.setChecked(False)
        elif self.ui.cikarma.isChecked():
            yenideger=self.sayi-self.sayi2
            self.ui.sonuc.setText(format(yenideger,".15g"))
            self.ui.cikarma.setChecked(False)
        elif self.ui.carpma.isChecked():
            yenideger=self.sayi*self.sayi2
            self.ui.sonuc.setText(format(yenideger,".15g"))
            self.ui.carpma.setChecked(False)
        elif self.ui.bolme.isChecked():
            yenideger=self.sayi/self.sayi2
            self.ui.sonuc.setText(format(yenideger,".15g"))
            self.ui.bolme.setChecked(False)
        
        self.sayi=yenideger
        self.ui.esittir.setChecked(True)



def app():
    app=qtw.QApplication(sys.argv)
    win=Uygulama()
    win.show()
    sys.exit(app.exec())

app()