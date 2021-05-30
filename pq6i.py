from pq6 import *
from mesh import tabletka
import sys


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.text)

    def text(self):
#        self.ui.plainTextEdit.appendPlainText(f'{get_answers(self.ui.textEdit.toPlainText())}')
        self.ui.plainTextEdit.appendPlainText(f'{tabletka(self.ui.textEdit.toPlainText())}')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
