# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PreferenceUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.setWindowModality(Qt.ApplicationModal)
        Form.resize(1966, 1330)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush1 = QBrush(QColor(240, 240, 240, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        Form.setPalette(palette)
        Form.setFocusPolicy(Qt.StrongFocus)
        Form.setContextMenuPolicy(Qt.NoContextMenu)
        Form.setWindowTitle("Preferences")
        Form.setInputMethodHints(Qt.ImhNone)
        self.widget = QWidget(Form)
        self.widget.setObjectName("widget")
        self.widget.setGeometry(QRect(10, 525, 421, 56))
        self.label = QLabel(self.widget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(10, 5, 401, 16))
        font = QFont()
        font.setItalic(True)
        self.label.setFont(font)
        self.layoutWidget_2 = QWidget(self.widget)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 30, 397, 19))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.EnableDebug = Gui_PrefCheckBox(self.layoutWidget_2)
        self.EnableDebug.setObjectName("EnableDebug")
        self.EnableDebug.setChecked(False)
        self.EnableDebug.setProperty("prefEntry", QByteArray("EnableDebug"))
        self.EnableDebug.setProperty("prefPath", QByteArray("Mod/TitleBlock Workbench"))

        self.horizontalLayout.addWidget(self.EnableDebug)

        self.label_11 = QLabel(self.layoutWidget_2)
        self.label_11.setObjectName("label_11")

        self.horizontalLayout.addWidget(self.label_11)

        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setGeometry(QRect(5, 5, 456, 516))
        self.tabWidget.setAutoFillBackground(False)
        self.TitleBlock = QWidget()
        self.TitleBlock.setObjectName("TitleBlock")
        self.scrollArea = QScrollArea(self.TitleBlock)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 451, 491))
        self.scrollArea.setFocusPolicy(Qt.NoFocus)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 434, 805))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_DrawingNumber = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_DrawingNumber.setObjectName("groupBox_DrawingNumber")
        self.groupBox_DrawingNumber.setEnabled(True)
        self.groupBox_DrawingNumber.setMinimumSize(QSize(0, 101))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.groupBox_DrawingNumber.setFont(font1)
        self.groupBox_DrawingNumber.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop
        )
        self.groupBox_DrawingNumber.setFlat(False)
        self.UseFileName = Gui_PrefCheckBox(self.groupBox_DrawingNumber)
        self.UseFileName.setObjectName("UseFileName")
        self.UseFileName.setGeometry(QRect(10, 25, 241, 17))
        font2 = QFont()
        font2.setBold(False)
        font2.setWeight(50)
        self.UseFileName.setFont(font2)
        self.UseFileName.setProperty("prefEntry", QByteArray("UseFileName"))
        self.UseFileName.setProperty("prefPath", QByteArray("Mod/TitleBlock Workbench"))
        self.DrawingNumber = Gui_PrefLineEdit(self.groupBox_DrawingNumber)
        self.DrawingNumber.setObjectName("DrawingNumber")
        self.DrawingNumber.setEnabled(False)
        self.DrawingNumber.setGeometry(QRect(10, 70, 241, 20))
        self.DrawingNumber.setFont(font2)
        self.DrawingNumber.setProperty("prefEntry", QByteArray("DrwNrFieldName"))
        self.DrawingNumber.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )
        self.label_10 = QLabel(self.groupBox_DrawingNumber)
        self.label_10.setObjectName("label_10")
        self.label_10.setEnabled(False)
        self.label_10.setGeometry(QRect(10, 50, 256, 16))
        self.label_10.setFont(font2)

        self.verticalLayout_3.addWidget(self.groupBox_DrawingNumber)

        self.groupBox_Map_Items = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_Map_Items.setObjectName("groupBox_Map_Items")
        self.groupBox_Map_Items.setMinimumSize(QSize(0, 176))
        self.groupBox_Map_Items.setFont(font1)
        self.label_3 = QLabel(self.groupBox_Map_Items)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(10, 20, 321, 36))
        self.label_3.setFont(font2)
        self.label_3.setTextFormat(Qt.AutoText)
        self.label_3.setWordWrap(True)
        self.layoutWidget = QWidget(self.groupBox_Map_Items)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 65, 281, 100))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.MapLength = Gui_PrefLineEdit(self.layoutWidget)
        self.MapLength.setObjectName("MapLength")
        self.MapLength.setFont(font2)
        self.MapLength.setProperty("prefEntry", QByteArray("MapLength"))
        self.MapLength.setProperty("prefPath", QByteArray("Mod/TitleBlock Workbench"))

        self.gridLayout.addWidget(self.MapLength, 0, 1, 1, 1)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.label_8.setFont(font2)

        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

        self.MapAngle = Gui_PrefLineEdit(self.layoutWidget)
        self.MapAngle.setObjectName("MapAngle")
        self.MapAngle.setFont(font2)
        self.MapAngle.setProperty("prefEntry", QByteArray("MapAngle"))
        self.MapAngle.setProperty("prefPath", QByteArray("Mod/TitleBlock Workbench"))

        self.gridLayout.addWidget(self.MapAngle, 1, 1, 1, 1)

        self.MapMass = Gui_PrefLineEdit(self.layoutWidget)
        self.MapMass.setObjectName("MapMass")
        self.MapMass.setFont(font2)
        self.MapMass.setProperty("prefEntry", QByteArray("MapMass"))
        self.MapMass.setProperty("prefPath", QByteArray("Mod/TitleBlock Workbench"))

        self.gridLayout.addWidget(self.MapMass, 2, 1, 1, 1)

        self.MapNoSheets = Gui_PrefLineEdit(self.layoutWidget)
        self.MapNoSheets.setObjectName("MapNoSheets")
        self.MapNoSheets.setFont(font2)
        self.MapNoSheets.setInputMethodHints(Qt.ImhNone)
        self.MapNoSheets.setProperty("prefEntry", QByteArray("MapNoSheets"))
        self.MapNoSheets.setProperty("prefPath", QByteArray("Mod/TitleBlock Workbench"))

        self.gridLayout.addWidget(self.MapNoSheets, 3, 1, 1, 1)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.label_7.setFont(font2)

        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.label_5.setFont(font2)

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.label_6.setFont(font2)

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.verticalLayout_3.addWidget(self.groupBox_Map_Items)

        self.groupBox_Map_DocInfo = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_Map_DocInfo.setObjectName("groupBox_Map_DocInfo")
        self.groupBox_Map_DocInfo.setMinimumSize(QSize(0, 311))
        self.groupBox_Map_DocInfo.setFont(font1)
        self.label_17 = QLabel(self.groupBox_Map_DocInfo)
        self.label_17.setObjectName("label_17")
        self.label_17.setGeometry(QRect(10, 20, 321, 36))
        self.label_17.setFont(font2)
        self.label_17.setTextFormat(Qt.AutoText)
        self.label_17.setWordWrap(True)
        self.layoutWidget1 = QWidget(self.groupBox_Map_DocInfo)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(11, 66, 246, 230))
        self.gridLayout_2 = QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.layoutWidget1)
        self.label_20.setObjectName("label_20")
        self.label_20.setFont(font2)

        self.gridLayout_2.addWidget(self.label_20, 0, 0, 1, 1)

        self.DocInfo_Name = Gui_PrefLineEdit(self.layoutWidget1)
        self.DocInfo_Name.setObjectName("DocInfo_Name")
        self.DocInfo_Name.setFont(font2)
        self.DocInfo_Name.setProperty("prefEntry", QByteArray("DocInfo_Name"))
        self.DocInfo_Name.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )

        self.gridLayout_2.addWidget(self.DocInfo_Name, 0, 1, 1, 2)

        self.label_21 = QLabel(self.layoutWidget1)
        self.label_21.setObjectName("label_21")
        self.label_21.setFont(font2)

        self.gridLayout_2.addWidget(self.label_21, 1, 0, 1, 1)

        self.DocInfo_CreatedBy = Gui_PrefLineEdit(self.layoutWidget1)
        self.DocInfo_CreatedBy.setObjectName("DocInfo_CreatedBy")
        self.DocInfo_CreatedBy.setFont(font2)
        self.DocInfo_CreatedBy.setProperty("prefEntry", QByteArray("DocInfo_CreatedBy"))
        self.DocInfo_CreatedBy.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )

        self.gridLayout_2.addWidget(self.DocInfo_CreatedBy, 1, 1, 1, 2)

        self.label_19 = QLabel(self.layoutWidget1)
        self.label_19.setObjectName("label_19")
        self.label_19.setFont(font2)

        self.gridLayout_2.addWidget(self.label_19, 2, 0, 1, 1)

        self.DocInfo_CreatedDate = Gui_PrefLineEdit(self.layoutWidget1)
        self.DocInfo_CreatedDate.setObjectName("DocInfo_CreatedDate")
        self.DocInfo_CreatedDate.setFont(font2)
        self.DocInfo_CreatedDate.setProperty(
            "prefEntry", QByteArray("DocInfo_CreatedDate")
        )
        self.DocInfo_CreatedDate.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )

        self.gridLayout_2.addWidget(self.DocInfo_CreatedDate, 2, 1, 1, 2)

        self.label_18 = QLabel(self.layoutWidget1)
        self.label_18.setObjectName("label_18")
        self.label_18.setFont(font2)

        self.gridLayout_2.addWidget(self.label_18, 3, 0, 1, 1)

        self.DocInfo_LastModifiedBy = Gui_PrefLineEdit(self.layoutWidget1)
        self.DocInfo_LastModifiedBy.setObjectName("DocInfo_LastModifiedBy")
        self.DocInfo_LastModifiedBy.setFont(font2)
        self.DocInfo_LastModifiedBy.setInputMethodHints(Qt.ImhNone)
        self.DocInfo_LastModifiedBy.setProperty(
            "prefEntry", QByteArray("DocInfo_LastModifiedBy")
        )
        self.DocInfo_LastModifiedBy.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )

        self.gridLayout_2.addWidget(self.DocInfo_LastModifiedBy, 3, 1, 1, 2)

        self.label_22 = QLabel(self.layoutWidget1)
        self.label_22.setObjectName("label_22")
        self.label_22.setFont(font2)

        self.gridLayout_2.addWidget(self.label_22, 4, 0, 1, 1)

        self.DocInfo_LastModifiedDate = Gui_PrefLineEdit(self.layoutWidget1)
        self.DocInfo_LastModifiedDate.setObjectName("DocInfo_LastModifiedDate")
        self.DocInfo_LastModifiedDate.setFont(font2)
        self.DocInfo_LastModifiedDate.setInputMethodHints(Qt.ImhNone)
        self.DocInfo_LastModifiedDate.setProperty(
            "prefEntry", QByteArray("DocInfo_LastModifiedDate")
        )
        self.DocInfo_LastModifiedDate.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )

        self.gridLayout_2.addWidget(self.DocInfo_LastModifiedDate, 4, 1, 1, 2)

        self.label_23 = QLabel(self.layoutWidget1)
        self.label_23.setObjectName("label_23")
        self.label_23.setFont(font2)

        self.gridLayout_2.addWidget(self.label_23, 5, 0, 1, 1)

        self.DocInfo_Company = Gui_PrefLineEdit(self.layoutWidget1)
        self.DocInfo_Company.setObjectName("DocInfo_Company")
        self.DocInfo_Company.setFont(font2)
        self.DocInfo_Company.setInputMethodHints(Qt.ImhNone)
        self.DocInfo_Company.setProperty("prefEntry", QByteArray("DocInfo_Company"))
        self.DocInfo_Company.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )

        self.gridLayout_2.addWidget(self.DocInfo_Company, 5, 1, 1, 2)

        self.label_24 = QLabel(self.layoutWidget1)
        self.label_24.setObjectName("label_24")
        self.label_24.setFont(font2)

        self.gridLayout_2.addWidget(self.label_24, 6, 0, 1, 1)

        self.DocInfo_License = Gui_PrefLineEdit(self.layoutWidget1)
        self.DocInfo_License.setObjectName("DocInfo_License")
        self.DocInfo_License.setFont(font2)
        self.DocInfo_License.setInputMethodHints(Qt.ImhNone)
        self.DocInfo_License.setProperty("prefEntry", QByteArray("DocInfo_License"))
        self.DocInfo_License.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )

        self.gridLayout_2.addWidget(self.DocInfo_License, 6, 1, 1, 2)

        self.label_25 = QLabel(self.layoutWidget1)
        self.label_25.setObjectName("label_25")
        self.label_25.setFont(font2)

        self.gridLayout_2.addWidget(self.label_25, 7, 0, 1, 1)

        self.DocInfo_LicenseURL = Gui_PrefLineEdit(self.layoutWidget1)
        self.DocInfo_LicenseURL.setObjectName("DocInfo_LicenseURL")
        self.DocInfo_LicenseURL.setFont(font2)
        self.DocInfo_LicenseURL.setInputMethodHints(Qt.ImhNone)
        self.DocInfo_LicenseURL.setProperty(
            "prefEntry", QByteArray("DocInfo_LicenseURL")
        )
        self.DocInfo_LicenseURL.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )

        self.gridLayout_2.addWidget(self.DocInfo_LicenseURL, 7, 1, 1, 2)

        self.label_26 = QLabel(self.layoutWidget1)
        self.label_26.setObjectName("label_26")
        self.label_26.setFont(font2)

        self.gridLayout_2.addWidget(self.label_26, 8, 0, 1, 1)

        self.DocInfo_Comment = Gui_PrefLineEdit(self.layoutWidget1)
        self.DocInfo_Comment.setObjectName("DocInfo_Comment")
        self.DocInfo_Comment.setFont(font2)
        self.DocInfo_Comment.setInputMethodHints(Qt.ImhNone)
        self.DocInfo_Comment.setProperty("prefEntry", QByteArray("DocInfo_Comment"))
        self.DocInfo_Comment.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )

        self.gridLayout_2.addWidget(self.DocInfo_Comment, 8, 1, 1, 2)

        self.verticalLayout_3.addWidget(self.groupBox_Map_DocInfo)

        self.groupBox_Included_Items = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_Included_Items.setObjectName("groupBox_Included_Items")
        self.groupBox_Included_Items.setMinimumSize(QSize(0, 181))
        self.groupBox_Included_Items.setFont(font1)
        self.label_4 = QLabel(self.groupBox_Included_Items)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(10, 20, 396, 61))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font2)
        self.label_4.setTextFormat(Qt.RichText)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.label_4.setWordWrap(True)
        self.layoutWidget2 = QWidget(self.groupBox_Included_Items)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 80, 144, 88))
        self.verticalLayout = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.IncludeLengthUnit = Gui_PrefCheckBox(self.layoutWidget2)
        self.IncludeLengthUnit.setObjectName("IncludeLengthUnit")
        self.IncludeLengthUnit.setFont(font2)
        self.IncludeLengthUnit.setProperty("prefEntry", QByteArray("IncludeLength"))
        self.IncludeLengthUnit.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )

        self.verticalLayout.addWidget(self.IncludeLengthUnit)

        self.IncludeAngleUnit = Gui_PrefCheckBox(self.layoutWidget2)
        self.IncludeAngleUnit.setObjectName("IncludeAngleUnit")
        self.IncludeAngleUnit.setFont(font2)
        self.IncludeAngleUnit.setProperty("prefEntry", QByteArray("IncludeAngle"))
        self.IncludeAngleUnit.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )

        self.verticalLayout.addWidget(self.IncludeAngleUnit)

        self.IncludeMassUnit = Gui_PrefCheckBox(self.layoutWidget2)
        self.IncludeMassUnit.setObjectName("IncludeMassUnit")
        self.IncludeMassUnit.setFont(font2)
        self.IncludeMassUnit.setProperty("prefEntry", QByteArray("IncludeMass"))
        self.IncludeMassUnit.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )

        self.verticalLayout.addWidget(self.IncludeMassUnit)

        self.IncludeNoOfSheets = Gui_PrefCheckBox(self.layoutWidget2)
        self.IncludeNoOfSheets.setObjectName("IncludeNoOfSheets")
        self.IncludeNoOfSheets.setFont(font2)
        self.IncludeNoOfSheets.setProperty("prefEntry", QByteArray("IncludeNoOfSheets"))
        self.IncludeNoOfSheets.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )

        self.verticalLayout.addWidget(self.IncludeNoOfSheets)

        self.verticalLayout_3.addWidget(self.groupBox_Included_Items)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.TitleBlock, "")
        self.External_Source = QWidget()
        self.External_Source.setObjectName("External_Source")
        self.groupBox_2 = QGroupBox(self.External_Source)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setGeometry(QRect(5, 10, 421, 246))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.UseExternalSource = Gui_PrefCheckBox(self.groupBox_2)
        self.UseExternalSource.setObjectName("UseExternalSource")
        self.UseExternalSource.setGeometry(QRect(10, 25, 231, 17))
        self.UseExternalSource.setFont(font2)
        self.UseExternalSource.setProperty("prefEntry", QByteArray("UseExternalSource"))
        self.UseExternalSource.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )
        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName("label_16")
        self.label_16.setEnabled(False)
        self.label_16.setGeometry(QRect(10, 85, 371, 16))
        self.label_16.setFont(font2)
        self.label_16.setFrameShadow(QFrame.Plain)
        self.label_16.setWordWrap(True)
        self.SheetName = Gui_PrefLineEdit(self.groupBox_2)
        self.SheetName.setObjectName("SheetName")
        self.SheetName.setEnabled(False)
        self.SheetName.setGeometry(QRect(10, 105, 361, 25))
        self.SheetName.setFont(font2)
        self.SheetName.setProperty("prefEntry", QByteArray("SheetName"))
        self.SheetName.setProperty("prefPath", QByteArray("Mod/TitleBlock Workbench"))
        self.ExternalFileChooser = Gui_PrefFileChooser(self.groupBox_2)
        self.ExternalFileChooser.setObjectName("ExternalFileChooser")
        self.ExternalFileChooser.setEnabled(False)
        self.ExternalFileChooser.setGeometry(QRect(10, 45, 401, 25))
        self.ExternalFileChooser.setFont(font2)
        self.ExternalFileChooser.setProperty("prefEntry", QByteArray("ExternalFile"))
        self.ExternalFileChooser.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )
        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName("label_15")
        self.label_15.setEnabled(False)
        self.label_15.setGeometry(QRect(10, 135, 341, 51))
        self.label_15.setFont(font2)
        self.label_15.setFrameShadow(QFrame.Plain)
        self.label_15.setWordWrap(True)
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QRect(170, 175, 216, 31))
        font3 = QFont()
        font3.setBold(False)
        font3.setItalic(True)
        font3.setWeight(50)
        self.label_2.setFont(font3)
        self.label_2.setWordWrap(True)
        self.StartCell = Gui_PrefLineEdit(self.groupBox_2)
        self.StartCell.setObjectName("StartCell")
        self.StartCell.setEnabled(False)
        self.StartCell.setGeometry(QRect(10, 180, 153, 25))
        self.StartCell.setFont(font2)
        self.StartCell.setProperty("prefEntry", QByteArray("StartCell"))
        self.StartCell.setProperty("prefPath", QByteArray("Mod/TitleBlock Workbench"))
        self.AutoFillTitleBlock = Gui_PrefCheckBox(self.groupBox_2)
        self.AutoFillTitleBlock.setObjectName("AutoFillTitleBlock")
        self.AutoFillTitleBlock.setEnabled(False)
        self.AutoFillTitleBlock.setGeometry(QRect(10, 215, 158, 17))
        self.AutoFillTitleBlock.setFont(font2)
        self.AutoFillTitleBlock.setChecked(True)
        self.AutoFillTitleBlock.setProperty(
            "prefEntry", QByteArray("AutoFillTitleBlock")
        )
        self.AutoFillTitleBlock.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )
        self.groupBox_3 = QGroupBox(self.External_Source)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setGeometry(QRect(5, 275, 421, 206))
        self.widget_ImportSettings = QWidget(self.groupBox_3)
        self.widget_ImportSettings.setObjectName("widget_ImportSettings")
        self.widget_ImportSettings.setEnabled(False)
        self.widget_ImportSettings.setGeometry(QRect(5, 20, 406, 176))
        self.ImportSettingsXL = Gui_PrefCheckBox(self.widget_ImportSettings)
        self.ImportSettingsXL.setObjectName("ImportSettingsXL")
        self.ImportSettingsXL.setEnabled(False)
        self.ImportSettingsXL.setGeometry(QRect(5, 10, 381, 17))
        self.ImportSettingsXL.setFont(font2)
        self.ImportSettingsXL.setProperty("prefEntry", QByteArray("ImportSettingsXL"))
        self.ImportSettingsXL.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )
        self.SheetName_Settings = Gui_PrefLineEdit(self.widget_ImportSettings)
        self.SheetName_Settings.setObjectName("SheetName_Settings")
        self.SheetName_Settings.setEnabled(False)
        self.SheetName_Settings.setGeometry(QRect(10, 70, 133, 25))
        self.SheetName_Settings.setFont(font2)
        self.SheetName_Settings.setProperty(
            "prefEntry", QByteArray("SheetName_Settings")
        )
        self.SheetName_Settings.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )
        self.StartCell_Settings = Gui_PrefLineEdit(self.widget_ImportSettings)
        self.StartCell_Settings.setObjectName("StartCell_Settings")
        self.StartCell_Settings.setEnabled(False)
        self.StartCell_Settings.setGeometry(QRect(7, 140, 151, 25))
        self.StartCell_Settings.setFont(font2)
        self.StartCell_Settings.setProperty(
            "prefEntry", QByteArray("StartCell_Settings")
        )
        self.StartCell_Settings.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )
        self.label_9 = QLabel(self.widget_ImportSettings)
        self.label_9.setObjectName("label_9")
        self.label_9.setEnabled(False)
        self.label_9.setGeometry(QRect(165, 135, 216, 31))
        self.label_9.setFont(font3)
        self.label_9.setWordWrap(True)
        self.label_13 = QLabel(self.widget_ImportSettings)
        self.label_13.setObjectName("label_13")
        self.label_13.setEnabled(False)
        self.label_13.setGeometry(QRect(10, 105, 206, 31))
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        self.label_13.setFont(font2)
        self.label_13.setFrameShadow(QFrame.Plain)
        self.label_13.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.label_13.setWordWrap(True)
        self.label_14 = QLabel(self.widget_ImportSettings)
        self.label_14.setObjectName("label_14")
        self.label_14.setEnabled(False)
        self.label_14.setGeometry(QRect(10, 50, 371, 16))
        self.label_14.setFont(font2)
        self.label_14.setFrameShadow(QFrame.Plain)
        self.label_14.setWordWrap(True)
        self.tabWidget.addTab(self.External_Source, "")
        self.TechDraw_Workbench = QWidget()
        self.TechDraw_Workbench.setObjectName("TechDraw_Workbench")
        self.groupBox = QGroupBox(self.TechDraw_Workbench)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setGeometry(QRect(5, 10, 421, 121))
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.AddToolBarTechDraw = Gui_PrefCheckBox(self.groupBox)
        self.AddToolBarTechDraw.setObjectName("AddToolBarTechDraw")
        self.AddToolBarTechDraw.setEnabled(True)
        self.AddToolBarTechDraw.setGeometry(QRect(11, 26, 219, 17))
        self.AddToolBarTechDraw.setFont(font2)
        self.AddToolBarTechDraw.setChecked(True)
        self.AddToolBarTechDraw.setProperty(
            "prefEntry", QByteArray("AddToolBarTechDraw")
        )
        self.AddToolBarTechDraw.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.label_12.setEnabled(False)
        self.label_12.setGeometry(QRect(11, 72, 211, 16))
        self.Import_templates = Gui_PrefCheckBox(self.groupBox)
        self.Import_templates.setObjectName("Import_templates")
        self.Import_templates.setGeometry(QRect(11, 49, 148, 17))
        self.Import_templates.setProperty("prefEntry", QByteArray("Import_templates"))
        self.Import_templates.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )
        self.Default_Template = Gui_PrefComboBox(self.groupBox)
        self.Default_Template.addItem("")
        self.Default_Template.addItem("")
        self.Default_Template.addItem("")
        self.Default_Template.addItem("")
        self.Default_Template.addItem("")
        self.Default_Template.addItem("")
        self.Default_Template.setObjectName("Default_Template")
        self.Default_Template.setEnabled(False)
        self.Default_Template.setGeometry(QRect(11, 91, 211, 20))
        self.Default_Template.setProperty("prefEntry", QByteArray("Default_Template"))
        self.Default_Template.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )
        self.tabWidget.addTab(self.TechDraw_Workbench, "")
        self.UIsettings = QWidget()
        self.UIsettings.setObjectName("UIsettings")
        self.Spreadsheet_Layout = QGroupBox(self.UIsettings)
        self.Spreadsheet_Layout.setObjectName("Spreadsheet_Layout")
        self.Spreadsheet_Layout.setGeometry(QRect(5, 10, 426, 261))
        self.layoutWidget3 = QWidget(self.Spreadsheet_Layout)
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(17, 27, 301, 220))
        self.formLayout = QFormLayout(self.layoutWidget3)
        self.formLayout.setSpacing(6)
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.formLayout.setObjectName("formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_27 = QLabel(self.layoutWidget3)
        self.label_27.setObjectName("label_27")

        self.gridLayout_3.addWidget(self.label_27, 0, 0, 1, 1)

        self.SprHeaderBackGround = Gui_PrefColorButton(self.layoutWidget3)
        self.SprHeaderBackGround.setObjectName("SprHeaderBackGround")
        self.SprHeaderBackGround.setAutoDefault(False)
        self.SprHeaderBackGround.setColor(QColor(243, 202, 98))
        self.SprHeaderBackGround.setAllowTransparency(False)
        self.SprHeaderBackGround.setProperty(
            "prefEntry", QByteArray("SpreadSheetHeaderBackGround")
        )
        self.SprHeaderBackGround.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )

        self.gridLayout_3.addWidget(self.SprHeaderBackGround, 0, 1, 1, 1)

        self.label_28 = QLabel(self.layoutWidget3)
        self.label_28.setObjectName("label_28")

        self.gridLayout_3.addWidget(self.label_28, 1, 0, 1, 1)

        self.SprHeaderForeGround = Gui_PrefColorButton(self.layoutWidget3)
        self.SprHeaderForeGround.setObjectName("SprHeaderForeGround")
        self.SprHeaderForeGround.setCheckable(False)
        self.SprHeaderForeGround.setChecked(False)
        self.SprHeaderForeGround.setAutoDefault(False)
        self.SprHeaderForeGround.setFlat(False)
        self.SprHeaderForeGround.setColor(QColor(0, 0, 0))
        self.SprHeaderForeGround.setAllowTransparency(False)
        self.SprHeaderForeGround.setProperty(
            "prefEntry", QByteArray("SpreadSheetHeaderForeGround")
        )
        self.SprHeaderForeGround.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )

        self.gridLayout_3.addWidget(self.SprHeaderForeGround, 1, 1, 1, 1)

        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.gridLayout_3)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_29 = QLabel(self.layoutWidget3)
        self.label_29.setObjectName("label_29")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(40)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy3)

        self.gridLayout_4.addWidget(self.label_29, 0, 0, 1, 1)

        self.SprHeaderFontStyle_Bold = Gui_PrefCheckBox(self.layoutWidget3)
        self.SprHeaderFontStyle_Bold.setObjectName("SprHeaderFontStyle_Bold")
        self.SprHeaderFontStyle_Bold.setFont(font1)
        self.SprHeaderFontStyle_Bold.setChecked(True)
        self.SprHeaderFontStyle_Bold.setProperty(
            "prefEntry", QByteArray("SpreadsheetHeaderFontStyle_Bold")
        )
        self.SprHeaderFontStyle_Bold.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )

        self.gridLayout_4.addWidget(self.SprHeaderFontStyle_Bold, 0, 1, 1, 1)

        self.SprHeaderFontStyle_Italic = Gui_PrefCheckBox(self.layoutWidget3)
        self.SprHeaderFontStyle_Italic.setObjectName("SprHeaderFontStyle_Italic")
        self.SprHeaderFontStyle_Italic.setFont(font)
        self.SprHeaderFontStyle_Italic.setProperty(
            "prefEntry", QByteArray("SpreadsheetHeaderFontStyle_Italic")
        )
        self.SprHeaderFontStyle_Italic.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )

        self.gridLayout_4.addWidget(self.SprHeaderFontStyle_Italic, 0, 2, 1, 1)

        self.SprHeaderFontStyle_Underline = Gui_PrefCheckBox(self.layoutWidget3)
        self.SprHeaderFontStyle_Underline.setObjectName("SprHeaderFontStyle_Underline")
        font4 = QFont()
        font4.setUnderline(True)
        self.SprHeaderFontStyle_Underline.setFont(font4)
        self.SprHeaderFontStyle_Underline.setChecked(True)
        self.SprHeaderFontStyle_Underline.setProperty(
            "prefEntry", QByteArray("SpreadsheetHeaderFontStyle_Underline")
        )
        self.SprHeaderFontStyle_Underline.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )

        self.gridLayout_4.addWidget(self.SprHeaderFontStyle_Underline, 0, 3, 1, 1)

        self.formLayout.setLayout(1, QFormLayout.SpanningRole, self.gridLayout_4)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_31 = QLabel(self.layoutWidget3)
        self.label_31.setObjectName("label_31")

        self.gridLayout_5.addWidget(self.label_31, 2, 0, 1, 1)

        self.SprTableBackGround_1 = Gui_PrefColorButton(self.layoutWidget3)
        self.SprTableBackGround_1.setObjectName("SprTableBackGround_1")
        self.SprTableBackGround_1.setColor(QColor(169, 169, 169))
        self.SprTableBackGround_1.setProperty(
            "prefEntry", QByteArray("SpreadSheetTableBackGround_1")
        )
        self.SprTableBackGround_1.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )

        self.gridLayout_5.addWidget(self.SprTableBackGround_1, 0, 1, 1, 1)

        self.label_30 = QLabel(self.layoutWidget3)
        self.label_30.setObjectName("label_30")

        self.gridLayout_5.addWidget(self.label_30, 0, 0, 1, 1)

        self.SprTableForeGround = Gui_PrefColorButton(self.layoutWidget3)
        self.SprTableForeGround.setObjectName("SprTableForeGround")
        self.SprTableForeGround.setColor(QColor(0, 0, 0))
        self.SprTableForeGround.setProperty(
            "prefEntry", QByteArray("SpreadSheetTableForeGround")
        )
        self.SprTableForeGround.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )

        self.gridLayout_5.addWidget(self.SprTableForeGround, 2, 1, 1, 1)

        self.label_33 = QLabel(self.layoutWidget3)
        self.label_33.setObjectName("label_33")

        self.gridLayout_5.addWidget(self.label_33, 1, 0, 1, 1)

        self.SprTableBackGround_2 = Gui_PrefColorButton(self.layoutWidget3)
        self.SprTableBackGround_2.setObjectName("SprTableBackGround_2")
        self.SprTableBackGround_2.setColor(QColor(128, 128, 128))
        self.SprTableBackGround_2.setProperty(
            "prefEntry", QByteArray("SpreadSheetTableBackGround_2")
        )
        self.SprTableBackGround_2.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )

        self.gridLayout_5.addWidget(self.SprTableBackGround_2, 1, 1, 1, 1)

        self.formLayout.setLayout(2, QFormLayout.LabelRole, self.gridLayout_5)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_32 = QLabel(self.layoutWidget3)
        self.label_32.setObjectName("label_32")
        sizePolicy3.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy3)

        self.gridLayout_6.addWidget(self.label_32, 0, 0, 1, 1)

        self.SprTableFontStyle_Bold = Gui_PrefCheckBox(self.layoutWidget3)
        self.SprTableFontStyle_Bold.setObjectName("SprTableFontStyle_Bold")
        self.SprTableFontStyle_Bold.setFont(font1)
        self.SprTableFontStyle_Bold.setProperty(
            "prefEntry", QByteArray("SpreadsheetTableFontStyle_Bold")
        )
        self.SprTableFontStyle_Bold.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )

        self.gridLayout_6.addWidget(self.SprTableFontStyle_Bold, 0, 1, 1, 1)

        self.SprTableFontStyle_Italic = Gui_PrefCheckBox(self.layoutWidget3)
        self.SprTableFontStyle_Italic.setObjectName("SprTableFontStyle_Italic")
        self.SprTableFontStyle_Italic.setFont(font)
        self.SprTableFontStyle_Italic.setProperty(
            "prefEntry", QByteArray("SpreadsheetTableFontStyle_Italic")
        )
        self.SprTableFontStyle_Italic.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )

        self.gridLayout_6.addWidget(self.SprTableFontStyle_Italic, 0, 2, 1, 1)

        self.SprTableFontStyle_Underline = Gui_PrefCheckBox(self.layoutWidget3)
        self.SprTableFontStyle_Underline.setObjectName("SprTableFontStyle_Underline")
        self.SprTableFontStyle_Underline.setFont(font4)
        self.SprTableFontStyle_Underline.setProperty(
            "prefEntry", QByteArray("SpreadsheetTableFontStyle_Underline")
        )
        self.SprTableFontStyle_Underline.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )

        self.gridLayout_6.addWidget(self.SprTableFontStyle_Underline, 0, 3, 1, 1)

        self.formLayout.setLayout(3, QFormLayout.SpanningRole, self.gridLayout_6)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_7.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_7.setHorizontalSpacing(6)
        self.label_34 = QLabel(self.layoutWidget3)
        self.label_34.setObjectName("label_34")
        sizePolicy3.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy3)

        self.gridLayout_7.addWidget(self.label_34, 0, 0, 1, 1)

        self.SprColumnFontStyle_Bold = Gui_PrefCheckBox(self.layoutWidget3)
        self.SprColumnFontStyle_Bold.setObjectName("SprColumnFontStyle_Bold")
        self.SprColumnFontStyle_Bold.setFont(font1)
        self.SprColumnFontStyle_Bold.setChecked(True)
        self.SprColumnFontStyle_Bold.setProperty(
            "prefEntry", QByteArray("SpreadsheetColumnFontStyle_Bold")
        )
        self.SprColumnFontStyle_Bold.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )

        self.gridLayout_7.addWidget(self.SprColumnFontStyle_Bold, 0, 1, 1, 1)

        self.SprColumnFontStyle_Italic = Gui_PrefCheckBox(self.layoutWidget3)
        self.SprColumnFontStyle_Italic.setObjectName("SprColumnFontStyle_Italic")
        self.SprColumnFontStyle_Italic.setFont(font)
        self.SprColumnFontStyle_Italic.setProperty(
            "prefEntry", QByteArray("SpreadsheetColumnFontStyle_Italic")
        )
        self.SprColumnFontStyle_Italic.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )

        self.gridLayout_7.addWidget(self.SprColumnFontStyle_Italic, 0, 2, 1, 1)

        self.SprColumnFontStyle_Underline = Gui_PrefCheckBox(self.layoutWidget3)
        self.SprColumnFontStyle_Underline.setObjectName("SprColumnFontStyle_Underline")
        self.SprColumnFontStyle_Underline.setFont(font4)
        self.SprColumnFontStyle_Underline.setProperty(
            "prefEntry", QByteArray("SpreadsheetColumnFontStyle_Underline")
        )
        self.SprColumnFontStyle_Underline.setProperty(
            "prefPath", QByteArray("Mod/TitleBlock Workbench")
        )

        self.gridLayout_7.addWidget(self.SprColumnFontStyle_Underline, 0, 3, 1, 1)

        self.formLayout.setLayout(4, QFormLayout.SpanningRole, self.gridLayout_7)

        self.tabWidget.addTab(self.UIsettings, "")
        QWidget.setTabOrder(self.tabWidget, self.UseFileName)
        QWidget.setTabOrder(self.UseFileName, self.DrawingNumber)
        QWidget.setTabOrder(self.DrawingNumber, self.MapLength)
        QWidget.setTabOrder(self.MapLength, self.MapAngle)
        QWidget.setTabOrder(self.MapAngle, self.MapMass)
        QWidget.setTabOrder(self.MapMass, self.MapNoSheets)
        QWidget.setTabOrder(self.MapNoSheets, self.DocInfo_Name)
        QWidget.setTabOrder(self.DocInfo_Name, self.DocInfo_CreatedBy)
        QWidget.setTabOrder(self.DocInfo_CreatedBy, self.DocInfo_CreatedDate)
        QWidget.setTabOrder(self.DocInfo_CreatedDate, self.DocInfo_LastModifiedBy)
        QWidget.setTabOrder(self.DocInfo_LastModifiedBy, self.DocInfo_LastModifiedDate)
        QWidget.setTabOrder(self.DocInfo_LastModifiedDate, self.DocInfo_Company)
        QWidget.setTabOrder(self.DocInfo_Company, self.DocInfo_License)
        QWidget.setTabOrder(self.DocInfo_License, self.DocInfo_LicenseURL)
        QWidget.setTabOrder(self.DocInfo_LicenseURL, self.DocInfo_Comment)
        QWidget.setTabOrder(self.DocInfo_Comment, self.IncludeLengthUnit)
        QWidget.setTabOrder(self.IncludeLengthUnit, self.IncludeAngleUnit)
        QWidget.setTabOrder(self.IncludeAngleUnit, self.IncludeMassUnit)
        QWidget.setTabOrder(self.IncludeMassUnit, self.IncludeNoOfSheets)
        QWidget.setTabOrder(self.IncludeNoOfSheets, self.UseExternalSource)
        QWidget.setTabOrder(self.UseExternalSource, self.SheetName)
        QWidget.setTabOrder(self.SheetName, self.StartCell)
        QWidget.setTabOrder(self.StartCell, self.AutoFillTitleBlock)
        QWidget.setTabOrder(self.AutoFillTitleBlock, self.ImportSettingsXL)
        QWidget.setTabOrder(self.ImportSettingsXL, self.SheetName_Settings)
        QWidget.setTabOrder(self.SheetName_Settings, self.StartCell_Settings)
        QWidget.setTabOrder(self.StartCell_Settings, self.AddToolBarTechDraw)
        QWidget.setTabOrder(self.AddToolBarTechDraw, self.Import_templates)
        QWidget.setTabOrder(self.Import_templates, self.Default_Template)

        self.retranslateUi(Form)
        self.ImportSettingsXL.toggled.connect(self.SheetName_Settings.setEnabled)
        self.UseExternalSource.toggled.connect(self.SheetName.setEnabled)
        self.ImportSettingsXL.toggled.connect(self.groupBox_DrawingNumber.setDisabled)
        self.ImportSettingsXL.toggled.connect(self.groupBox_Included_Items.setDisabled)
        self.Import_templates.toggled.connect(self.Default_Template.setEnabled)
        self.ImportSettingsXL.toggled.connect(self.groupBox_Map_Items.setDisabled)
        self.UseExternalSource.toggled.connect(self.label_2.setEnabled)
        self.UseExternalSource.toggled.connect(self.widget_ImportSettings.setEnabled)
        self.UseExternalSource.toggled.connect(self.ExternalFileChooser.setEnabled)
        self.ImportSettingsXL.toggled.connect(self.label_13.setEnabled)
        self.ImportSettingsXL.toggled.connect(self.StartCell_Settings.setEnabled)
        self.ImportSettingsXL.toggled.connect(self.label_9.setEnabled)
        self.Import_templates.toggled.connect(self.label_12.setEnabled)
        self.UseExternalSource.toggled.connect(self.groupBox_Map_DocInfo.setDisabled)
        self.UseExternalSource.toggled.connect(self.AutoFillTitleBlock.setEnabled)
        self.UseFileName.toggled.connect(self.DrawingNumber.setEnabled)
        self.UseExternalSource.toggled.connect(self.StartCell.setEnabled)
        self.UseExternalSource.toggled.connect(self.label_15.setEnabled)
        self.UseExternalSource.toggled.connect(self.label_16.setEnabled)
        self.UseExternalSource.toggled.connect(self.ImportSettingsXL.setChecked)
        self.UseExternalSource.toggled.connect(self.ImportSettingsXL.setEnabled)
        self.UseFileName.toggled.connect(self.label_10.setEnabled)
        self.ImportSettingsXL.toggled.connect(self.label_14.setEnabled)

        self.tabWidget.setCurrentIndex(3)
        self.SprHeaderBackGround.setDefault(True)
        self.SprHeaderForeGround.setDefault(False)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        self.label.setText(
            QCoreApplication.translate(
                "Form",
                "FreeCAD needs to be restarted before changes become active.",
                None,
            )
        )
        self.EnableDebug.setText(QCoreApplication.translate("Form", "Debug mode", None))
        self.label_11.setText(
            QCoreApplication.translate(
                "Form",
                '<html><head/><body><p><span style=" font-style:italic;">(If enabled, extra information will be shown in the report view.)</span></p></body></html>',
                None,
            )
        )
        self.groupBox_DrawingNumber.setTitle("")
        self.UseFileName.setText(
            QCoreApplication.translate("Form", "Use filename as drawing number", None)
        )
        self.DrawingNumber.setInputMask("")
        self.DrawingNumber.setText("")
        self.DrawingNumber.setPlaceholderText(
            QCoreApplication.translate("Form", "Enter the property name...", None)
        )
        self.label_10.setText(
            QCoreApplication.translate(
                "Form", "The property name for drawing number:", None
            )
        )
        self.groupBox_Map_Items.setTitle("")
        self.label_3.setText(
            QCoreApplication.translate(
                "Form",
                '<html><head/><body><p>The following system properties can be mapped to the titleblock: <span style=" font-style:italic;">(If not applicalbe, leave empty.)</span></p></body></html>',
                None,
            )
        )
        self.MapLength.setPlaceholderText(
            QCoreApplication.translate("Form", "Enter property name here...", None)
        )
        self.label_8.setText(
            QCoreApplication.translate("Form", "Number of pages:", None)
        )
        self.MapAngle.setPlaceholderText(
            QCoreApplication.translate("Form", "Enter property name here...", None)
        )
        self.MapMass.setPlaceholderText(
            QCoreApplication.translate("Form", "Enter property name here...", None)
        )
        self.MapNoSheets.setText("")
        self.MapNoSheets.setPlaceholderText(
            QCoreApplication.translate("Form", "Enter property name here...", None)
        )
        self.label_7.setText(QCoreApplication.translate("Form", "Mass unit:", None))
        self.label_5.setText(QCoreApplication.translate("Form", "Length unit:", None))
        self.label_6.setText(QCoreApplication.translate("Form", "Angle unit:", None))
        self.groupBox_Map_DocInfo.setTitle("")
        self.label_17.setText(
            QCoreApplication.translate(
                "Form",
                '<html><head/><body><p>The following document information values can be mapped to the titleblock: <span style=" font-style:italic;">(If not applicalbe, leave empty.)</span></p></body></html>',
                None,
            )
        )
        self.label_20.setText(QCoreApplication.translate("Form", "Name:", None))
        self.DocInfo_Name.setPlaceholderText(
            QCoreApplication.translate("Form", "Enter property name here...", None)
        )
        self.label_21.setText(QCoreApplication.translate("Form", "Created by:", None))
        self.DocInfo_CreatedBy.setPlaceholderText(
            QCoreApplication.translate("Form", "Enter property name here...", None)
        )
        self.label_19.setText(
            QCoreApplication.translate("Form", "Creation date:", None)
        )
        self.DocInfo_CreatedDate.setPlaceholderText(
            QCoreApplication.translate("Form", "Enter property name here...", None)
        )
        self.label_18.setText(
            QCoreApplication.translate("Form", "Last modified by:", None)
        )
        self.DocInfo_LastModifiedBy.setText("")
        self.DocInfo_LastModifiedBy.setPlaceholderText(
            QCoreApplication.translate("Form", "Enter property name here...", None)
        )
        self.label_22.setText(
            QCoreApplication.translate("Form", "Last modification by:", None)
        )
        self.DocInfo_LastModifiedDate.setText("")
        self.DocInfo_LastModifiedDate.setPlaceholderText(
            QCoreApplication.translate("Form", "Enter property name here...", None)
        )
        self.label_23.setText(QCoreApplication.translate("Form", "Company:", None))
        self.DocInfo_Company.setText("")
        self.DocInfo_Company.setPlaceholderText(
            QCoreApplication.translate("Form", "Enter property name here...", None)
        )
        self.label_24.setText(
            QCoreApplication.translate("Form", "License information:", None)
        )
        self.DocInfo_License.setText("")
        self.DocInfo_License.setPlaceholderText(
            QCoreApplication.translate("Form", "Enter property name here...", None)
        )
        self.label_25.setText(QCoreApplication.translate("Form", "License URL:", None))
        self.DocInfo_LicenseURL.setText("")
        self.DocInfo_LicenseURL.setPlaceholderText(
            QCoreApplication.translate("Form", "Enter property name here...", None)
        )
        self.label_26.setText(QCoreApplication.translate("Form", "Comment:", None))
        self.DocInfo_Comment.setText("")
        self.DocInfo_Comment.setPlaceholderText(
            QCoreApplication.translate("Form", "Enter property name here...", None)
        )
        self.groupBox_Included_Items.setTitle("")
        self.label_4.setText(
            QCoreApplication.translate(
                "Form",
                '<html><head/><body><p>The following properties can be included from the system:</p><p><span style=" font-style:italic;">(When the titleblock does have one or more properties already, you will end up with duplicates! It is advised to map the properties instead)</span></p></body></html>',
                None,
            )
        )
        self.IncludeLengthUnit.setText(
            QCoreApplication.translate("Form", "Include lengths", None)
        )
        self.IncludeAngleUnit.setText(
            QCoreApplication.translate("Form", "Include angles", None)
        )
        self.IncludeMassUnit.setText(
            QCoreApplication.translate("Form", "Include mass", None)
        )
        self.IncludeNoOfSheets.setText(
            QCoreApplication.translate("Form", "Include number of pages", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.TitleBlock),
            QCoreApplication.translate("Form", "TitleBlock", None),
        )
        self.groupBox_2.setTitle("")
        self.UseExternalSource.setText(
            QCoreApplication.translate("Form", "Use external source", None)
        )
        self.label_16.setText(
            QCoreApplication.translate(
                "Form",
                "<html><head/><body><p>The name of the worksheet that contains the date for the titleblock:</p></body></html>",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.SheetName.setToolTip(
            QCoreApplication.translate(
                "Form", "Enter the name of the sheet for the titleblock data", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.SheetName.setWhatsThis(
            QCoreApplication.translate(
                "Form", "Enter the name of the sheet for the titleblock data", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.SheetName.setInputMask("")
        self.SheetName.setText("")
        self.SheetName.setPlaceholderText(
            QCoreApplication.translate("Form", "Enter the name of sheet...", None)
        )
        self.ExternalFileChooser.setFileName("")
        self.ExternalFileChooser.setFilter(
            QCoreApplication.translate("Form", "*.xlsx", None)
        )
        self.label_15.setText(
            QCoreApplication.translate(
                "Form",
                '<html><head/><body><p>The startcell of the table which contains to the data for the titleblock: <span style=" font-style:italic;">(This must be the top left cell.)</span></p></body></html>',
                None,
            )
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "Form",
                "<html><head/><body><p>Cell adress must be like &quot;B1&quot; or like &quot;R1C1&quot;. If empty, A1 will be used.</p></body></html>",
                None,
            )
        )
        self.StartCell.setInputMask("")
        self.StartCell.setText("")
        self.StartCell.setPlaceholderText(
            QCoreApplication.translate("Form", "Enter the start cell...", None)
        )
        self.AutoFillTitleBlock.setText(
            QCoreApplication.translate("Form", "Populate titleblock on import", None)
        )
        self.groupBox_3.setTitle("")
        self.ImportSettingsXL.setText(
            QCoreApplication.translate(
                "Form", "Import workbench settings from external source", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.SheetName_Settings.setToolTip(
            QCoreApplication.translate(
                "Form", "Enter the name of sheet to import the settings from.", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.SheetName_Settings.setStatusTip(
            QCoreApplication.translate(
                "Form", "Enter the name of sheet to import the settings from.", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.SheetName_Settings.setWhatsThis(
            QCoreApplication.translate("Form", "Enter the name of sheet...", None)
        )
        # endif // QT_CONFIG(whatsthis)
        self.SheetName_Settings.setInputMask("")
        self.SheetName_Settings.setText("")
        self.SheetName_Settings.setPlaceholderText(
            QCoreApplication.translate("Form", "Enter the name of sheet...", None)
        )
        # if QT_CONFIG(tooltip)
        self.StartCell_Settings.setToolTip(
            QCoreApplication.translate(
                "Form", "Enter the cell to import the settings from.", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.StartCell_Settings.setWhatsThis(
            QCoreApplication.translate(
                "Form", "Enter the cell to import the settings from.", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.StartCell_Settings.setInputMask("")
        self.StartCell_Settings.setText("")
        self.StartCell_Settings.setPlaceholderText(
            QCoreApplication.translate("Form", "Enter the start cell...", None)
        )
        self.label_9.setText(
            QCoreApplication.translate(
                "Form",
                "<html><head/><body><p>Cell adress must be like &quot;B1&quot; or like &quot;R1C1&quot;. If empty, A1 will be used.</p></body></html>",
                None,
            )
        )
        self.label_13.setText(
            QCoreApplication.translate(
                "Form",
                '<html><head/><body><p>The startcell of the table with settings: <span style=" font-style:italic;">(This must be the top left cell.)</span></p></body></html>',
                None,
            )
        )
        self.label_14.setText(
            QCoreApplication.translate(
                "Form",
                "<html><head/><body><p>The name of the worksheet that containts the table with settings:</p></body></html>",
                None,
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.External_Source),
            QCoreApplication.translate("Form", "External Source", None),
        )
        self.groupBox.setTitle("")
        self.AddToolBarTechDraw.setText(
            QCoreApplication.translate(
                "Form", "Add toolbar to the TechDraw Workbench", None
            )
        )
        self.label_12.setText(
            QCoreApplication.translate("Form", "Set default template", None)
        )
        self.Import_templates.setText(
            QCoreApplication.translate("Form", "Import example templates", None)
        )
        self.Default_Template.setItemText(
            0, QCoreApplication.translate("Form", "A0_Landscape", None)
        )
        self.Default_Template.setItemText(
            1, QCoreApplication.translate("Form", "A1_Landscape", None)
        )
        self.Default_Template.setItemText(
            2, QCoreApplication.translate("Form", "A2_Landscape", None)
        )
        self.Default_Template.setItemText(
            3, QCoreApplication.translate("Form", "A3_Landscape", None)
        )
        self.Default_Template.setItemText(
            4, QCoreApplication.translate("Form", "A4_Landscape", None)
        )
        self.Default_Template.setItemText(
            5, QCoreApplication.translate("Form", "A4_Portrait", None)
        )

        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.TechDraw_Workbench),
            QCoreApplication.translate("Form", "TechDraw Workbench", None),
        )
        self.Spreadsheet_Layout.setTitle(
            QCoreApplication.translate("Form", "Spreadsheet", None)
        )
        self.label_27.setText(
            QCoreApplication.translate("Form", "Header background       ", None)
        )
        self.label_28.setText(
            QCoreApplication.translate("Form", "Header foreground", None)
        )
        self.label_29.setText(
            QCoreApplication.translate("Form", "Header font style", None)
        )
        self.SprHeaderFontStyle_Bold.setText(
            QCoreApplication.translate("Form", "Bold", None)
        )
        self.SprHeaderFontStyle_Italic.setText(
            QCoreApplication.translate("Form", "Italic", None)
        )
        self.SprHeaderFontStyle_Underline.setText(
            QCoreApplication.translate("Form", "Underline", None)
        )
        self.label_31.setText(
            QCoreApplication.translate("Form", "Table foreground", None)
        )
        self.label_30.setText(
            QCoreApplication.translate("Form", "Table background 1       ", None)
        )
        self.label_33.setText(
            QCoreApplication.translate("Form", "Table background 2", None)
        )
        self.label_32.setText(
            QCoreApplication.translate("Form", "Table font style", None)
        )
        self.SprTableFontStyle_Bold.setText(
            QCoreApplication.translate("Form", "Bold", None)
        )
        self.SprTableFontStyle_Italic.setText(
            QCoreApplication.translate("Form", "Italic", None)
        )
        self.SprTableFontStyle_Underline.setText(
            QCoreApplication.translate("Form", "Underline", None)
        )
        self.label_34.setText(
            QCoreApplication.translate("Form", "1st column font style", None)
        )
        self.SprColumnFontStyle_Bold.setText(
            QCoreApplication.translate("Form", "Bold", None)
        )
        self.SprColumnFontStyle_Italic.setText(
            QCoreApplication.translate("Form", "Italic", None)
        )
        self.SprColumnFontStyle_Underline.setText(
            QCoreApplication.translate("Form", "Underline", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.UIsettings),
            QCoreApplication.translate("Form", "UI Settings", None),
        )
        pass

    # retranslateUi
