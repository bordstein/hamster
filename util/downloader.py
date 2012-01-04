#!/usr/bin/env python
import sys
from PySide.QtCore import QFile, QFileInfo, QTimer, QUrl, QObject, QIODevice, QCoreApplication
from PySide.QtNetwork import QNetworkRequest, QNetworkReply, QNetworkAccessManager

class DownloadManager(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.manager = QNetworkAccessManager()
        self.current_downloads = []

        self.manager.finished.connect(self.download_finished)

    def do_download(self, url):
        req = QNetworkRequest(url)
        reply = self.manager.get(req)
        self.current_downloads.append(reply)

    def save_file_name(self, url):
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
        dls = ["http://www.pyside.org/docs/pyside/_static/pysidelogo.png"]
        for dl in dls:
            url = QUrl.fromEncoded(dl)
            self.do_download(url)

    def download_finished(self, reply):
        url = reply.url()
        if reply.error():
            print "Dowload of %s failed" % url.toEncoded()
        else:
            filename = self.save_file_name(url)
        if self.save_to_disk(filename, reply):
            print "Download of %s succeded (saved to %s)\n" % (
                    url.toEncoded(), filename)
            self.current_downloads.remove(reply)
            reply.deleteLater()
            if len(self.current_downloads) == 0:
                QCoreApplication.instance().quit()

if __name__ == "__main__":
    d = DownloadManager()
    app = QCoreApplication(sys.argv)
    QTimer.singleShot(0, d.execute)
    app.exec_()
