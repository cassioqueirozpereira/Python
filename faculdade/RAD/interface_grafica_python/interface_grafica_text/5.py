from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.nome = QLineEdit(self)
        self.nome.setPlaceholderText("Nome")
        self.sobrenome = QLineEdit(self)
        self.sobrenome.setPlaceholderText("Sobrenome")
        self.nome_completo = QLineEdit(self)
        self.nome_completo.setPlaceholderText("Nome completo")
        self.nome_completo.setReadOnly(True)

        self.button = QPushButton('Pressione o Botão', self)
        self.button.clicked.connect(self.mostrar_nome_completo)

        self.layout.addWidget(self.nome)
        self.layout.addWidget(self.sobrenome)
        self.layout.addWidget(self.nome_completo)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)
        self.setWindowTitle("Exemplo Simples")

    def mostrar_nome_completo(self):
        nome = self.nome.text()
        sobrenome = self.sobrenome.text()
        self.nome_completo.setText(f"{nome} {sobrenome}")

if __name__ == '__main__':
    app = QApplication([])
    window = MyApp()
    window.show()
    app.exec_()
