from PyQt4.QtCore import *
from PyQt4.QtGui import *

from src.views.preloaderWidgetUI import Ui_preloaderWidgetForm

class PreloaderWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.parent = parent

    def start(self):
        self.mainWidget = QWidget()
        self.mainWidget.ui = Ui_preloaderWidgetForm()
        self.mainWidget.ui.setupUi(self.mainWidget)
        self.mainWidget.setGeometry(self.parent.geometry())
        self.mainWidget.setParent(self.parent)
        self.mainWidget.setStyleSheet("background-color: rgb(50,50,52,80%)")
        self.mainWidget.ui.loadingLabel.setStyleSheet("background-color: rgb(0,0,0,0); color: #d1d1d1;")
        self.mainWidget.show()

    def stop(self):
        self.mainWidget.close()
