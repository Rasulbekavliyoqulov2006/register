from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys
import json
class Register(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Register")
        self.setGeometry(200, 200, 1500, 800)

        self.txt_username = QLabel("Username: ", self)
        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Enter username...")
        self.font(self.txt_username, 20, 100)
        self.font(self.username, 400, 100)

        self.txt_email = QLabel("Email: ", self)
        self.email = QLineEdit(self)
        self.email.setPlaceholderText("Enter email...")
        self.font(self.txt_email, 20, 200)
        self.font(self.email, 400, 200)

        self.txt_password = QLabel("Password: ", self)
        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Enter password...")
        self.font(self.txt_password, 20, 300)
        self.font(self.password, 400, 300)
        self.password.setEchoMode(QLineEdit.Password)

        self.eye_button = QPushButton("👁️", self)
        self.eye_button.setCheckable(True)
        self.eye_button.clicked.connect(self.toggle_password_visibility)
        self.eye_button.setGeometry(770, 300, 50, 30)

        self.reset_button = QPushButton("Clear", self)
        self.font(self.reset_button, 20, 700)
        self.reset_button.setFixedWidth(350)
        self.reset_button.clicked.connect(self.clear)

        self.register_button = QPushButton("Register", self)
        self.font(self.register_button, 20, 600)
        self.register_button.setFixedWidth(350)
        self.register_button.clicked.connect(self.register)

        self.show()

    def clear(self):
        self.username.setText("")
        self.email.setText("")
        self.password.setText("")

    def toggle_password_visibility(self):
        if self.eye_button.isChecked():
            self.password.setEchoMode(QLineEdit.Normal)
        else:
            self.password.setEchoMode(QLineEdit.Password)

    def font(self, obj, x, y):
        obj.setFont(QFont("Kristen ITC", 24))
        obj.move(x, y)

    def register(self):
        username = self.username.text()
        email = self.email.text()
        password = self.password.text()

        try:
            self.check_username(username)
            self.check_email(email)
            self.check_password(password)

            new_user = {
                "username": username,
                "email": email,
                "password": password
            }

            self.write_json(new_user)
            QMessageBox.information(self, "Success", "Registration successful!")
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def write_json(self, new_user):
        try:
            with open("users.json", "r") as file:
                users = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            users = []

        users.append(new_user)

        with open("users.json", "w") as file:
            json.dump(users, file, indent=4)


    def check_username(self, new_username):
        if len(new_username) < 5:
            raise Exception("Username must be at least 5 characters long!")

    def check_email(self, new_email):
        if "@" not in new_email:
            raise Exception("Email must contain '@' symbol!")
        if len(new_email[:new_email.find("@")]) < 5:
            raise Exception("The part before '@' in the email must be longer than 5 characters!")
        if not (new_email.endswith("@gmail.com") or new_email.endswith("@gmail.ru")):
            raise Exception("Email must end with @gmail.com or @gmail.ru.")

    def check_password(self, new_password):
        if len(new_password) < 8:
            raise Exception("Password must be at least 8 characters long!")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Register()
    sys.exit(app.exec_())
