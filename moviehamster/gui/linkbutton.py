from PySide.QtCore import Qt
from PySide.QtGui import QToolButton

class LinkButton(QToolButton):
    def __init__(self, text, parent=None):
        QToolButton.__init__(self, parent)
        self.setText(text)
        self.setCursor(Qt.PointingHandCursor)
        self.setStyleSheet("QToolButton:hover{\n"
                           "    text-decoration:underline;\n"
                           "    color:rgb(47, 111, 112)"
                           "\n}"
                           "QToolButton{\n"
                           "    border:none;\n"
                           "    background:none;\n"
                           "}")

