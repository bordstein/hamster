from PySide.QtGui import QStyledItemDelegate, QColor, QStyle, QPen, QPixmap, QAbstractItemView
from PySide.QtCore import Qt
from moviehamster.constants import *

class HamsterDelegate(QStyledItemDelegate):
    def __init__(self, parentView):
        QStyledItemDelegate.__init__(self, parentView)
        assert isinstance(parentView, QAbstractItemView), \
            "The first argument must be the view"

        # We need that to receive mouse move events in editorEvent
        self.parentView = parentView

        # Revert the mouse cursor when the mouse isn't over 
        # an item but still on the view widget
        self.parentView.viewportEntered.connect(self.parentView.unsetCursor)
        
        self.pixmap_favourite_enabled = QPixmap(":/icons/favorite_enabled");
        self.pixmap_favourite_disabled = QPixmap(":/icons/favorite_disabled");
        self.pixmap_watchlater_enabled = QPixmap(":/icons/clock_enabled");
        self.pixmap_watchlater_disabled = QPixmap(":/icons/clock_disabled");

    def paint(self, painter, option, index):
        if not index.isValid():
            self.unsetCursor()
            return
        value = index.data()

        if index.column() != MOVIELIST_COL_TITLE and option.state & QStyle.State_MouseOver:
            self.parentView.unsetCursor()

        if index.column() == MOVIELIST_COL_FAVOURITE:
            option.rect.setRight(option.rect.left()+18)
            option.rect.setHeight(21)
            option.rect.setTop(option.rect.top()+3) #4 up -> reduce height by 4
            if value:
                painter.drawPixmap(option.rect, self.pixmap_favourite_enabled)
            else:
                painter.drawPixmap(option.rect, self.pixmap_favourite_disabled)

        elif index.column() == MOVIELIST_COL_WATCHLATER:
            option.rect.setRight(option.rect.left()+18)
            option.rect.setHeight(21)
            option.rect.setTop(option.rect.top()+3) #4 up -> reduce height by 4
            if value:
                painter.drawPixmap(option.rect, self.pixmap_watchlater_enabled)
            else:
                painter.drawPixmap(option.rect, self.pixmap_watchlater_disabled)

        elif index.column() == MOVIELIST_COL_TITLE and option.state & QStyle.State_MouseOver:
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
                self.parent().setCursor(Qt.PointingHandCursor)
        else:
            option.rect.setLeft(option.rect.left()+4)
            painter.drawText(option.rect, Qt.AlignLeft, unicode(value))
