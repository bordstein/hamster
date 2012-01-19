#!/usr/bin/env python

#############################################################################
##  Hamster - Nice and friendly movie collection manager
##  Copyright (C) 2012 Christoph Meinhart, Michael Seiwald
##  
##  This file is part of Hamster.
##  
##  Hamster is free software; you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation; either version 2 of the License, or
##  (at your option) any later version.
##  
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##  
##  You should have received a copy of the GNU General Public License along
##  with this program; if not, write to the Free Software Foundation, Inc.,
##  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
## 
#############################################################################

import sys
from PySide.QtCore import QTimer, QUrl, QObject, QCoreApplication, Signal, QBuffer, QIODevice, Qt
from PySide.QtGui import QImage
from PySide.QtNetwork import QNetworkRequest, QNetworkAccessManager

class DownloadManager(QObject):
    dl_finished = Signal(str, str)
    dl_failed = Signal(str)

    def __init__(self):
        QObject.__init__(self)
        self.manager = QNetworkAccessManager()
        self.current_downloads = {}

        self.manager.finished.connect(self.download_finished)

    def download_cover(self, imdb_id, dl_url):
        url = QUrl(dl_url)
        req = QNetworkRequest(url)
        reply = self.manager.get(req)
        self.current_downloads[reply] = imdb_id

    def execute(self):
        print "downloader on the run"
        dls = ["http://www.pyside.org/docs/pyside/_static/pysidelogo.png",
                "https://www.google.com/intl/en_com/images/srpr/logo3w.png"]
        for dl in dls:
            self.do_download(dl)

    def download_finished(self, reply):
        url = reply.url()
        imdb_id = self.current_downloads.pop(reply)

        if reply.error():
            print "Dowload of %s (%s) failed" % (imdb_id, url.toEncoded())
            self.dl_failed.emit(imdb_id)
            return

        # save to buffer in memory
        buffer = QBuffer()
        buffer.open(QIODevice.WriteOnly);
        buffer.write(reply.readAll())
        buffer.close()
        raw_img = buffer.data()
        scaled_raw_img = self.downscale_image(raw_img)
        if not scaled_raw_img:
            # fallback to unscaled cover
            scaled_raw_img = raw_img
        payload = scaled_raw_img.toBase64()
        base64_image = unicode(payload)
        print "Download of %s succeded" % url.toEncoded()
        reply.deleteLater()
        self.dl_finished.emit(imdb_id, base64_image)

    def downscale_image(self, raw_img):
        img = QImage()
        success = img.loadFromData(raw_img)
        if not success:
            return
        success = scaledPixmap = img.scaled(200, 300,
                Qt.KeepAspectRatio, Qt.SmoothTransformation)
        if not success:
            return
        buffer = QBuffer()
        buffer.open(QIODevice.WriteOnly);
        success = scaledPixmap.save(buffer, 'JPG')
        buffer.close()
        if not success:
            print "could not write!"
            return
        print "successfully downsized"
        return buffer.data()


    def lastlog(self, url, filename):
        print url, "to", filename, "ok"
        if len(self.current_downloads) == 0:
            print "bye"
            QCoreApplication.instance().quit()

if __name__ == "__main__":
    d = DownloadManager()
    app = QCoreApplication(sys.argv)
    d.dl_finished.connect(d.lastlog)
    QTimer.singleShot(0, d.execute)
    app.exec_()
