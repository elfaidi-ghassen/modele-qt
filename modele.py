
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication





app=QApplication([])
windows=loadUi('interface.ui')
windows.show()
windows.btn.clicked.connect(afficher)
app.exec()

