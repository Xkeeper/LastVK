from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import QWebPage
from PyQt4.QtNetwork import QNetworkAccessManager, QNetworkCookieJar

from src.views.loginVkFormUI import Ui_Form
class UserAgentWebPage(QWebPage):
    def userAgentForUrl(self, QUrl):
        return 'Opera/9.80 (S60; SymbOS; Opera Mobi/499; U; ru) Presto/2.4.18 Version/10.00'


class LoginVk(QWidget):
    acceptCookieSignal = pyqtSignal(str)
    def __init__(self):
        QWidget.__init__(self)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.webview = self.ui.vkWebView
        self.manager = QNetworkAccessManager()
        self.manager.setCookieJar(QNetworkCookieJar())
        self.webview.setPage(UserAgentWebPage())
        self.webview.page().setNetworkAccessManager(self.manager)
        self.connect (self.webview.page().networkAccessManager(),
                      SIGNAL("sslErrors (QNetworkReply *, const QList<QSslError> &)"),
                        self.sslErrorHandler)
        self.webview.load(QUrl("https://m.vk.com"))
        self.isCookieSaved = False


    def sslErrorHandler(self, reply, errorList):
        reply.ignoreSslErrors()


    @pyqtSlot(QUrl)
    def on_vkWebView_urlChanged(self, url):
        print 'url: {0}'.format(url)
        self.cookies = {}
        _url = unicode(url.toString())
        login_status = _url.split('/')[-1]
        for cookie in self.manager.cookieJar().allCookies():
            self.cookies[str(cookie.name())] = str(cookie.value())
        if 'remixsid' in self.cookies and login_status != 'login?act=blocked':
            self.acceptCookieSignal.emit(self.cookies['remixsid'])
            self.isCookieSaved = True

    @pyqtSlot(bool)
    def on_vkWebView_loadFinished(self, status): #Hack to fix crash QWebView on close() in slot urlChanged
        if self.isCookieSaved:
            self.close()