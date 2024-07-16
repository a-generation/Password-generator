import sys
import random
import string
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox, QMessageBox
from PyQt5.QtCore import Qt, pyqtSlot

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Password Generator')
        self.setGeometry(100, 100, 400, 250)

        # Labels and checkboxes for password options
        self.length_label = QLabel('Password Length:')
        self.length_input = QLineEdit(self)
        self.length_input.setText('12')  # Default length
        self.uppercase_checkbox = QCheckBox('Include Uppercase Letters')
        self.lowercase_checkbox = QCheckBox('Include Lowercase Letters')
        self.digits_checkbox = QCheckBox('Include Digits')
        self.special_chars_checkbox = QCheckBox('Include Special Characters (%*()?,@#$~)')

        # Generate button
        self.generate_button = QPushButton('Generate Password')
        self.generate_button.clicked.connect(self.generate_password)

        # Result line edit for generated password (read-only)
        self.password_output = QLineEdit(self)
        self.password_output.setReadOnly(True)

        # Copy button for copying password to clipboard
        self.copy_button = QPushButton('Copy Password')
        self.copy_button.setEnabled(False)  # Initially disabled
        self.copy_button.clicked.connect(self.copy_password)

        # Layout
        vbox = QVBoxLayout()
        hbox_length = QHBoxLayout()
        hbox_length.addWidget(self.length_label)
        hbox_length.addWidget(self.length_input)
        vbox.addLayout(hbox_length)
        vbox.addWidget(self.uppercase_checkbox)
        vbox.addWidget(self.lowercase_checkbox)
        vbox.addWidget(self.digits_checkbox)
        vbox.addWidget(self.special_chars_checkbox)
        vbox.addWidget(self.generate_button)
        vbox.addWidget(self.password_output)
        vbox.addWidget(self.copy_button)

        self.setLayout(vbox)

    @pyqtSlot()
    def generate_password(self):
        length = int(self.length_input.text())
        use_uppercase = self.uppercase_checkbox.isChecked()
        use_lowercase = self.lowercase_checkbox.isChecked()
        use_digits = self.digits_checkbox.isChecked()
        use_special_chars = self.special_chars_checkbox.isChecked()

        if not (use_uppercase or use_lowercase or use_digits or use_special_chars):
            QMessageBox.warning(self, 'Warning', 'Select at least one option for password generation.')
            return

        characters = ''
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_lowercase:
            characters += string.ascii_lowercase
        if use_digits:
            characters += string.digits
        if use_special_chars:
            characters += '%*()?@#$~'

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_output.setText(password)
        self.copy_button.setEnabled(True)  # Enable copy button after generating password

    @pyqtSlot()
    def copy_password(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.password_output.text())
        QMessageBox.information(self, 'Password Copied', 'Password copied to clipboard.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PasswordGenerator()
    ex.show()
    sys.exit(app.exec_())
