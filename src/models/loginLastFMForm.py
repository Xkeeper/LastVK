from PyQt4.QtCore import *
from PyQt4.QtGui import *

from src.views.loginLastFMFormUI import Ui_Form

class LoginLastFM(QWidget):
    getAuthUrlSignal = pyqtSignal(unicode)
    goUrlSignal = pyqtSignal(str)
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.webview = self.ui.lastFMwebView
        self.goUrlSignal.connect(self.goUrl)
        self.connect (self.webview.page().networkAccessManager(),
                      SIGNAL("sslErrors (QNetworkReply *, const QList<QSslError> &)"),
                      self.sslErrorHandler)

    def sslErrorHandler(self, reply, errorList):
            reply.ignoreSslErrors()

    @pyqtSlot(str)
    def goUrl(self, url):
        self.webview.load(QUrl(url))

    @pyqtSlot(QUrl)
    def on_lastFMwebView_urlChanged(self, url):
        self.getAuthUrlSignal.emit(unicode(url.toString()))
