from PySide.QtGui import QStyledItemDelegate, QColor, QStyle, QPen, QPixmap
from PySide.QtCore import Qt

class HamsterDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        if not index.isValid():
            return
        value = index.data()

        if index.column() == 3:
            pixmap =  QPixmap(":/icons/icons/bookmark.png");
            option.rect.setRight(option.rect.left()+28)
            option.rect.setHeight(28)
            painter.drawPixmap(option.rect, pixmap)

        elif index.column() == 4:
            pixmap =  QPixmap(":/icons/icons/emblem-favorite.png");
            option.rect.setRight(option.rect.left()+28)
            option.rect.setHeight(28)
            painter.drawPixmap(option.rect, pixmap)

        elif index.column() == 0 and option.state & QStyle.State_MouseOver:
            if value:
                painter.save()

                option.font.setUnderline(True)
                pen = painter.pen()
                pen.setColor(QColor(47, 111, 112))
                painter.setPen(pen)
                font = painter.font()
                font.setUnderline(True)
                painter.setFont(font)
                option.rect.setLeft(option.rect.left()+4)
                painter.drawText(option.rect, Qt.AlignLeft, unicode(value))

                painter.restore()
        else:
            painter.setPen(QPen(Qt.black))
            option.rect.setLeft(option.rect.left()+4)
            painter.drawText(option.rect, Qt.AlignLeft, unicode(value))
            #QStyledItemDelegate.paint(self, painter, option, index)
