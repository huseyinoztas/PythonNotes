from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
import sys

app=QApplication(sys.argv)
w=QMainWindow()
w.setWindowTitle("Hoşgeldiniz")
w.resize(640,480)
w.move(500,200)

yazi=QLabel(w)
yazi.setText("Kullanıcı Adı: ")
yazi.move(30,30)
yazi.setFont(QFont("Arial",10))

kutu=QLineEdit(w)
kutu.move(100,30)

button=QPushButton(w)
button.setText("Giriş")
button.move(100,70)
w.show()
app.exec_()