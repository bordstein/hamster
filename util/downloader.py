#!/usr/bin/env python
import sys
from PySide.QtCore import QFile, QFileInfo, QTimer, QUrl, QObject, QIODevice, QCoreApplication, QTemporaryFile, Signal
from PySide.QtNetwork import QNetworkRequest, QNetworkAccessManager

class DownloadManager(QObject):
    dl_finished = Signal(str)

    def __init__(self):
        QObject.__init__(self)
        self.manager = QNetworkAccessManager()
        self.current_downloads = {}

        self.manager.finished.connect(self.download_finished)

    def do_download(self, dl_url):
        url = QUrl.fromEncoded(dl_url)
        req = QNetworkRequest(url)
        reply = self.manager.get(req)
        self.current_downloads[reply] = dl_url

    def get_file_name(self, url):
        path = url.path()
        basename = QFileInfo(path).fileName()
        if not basename:
            basename = "download"
        if QFile.exists(basename):
            print "aaaaaaaaaaaaaaaah"
            return
        return basename

    def save_to_disk(self, filename, data):
        f = QFile(filename)
        if not f.open(QIODevice.WriteOnly):
            print "could not open %s for writing" % filename
            return False
        f.write(data.readAll())
        f.close()
        return True

    def execute(self):
        print "downloader on the run"
        dls = ["http://www.pyside.org/docs/pyside/_static/pysidelogo.png",
                "https://www.google.com/intl/en_com/images/srpr/logo3w.png"]
        for dl in dls:
            self.do_download(dl)

    def download_finished(self, reply):
        url = reply.url()
        if reply.error():
            print "Dowload of %s failed" % url.toEncoded()
            return
        else:
            #filename = self.save_file_name(url)
            f = QTemporaryFile()
            if f.open():
                filename = f.fileName()
            else:
                print "Creation of tempfile for %s failed" % url.toEncoded()
                return

        if self.save_to_disk(filename, reply):
            print "Download of %s succeded (saved to %s)\n" % (
                    url.toEncoded(), filename)
            url = self.current_downloads.pop(reply)
            reply.deleteLater()
            self.dl_finished.emit(url)

    def lastlog(self, url):
        print url, "ok"
        if len(self.current_downloads) == 0:
            print "bye"
            QCoreApplication.instance().quit()

if __name__ == "__main__":
    d = DownloadManager()
    app = QCoreApplication(sys.argv)
    d.dl_finished.connect(d.lastlog)
    QTimer.singleShot(0, d.execute)
    app.exec_()
