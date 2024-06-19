# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceVCEDrX.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

from Custom_Widgets.AnalogGaugeWidget import AnalogGaugeWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 740)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(1280, 720))
        self.Header_Frame = QFrame(self.centralwidget)
        self.Header_Frame.setObjectName(u"Header_Frame")
        self.Header_Frame.setGeometry(QRect(0, 0, 1280, 80))
        sizePolicy.setHeightForWidth(self.Header_Frame.sizePolicy().hasHeightForWidth())
        self.Header_Frame.setSizePolicy(sizePolicy)
        self.Header_Frame.setFrameShape(QFrame.StyledPanel)
        self.Header_Frame.setFrameShadow(QFrame.Raised)
        self.Header_Left = QFrame(self.Header_Frame)
        self.Header_Left.setObjectName(u"Header_Left")
        self.Header_Left.setEnabled(True)
        self.Header_Left.setGeometry(QRect(0, 0, 80, 80))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Header_Left.sizePolicy().hasHeightForWidth())
        self.Header_Left.setSizePolicy(sizePolicy1)
        self.Header_Left.setFrameShape(QFrame.StyledPanel)
        self.Header_Left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Header_Left)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lb_Left_Signal = QLabel(self.Header_Left)
        self.lb_Left_Signal.setObjectName(u"lb_Left_Signal")
        self.lb_Left_Signal.setPixmap(QPixmap(u"images/left_arrow_small.png"))
        self.lb_Left_Signal.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lb_Left_Signal)

        self.Header_Title = QFrame(self.Header_Frame)
        self.Header_Title.setObjectName(u"Header_Title")
        self.Header_Title.setGeometry(QRect(80, 0, 1120, 80))
        sizePolicy1.setHeightForWidth(self.Header_Title.sizePolicy().hasHeightForWidth())
        self.Header_Title.setSizePolicy(sizePolicy1)
        self.Header_Title.setFrameShape(QFrame.StyledPanel)
        self.Header_Title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Header_Title)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lb_Title = QLabel(self.Header_Title)
        self.lb_Title.setObjectName(u"lb_Title")
        self.lb_Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lb_Title)

        self.Header_Right = QFrame(self.Header_Frame)
        self.Header_Right.setObjectName(u"Header_Right")
        self.Header_Right.setGeometry(QRect(1200, 0, 80, 80))
        sizePolicy1.setHeightForWidth(self.Header_Right.sizePolicy().hasHeightForWidth())
        self.Header_Right.setSizePolicy(sizePolicy1)
        self.Header_Right.setFrameShape(QFrame.StyledPanel)
        self.Header_Right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Header_Right)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lb_Right_Signal = QLabel(self.Header_Right)
        self.lb_Right_Signal.setObjectName(u"lb_Right_Signal")
        self.lb_Right_Signal.setPixmap(QPixmap(u"images/right_arrow_small.png"))
        self.lb_Right_Signal.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lb_Right_Signal)

        self.WebviewFrame = QFrame(self.centralwidget)
        self.WebviewFrame.setObjectName(u"WebviewFrame")
        self.WebviewFrame.setGeometry(QRect(0, 400, 1280, 340))
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.WebviewFrame.sizePolicy().hasHeightForWidth())
        self.WebviewFrame.setSizePolicy(sizePolicy2)
        self.WebviewFrame.setFrameShape(QFrame.StyledPanel)
        self.WebviewFrame.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.WebviewFrame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 1280, 340))
        self.lb_Web = QLabel(self.widget)
        self.lb_Web.setObjectName(u"lb_Web")
        self.lb_Web.setGeometry(QRect(0, 0, 1280, 340))
        self.BodyFrame = QFrame(self.centralwidget)
        self.BodyFrame.setObjectName(u"BodyFrame")
        self.BodyFrame.setGeometry(QRect(0, 80, 1280, 320))
        sizePolicy.setHeightForWidth(self.BodyFrame.sizePolicy().hasHeightForWidth())
        self.BodyFrame.setSizePolicy(sizePolicy)
        self.BodyFrame.setFrameShape(QFrame.StyledPanel)
        self.BodyFrame.setFrameShadow(QFrame.Raised)
        self.Body_Left_Frame = QFrame(self.BodyFrame)
        self.Body_Left_Frame.setObjectName(u"Body_Left_Frame")
        self.Body_Left_Frame.setGeometry(QRect(0, 0, 480, 320))
        self.Body_Left_Frame.setFrameShape(QFrame.StyledPanel)
        self.Body_Left_Frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.Body_Left_Frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 480, 320))
        self.label.setAlignment(Qt.AlignCenter)
        self.Body_Center_Frame = QFrame(self.BodyFrame)
        self.Body_Center_Frame.setObjectName(u"Body_Center_Frame")
        self.Body_Center_Frame.setGeometry(QRect(480, 0, 320, 320))
        self.Body_Center_Frame.setFrameShape(QFrame.StyledPanel)
        self.Body_Center_Frame.setFrameShadow(QFrame.Raised)
        self.Analog_Gauge_Speed = AnalogGaugeWidget(self.Body_Center_Frame)
        self.Analog_Gauge_Speed.setObjectName(u"Analog_Gauge_Speed")
        self.Analog_Gauge_Speed.setGeometry(QRect(0, 0, 320, 320))
        self.Body_Right_Frame = QFrame(self.BodyFrame)
        self.Body_Right_Frame.setObjectName(u"Body_Right_Frame")
        self.Body_Right_Frame.setGeometry(QRect(800, 0, 480, 320))
        self.Body_Right_Frame.setFrameShape(QFrame.StyledPanel)
        self.Body_Right_Frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.Body_Right_Frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 480, 320))
        self.label_2.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lb_Left_Signal.setText("")
        self.lb_Title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:36pt; font-weight:600; color:#0000ff;\">UIT CAR DASHBOARD</span></p></body></html>", None))
        self.lb_Right_Signal.setText("")
        self.lb_Web.setText(QCoreApplication.translate("MainWindow", u"Webpage", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Raw_Img", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Output", None))
    # retranslateUi

