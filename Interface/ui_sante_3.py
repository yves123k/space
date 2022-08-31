# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'santeXaNyAo.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QMainWindow, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(777, 720)
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"#label_welcome{\n"
"	font-weight:bold;\n"
"	font-size:18px;\n"
"	background-color:white;\n"
"}\n"
"	\n"
"\n"
"#frame{\n"
"	background-color:rgb(108, 99, 255)\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	font-size:15px;\n"
"	font-weight: bold\n"
"	\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(170, 170, 255);\n"
"	\n"
"	\n"
"}\n"
"#page{\n"
"	background-color:white;\n"
"\n"
"}\n"
"#label_2{\n"
"	font-size:11;\n"
"	font-weight: bold;\n"
"	\n"
"}\n"
"#label_3{\n"
"font-size:11;\n"
"	font-weight: bold\n"
"}\n"
"#label_6{\n"
"font-size:11;\n"
"	font-weight: bold\n"
"}\n"
"#label_8{\n"
"font-size:11;\n"
"	font-weight: bold\n"
"}\n"
"#frame_principal_right{\n"
"	background-color:white;\n"
"}\n"
"#widget{\n"
"	background-color:rgb(108, 99, 255);\n"
"}\n"
"\n"
"#frame_3:hover{ \n"
"background-color:bisque;\n"
"\n"
"	\n"
"\n"
"}\n"
"\n"
"#frame_4:hover{ \n"
"background-color:bisque;\n"
"}\n"
"\n"
"#frame_5:hover{ \n"
"background-color:bisque;\n"
"}\n"
"\n"
"#frame_6:hover{ \n"
"background-color:bisque;\n"
"}\n"
"#la"
                        "bel_logo{\n"
"	border : 1px solid rgb(97, 97, 97);\n"
"	\n"
"}\n"
"#widget_3{\n"
"	background-color:white;\n"
"}\n"
"#label_10{\n"
"	color:white;\n"
"	font-weight:bold;\n"
"}\n"
"#widget_2{\n"
"	background-color:white;\n"
"}\n"
"#frame_10{\n"
"	background-color:rgb(108, 99, 255)\n"
"}\n"
"#pushButton_confirm_login{\n"
"	color:black;\n"
"}\n"
"#QLineEdit{\n"
"	width:50px;\n"
"}\n"
"#label_11{\n"
"	font-weight:bold;\n"
"	font-size:18px;\n"
"	background-color:white;\n"
"}\n"
"#pushButton_LOGIN{\n"
"	color:black;\n"
"	background-color:white;\n"
"\n"
"}\n"
"#pushButton_LOGIN:hover{\n"
"	color:white;\n"
"	background-color:rgb(108, 99, 255)\n"
"\n"
"}\n"
"\n"
"\n"
"#frame_9{\n"
"	background-color:rgb(207, 207, 207);\n"
"}\n"
"#widget_6{\n"
"	background-color:rgb(207, 207, 207);\n"
"}\n"
"#frame_13{\n"
"	background-color:rgb(108, 99, 255)\n"
"}\n"
"#label_13{\n"
"	font-weight:bold;\n"
"	font-size:18px;\n"
"	background-color:white;\n"
"}\n"
"#pushButton_INSCRIPTION{\n"
"	color:black;\n"
"	background-color:white;\n"
"\n"
""
                        "}\n"
"#pushButton_INSCRIPTION:hover{\n"
"	color:white;\n"
"	background-color:rgb(108, 99, 255)\n"
"}\n"
"#frame_14{\n"
"	background-color:rgb(207, 207, 207);\n"
"}\n"
"#widget_9{\n"
"	background-color:rgb(207, 207, 207)\n"
"}\n"
"#page_connexion{\n"
"	background-color:rgb(247, 247, 247);\n"
"}\n"
"#page_Inscription{\n"
"	background-color:rgb(247, 247, 247);\n"
"}\n"
"#frame_8{\n"
"	background-color:rgb(247, 247, 247);\n"
"}\n"
"#frame_12{\n"
"	background-color:rgb(247, 247, 247);\n"
"}\n"
"#pushButton_eye{\n"
"	\n"
"}\n"
"#widget_13{\n"
"	background-color:rgb(255, 255, 255);\n"
"}\n"
"#widget_button_5{\n"
"		background-color:rgb(97, 97, 97)\n"
"}\n"
"#pushButton_1{\n"
"	color:white;\n"
"	background-color:rgb(108, 99, 255)\n"
"}\n"
"\n"
"#pushButton_2{\n"
"	color:white;\n"
"	background-color:rgb(108, 99, 255)\n"
"}\n"
"\n"
"#pushButton_3{\n"
"	color:white;\n"
"	background-color:rgb(108, 99, 255)\n"
"}\n"
"\n"
"#pushButton_4{\n"
"	color:white;\n"
"	background-color:rgb(108, 99, 255)\n"
"}\n"
"\n"
"#pushButton_20"
                        "{\n"
"	color:white;\n"
"	background-color:rgb(108, 99, 255)\n"
"}\n"
"#pushButton{\n"
"	color:white;\n"
"	background-color:rgb(108, 99, 255)\n"
"}\n"
"#pushButton_21{\n"
"	color:white;\n"
"	background-color:rgb(108, 99, 255)\n"
"}\n"
"#widget_24{\n"
"	background-color:rgb(108, 99, 255)\n"
"\n"
"}\n"
"\n"
"\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: blue;\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setLineWidth(1)
        self.page_bienvenue = QWidget()
        self.page_bienvenue.setObjectName(u"page_bienvenue")
        self.horizontalLayout_10 = QHBoxLayout(self.page_bienvenue)
        self.horizontalLayout_10.setSpacing(1)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.widget = QWidget(self.page_bienvenue)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(120, 0))
        self.verticalLayout_8 = QVBoxLayout(self.widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_logo = QLabel(self.frame_2)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setMaximumSize(QSize(90, 90))
        self.label_logo.setPixmap(QPixmap(u":/im/images/images/OIP (1).jpg"))
        self.label_logo.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_logo, 0, Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.frame_7 = QFrame(self.widget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 500))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_3.addWidget(self.label_10, 0, Qt.AlignBottom)


        self.verticalLayout_8.addWidget(self.frame_7)


        self.horizontalLayout_10.addWidget(self.widget)

        self.widget_3 = QWidget(self.page_bienvenue)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.label_welcome = QLabel(self.widget_3)
        self.label_welcome.setObjectName(u"label_welcome")
        self.label_welcome.setMinimumSize(QSize(235, 0))
        self.label_welcome.setAlignment(Qt.AlignCenter)
        self.label_welcome.setIndent(-1)

        self.horizontalLayout_4.addWidget(self.label_welcome)


        self.horizontalLayout_10.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.page_bienvenue)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.frame = QFrame(self.widget_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_button_2 = QWidget(self.frame)
        self.widget_button_2.setObjectName(u"widget_button_2")
        self.widget_button_2.setMinimumSize(QSize(0, 0))
        self.widget_button_2.setLayoutDirection(Qt.RightToLeft)
        self.horizontalLayout_9 = QHBoxLayout(self.widget_button_2)
        self.horizontalLayout_9.setSpacing(2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_5 = QPushButton(self.widget_button_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFlat(True)

        self.horizontalLayout_9.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.widget_button_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFlat(True)

        self.horizontalLayout_9.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.widget_button_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFlat(True)

        self.horizontalLayout_9.addWidget(self.pushButton_7)


        self.verticalLayout_7.addWidget(self.widget_button_2, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.frame)

        self.frame_principal_right = QFrame(self.widget_2)
        self.frame_principal_right.setObjectName(u"frame_principal_right")
        self.frame_principal_right.setMinimumSize(QSize(0, 530))
        self.frame_principal_right.setFrameShape(QFrame.StyledPanel)
        self.frame_principal_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_principal_right)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.stackedWidget_2 = QStackedWidget(self.frame_principal_right)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_4 = QWidget(self.page)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_3 = QFrame(self.widget_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(100, 100))
        self.label.setPixmap(QPixmap(u":/im/images/images/undraw_mindfulness_scgo.svg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)


        self.horizontalLayout_6.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.widget_4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(100, 100))
        self.label_5.setPixmap(QPixmap(u":/im/images/images/undraw_fitness_stats_sht6.svg"))
        self.label_5.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_6, 0, Qt.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.page)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_5 = QFrame(self.widget_5)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(100, 100))
        self.label_7.setPixmap(QPixmap(u":/im/images/images/undraw_teacher_re_sico.svg"))
        self.label_7.setScaledContents(True)

        self.verticalLayout_5.addWidget(self.label_7, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_3)


        self.horizontalLayout_7.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.widget_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(100, 100))
        self.label_4.setPixmap(QPixmap(u":/im/images/images/healthcare.png"))
        self.label_4.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_8)


        self.horizontalLayout_7.addWidget(self.frame_6)


        self.verticalLayout_2.addWidget(self.widget_5)

        self.stackedWidget_2.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_8 = QHBoxLayout(self.page_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(334, 492))
        self.label_9.setPixmap(QPixmap(u"../../../../../Documents/5480_humanheartanatomy_as_918525.jpeg"))
        self.label_9.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_9)

        self.stackedWidget_2.addWidget(self.page_3)

        self.horizontalLayout_5.addWidget(self.stackedWidget_2)


        self.verticalLayout.addWidget(self.frame_principal_right)

        self.pushButton_move_main_app = QPushButton(self.widget_2)
        self.pushButton_move_main_app.setObjectName(u"pushButton_move_main_app")
        self.pushButton_move_main_app.setStyleSheet(u"background-color:rgb(108, 99, 255);color:white;")

        self.verticalLayout.addWidget(self.pushButton_move_main_app)


        self.horizontalLayout_10.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.page_bienvenue)
        self.page_start = QWidget()
        self.page_start.setObjectName(u"page_start")
        self.verticalLayout_17 = QVBoxLayout(self.page_start)
        self.verticalLayout_17.setSpacing(1)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.widget_14 = QWidget(self.page_start)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_24 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.frame_16 = QFrame(self.widget_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_16)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_logo_2 = QLabel(self.frame_16)
        self.label_logo_2.setObjectName(u"label_logo_2")
        self.label_logo_2.setMaximumSize(QSize(90, 90))
        self.label_logo_2.setPixmap(QPixmap(u":/img/Images/OIP (1).jpg"))
        self.label_logo_2.setScaledContents(True)

        self.verticalLayout_18.addWidget(self.label_logo_2)


        self.horizontalLayout_24.addWidget(self.frame_16)

        self.widget_button_5 = QWidget(self.widget_14)
        self.widget_button_5.setObjectName(u"widget_button_5")
        self.widget_button_5.setMinimumSize(QSize(0, 0))
        self.widget_button_5.setLayoutDirection(Qt.RightToLeft)
        self.horizontalLayout_23 = QHBoxLayout(self.widget_button_5)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.pushButton_17 = QPushButton(self.widget_button_5)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setFlat(True)

        self.horizontalLayout_23.addWidget(self.pushButton_17)

        self.pushButton_18 = QPushButton(self.widget_button_5)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setFlat(True)

        self.horizontalLayout_23.addWidget(self.pushButton_18)

        self.pushButton_19 = QPushButton(self.widget_button_5)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setFlat(True)

        self.horizontalLayout_23.addWidget(self.pushButton_19)


        self.horizontalLayout_24.addWidget(self.widget_button_5, 0, Qt.AlignTop)


        self.verticalLayout_17.addWidget(self.widget_14, 0, Qt.AlignTop)

        self.widget_16 = QWidget(self.page_start)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(0, 500))
        self.horizontalLayout_25 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.widget_16)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 775, 624))
        self.verticalLayout_19 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_19.setSpacing(6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.scrollAreaWidgetContents)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(1, 1, 0, 1)
        self.stackedWidget_3 = QStackedWidget(self.frame_17)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_27 = QHBoxLayout(self.page_2)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.stackedWidget_3.addWidget(self.page_2)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget_3.addWidget(self.page_4)

        self.horizontalLayout_26.addWidget(self.stackedWidget_3)


        self.verticalLayout_19.addWidget(self.frame_17)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_25.addWidget(self.scrollArea)


        self.verticalLayout_17.addWidget(self.widget_16)

        self.widget_15 = QWidget(self.page_start)
        self.widget_15.setObjectName(u"widget_15")

        self.verticalLayout_17.addWidget(self.widget_15)

        self.stackedWidget.addWidget(self.page_start)
        self.page_main = QWidget()
        self.page_main.setObjectName(u"page_main")
        self.horizontalLayout_28 = QHBoxLayout(self.page_main)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.widget_21 = QWidget(self.page_main)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setMinimumSize(QSize(500, 0))
        self.horizontalLayout_37 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.widget_21)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setMinimumSize(QSize(0, 0))
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.bgApp)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(0, 0))
        self.leftMenuBg.setMaximumSize(QSize(62, 16777215))
        self.leftMenuBg.setStyleSheet(u"background-color:rgb(108, 99, 255);")
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setStyleSheet(u"")
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_17 = QLabel(self.topLogoInfo)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(0, 0, 61, 51))
        self.label_17.setMaximumSize(QSize(61, 51))
        self.label_17.setPixmap(QPixmap(u"../../../.designer/images/images/girl-g65e6d80c5_640.jpg"))
        self.label_17.setScaledContents(True)

        self.verticalLayout_23.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setMinimumSize(QSize(0, 0))
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 8, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setBold(True)
        font3.setItalic(False)
        self.toggleButton.setFont(font3)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"#toggleButton{\n"
