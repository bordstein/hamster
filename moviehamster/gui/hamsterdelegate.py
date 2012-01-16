from PySide.QtGui import QStyledItemDelegate, QColor, QStyle, QPen, QPixmap, QAbstractItemView
from PySide.QtCore import Qt

class HamsterDelegate(QStyledItemDelegate):
    def __init__(self, parentView):
        QStyledItemDelegate.__init__(self, parentView)
        assert isinstance(parentView, QAbstractItemView), \
            "The first argument must be the view"

        # We need that to receive mouse move events in editorEvent
        self.parentView = parentView
        self.parentView.setMouseTracking(True)

        # Revert the mouse cursor when the mouse isn't over 
        # an item but still on the view widget
        self.parentView.viewportEntered.connect(self.parentView.unsetCursor)

    def paint(self, painter, option, index):
        if not index.isValid():
            self.unsetCursor()
            return
        value = index.data()

        if index.column() != 0 and option.state & QStyle.State_MouseOver:
            self.parentView.unsetCursor()

        if index.column() == 3:
            pixmap =  QPixmap(":/icons/icons/emblem-favorite.png");
            option.rect.setRight(option.rect.left()+16)
            option.rect.setHeight(20)
            option.rect.setTop(option.rect.top()+4) #4 up -> reduce height by 4
            painter.drawPixmap(option.rect, pixmap)

        elif index.column() == 4:
            pixmap =  QPixmap(":/icons/icons/bookmark.png");
            option.rect.setRight(option.rect.left()+16)
            option.rect.setHeight(20)
            option.rect.setTop(option.rect.top()+4) #4 up -> reduce height by 4
            painter.drawPixmap(option.rect, pixmap)

        elif index.column() == 0 and option.state & QStyle.State_MouseOver:
            if value:
                painter.save()

                option.font.setUnderline(True)
                pen = painter.pen()
                pen.setColor(QColor(250, 250, 250))
                painter.setPen(pen)
                font = painter.font()
                font.setUnderline(True)
                painter.setFont(font)
                option.rect.setLeft(option.rect.left()+10)
                option.rect.setTop(option.rect.top()+4) #4 up -> reduce height by 4
                painter.drawText(option.rect, Qt.AlignLeft, unicode(value))

                painter.restore()
                self.parent().setCursor(Qt.PointingHandCursor)
        else:
            option.rect.setLeft(option.rect.left()+10)
            option.rect.setTop(option.rect.top()+4) #4 up -> reduce height by 4
            painter.drawText(option.rect, Qt.AlignLeft, unicode(value))
            #QStyledItemDelegate.paint(self, painter, option, index)
