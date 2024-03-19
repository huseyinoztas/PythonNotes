from PyQt5 import QtWidgets
import sys

uygulama=QtWidgets.QApplication(sys.argv)
pencere=QtWidgets.QMainWindow()
pencere.setWindowTitle("Merhaba Dünya")
pencere.show()

sys.exit(uygulama.exec_())