"background-image: url(:/img/images/icons/icon_menu.png);\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"text-align: left;\n"
"padding-left: 44px;\n"
"color: rgb(255, 255, 255);\n"
"font-size:12px;\n"
"}\n"
"#toggleButton:hover{\n"
"	background-color:rgb(106, 106, 106);\n"
"}\n"
"\n"
"")
        self.toggleButton.setCheckable(True)

        self.verticalLayout_24.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.topMenu)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(True)
        font4.setItalic(False)
        font4.setStrikeOut(False)
        self.btn_home.setFont(font4)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"#btn_home{background-image:url(:/img/images/icons/cil-home.png);\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"text-align: left;\n"
"padding-left: 44px;\n"
"color: rgb(255, 255, 255);\n"
"font-size:12px;}\n"
"\n"
"#btn_home:hover{\n"
"	background-color:rgb(106, 106, 106);\n"
"\n"
"}")

        self.verticalLayout_25.addWidget(self.btn_home)

        self.btn_dashboard = QPushButton(self.topMenu)
        self.btn_dashboard.setObjectName(u"btn_dashboard")
        sizePolicy.setHeightForWidth(self.btn_dashboard.sizePolicy().hasHeightForWidth())
        self.btn_dashboard.setSizePolicy(sizePolicy)
        self.btn_dashboard.setMinimumSize(QSize(0, 45))
        self.btn_dashboard.setFont(font3)
        self.btn_dashboard.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_dashboard.setLayoutDirection(Qt.LeftToRight)
        self.btn_dashboard.setStyleSheet(u"#btn_dashboard{\n"
"\n"
"background-image:url(:/img/images/icons/cil-chart-line.png);\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"text-align: left;\n"
"padding-left: 44px;\n"
"color: rgb(255, 255, 255);\n"
"font-size:12px;\n"
"}\n"
"\n"
"#btn_dashboard:hover{\n"
"		background-color:rgb(106, 106, 106);\n"
"}\n"
"\n"
"")

        self.verticalLayout_25.addWidget(self.btn_dashboard)

        self.btn_program = QPushButton(self.topMenu)
        self.btn_program.setObjectName(u"btn_program")
        sizePolicy.setHeightForWidth(self.btn_program.sizePolicy().hasHeightForWidth())
        self.btn_program.setSizePolicy(sizePolicy)
        self.btn_program.setMinimumSize(QSize(0, 45))
        self.btn_program.setFont(font3)
        self.btn_program.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_program.setLayoutDirection(Qt.LeftToRight)
        self.btn_program.setStyleSheet(u"#btn_program{\n"
"\n"
"background-image: url(:/img/images/icons/cil-calendar-check.png);\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"text-align: left;\n"
"padding-left: 44px;\n"
"color: rgb(255, 255, 255);\n"
"font-size:12px;\n"
"\n"
"}\n"
"#btn_program:hover{\n"
"	background-color:rgb(106, 106, 106);\n"
"\n"
"}\n"
"\n"
"")

        self.verticalLayout_25.addWidget(self.btn_program)

        self.btn_test = QPushButton(self.topMenu)
        self.btn_test.setObjectName(u"btn_test")
        self.btn_test.setEnabled(True)
        sizePolicy.setHeightForWidth(self.btn_test.sizePolicy().hasHeightForWidth())
        self.btn_test.setSizePolicy(sizePolicy)
        self.btn_test.setMinimumSize(QSize(0, 45))
        self.btn_test.setFont(font3)
        self.btn_test.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_test.setLayoutDirection(Qt.LeftToRight)
        self.btn_test.setStyleSheet(u"#btn_test{\n"
"background-image: url(:/img/images/icons/cil-medical-cross.png);\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"text-align: left;\n"
"padding-left: 44px;\n"
"color: rgb(255, 255, 255);\n"
"font-size:12px;}\n"
"\n"
"#btn_test:hover{\n"
"	background-color:rgb(106, 106, 106);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_25.addWidget(self.btn_test)

        self.btn_messages = QPushButton(self.topMenu)
        self.btn_messages.setObjectName(u"btn_messages")
        sizePolicy.setHeightForWidth(self.btn_messages.sizePolicy().hasHeightForWidth())
        self.btn_messages.setSizePolicy(sizePolicy)
        self.btn_messages.setMinimumSize(QSize(0, 45))
        self.btn_messages.setFont(font3)
        self.btn_messages.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_messages.setLayoutDirection(Qt.LeftToRight)
        self.btn_messages.setStyleSheet(u"#btn_messages{\n"
"\n"
"background-image: url(:/img/images/icons/cil-comment-bubble.png);\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"text-align: left;\n"
"padding-left: 44px;\n"
"color: rgb(255, 255, 255);\n"
"font-size:12px;\n"
"}\n"
"#btn_messages:hover{\n"
"	background-color:rgb(106, 106, 106);\n"
"}\n"
"")

        self.verticalLayout_25.addWidget(self.btn_messages)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font3)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setAutoFillBackground(False)
        self.toggleLeftBox.setStyleSheet(u"#toggleLeftBox{\n"
"\n"
"background-image: url(:/img/images/icons/cil-settings.png);	\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"text-align: left;\n"
"padding-left: 44px;\n"
"color: rgb(255, 255, 255);\n"
"font-size:12px;\n"
"}\n"
"\n"
"#toggleLeftBox:hover{\n"
"	background-color:rgb(106, 106, 106);\n"
"}\n"
"\n"
"")
        self.toggleLeftBox.setCheckable(True)

        self.verticalLayout_26.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_23.addWidget(self.leftMenuFrame)


        self.horizontalLayout_38.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setStyleSheet(u"background-color:white;")
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setStyleSheet(u"background-color: rgb(189, 147, 249)\n"
"")
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        font5 = QFont()
        font5.setPointSize(5)
        self.extraIcon.setFont(font5)
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))
        font6 = QFont()
        font6.setPointSize(15)
        font6.setBold(True)
        self.extraLabel.setFont(font6)
        self.extraLabel.setStyleSheet(u"color:white")

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.extraCloseColumnBtn.setStyleSheet(u"background-color:")
        icon = QIcon()
        icon.addFile(u":/img/images/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_27.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.extraContent)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.btn_profile = QPushButton(self.extraTopMenu)
        self.btn_profile.setObjectName(u"btn_profile")
        sizePolicy.setHeightForWidth(self.btn_profile.sizePolicy().hasHeightForWidth())
        self.btn_profile.setSizePolicy(sizePolicy)
        self.btn_profile.setMinimumSize(QSize(0, 45))
        self.btn_profile.setFont(font3)
        self.btn_profile.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_profile.setLayoutDirection(Qt.LeftToRight)
        self.btn_profile.setStyleSheet(u"#btn_profile{\n"
"background-image: url(:/img/images/icons/cil-people.png);\n"
"background-color: rgb(167, 167, 167);\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"text-align: left;\n"
"padding-left: 44px;\n"
"color: rgb(255, 255, 255);\n"
"font-size:12px;\n"
"}\n"
"#btn_profile:hover{\n"
"\n"
"background-color: rgb(108, 99, 255);\n"
"\n"
"}\n"
"\n"
"")

        self.verticalLayout_29.addWidget(self.btn_profile)

        self.btn_session_admin = QPushButton(self.extraTopMenu)
        self.btn_session_admin.setObjectName(u"btn_session_admin")
        sizePolicy.setHeightForWidth(self.btn_session_admin.sizePolicy().hasHeightForWidth())
        self.btn_session_admin.setSizePolicy(sizePolicy)
        self.btn_session_admin.setMinimumSize(QSize(0, 45))
        self.btn_session_admin.setFont(font3)
        self.btn_session_admin.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_session_admin.setLayoutDirection(Qt.LeftToRight)
        self.btn_session_admin.setStyleSheet(u"#btn_session_admin{\n"
"background-image: url(:/im/images/images/icons8-admin-settings-male-16.png);\n"
"background-color: rgb(167, 167, 167);\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"text-align: left;\n"
"padding-left: 44px;\n"
"color: rgb(255, 255, 255);\n"
"font-size:12px;}\n"
"\n"
"#btn_session_admin:hover {\n"
"\n"
"background-color:rgb(108, 99, 255);\n"
"}")
        self.btn_session_admin.setIconSize(QSize(17, 16))

        self.verticalLayout_29.addWidget(self.btn_session_admin)

        self.btn_update = QPushButton(self.extraTopMenu)
        self.btn_update.setObjectName(u"btn_update")
        sizePolicy.setHeightForWidth(self.btn_update.sizePolicy().hasHeightForWidth())
        self.btn_update.setSizePolicy(sizePolicy)
        self.btn_update.setMinimumSize(QSize(0, 45))
        self.btn_update.setFont(font3)
        self.btn_update.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_update.setLayoutDirection(Qt.LeftToRight)
        self.btn_update.setStyleSheet(u"#btn_update{\n"
"background-image: url(:/im/images/images/icons8-downloading-updates-16.png);\n"
"background-color: rgb(167, 167, 167);\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"text-align: left;\n"
"padding-left: 44px;\n"
"color: rgb(255, 255, 255);\n"
"font-size:12px;}\n"
"\n"
"#btn_update:hover{\n"
"	background-color:rgb(108, 99, 255);\n"
"}")

        self.verticalLayout_29.addWidget(self.btn_update)


        self.verticalLayout_28.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(190, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_30.addWidget(self.textEdit)


        self.verticalLayout_28.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_28.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.horizontalLayout_38.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.contentBox)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setStyleSheet(u"background-color:white")
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setStyleSheet(u"background-color:rgb(108, 99, 255);")
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(12)
        font7.setBold(True)
        font7.setItalic(False)
        self.titleRightInfo.setFont(font7)
        self.titleRightInfo.setStyleSheet(u"color:white")
        self.titleRightInfo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.titleRightInfo)


        self.horizontalLayout_29.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setStyleSheet(u"background-color:white")
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_31.setSpacing(5)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(4, 0, 0, 0)
        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setStyleSheet(u"background-color:rgb(108, 99, 255)")
        icon1 = QIcon()
        icon1.addFile(u":/img/images/icons/cil-briefcase.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon1)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_31.addWidget(self.closeAppBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        font8 = QFont()
        font8.setBold(True)
        font8.setUnderline(False)
        font8.setStrikeOut(False)
        self.minimizeAppBtn.setFont(font8)
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimizeAppBtn.setStyleSheet(u"\n"
"background-color:rgb(108, 99, 255)\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/im/images/images/icons8-logout-rounded-down-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))
        self.minimizeAppBtn.setFlat(False)

        self.horizontalLayout_31.addWidget(self.minimizeAppBtn)


        self.horizontalLayout_29.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_31.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.content)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(10, 10, 10, -1)
        self.stackedWidget_4 = QStackedWidget(self.pagesContainer)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.stackedWidget_4.setStyleSheet(u"")
        self.page_chat = QWidget()
        self.page_chat.setObjectName(u"page_chat")
        self.page_chat.setStyleSheet(u"background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.horizontalLayout_39 = QHBoxLayout(self.page_chat)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.widget_31 = QWidget(self.page_chat)
        self.widget_31.setObjectName(u"widget_31")
        self.widget_31.setMaximumSize(QSize(190, 16777215))
        self.verticalLayout_49 = QVBoxLayout(self.widget_31)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.label_48 = QLabel(self.widget_31)
        self.label_48.setObjectName(u"label_48")

        self.verticalLayout_49.addWidget(self.label_48, 0, Qt.AlignLeft|Qt.AlignTop)

        self.listWidget = QListWidget(self.widget_31)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(150, 0))
        self.listWidget.setFrameShadow(QFrame.Plain)
        self.listWidget.setLineWidth(1)
        self.listWidget.setIconSize(QSize(30, 30))
        self.listWidget.setMovement(QListView.Static)
        self.listWidget.setLayoutMode(QListView.Batched)
        self.listWidget.setSpacing(0)
        self.listWidget.setGridSize(QSize(100, 40))
        self.listWidget.setSelectionRectVisible(False)
        self.listWidget.setSortingEnabled(True)

        self.verticalLayout_49.addWidget(self.listWidget)


        self.horizontalLayout_39.addWidget(self.widget_31)

        self.stackedWidget_34 = QStackedWidget(self.page_chat)
        self.stackedWidget_34.setObjectName(u"stackedWidget_34")
        self.stackedWidget_34Page1 = QWidget()
        self.stackedWidget_34Page1.setObjectName(u"stackedWidget_34Page1")
        self.verticalLayout_52 = QVBoxLayout(self.stackedWidget_34Page1)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.widget_33 = QWidget(self.stackedWidget_34Page1)
        self.widget_33.setObjectName(u"widget_33")
        self.widget_33.setMinimumSize(QSize(0, 0))
        self.widget_33.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_42 = QHBoxLayout(self.widget_33)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.pushButton_add_contact = QPushButton(self.widget_33)
        self.pushButton_add_contact.setObjectName(u"pushButton_add_contact")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_add_contact.sizePolicy().hasHeightForWidth())
        self.pushButton_add_contact.setSizePolicy(sizePolicy3)
        self.pushButton_add_contact.setMaximumSize(QSize(16777215, 50))
        font9 = QFont()
        font9.setBold(True)
        self.pushButton_add_contact.setFont(font9)
        self.pushButton_add_contact.setStyleSheet(u"color:black;\n"
"font-size: 9px;")

        self.horizontalLayout_42.addWidget(self.pushButton_add_contact)

        self.pushButton_23 = QPushButton(self.widget_33)
        self.pushButton_23.setObjectName(u"pushButton_23")
        sizePolicy3.setHeightForWidth(self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy3)
        self.pushButton_23.setMaximumSize(QSize(16777215, 50))
        self.pushButton_23.setFont(font9)
        self.pushButton_23.setStyleSheet(u"color:black;\n"
"font-size: 9px;")

        self.horizontalLayout_42.addWidget(self.pushButton_23)

        self.pushButton_24 = QPushButton(self.widget_33)
        self.pushButton_24.setObjectName(u"pushButton_24")
        sizePolicy3.setHeightForWidth(self.pushButton_24.sizePolicy().hasHeightForWidth())
        self.pushButton_24.setSizePolicy(sizePolicy3)
        self.pushButton_24.setMaximumSize(QSize(16777215, 50))
        self.pushButton_24.setFont(font9)
        self.pushButton_24.setStyleSheet(u"color:black;\n"
"font-size: 9px;")

        self.horizontalLayout_42.addWidget(self.pushButton_24)


        self.verticalLayout_52.addWidget(self.widget_33, 0, Qt.AlignRight|Qt.AlignTop)

        self.widget_39 = QWidget(self.stackedWidget_34Page1)
        self.widget_39.setObjectName(u"widget_39")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_39.sizePolicy().hasHeightForWidth())
        self.widget_39.setSizePolicy(sizePolicy4)
        self.widget_39.setMinimumSize(QSize(0, 0))
        self.verticalLayout_53 = QVBoxLayout(self.widget_39)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.widget_40 = QWidget(self.widget_39)
        self.widget_40.setObjectName(u"widget_40")
        self.widget_40.setMinimumSize(QSize(0, 0))
        self.widget_40.setMaximumSize(QSize(16777215, 60))
        self.widget_40.setStyleSheet(u"background-color:rgb(108, 99, 255)")
        self.horizontalLayout_43 = QHBoxLayout(self.widget_40)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_img_chat = QLabel(self.widget_40)
        self.label_img_chat.setObjectName(u"label_img_chat")
        self.label_img_chat.setMaximumSize(QSize(50, 50))
        self.label_img_chat.setStyleSheet(u"border-radius:5px")
        self.label_img_chat.setPixmap(QPixmap(u":/im/images/images/girl-g65e6d80c5_640.jpg"))
        self.label_img_chat.setScaledContents(True)

        self.horizontalLayout_43.addWidget(self.label_img_chat)

        self.label_Name_chat = QLabel(self.widget_40)
        self.label_Name_chat.setObjectName(u"label_Name_chat")
        font10 = QFont()
        font10.setPointSize(11)
        font10.setBold(True)
        self.label_Name_chat.setFont(font10)

        self.horizontalLayout_43.addWidget(self.label_Name_chat)

        self.label_51 = QLabel(self.widget_40)
        self.label_51.setObjectName(u"label_51")

        self.horizontalLayout_43.addWidget(self.label_51)

        self.pushButton_25 = QPushButton(self.widget_40)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setMaximumSize(QSize(60, 50))
        self.pushButton_25.setStyleSheet(u"background-color:rgb(108, 99, 255);color:black")
        icon3 = QIcon()
        icon3.addFile(u":/im/images/images/icons8-call-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_25.setIcon(icon3)
        self.pushButton_25.setFlat(True)

        self.horizontalLayout_43.addWidget(self.pushButton_25)

        self.pushButton_26 = QPushButton(self.widget_40)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setMaximumSize(QSize(60, 50))
        self.pushButton_26.setStyleSheet(u"background-color:rgb(108, 99, 255);color:black")
        icon4 = QIcon()
        icon4.addFile(u":/im/images/images/icons8-video-call-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_26.setIcon(icon4)
        self.pushButton_26.setFlat(True)

        self.horizontalLayout_43.addWidget(self.pushButton_26)


        self.verticalLayout_53.addWidget(self.widget_40)

        self.listWidget_2 = QListWidget(self.widget_39)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setIconSize(QSize(50, 42))
        self.listWidget_2.setGridSize(QSize(200, 78))
        self.listWidget_2.setModelColumn(0)
        self.listWidget_2.setBatchSize(130)
        self.listWidget_2.setSelectionRectVisible(False)

        self.verticalLayout_53.addWidget(self.listWidget_2)


        self.verticalLayout_52.addWidget(self.widget_39)

        self.widget_38 = QWidget(self.stackedWidget_34Page1)
        self.widget_38.setObjectName(u"widget_38")
        self.horizontalLayout_41 = QHBoxLayout(self.widget_38)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.lineEdit_send = QLineEdit(self.widget_38)
        self.lineEdit_send.setObjectName(u"lineEdit_send")
        self.lineEdit_send.setMinimumSize(QSize(0, 0))
        self.lineEdit_send.setMaximumSize(QSize(16777215, 58))

        self.horizontalLayout_41.addWidget(self.lineEdit_send)

        self.pushButton_send = QPushButton(self.widget_38)
        self.pushButton_send.setObjectName(u"pushButton_send")
        self.pushButton_send.setStyleSheet(u"background-color:rgb(108, 99, 255);color:white;")

        self.horizontalLayout_41.addWidget(self.pushButton_send)


        self.verticalLayout_52.addWidget(self.widget_38, 0, Qt.AlignBottom)

        self.stackedWidget_34.addWidget(self.stackedWidget_34Page1)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_50 = QVBoxLayout(self.page_5)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.pushButton_return_contact = QPushButton(self.page_5)
        self.pushButton_return_contact.setObjectName(u"pushButton_return_contact")
        self.pushButton_return_contact.setStyleSheet(u"background-color:rgb(108, 99, 255);color:white;")

        self.verticalLayout_50.addWidget(self.pushButton_return_contact, 0, Qt.AlignLeft)

        self.listWidget_3 = QListWidget(self.page_5)
        icon5 = QIcon()
        icon5.addFile(u":/im/images/images/th (3).jpg", QSize(), QIcon.Normal, QIcon.Off)
        brush = QBrush(QColor(230, 230, 230, 255))
        brush.setStyle(Qt.SolidPattern)
        __qlistwidgetitem = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem.setBackground(brush);
        __qlistwidgetitem.setIcon(icon5);
        icon6 = QIcon()
        icon6.addFile(u":/im/images/images/th (1).jpg", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem1.setBackground(brush);
        __qlistwidgetitem1.setIcon(icon6);
        icon7 = QIcon()
        icon7.addFile(u":/im/images/images/th (2).jpg", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem2.setBackground(brush);
        __qlistwidgetitem2.setIcon(icon7);
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setIconSize(QSize(76, 65))
        self.listWidget_3.setLayoutMode(QListView.Batched)
        self.listWidget_3.setSpacing(0)
        self.listWidget_3.setGridSize(QSize(103, 65))
        self.listWidget_3.setViewMode(QListView.ListMode)
        self.listWidget_3.setUniformItemSizes(True)
        self.listWidget_3.setSortingEnabled(True)

        self.verticalLayout_50.addWidget(self.listWidget_3)

        self.pushButton_add_in_contact = QPushButton(self.page_5)
        self.pushButton_add_in_contact.setObjectName(u"pushButton_add_in_contact")
        self.pushButton_add_in_contact.setStyleSheet(u"background-color:rgb(108, 99, 255);color:white;")

        self.verticalLayout_50.addWidget(self.pushButton_add_in_contact)

        self.stackedWidget_34.addWidget(self.page_5)

        self.horizontalLayout_39.addWidget(self.stackedWidget_34)

        self.stackedWidget_4.addWidget(self.page_chat)
        self.widgets_dashboard = QWidget()
        self.widgets_dashboard.setObjectName(u"widgets_dashboard")
        self.widgets_dashboard.setStyleSheet(u"b")
        self.verticalLayout_34 = QVBoxLayout(self.widgets_dashboard)
        self.verticalLayout_34.setSpacing(10)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(10, 10, 10, 10)
        self.widget_19 = QWidget(self.widgets_dashboard)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setStyleSheet(u"background-color: rgb(230, 231, 235)")
        self.verticalLayout_20 = QVBoxLayout(self.widget_19)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_18 = QFrame(self.widget_19)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_18)
        self.verticalLayout_35.setSpacing(8)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.widget_20 = QWidget(self.frame_18)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMaximumSize(QSize(16777215, 40))
        self.verticalLayout_36 = QVBoxLayout(self.widget_20)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_16 = QLabel(self.widget_20)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_36.addWidget(self.label_16)


        self.verticalLayout_35.addWidget(self.widget_20)

        self.widget_22 = QWidget(self.frame_18)
        self.widget_22.setObjectName(u"widget_22")
        self.horizontalLayout_33 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_33.setSpacing(19)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(-1, 13, -1, -1)
        self.widget_24 = QWidget(self.widget_22)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setMinimumSize(QSize(0, 0))
        self.widget_24.setStyleSheet(u"box-shadow: 0px 10px 4px rgba(0,0,0,0.01);\n"
"background-color: rgb(255, 255, 255)\n"
"")
        self.verticalLayout_38 = QVBoxLayout(self.widget_24)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_19 = QLabel(self.widget_24)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_38.addWidget(self.label_19)

        self.label_poids = QLabel(self.widget_24)
        self.label_poids.setObjectName(u"label_poids")
        self.label_poids.setStyleSheet(u" font-family: SofiaProSemiBold;\n"
" font-size: 32px;\n"
" font-weight: 400;\n"
" line-height: 57px;")

        self.verticalLayout_38.addWidget(self.label_poids)

        self.label_21 = QLabel(self.widget_24)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setPixmap(QPixmap(u"../images/images/Triangle.png"))

        self.verticalLayout_38.addWidget(self.label_21)

        self.label_22 = QLabel(self.widget_24)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"color:red")

        self.verticalLayout_38.addWidget(self.label_22)

        self.label_18 = QLabel(self.widget_24)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 0))
        self.label_18.setStyleSheet(u"box-shadow: 0px 2px 4px rgba(0,0,0,0.04);\n"
"background-color: rgb(255, 255, 255)\n"
"")
        self.label_18.setPixmap(QPixmap(u":/im/images/images/background.png"))
        self.label_18.setScaledContents(True)

        self.verticalLayout_38.addWidget(self.label_18)


        self.horizontalLayout_33.addWidget(self.widget_24)

        self.widget_25 = QWidget(self.widget_22)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setMinimumSize(QSize(0, 0))
        self.widget_25.setMaximumSize(QSize(16777215, 16777215))
        self.widget_25.setStyleSheet(u"box-shadow: 0px 2px 8px rgba(0,0,0,0.01);\n"
"background-color: rgb(255, 255, 255)\n"
"")
        self.verticalLayout_37 = QVBoxLayout(self.widget_25)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_25 = QLabel(self.widget_25)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_37.addWidget(self.label_25)

        self.label_dis = QLabel(self.widget_25)
        self.label_dis.setObjectName(u"label_dis")
        self.label_dis.setStyleSheet(u" font-family: SofiaProSemiBold;\n"
" font-size: 32px;\n"
" font-weight: 400;\n"
" line-height: 57px;")

        self.verticalLayout_37.addWidget(self.label_dis)

        self.label_26 = QLabel(self.widget_25)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setPixmap(QPixmap(u":/im/images/images/Triangle_YES.png"))

        self.verticalLayout_37.addWidget(self.label_26)

        self.label_27 = QLabel(self.widget_25)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"color:rgb(140, 115, 255)")

        self.verticalLayout_37.addWidget(self.label_27)

        self.label_23 = QLabel(self.widget_25)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"box-shadow: 0px 2px 4px rgba(0,0,0,0.04);\n"
