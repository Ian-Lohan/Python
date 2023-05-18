import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from MinhaCalculadora import Ui_MinhaCalculadora

class MainWindow(QtWidgets.QMainWindow, Ui_MinhaCalculadora):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        self.operand1 = None
        self.operador = None
        self.visor_2 = self.visor_2
        self.operacao_pendente = False
        
        def calc(arg):
            if arg.isdigit() or arg == '.':
                current_text = self.visor.text()
                if current_text == '0' or self.operacao_pendente:
                    current_text = ''
                    self.operacao_pendente = False
                new_text = current_text + arg
                self.visor.setText(new_text)
            elif arg == 'C':
                self.visor.setText('0')
                self.visor_2.setText('0')
                self.operand1 = None
                self.operador = None
                self.operacao_pendente = False
            elif arg in ['+', '-', 'X', '/']:
                if self.operand1 is not None and not self.operacao_pendente:
                    operand2 = int(self.visor.text()) if self.visor.text().isdigit() else float(self.visor.text())
                    if self.operador == '+':
                        result = self.operand1 + operand2
                    elif self.operador == '-':
                        result = self.operand1 - operand2
                    elif self.operador == 'X':
                        result = self.operand1 * operand2
                    elif self.operador == '/':
                        result = self.operand1 / operand2
                    self.visor.setText(str(round(result, 5)))
                    self.visor_2.setText('0')
                    self.operacao_pendente = True
                self.operand1 = int(self.visor.text()) if self.visor.text().isdigit() else float(self.visor.text())
                self.operador = arg
                self.visor.setText('0')
                self.visor_2.setText(str(round(self.operand1, 5)) + " " + arg)
            elif arg == '=':
                operand2 = int(self.visor.text()) if self.visor.text().isdigit() else float(self.visor.text())
                if self.operador == '+':
                    result = self.operand1 + operand2
                elif self.operador == '-':
                    result = self.operand1 - operand2
                elif self.operador == 'X':
                    result = self.operand1 * operand2
                elif self.operador == '/':
                    result = self.operand1 / operand2
                else:
                    result = 0
                self.visor.setText(str(round(result, 5)))
                self.visor_2.setText('0')
                self.operand1 = 0
                self.operacao_pendente = True
        
        self.p0.clicked.connect(lambda: calc(self.p0.text()))
        self.p1.clicked.connect(lambda: calc(self.p1.text()))
        self.p2.clicked.connect(lambda: calc(self.p2.text()))
        self.p3.clicked.connect(lambda: calc(self.p3.text()))
        self.p4.clicked.connect(lambda: calc(self.p4.text()))
        self.p5.clicked.connect(lambda: calc(self.p5.text()))
        self.p6.clicked.connect(lambda: calc(self.p6.text()))
        self.p7.clicked.connect(lambda: calc(self.p7.text()))
        self.p8.clicked.connect(lambda: calc(self.p8.text()))
        self.p9.clicked.connect(lambda: calc(self.p9.text()))
        self.ponto.clicked.connect(lambda: calc(self.ponto.text()))
        self.somar.clicked.connect(lambda: calc(self.somar.text()))
        self.subtrair.clicked.connect(lambda: calc(self.subtrair.text()))
        self.multiplicar.clicked.connect(lambda: calc(self.multiplicar.text()))
        self.dividir.clicked.connect(lambda: calc(self.dividir.text()))
        self.igual.clicked.connect(lambda: calc(self.igual.text()))
        self.clear.clicked.connect(lambda: calc(self.clear.text()))
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
