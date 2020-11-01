from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QHeaderView
from python_files import connection_clone
import hashlib


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(813, 484)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(234, 9, 231, 255), stop:1 rgba(9, 233, 236, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_main.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_main)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        MainWindow.setMaximumSize(800,600)

        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_main)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_login = QtWidgets.QWidget()
        self.page_login.setObjectName("page_login")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_login)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_upper_image_part = QtWidgets.QFrame(self.page_login)
        self.frame_upper_image_part.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_upper_image_part.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                                  "border-radius:20px;\n"
                                                  "")
        self.frame_upper_image_part.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_upper_image_part.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_upper_image_part.setObjectName("frame_upper_image_part")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_upper_image_part)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_Vault_title = QtWidgets.QPushButton(self.frame_upper_image_part)
        self.pushButton_Vault_title.setMinimumSize(QtCore.QSize(0, 49))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton_Vault_title.setFont(font)
        self.pushButton_Vault_title.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_Vault_title.setStyleSheet("background-color: rgb(230, 176, 13);\n"
                                                  "border-radius:20px;")
        self.pushButton_Vault_title.setFlat(True)
        self.pushButton_Vault_title.setObjectName("pushButton_Vault_title")
        self.verticalLayout_4.addWidget(self.pushButton_Vault_title)
        self.verticalLayout_3.addWidget(self.frame_upper_image_part)
        self.frame_lower_login_part = QtWidgets.QFrame(self.page_login)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.frame_lower_login_part.setFont(font)
        self.frame_lower_login_part.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame_lower_login_part.setStyleSheet("background-color: rgb(56, 56, 56);\n"
                                                  "border-radius:30px;")
        self.frame_lower_login_part.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_lower_login_part.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_lower_login_part.setObjectName("frame_lower_login_part")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_lower_login_part)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_login_text_part = QtWidgets.QFrame(self.frame_lower_login_part)
        self.frame_login_text_part.setMinimumSize(QtCore.QSize(100, 0))
        self.frame_login_text_part.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_login_text_part.setStyleSheet("background-color: rgb(16, 16, 16);\n"
                                                 "border-radius:20px;")
        self.frame_login_text_part.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_login_text_part.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_login_text_part.setObjectName("frame_login_text_part")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_login_text_part)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_login_text = QtWidgets.QPushButton(self.frame_login_text_part)
        self.pushButton_login_text.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_login_text.setFont(font)
        self.pushButton_login_text.setStyleSheet("background-color: rgb(255, 176, 17);\n"
                                                 "border-radius:20px;")
        self.pushButton_login_text.setObjectName("pushButton_login_text")
        self.verticalLayout_6.addWidget(self.pushButton_login_text)
        self.verticalLayout_5.addWidget(self.frame_login_text_part)
        self.line = QtWidgets.QFrame(self.frame_lower_login_part)
        self.line.setMinimumSize(QtCore.QSize(500, 0))
        self.line.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(252, 200, 11, 255), stop:1 rgba(8, 8, 8, 255));")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.frame_login_input_widgets = QtWidgets.QFrame(self.frame_lower_login_part)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.frame_login_input_widgets.setFont(font)
        self.frame_login_input_widgets.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_login_input_widgets.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_login_input_widgets.setObjectName("frame_login_input_widgets")
        self.label_username = QtWidgets.QLabel(self.frame_login_input_widgets)
        self.label_username.setGeometry(QtCore.QRect(170, 40, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_username.setFont(font)
        self.label_username.setStyleSheet("background-color: rgb(255, 176, 17);\n"
                                          "border-radius:5px;")
        self.label_username.setObjectName("label_username")
        self.label_password = QtWidgets.QLabel(self.frame_login_input_widgets)
        self.label_password.setGeometry(QtCore.QRect(170, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_password.setFont(font)
        self.label_password.setStyleSheet("background-color: rgb(255, 176, 17);\n"
                                          "border-radius:5px;")
        self.label_password.setObjectName("label_password")
        self.lineEdit_username = QtWidgets.QLineEdit(self.frame_login_input_widgets)
        self.lineEdit_username.setGeometry(QtCore.QRect(300, 40, 201, 41))
        self.lineEdit_username.setStyleSheet("background-color: rgb(248, 248, 248);\n"
                                             "border-radius:15px;")
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_password = QtWidgets.QLineEdit(self.frame_login_input_widgets)
        self.lineEdit_password.setGeometry(QtCore.QRect(300, 90, 201, 41))
        self.lineEdit_password.setStyleSheet("background-color: rgb(248, 248, 248);\n"
                                             "border-radius:15px;")
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.frame_signup = QtWidgets.QFrame(self.frame_login_input_widgets)
        self.frame_signup.setGeometry(QtCore.QRect(569, 10, 71, 36))
        self.frame_signup.setStyleSheet("background-color: rgb(103, 103, 103);\n"
                                        "\n"
                                        "border-radius:10px;")
        self.frame_signup.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_signup.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_signup.setObjectName("frame_signup")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_signup)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton = QtWidgets.QPushButton(self.frame_signup)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-radius:20px;")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_7.addWidget(self.pushButton)
        self.line_3 = QtWidgets.QFrame(self.frame_login_input_widgets)
        self.line_3.setGeometry(QtCore.QRect(0, 280, 757, 3))
        self.line_3.setMinimumSize(QtCore.QSize(500, 0))
        self.line_3.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(252, 200, 11, 255), stop:1 rgba(8, 8, 8, 255));")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.frame_2 = QtWidgets.QFrame(self.frame_login_input_widgets)
        self.frame_2.setGeometry(QtCore.QRect(320, 170, 161, 81))
        self.frame_2.setStyleSheet("background-color: rgb(255, 176, 17);\\nborder-radius:20px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_19.addWidget(self.pushButton_5)
        self.verticalLayout_5.addWidget(self.frame_login_input_widgets)
        self.verticalLayout_3.addWidget(self.frame_lower_login_part)
        self.stackedWidget.addWidget(self.page_login)
        self.page_data = QtWidgets.QWidget()
        self.page_data.setObjectName("page_data")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.page_data)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_client_data_title = QtWidgets.QFrame(self.page_data)
        self.frame_client_data_title.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_client_data_title.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_client_data_title.setStyleSheet("background-color: rgb(255, 176, 17);\n"
                                                   "border-radius:20px;")
        self.frame_client_data_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_client_data_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_client_data_title.setObjectName("frame_client_data_title")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_client_data_title)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_client_data_title)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_13.addWidget(self.pushButton_3)
        self.verticalLayout_12.addWidget(self.frame_client_data_title)
        self.frame_client_actual_data = QtWidgets.QFrame(self.page_data)
        self.frame_client_actual_data.setStyleSheet("background-color: rgb(56, 56, 56);\n"
                                                    "border-radius:30px;")
        self.frame_client_actual_data.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_client_actual_data.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_client_actual_data.setObjectName("frame_client_actual_data")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_client_actual_data)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_clients_name_title = QtWidgets.QFrame(self.frame_client_actual_data)
        self.frame_clients_name_title.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_clients_name_title.setStyleSheet("background-color: rgb(17, 17, 17);\n"
                                                    "border-radius:20px;")
        self.frame_clients_name_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_clients_name_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_clients_name_title.setObjectName("frame_clients_name_title")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_clients_name_title)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.pushButton_clients_name = QtWidgets.QPushButton(self.frame_clients_name_title)
        self.pushButton_clients_name.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_clients_name.setFont(font)
        self.pushButton_clients_name.setStyleSheet("background-color: rgb(255, 176, 17);\n"
                                                   "border-radius:15px;")
        self.pushButton_clients_name.setObjectName("pushButton_clients_name")
        self.verticalLayout_15.addWidget(self.pushButton_clients_name)
        self.verticalLayout_14.addWidget(self.frame_clients_name_title)
        self.line_4 = QtWidgets.QFrame(self.frame_client_actual_data)
        self.line_4.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(229, 2, 226, 255), stop:1 rgba(7, 255, 239, 255));")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_14.addWidget(self.line_4)
        self.frame_clients_data = QtWidgets.QFrame(self.frame_client_actual_data)
        self.frame_clients_data.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_clients_data.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_clients_data.setObjectName("frame_clients_data")
        self.pushButton_logout = QtWidgets.QPushButton(self.frame_clients_data)
        self.pushButton_logout.setGeometry(QtCore.QRect(170, 230, 151, 41))
        self.pushButton_logout.setStyleSheet("background-color: rgb(255, 176, 17);\n"
                                             "border-radius:15px;")
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.pushButton_add_data = QtWidgets.QPushButton(self.frame_clients_data)
        self.pushButton_add_data.setGeometry(QtCore.QRect(580, 160, 151, 41))
        self.pushButton_add_data.setStyleSheet("background-color: rgb(255, 176, 17);\n"
                                               "border-radius:15px;")
        self.pushButton_add_data.setObjectName("pushButton_add_data")
        self.textEdit_data_entry_email = QtWidgets.QTextEdit(self.frame_clients_data)
        self.textEdit_data_entry_email.setGeometry(QtCore.QRect(550, 10, 201, 61))
        self.textEdit_data_entry_email.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_data_entry_email.setObjectName("textEdit_data_entry_email")
        self.line_5 = QtWidgets.QFrame(self.frame_clients_data)
        self.line_5.setGeometry(QtCore.QRect(430, 10, 3, 220))
        self.line_5.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(229, 2, 226, 255), stop:1 rgba(7, 255, 239, 255));")
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.textEdit_data_entry_password = QtWidgets.QTextEdit(self.frame_clients_data)
        self.textEdit_data_entry_password.setGeometry(QtCore.QRect(550, 80, 201, 61))
        self.textEdit_data_entry_password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_data_entry_password.setObjectName("textEdit_data_entry_password")
        self.label_client_data_email = QtWidgets.QLabel(self.frame_clients_data)
        self.label_client_data_email.setGeometry(QtCore.QRect(440, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_client_data_email.setFont(font)
        self.label_client_data_email.setStyleSheet("background-color: rgb(255, 176, 17);\n"
                                                   "border-radius:5px;")
        self.label_client_data_email.setObjectName("label_client_data_email")
        self.label_client_data_password = QtWidgets.QLabel(self.frame_clients_data)
        self.label_client_data_password.setGeometry(QtCore.QRect(440, 100, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_client_data_password.setFont(font)
        self.label_client_data_password.setStyleSheet("background-color: rgb(255, 176, 17);\n"
                                                      "border-radius:5px;")
        self.label_client_data_password.setObjectName("label_client_data_password")
        self.pushButton_delete_all = QtWidgets.QPushButton(self.frame_clients_data)
        self.pushButton_delete_all.setGeometry(QtCore.QRect(10, 230, 151, 41))
        self.pushButton_delete_all.setStyleSheet("background-color: rgb(255, 176, 17);\n"
                                                 "border-radius:15px;")
        self.pushButton_delete_all.setObjectName("pushButton_delete_all")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_clients_data)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 401, 191))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_14.addWidget(self.frame_clients_data)
        self.verticalLayout_12.addWidget(self.frame_client_actual_data)
        self.stackedWidget.addWidget(self.page_data)
        self.page_registration = QtWidgets.QWidget()
        self.page_registration.setObjectName("page_registration")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.page_registration)
        self.verticalLayout_16.setObjectName("verticalLayout_16")

        self.frame_register_title = QtWidgets.QFrame(self.page_registration)
        self.frame_register_title.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_register_title.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                                "border-radius:15px;")
        self.frame_register_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_register_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_register_title.setObjectName("frame_register_title")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_register_title)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.registration_label = QtWidgets.QPushButton(self.frame_register_title)
        self.registration_label.setMinimumSize(QtCore.QSize(0, 44))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.registration_label.setFont(font)
        self.registration_label.setStyleSheet("background-color: rgb(255, 176, 17);\n"
                                              "border-radius:15px;")
        self.registration_label.setObjectName("registration_label")
        self.verticalLayout_17.addWidget(self.registration_label)
        self.verticalLayout_16.addWidget(self.frame_register_title)
        self.frame_registration_contents = QtWidgets.QFrame(self.page_registration)
        self.frame_registration_contents.setStyleSheet("background-color: rgb(56, 56, 56);\n"
                                                       "border-radius:30px;")
        self.frame_registration_contents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_registration_contents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_registration_contents.setObjectName("frame_registration_contents")
        self.label_client_data_first_name = QtWidgets.QLabel(self.frame_registration_contents)
        self.label_client_data_first_name.setGeometry(QtCore.QRect(10, 50, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_client_data_first_name.setFont(font)
        self.label_client_data_first_name.setStyleSheet("background-color: rgb(255, 176, 17);\n"
                                                        "border-radius:5px;")
        self.label_client_data_first_name.setObjectName("label_client_data_first_name")
        self.label_client_data_last_name = QtWidgets.QLabel(self.frame_registration_contents)
        self.label_client_data_last_name.setGeometry(QtCore.QRect(10, 140, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_client_data_last_name.setFont(font)
        self.label_client_data_last_name.setStyleSheet("background-color: rgb(255, 176, 17);\n"
                                                       "border-radius:5px;")
        self.label_client_data_last_name.setObjectName("label_client_data_last_name")
        self.label_client_data_contact_number = QtWidgets.QLabel(self.frame_registration_contents)
        self.label_client_data_contact_number.setGeometry(QtCore.QRect(10, 220, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_client_data_contact_number.setFont(font)
        self.label_client_data_contact_number.setStyleSheet("background-color: rgb(255, 176, 17);\n"
                                                            "border-radius:5px;")
        self.label_client_data_contact_number.setObjectName("label_client_data_contact_number")
        self.lineEdit_first_name = QtWidgets.QLineEdit(self.frame_registration_contents)
        self.lineEdit_first_name.setGeometry(QtCore.QRect(130, 40, 241, 41))
        self.lineEdit_first_name.setStyleSheet("background-color: rgb(248, 248, 248);\n"
                                               "border-radius:15px;")
        self.lineEdit_first_name.setObjectName("lineEdit_first_name")
        self.lineEdit_last_name = QtWidgets.QLineEdit(self.frame_registration_contents)
        self.lineEdit_last_name.setGeometry(QtCore.QRect(130, 130, 241, 41))
        self.lineEdit_last_name.setStyleSheet("background-color: rgb(248, 248, 248);\n"
                                              "border-radius:15px;")
        self.lineEdit_last_name.setObjectName("lineEdit_last_name")
        self.lineEdit_contact_number = QtWidgets.QLineEdit(self.frame_registration_contents)
        self.lineEdit_contact_number.setGeometry(QtCore.QRect(130, 210, 241, 41))
        self.lineEdit_contact_number.setStyleSheet("background-color: rgb(248, 248, 248);\n"
                                                   "border-radius:15px;")
        self.lineEdit_contact_number.setObjectName("lineEdit_contact_number")
        self.line_6 = QtWidgets.QFrame(self.frame_registration_contents)
        self.line_6.setGeometry(QtCore.QRect(390, 10, 3, 250))
        self.line_6.setStyleSheet(
            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(248, 204, 24, 255), stop:1 rgba(29, 29, 29, 255));")
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_client_data_Username = QtWidgets.QLabel(self.frame_registration_contents)
        self.label_client_data_Username.setGeometry(QtCore.QRect(400, 50, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_client_data_Username.setFont(font)
        self.label_client_data_Username.setStyleSheet("background-color: rgb(255, 176, 17);\n"
                                                      "border-radius:5px;")
        self.label_client_data_Username.setObjectName("label_client_data_Username")
        self.lineEdit_username_3 = QtWidgets.QLineEdit(self.frame_registration_contents)
        self.lineEdit_username_3.setGeometry(QtCore.QRect(520, 40, 241, 41))
        self.lineEdit_username_3.setStyleSheet("background-color: rgb(248, 248, 248);\n"
                                               "border-radius:15px;")
        self.lineEdit_username_3.setObjectName("lineEdit_username_3")
        self.label_client_data_Username_2 = QtWidgets.QLabel(self.frame_registration_contents)
        self.label_client_data_Username_2.setGeometry(QtCore.QRect(400, 130, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_client_data_Username_2.setFont(font)
        self.label_client_data_Username_2.setStyleSheet("background-color: rgb(255, 176, 17);\n"
                                                        "border-radius:5px;")
        self.label_client_data_Username_2.setObjectName("label_client_data_Username_2")
        self.lineEdit_password_3 = QtWidgets.QLineEdit(self.frame_registration_contents)
        self.lineEdit_password_3.setGeometry(QtCore.QRect(520, 120, 241, 41))
        self.lineEdit_password_3.setStyleSheet("background-color: rgb(248, 248, 248);\n"
                                               "border-radius:15px;")
        self.lineEdit_password_3.setObjectName("lineEdit_password_3")

        self.frame = QtWidgets.QFrame(self.frame_registration_contents)
        self.frame.setGeometry(QtCore.QRect(260, 300, 231, 61))
        self.frame.setStyleSheet("background-color: rgb(255, 176, 17);\n"
                                 "border-radius:15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_18.addWidget(self.pushButton_4)
        self.verticalLayout_16.addWidget(self.frame_registration_contents)
        self.stackedWidget.addWidget(self.page_registration)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.frame_main)
        MainWindow.setCentralWidget(self.centralwidget)

        # login button binding
        self.pushButton_5.clicked.connect(self.login)

        # Signup Button Binding
        self.pushButton.clicked.connect(self.switch_to_page_reister)

        # Register Button Binding
        self.pushButton_4.clicked.connect(self.register)

        # Add Data Button Binding
        self.pushButton_add_data.clicked.connect(self.add_data)

        # logout button binding
        self.pushButton_logout.clicked.connect(self.logout)

        # Delete All button Binding
        self.pushButton_delete_all.clicked.connect(self.delete_all)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Vault_title.setText(_translate("MainWindow", "Safe Place For Your Detalils"))
        self.pushButton_login_text.setText(_translate("MainWindow", "Login Pannel"))
        self.label_username.setText(_translate("MainWindow", "UserName"))
        self.label_password.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "SignUp"))
        self.pushButton_5.setText(_translate("MainWindow", "Login"))
        self.pushButton_3.setText(_translate("MainWindow", "DataBase(MySQl Server)"))
        self.pushButton_clients_name.setText(_translate("MainWindow", "ClientsName"))
        self.pushButton_logout.setText(_translate("MainWindow", "Logout"))
        self.pushButton_add_data.setText(_translate("MainWindow", "Add Data"))
        self.label_client_data_email.setText(_translate("MainWindow", "Email"))
        self.label_client_data_password.setText(_translate("MainWindow", "Password"))
        self.pushButton_delete_all.setText(_translate("MainWindow", "Delete All"))
        self.registration_label.setText(_translate("MainWindow", "Registration"))
        self.label_client_data_first_name.setText(_translate("MainWindow", "First Name"))
        self.label_client_data_last_name.setText(_translate("MainWindow", "Last Name"))
        self.label_client_data_contact_number.setText(_translate("MainWindow", "Contact Number"))
        self.label_client_data_Username.setText(_translate("MainWindow", "Username"))
        self.label_client_data_Username_2.setText(_translate("MainWindow", "Password"))
        self.pushButton_4.setText(_translate("MainWindow", "Register"))

    # Page Switchers
    def switch_to_page_data(self):
        self.stackedWidget.setCurrentIndex(1)
        self.pushButton_clients_name.setText(self.username_1)
        # self.load_data()

    def switch_to_page_reister(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_page_login(self):
        self.stackedWidget.setCurrentIndex(0)

    # Searcher

    def verification_username_password(self):
        # self.username_2 = self.lineEdit_username_3.text()
        # self.password_2 = self.lineEdit_password_3.text()
        print('entered password',self.password_1)

        print('inside Authentication system')
        self.hashed_password_1 = self.password_encryptor(bytes(self.password_1,'utf-8'))
        print('After Hash Creation')
        for i in self.list_login:
            if i[0] == self.username_1:
                print('Username Authenticated')
                print('user', i[0])
                print('password = ', i[1])
                print('hashed',self.hashed_password_1)
                if self.hashed_password_1 == i[1]:
                    print('Password Authenticated', self.hashed_password_1)

                    return 1

    # core requirements

    def login(self):
        self.username_1 = self.lineEdit_username.displayText()
        self.password_1 = self.lineEdit_password.text()

        self.obj = connection.sqlConnections()
        self.obj.establish_connection()
        self.list_login = self.obj.read_data()

        print('Entering Verification Function')
        result = self.verification_username_password()
        print('Exiting Verification function')

        if result == 1:
            self.switch_to_page_data()
            self.load_data()
        else:
            print('Wrong Data entry')

        # Displaying Users Data in Table Qwidget
        # self.load_data()

    def register(self):
        self.first_name = self.lineEdit_first_name.text()
        self.last_name = self.lineEdit_last_name.text()
        self.contact_num = self.lineEdit_contact_number.text()

        self.username_2 = self.lineEdit_username_3.text()
        self.password_2 = self.lineEdit_password_3.text()

        print('before Encryption')

        self.password_2 = self.password_encryptor(bytes(self.password_2,'utf-8'))
        print('After Encryption = ',self.password_2)

        obj = connection.sqlConnections()
        obj.establish_connection()

        print('SQL Conncetion Established')

        # adding new users data inside the general table
        obj.add_row_in_general(
            values=(self.first_name, self.last_name, self.contact_num, self.username_2, self.password_2))

        print('Rows Added in The Database')
        # creating a new seperate tabe for storing data for user

        obj.create_table(Username=self.username_2)

        # return to main page again
        self.switch_to_page_login()

    def add_data(self):

        self.email = self.textEdit_data_entry_email.toPlainText()
        self.password_3 = self.textEdit_data_entry_password.toPlainText()

        # self.obj = connection.sqlConnections()
        # self.obj.establish_connection()
        print('its here')
        print(self.username_1)
        self.obj.add_row_in_personal(table_name=self.username_1, values=(self.email, self.password_3))

        self.textEdit_data_entry_email.clear()
        self.textEdit_data_entry_password.clear()

        self.load_data()


    # data Displaying part

    def create_table(self, rows, columns, data):
        print('starting create table function')
        # self.tableWidget.setColumnCount(columns)
        self.tableWidget.setRowCount(rows)
        self.tableWidget.setColumnCount(2)

        print('After setting the row count')
        print(rows)
        print(columns)

        # self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(data[]))

        for i in range(rows):

            for j in range(2):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(data[i][j]))

        print('ending create table function')

    def load_data(self):
        print('starting Load Function')
        rows, columns, data = self.obj.row_col_count(self.username_1)
        print(data)

        # Creating the table
        if not(data == 0):
            self.create_table(rows, columns, data)

        print(' Table is Empty')
        # self.tableWidget.horizontalHeader().setStretchLastSection(True)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(
        #     QHeaderView.Stretch)
        print('ending Load function')

    def logout(self):
        self.switch_to_page_login()

    def password_encryptor(self,password1=b'testText'):
        print('Entered Encryption State')
        hased = hashlib.md5(password1)
        hashed_password = hased.hexdigest()
        # hashed = bcrypt.hashpw(password=password1,salt=bcrypt.gensalt())
        print('Encryption Completed')
        return hashed_password

    def delete_all(self):
        self.obj.delete_all_rows(self.username_1)
        self.tableWidget.clear()









if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