"background-color: rgb(255, 255, 255)\n"
"")
        self.label_23.setPixmap(QPixmap(u":/im/images/images/background.png"))
        self.label_23.setScaledContents(True)

        self.verticalLayout_37.addWidget(self.label_23)


        self.horizontalLayout_33.addWidget(self.widget_25)

        self.widget_27 = QWidget(self.widget_22)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setMinimumSize(QSize(0, 0))
        self.widget_27.setMaximumSize(QSize(16777215, 16777215))
        self.widget_27.setStyleSheet(u"box-shadow: 0px 2px 8px rgba(0,0,0,0.01);\n"
"background-color: rgb(255, 255, 255)\n"
"")
        self.verticalLayout_46 = QVBoxLayout(self.widget_27)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.label_33 = QLabel(self.widget_27)
        self.label_33.setObjectName(u"label_33")

        self.verticalLayout_46.addWidget(self.label_33)

        self.label_jours = QLabel(self.widget_27)
        self.label_jours.setObjectName(u"label_jours")
        self.label_jours.setStyleSheet(u" font-family: SofiaProSemiBold;\n"
" font-size: 32px;\n"
" font-weight: 400;\n"
" line-height: 57px;")

        self.verticalLayout_46.addWidget(self.label_jours)

        self.label_35 = QLabel(self.widget_27)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setPixmap(QPixmap(u":/im/images/images/Triangle_YES.png"))

        self.verticalLayout_46.addWidget(self.label_35)

        self.label_36 = QLabel(self.widget_27)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"color:rgb(140, 115, 255)")

        self.verticalLayout_46.addWidget(self.label_36)

        self.label_37 = QLabel(self.widget_27)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"box-shadow: 0px 2px 4px rgba(0,0,0,0.04);\n"
"background-color: rgb(255, 255, 255)\n"
"")
        self.label_37.setPixmap(QPixmap(u":/im/images/images/background.png"))
        self.label_37.setScaledContents(True)

        self.verticalLayout_46.addWidget(self.label_37)


        self.horizontalLayout_33.addWidget(self.widget_27)


        self.verticalLayout_35.addWidget(self.widget_22)

        self.widget_23 = QWidget(self.frame_18)
        self.widget_23.setObjectName(u"widget_23")
        self.verticalLayout_45 = QVBoxLayout(self.widget_23)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.widget_30 = QWidget(self.widget_23)
        self.widget_30.setObjectName(u"widget_30")
        self.verticalLayout_47 = QVBoxLayout(self.widget_30)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.label_29 = QLabel(self.widget_30)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_47.addWidget(self.label_29)

        self.widget_26 = QWidget(self.widget_30)
        self.widget_26.setObjectName(u"widget_26")
        self.verticalLayout_48 = QVBoxLayout(self.widget_26)
        self.verticalLayout_48.setSpacing(12)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.label_42 = QLabel(self.widget_26)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(0, 0))
        self.label_42.setMaximumSize(QSize(20, 16777215))
        self.label_42.setStyleSheet(u"background-color:rgb(108, 99, 255);\n"
" border-radius: 5px;\n"
" background-blend-mode: normal\n"
"")

        self.verticalLayout_48.addWidget(self.label_42)

        self.label_41 = QLabel(self.widget_26)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(0, 0))
        self.label_41.setMaximumSize(QSize(20, 16777215))
        self.label_41.setStyleSheet(u"background-color:rgb(255, 55, 255);\n"
" border-radius: 5px;\n"
" background-blend-mode: normal\n"
"")

        self.verticalLayout_48.addWidget(self.label_41)

        self.label_28 = QLabel(self.widget_26)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(0, 0))
        self.label_28.setMaximumSize(QSize(20, 16777215))
        self.label_28.setStyleSheet(u"background-color:rgb(255, 0, 0);\n"
" border-radius: 5px;\n"
" background-blend-mode: normal\n"
"")

        self.verticalLayout_48.addWidget(self.label_28)


        self.verticalLayout_47.addWidget(self.widget_26)

        self.widget_28 = QWidget(self.widget_30)
        self.widget_28.setObjectName(u"widget_28")
        self.horizontalLayout_34 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_38 = QLabel(self.widget_28)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMaximumSize(QSize(20, 20))
        self.label_38.setStyleSheet(u"background-color:rgb(108, 99, 255);")

        self.horizontalLayout_34.addWidget(self.label_38)

        self.label_30 = QLabel(self.widget_28)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"box-shadow: 0px 2px 4px rgba(0,0,0,0.04);\n"
"\n"
"")

        self.horizontalLayout_34.addWidget(self.label_30)

        self.label_39 = QLabel(self.widget_28)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(20, 20))
        self.label_39.setStyleSheet(u"background-color:rgb(255, 55, 255);")

        self.horizontalLayout_34.addWidget(self.label_39)

        self.label_32 = QLabel(self.widget_28)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"box-shadow: 0px 2px 4px rgba(0,0,0,0.04);\n"
"\n"
"")

        self.horizontalLayout_34.addWidget(self.label_32)

        self.label_40 = QLabel(self.widget_28)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(20, 20))
        self.label_40.setStyleSheet(u"background-color:rgb(255, 0, 0);")

        self.horizontalLayout_34.addWidget(self.label_40)

        self.label_31 = QLabel(self.widget_28)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"box-shadow: 0px 2px 4px rgba(0,0,0,0.04);\n"
"\n"
"")

        self.horizontalLayout_34.addWidget(self.label_31)


        self.verticalLayout_47.addWidget(self.widget_28)

        self.widget_29 = QWidget(self.widget_30)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setMaximumSize(QSize(16777215, 32))
        self.horizontalLayout_35 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_43 = QLabel(self.widget_29)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_35.addWidget(self.label_43)

        self.label_44 = QLabel(self.widget_29)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_35.addWidget(self.label_44)

        self.label_45 = QLabel(self.widget_29)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_35.addWidget(self.label_45)


        self.verticalLayout_47.addWidget(self.widget_29)


        self.verticalLayout_45.addWidget(self.widget_30)


        self.verticalLayout_35.addWidget(self.widget_23)


        self.verticalLayout_20.addWidget(self.frame_18)


        self.verticalLayout_34.addWidget(self.widget_19)

        self.stackedWidget_4.addWidget(self.widgets_dashboard)
        self.page_test = QWidget()
        self.page_test.setObjectName(u"page_test")
        self.horizontalLayout_40 = QHBoxLayout(self.page_test)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.widget_34 = QWidget(self.page_test)
        self.widget_34.setObjectName(u"widget_34")
        self.verticalLayout_54 = QVBoxLayout(self.widget_34)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.label_20 = QLabel(self.widget_34)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(16777215, 30))
        font11 = QFont()
        font11.setPointSize(11)
        self.label_20.setFont(font11)

        self.verticalLayout_54.addWidget(self.label_20)

        self.widget_36 = QWidget(self.widget_34)
        self.widget_36.setObjectName(u"widget_36")
        self.verticalLayout_51 = QVBoxLayout(self.widget_36)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(-1, -1, -1, 9)
        self.label_24 = QLabel(self.widget_36)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_51.addWidget(self.label_24)

        self.lineEdit_3 = QLineEdit(self.widget_36)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_51.addWidget(self.lineEdit_3)

        self.label_34 = QLabel(self.widget_36)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_51.addWidget(self.label_34)

        self.lineEdit_2 = QLineEdit(self.widget_36)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_51.addWidget(self.lineEdit_2)

        self.label_49 = QLabel(self.widget_36)
        self.label_49.setObjectName(u"label_49")

        self.verticalLayout_51.addWidget(self.label_49)

        self.lineEdit_age = QLineEdit(self.widget_36)
        self.lineEdit_age.setObjectName(u"lineEdit_age")

        self.verticalLayout_51.addWidget(self.lineEdit_age)

        self.label_50 = QLabel(self.widget_36)
        self.label_50.setObjectName(u"label_50")

        self.verticalLayout_51.addWidget(self.label_50)

        self.lineEdit_4 = QLineEdit(self.widget_36)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_51.addWidget(self.lineEdit_4)


        self.verticalLayout_54.addWidget(self.widget_36)

        self.pushButton_check = QPushButton(self.widget_34)
        self.pushButton_check.setObjectName(u"pushButton_check")
        self.pushButton_check.setStyleSheet(u"background-color:rgb(108, 99, 255);color:white")

        self.verticalLayout_54.addWidget(self.pushButton_check)


        self.horizontalLayout_40.addWidget(self.widget_34)

        self.widget_37 = QWidget(self.page_test)
        self.widget_37.setObjectName(u"widget_37")
        self.widget_37.setMinimumSize(QSize(400, 0))
        self.verticalLayout_55 = QVBoxLayout(self.widget_37)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.widget_41 = QWidget(self.widget_37)
        self.widget_41.setObjectName(u"widget_41")
        self.widget_41.setMaximumSize(QSize(16777215, 50))
        self.verticalLayout_56 = QVBoxLayout(self.widget_41)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.label_52 = QLabel(self.widget_41)
        self.label_52.setObjectName(u"label_52")

        self.verticalLayout_56.addWidget(self.label_52, 0, Qt.AlignHCenter)


        self.verticalLayout_55.addWidget(self.widget_41)

        self.widget_42 = QWidget(self.widget_37)
        self.widget_42.setObjectName(u"widget_42")
        self.verticalLayout_57 = QVBoxLayout(self.widget_42)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.label_comment_result = QLabel(self.widget_42)
        self.label_comment_result.setObjectName(u"label_comment_result")
        self.label_comment_result.setMinimumSize(QSize(0, 200))
        self.label_comment_result.setAlignment(Qt.AlignCenter)

        self.verticalLayout_57.addWidget(self.label_comment_result, 0, Qt.AlignTop)

        self.pushButton_import_program = QPushButton(self.widget_42)
        self.pushButton_import_program.setObjectName(u"pushButton_import_program")
        self.pushButton_import_program.setStyleSheet(u"background-color:rgb(108, 99, 255);color:white")

        self.verticalLayout_57.addWidget(self.pushButton_import_program)


        self.verticalLayout_55.addWidget(self.widget_42)


        self.horizontalLayout_40.addWidget(self.widget_37)

        self.widget_35 = QWidget(self.page_test)
        self.widget_35.setObjectName(u"widget_35")

        self.horizontalLayout_40.addWidget(self.widget_35)

        self.stackedWidget_4.addWidget(self.page_test)
        self.page_progammes = QWidget()
        self.page_progammes.setObjectName(u"page_progammes")
        self.verticalLayout_43 = QVBoxLayout(self.page_progammes)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.widget_32 = QWidget(self.page_progammes)
        self.widget_32.setObjectName(u"widget_32")
        self.widget_32.setStyleSheet(u"background-color:none")
        self.verticalLayout_44 = QVBoxLayout(self.widget_32)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.label_46 = QLabel(self.widget_32)
        self.label_46.setObjectName(u"label_46")

        self.verticalLayout_44.addWidget(self.label_46)

        self.tableWidget = QTableWidget(self.widget_32)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 4):
            self.tableWidget.setRowCount(4)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(3, 1, __qtablewidgetitem11)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_44.addWidget(self.tableWidget)

        self.label_47 = QLabel(self.widget_32)
        self.label_47.setObjectName(u"label_47")

        self.verticalLayout_44.addWidget(self.label_47)

        self.plainTextEdit = QPlainTextEdit(self.widget_32)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_44.addWidget(self.plainTextEdit)

        self.label_57 = QLabel(self.widget_32)
        self.label_57.setObjectName(u"label_57")

        self.verticalLayout_44.addWidget(self.label_57)

        self.widget_45 = QWidget(self.widget_32)
        self.widget_45.setObjectName(u"widget_45")
        self.widget_45.setMinimumSize(QSize(0, 100))
        self.horizontalLayout_44 = QHBoxLayout(self.widget_45)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.widget_43 = QWidget(self.widget_45)
        self.widget_43.setObjectName(u"widget_43")
        self.widget_43.setMaximumSize(QSize(161, 16777215))
        self.verticalLayout_59 = QVBoxLayout(self.widget_43)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.label_54 = QLabel(self.widget_43)
        self.label_54.setObjectName(u"label_54")

        self.verticalLayout_59.addWidget(self.label_54)

        self.label_55 = QLabel(self.widget_43)
        self.label_55.setObjectName(u"label_55")

        self.verticalLayout_59.addWidget(self.label_55)

        self.label_56 = QLabel(self.widget_43)
        self.label_56.setObjectName(u"label_56")

        self.verticalLayout_59.addWidget(self.label_56)


        self.horizontalLayout_44.addWidget(self.widget_43)

        self.widget_44 = QWidget(self.widget_45)
        self.widget_44.setObjectName(u"widget_44")
        self.verticalLayout_58 = QVBoxLayout(self.widget_44)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.pushButton_seance1 = QPushButton(self.widget_44)
        self.pushButton_seance1.setObjectName(u"pushButton_seance1")
        self.pushButton_seance1.setStyleSheet(u"color:black")
        self.pushButton_seance1.setCheckable(True)

        self.verticalLayout_58.addWidget(self.pushButton_seance1)

        self.pushButton_seance2 = QPushButton(self.widget_44)
        self.pushButton_seance2.setObjectName(u"pushButton_seance2")
        self.pushButton_seance2.setStyleSheet(u"color:black")
        self.pushButton_seance2.setCheckable(True)

        self.verticalLayout_58.addWidget(self.pushButton_seance2)

        self.pushButton_seance3 = QPushButton(self.widget_44)
        self.pushButton_seance3.setObjectName(u"pushButton_seance3")
        self.pushButton_seance3.setStyleSheet(u"color:black")
        self.pushButton_seance3.setCheckable(True)

        self.verticalLayout_58.addWidget(self.pushButton_seance3)


        self.horizontalLayout_44.addWidget(self.widget_44, 0, Qt.AlignLeft)


        self.verticalLayout_44.addWidget(self.widget_45)


        self.verticalLayout_43.addWidget(self.widget_32)

        self.stackedWidget_4.addWidget(self.page_progammes)
        self.Home_logo = QWidget()
        self.Home_logo.setObjectName(u"Home_logo")
        self.verticalLayout_39 = QVBoxLayout(self.Home_logo)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_15 = QLabel(self.Home_logo)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 0))
        self.label_15.setPixmap(QPixmap(u":/im/images/images/OIP (1).jpg"))
        self.label_15.setScaledContents(False)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_39.addWidget(self.label_15)

        self.stackedWidget_4.addWidget(self.Home_logo)

        self.verticalLayout_33.addWidget(self.stackedWidget_4)


        self.horizontalLayout_32.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_40.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.topMenus)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font3)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_42.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font3)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_42.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font3)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_42.addWidget(self.btn_logout)


        self.verticalLayout_41.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_40.addWidget(self.contentSettings)


        self.horizontalLayout_32.addWidget(self.extraRightBox)


        self.verticalLayout_32.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setStyleSheet(u"background-color:white;")
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font12 = QFont()
        font12.setFamilies([u"Segoe UI"])
        font12.setPointSize(10)
        font12.setBold(True)
        font12.setItalic(False)
        self.creditsLabel.setFont(font12)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_36.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        font13 = QFont()
        font13.setPointSize(10)
        self.version.setFont(font13)
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_36.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_36.addWidget(self.frame_size_grip)


        self.verticalLayout_32.addWidget(self.bottomBar)


        self.verticalLayout_31.addWidget(self.contentBottom)


        self.horizontalLayout_38.addWidget(self.contentBox)


        self.horizontalLayout_37.addWidget(self.bgApp)


        self.horizontalLayout_28.addWidget(self.widget_21)

        self.stackedWidget.addWidget(self.page_main)
        self.page_connexion = QWidget()
        self.page_connexion.setObjectName(u"page_connexion")
        self.horizontalLayout_11 = QHBoxLayout(self.page_connexion)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.widget_11 = QWidget(self.page_connexion)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_12 = QLabel(self.widget_11)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(340, 400))
        self.label_12.setMaximumSize(QSize(300, 634))
        self.label_12.setStyleSheet(u"background-color:white;")
        self.label_12.setPixmap(QPixmap(u":/im/images/images/R.png"))
        self.label_12.setScaledContents(True)

        self.horizontalLayout_21.addWidget(self.label_12)


        self.horizontalLayout_11.addWidget(self.widget_11)

        self.frame_8 = QFrame(self.page_connexion)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 0))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_8)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 0))
        self.frame_10.setMaximumSize(QSize(16777215, 66))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_13.setSpacing(2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.widget_button_3 = QWidget(self.frame_10)
        self.widget_button_3.setObjectName(u"widget_button_3")
        self.widget_button_3.setMinimumSize(QSize(0, 0))
        self.widget_button_3.setLayoutDirection(Qt.RightToLeft)
        self.horizontalLayout_12 = QHBoxLayout(self.widget_button_3)
        self.horizontalLayout_12.setSpacing(2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.pushButton_9 = QPushButton(self.widget_button_3)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFlat(True)

        self.horizontalLayout_12.addWidget(self.pushButton_9)

        self.pushButton_20 = QPushButton(self.widget_button_3)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setFlat(True)

        self.horizontalLayout_12.addWidget(self.pushButton_20)

        self.pushButton_12 = QPushButton(self.widget_button_3)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setFlat(True)

        self.horizontalLayout_12.addWidget(self.pushButton_12)


        self.horizontalLayout_13.addWidget(self.widget_button_3, 0, Qt.AlignHCenter)


        self.verticalLayout_10.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 400))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 37, -1, -1)
        self.verticalWidget = QWidget(self.frame_9)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalLayout_11 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_11.setSpacing(41)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_11 = QLabel(self.verticalWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_11, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_11 = QFrame(self.verticalWidget)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(300, 200))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_11)
        self.verticalLayout_12.setSpacing(36)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_10 = QWidget(self.frame_11)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_9 = QVBoxLayout(self.widget_10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lineEdit_connexion_email = QLineEdit(self.widget_10)
        self.lineEdit_connexion_email.setObjectName(u"lineEdit_connexion_email")
        sizePolicy.setHeightForWidth(self.lineEdit_connexion_email.sizePolicy().hasHeightForWidth())
        self.lineEdit_connexion_email.setSizePolicy(sizePolicy)
        self.lineEdit_connexion_email.setMinimumSize(QSize(0, 40))
        font14 = QFont()
        font14.setPointSize(13)
        self.lineEdit_connexion_email.setFont(font14)
        self.lineEdit_connexion_email.setStyleSheet(u"#lineEdit_connexion_email{\n"
"	border:2px solid;\n"
"	border-top:none;\n"
"	border-left:none;\n"
"	border-right:none;\n"
"\n"
"}\n"
"\n"
"#lineEdit_connexion_email:hover{\n"
"	border:2px solid rgb(108, 99, 255);\n"
"	border-top:none;\n"
"	border-left:none;\n"
"	border-right:none;\n"
"\n"
"}")

        self.verticalLayout_9.addWidget(self.lineEdit_connexion_email)


        self.verticalLayout_12.addWidget(self.widget_10)

        self.widget_7 = QWidget(self.frame_11)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_15 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.lineEdit_connexion_passwd = QLineEdit(self.widget_7)
        self.lineEdit_connexion_passwd.setObjectName(u"lineEdit_connexion_passwd")
        sizePolicy.setHeightForWidth(self.lineEdit_connexion_passwd.sizePolicy().hasHeightForWidth())
        self.lineEdit_connexion_passwd.setSizePolicy(sizePolicy)
        self.lineEdit_connexion_passwd.setMinimumSize(QSize(200, 40))
        self.lineEdit_connexion_passwd.setFont(font)
        self.lineEdit_connexion_passwd.setStyleSheet(u"#lineEdit_connexion_passwd{\n"
"	border:2px solid;\n"
"	border-top:none;\n"
"	border-left:none;\n"
"	border-right:none;\n"
"\n"
"}\n"
"#lineEdit_connexion_passwd:hover{\n"
"	border:2px solid rgb(108, 99, 255);\n"
"	border-top:none;\n"
"	border-left:none;\n"
"	border-right:none;\n"
"\n"
"}")

        self.horizontalLayout_15.addWidget(self.lineEdit_connexion_passwd)


        self.verticalLayout_12.addWidget(self.widget_7)

        self.pushButton_LOGIN = QPushButton(self.frame_11)
        self.pushButton_LOGIN.setObjectName(u"pushButton_LOGIN")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton_LOGIN.sizePolicy().hasHeightForWidth())
        self.pushButton_LOGIN.setSizePolicy(sizePolicy5)
        self.pushButton_LOGIN.setMinimumSize(QSize(150, 40))

        self.verticalLayout_12.addWidget(self.pushButton_LOGIN, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.frame_11)


        self.horizontalLayout_14.addWidget(self.verticalWidget, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_10.addWidget(self.frame_9)

        self.widget_6 = QWidget(self.frame_8)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(0, 60))

        self.verticalLayout_10.addWidget(self.widget_6)


        self.horizontalLayout_11.addWidget(self.frame_8)

        self.stackedWidget.addWidget(self.page_connexion)
        self.page_Inscription = QWidget()
        self.page_Inscription.setObjectName(u"page_Inscription")
        self.horizontalLayout_20 = QHBoxLayout(self.page_Inscription)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.widget_13 = QWidget(self.page_Inscription)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_14 = QLabel(self.widget_13)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(340, 400))
        self.label_14.setMaximumSize(QSize(340, 634))
        self.label_14.setPixmap(QPixmap(u":/im/images/images/Girl-dancer-scaled.jpg"))
        self.label_14.setScaledContents(True)

        self.horizontalLayout_22.addWidget(self.label_14)


        self.horizontalLayout_20.addWidget(self.widget_13)

        self.frame_12 = QFrame(self.page_Inscription)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_12)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, -1, -1)
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 66))
        self.frame_13.setMaximumSize(QSize(16777215, 66))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_16.setSpacing(2)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.widget_button_4 = QWidget(self.frame_13)
        self.widget_button_4.setObjectName(u"widget_button_4")
        self.widget_button_4.setMinimumSize(QSize(0, 0))
        self.widget_button_4.setLayoutDirection(Qt.RightToLeft)
        self.horizontalLayout_17 = QHBoxLayout(self.widget_button_4)
        self.horizontalLayout_17.setSpacing(2)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.pushButton_13 = QPushButton(self.widget_button_4)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setFlat(True)

        self.horizontalLayout_17.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.widget_button_4)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setFlat(True)

        self.horizontalLayout_17.addWidget(self.pushButton_14)

        self.pushButton_16 = QPushButton(self.widget_button_4)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setFlat(True)

        self.horizontalLayout_17.addWidget(self.pushButton_16)


        self.horizontalLayout_16.addWidget(self.widget_button_4, 0, Qt.AlignHCenter)


        self.verticalLayout_13.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 400))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalWidget_2 = QWidget(self.frame_14)
        self.verticalWidget_2.setObjectName(u"verticalWidget_2")
        self.verticalLayout_14 = QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_14.setSpacing(41)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_13 = QLabel(self.verticalWidget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_13, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_15 = QFrame(self.verticalWidget_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(200, 200))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_15)
        self.verticalLayout_15.setSpacing(9)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.widget_12 = QWidget(self.frame_15)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_16 = QVBoxLayout(self.widget_12)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.lineEdit_ins_name = QLineEdit(self.widget_12)
        self.lineEdit_ins_name.setObjectName(u"lineEdit_ins_name")
        sizePolicy.setHeightForWidth(self.lineEdit_ins_name.sizePolicy().hasHeightForWidth())
        self.lineEdit_ins_name.setSizePolicy(sizePolicy)
        self.lineEdit_ins_name.setMinimumSize(QSize(0, 40))
        self.lineEdit_ins_name.setFont(font14)
        self.lineEdit_ins_name.setStyleSheet(u"#lineEdit_ins_name{\n"
"	border:2px solid;\n"
"	border-top:none;\n"
"	border-left:none;\n"
"	border-right:none;\n"
"\n"
"}\n"
"\n"
"#lineEdit_ins_name:hover{\n"
"	border:2px solid rgb(108, 99, 255);\n"
"	border-top:none;\n"
"	border-left:none;\n"
"	border-right:none;\n"
"\n"
"}")

        self.verticalLayout_16.addWidget(self.lineEdit_ins_name)


        self.verticalLayout_15.addWidget(self.widget_12)

        self.widget_8 = QWidget(self.frame_15)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_19 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.lineEdit_ins_email = QLineEdit(self.widget_8)
        self.lineEdit_ins_email.setObjectName(u"lineEdit_ins_email")
        sizePolicy.setHeightForWidth(self.lineEdit_ins_email.sizePolicy().hasHeightForWidth())
        self.lineEdit_ins_email.setSizePolicy(sizePolicy)
        self.lineEdit_ins_email.setMinimumSize(QSize(250, 40))
        self.lineEdit_ins_email.setFont(font)
        self.lineEdit_ins_email.setStyleSheet(u"#lineEdit_ins_email{\n"
"	border:2px solid;\n"
"	border-top:none;\n"
"	border-left:none;\n"
"	border-right:none;\n"
"\n"
"}\n"
"\n"
"#lineEdit_ins_email:hover{\n"
"	border:2px solid rgb(108, 99, 255);\n"
"	border-top:none;\n"
"	border-left:none;\n"
"	border-right:none;\n"
"\n"
"}")

        self.horizontalLayout_19.addWidget(self.lineEdit_ins_email)


        self.verticalLayout_15.addWidget(self.widget_8)

        self.widget_17 = QWidget(self.frame_15)
        self.widget_17.setObjectName(u"widget_17")
        self.verticalLayout_21 = QVBoxLayout(self.widget_17)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.lineEdit_ins_password = QLineEdit(self.widget_17)
        self.lineEdit_ins_password.setObjectName(u"lineEdit_ins_password")
        sizePolicy.setHeightForWidth(self.lineEdit_ins_password.sizePolicy().hasHeightForWidth())
        self.lineEdit_ins_password.setSizePolicy(sizePolicy)
        self.lineEdit_ins_password.setMinimumSize(QSize(250, 40))
        self.lineEdit_ins_password.setFont(font)
        self.lineEdit_ins_password.setStyleSheet(u"#lineEdit_ins_password{\n"
"	border:2px solid;\n"
"	border-top:none;\n"
"	border-left:none;\n"
"	border-right:none;\n"
"\n"
"}\n"
"\n"
"#lineEdit_ins_password:hover{\n"
"	border:2px solid rgb(108, 99, 255);\n"
"	border-top:none;\n"
"	border-left:none;\n"
"	border-right:none;\n"
"\n"
"}")

        self.verticalLayout_21.addWidget(self.lineEdit_ins_password)


        self.verticalLayout_15.addWidget(self.widget_17)

        self.widget_18 = QWidget(self.frame_15)
        self.widget_18.setObjectName(u"widget_18")
        self.verticalLayout_22 = QVBoxLayout(self.widget_18)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.lineEdit_ins_verifypasswd = QLineEdit(self.widget_18)
        self.lineEdit_ins_verifypasswd.setObjectName(u"lineEdit_ins_verifypasswd")
        sizePolicy.setHeightForWidth(self.lineEdit_ins_verifypasswd.sizePolicy().hasHeightForWidth())
        self.lineEdit_ins_verifypasswd.setSizePolicy(sizePolicy)
        self.lineEdit_ins_verifypasswd.setMinimumSize(QSize(250, 40))
        self.lineEdit_ins_verifypasswd.setFont(font)
        self.lineEdit_ins_verifypasswd.setStyleSheet(u"#lineEdit_ins_verifypasswd{\n"
"	border:2px solid;\n"
"	border-top:none;\n"
"	border-left:none;\n"
"	border-right:none;\n"
"\n"
"}\n"
"\n"
"#lineEdit_ins_verifypasswd:hover{\n"
"	border:2px solid rgb(108, 99, 255);\n"
"	border-top:none;\n"
"	border-left:none;\n"
"	border-right:none;\n"
"\n"
"}")

        self.verticalLayout_22.addWidget(self.lineEdit_ins_verifypasswd)


        self.verticalLayout_15.addWidget(self.widget_18)

        self.pushButton_INSCRIPTION = QPushButton(self.frame_15)
        self.pushButton_INSCRIPTION.setObjectName(u"pushButton_INSCRIPTION")
        sizePolicy5.setHeightForWidth(self.pushButton_INSCRIPTION.sizePolicy().hasHeightForWidth())
        self.pushButton_INSCRIPTION.setSizePolicy(sizePolicy5)
        self.pushButton_INSCRIPTION.setMinimumSize(QSize(150, 40))

        self.verticalLayout_15.addWidget(self.pushButton_INSCRIPTION, 0, Qt.AlignHCenter)


        self.verticalLayout_14.addWidget(self.frame_15)


        self.horizontalLayout_18.addWidget(self.verticalWidget_2, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_13.addWidget(self.frame_14)

        self.widget_9 = QWidget(self.frame_12)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 60))

        self.verticalLayout_13.addWidget(self.widget_9)


        self.horizontalLayout_20.addWidget(self.frame_12)

        self.stackedWidget.addWidget(self.page_Inscription)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(1)
        self.stackedWidget_4.setCurrentIndex(3)
        self.stackedWidget_34.setCurrentIndex(1)
        self.listWidget_2.setCurrentRow(-1)
        self.listWidget_3.setCurrentRow(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_logo.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>software@ </p><p>by yvesmarius</p></body></html>", None))
        self.label_welcome.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>BIENVENUE SUR FITNESS </p><p>GYM</p></body></html>", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Need Help?", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Connexion", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Inscription", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Des programmes minceurs </p><p>et alimentaires </p><p>fait pour vous</p></body></html>", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"suivi de votre progression", None))
        self.label_7.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Nos equipes d expert a votre </p><p>ecoute 24h/24</p></body></html>", None))
        self.label_4.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Dianostique de sante ", None))
        self.label_9.setText("")
        self.pushButton_move_main_app.setText(QCoreApplication.translate("MainWindow", u"continuer", None))
        self.label_logo_2.setText("")
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Need Help?", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Connexion", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Inscription", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"Fitness Gym", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"NaN Project", None))
        self.label_17.setText("")
#if QT_CONFIG(tooltip)
        self.toggleButton.setToolTip(QCoreApplication.translate("MainWindow", u"hide", None))
#endif // QT_CONFIG(tooltip)
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
#if QT_CONFIG(tooltip)
        self.btn_home.setToolTip(QCoreApplication.translate("MainWindow", u"home", None))
#endif // QT_CONFIG(tooltip)
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.btn_dashboard.setToolTip(QCoreApplication.translate("MainWindow", u"Dashboard", None))
#endif // QT_CONFIG(tooltip)
        self.btn_dashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
#if QT_CONFIG(tooltip)
        self.btn_program.setToolTip(QCoreApplication.translate("MainWindow", u"Calendrier", None))
#endif // QT_CONFIG(tooltip)
        self.btn_program.setText(QCoreApplication.translate("MainWindow", u"Program", None))
#if QT_CONFIG(tooltip)
        self.btn_test.setToolTip(QCoreApplication.translate("MainWindow", u"Test de sante", None))
#endif // QT_CONFIG(tooltip)
        self.btn_test.setText(QCoreApplication.translate("MainWindow", u"Test", None))
#if QT_CONFIG(tooltip)
        self.btn_messages.setToolTip(QCoreApplication.translate("MainWindow", u"contactez expert", None))
#endif // QT_CONFIG(tooltip)
        self.btn_messages.setText(QCoreApplication.translate("MainWindow", u"service expert", None))
#if QT_CONFIG(tooltip)
        self.toggleLeftBox.setToolTip(QCoreApplication.translate("MainWindow", u"settings", None))
#endif // QT_CONFIG(tooltip)
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_profile.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.btn_session_admin.setText(QCoreApplication.translate("MainWindow", u"Session Admin", None))
        self.btn_update.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700; color:#000000;\">FitnessGym</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#7f7f7f;\">Interface creer avec pyqt designer et python</span> </p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><sp"
                        "an style=\" font-size:10pt; color:#878787;\">NaN License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#bd93f9;\">Created by: YVES MARIUS</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#e445f9;\">MERCI BEAUCOUP!!!!</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; color:#bd93f9;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Desktop App Version 5.22", None))
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"non_disponible", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Deconnexion", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\"> MES CONTACTS </span></p></body></html>", None))
        self.pushButton_add_contact.setText(QCoreApplication.translate("MainWindow", u"Add Contacts", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Bloquer", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u" remove contacts", None))
        self.label_img_chat.setText("")
        self.label_Name_chat.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">COACH FRANCIS</span></p></body></html>", None))
        self.label_51.setText("")
        self.pushButton_25.setText("")
        self.pushButton_26.setText("")
        self.lineEdit_send.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Saissisez votre message........", None))
        self.pushButton_send.setText(QCoreApplication.translate("MainWindow", u"SEND", None))
        self.pushButton_return_contact.setText(QCoreApplication.translate("MainWindow", u"RETOUR", None))

        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_3.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"ALEXIA CAOCH SPORTIF", None));
        ___qlistwidgetitem1 = self.listWidget_3.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"COACH FRANCOIS ALIMENTAIRES", None));
        ___qlistwidgetitem2 = self.listWidget_3.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"MILICA SMITH USER", None));
        self.listWidget_3.setSortingEnabled(__sortingEnabled)

        self.pushButton_add_in_contact.setText(QCoreApplication.translate("MainWindow", u"Ajouter dans contacts", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">DASHBOARD</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Poids perdu", None))
        self.label_poids.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">50KG</span></p></body></html>", None))
        self.label_21.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">20 KG</span></p></body></html>", None))
        self.label_18.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Distance Total", None))
        self.label_dis.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">2.5 KM</span></p></body></html>", None))
        self.label_26.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">500 m</span></p></body></html>", None))
        self.label_23.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Train Day", None))
        self.label_jours.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">4 J</span></p></body></html>", None))
        self.label_35.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">3 jours</span></p></body></html>", None))
        self.label_37.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Activite</span></p></body></html>", None))
        self.label_38.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Taux d'activite", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Progression ", None))
        self.label_40.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">20%</span></p></body></html>", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">20%</span></p></body></html>", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">20%</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">TEST</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Combien de kilo faites vous(estimaton)", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"exple: 65", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Avez vous des problemes cardiaques?", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Oui  ou Non", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"votre age ?", None))
        self.lineEdit_age.setPlaceholderText(QCoreApplication.translate("MainWindow", u"exple 29", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u" votre Taille?", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"exple: 1m90", None))
        self.pushButton_check.setText(QCoreApplication.translate("MainWindow", u"CHECK", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Resultats</span></p></body></html>", None))
        self.label_comment_result.setText(QCoreApplication.translate("MainWindow", u"No Data", None))
        self.pushButton_import_program.setText(QCoreApplication.translate("MainWindow", u"import program", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">PROGRAMME SPORTIF</span></p></body></html>", None))

        __sortingEnabled1 = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled1)

        self.label_47.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">PROGRAMME ALIMENTAIRES</span></p></body></html>", None))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"........HERE.......", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Progression</span></p></body></html>", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">seance 1</span></p></body></html>", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">seance 2</span></p></body></html>", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">seance 3</span></p></body></html>", None))
        self.pushButton_seance1.setText(QCoreApplication.translate("MainWindow", u"Passed", None))
        self.pushButton_seance2.setText(QCoreApplication.translate("MainWindow", u"Passed", None))
        self.pushButton_seance3.setText(QCoreApplication.translate("MainWindow", u"Passed", None))
        self.label_15.setText("")
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By yves marius", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v5.22", None))
        self.label_12.setText("")
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Need Help?", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Inscription", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"CONNECTEZ-VOUS", None))
        self.lineEdit_connexion_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lineEdit_connexion_passwd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.pushButton_LOGIN.setText(QCoreApplication.translate("MainWindow", u"GO!!!!", None))
        self.label_14.setText("")
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Need Help?", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Connexion", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"INSCRIVEZ-VOUS ", None))
        self.lineEdit_ins_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom", None))
        self.lineEdit_ins_email.setText("")
        self.lineEdit_ins_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lineEdit_ins_password.setText("")
        self.lineEdit_ins_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_ins_verifypasswd.setText("")
        self.lineEdit_ins_verifypasswd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Verify Password", None))
        self.pushButton_INSCRIPTION.setText(QCoreApplication.translate("MainWindow", u"START", None))
    # retranslateUi

