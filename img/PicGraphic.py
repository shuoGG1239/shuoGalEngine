from PyQt5.QtCore import QObject, QSize, Qt, pyqtSignal
from PyQt5.QtWidgets import QGraphicsPixmapItem

from anime.AnimationGraphic import AnimationGraphic


class PicGraphic(QObject, QGraphicsPixmapItem):
    sizePixmapOrig = QSize()
    leftClick = pyqtSignal()
    rightClick = pyqtSignal()
    animeEffect = None

    def __init__(self, pic, x, y, animeGeomOn, animeOpacOn, parent):
        """
        初始化
        :param pic: QPixmap
        :param x:
        :param y:
        :param animeGeomOn: bool
        :param animeOpacOn: bool
        :param parent:
        """
        QGraphicsPixmapItem.__init__(pic, parent)
        # 改变几何中心, 默认在重心
        self.sizePixmapOrig.setWidth(pic.width())
        self.sizePixmapOrig.setHeight(pic.height())
        self.setTransformOriginPoint(pic.width() * 0.5, pic.height() * 0.5)
        self.setPos(x, y)
        self.setOpacity(1)
        self.setScale(1)
        self.show()
        self.enableAnime(animeGeomOn, animeOpacOn)

    def enableAnime(self, animeGeomOn, animeOpacOn):
        """
        动画效果使能
        :param animeGeomOn: bool
        :param animeOpacOn: bool
        :return:
        """
        if animeGeomOn and animeOpacOn:
            self.animeEffect = AnimationGraphic(self, self, True, True, True, True)
        elif animeGeomOn and not animeOpacOn:
            self.animeEffect = AnimationGraphic(self, self, True, True, True, False)
        elif not animeGeomOn and animeOpacOn:
            self.animeEffect = AnimationGraphic(self, self, False, False, False, True)

    def setGeomCenter(self, x_percent, y_percent):
        """
        设置几何中心
        :param x_percent:
        :param y_percent:
        :return:
        """
        self.setTransformOriginPoint(self.scale() * (self.sizePixmapOrig.width()) * x_percent,
                                     self.scale() * (self.sizePixmapOrig.height()) * y_percent)

    def getScaledPixmap(self, inputPic, scale):
        """
        缩放
        :param inputPic: QPixmap
        :param scale: float 缩放倍数
        :return: QPixmap
        """
        rePic = inputPic.scaled(inputPic.width() * scale, inputPic.height() * scale)
        return rePic

    def mouseReleaseEvent(self, e):
        # 响应左击事件
        if (e.button() & Qt.LeftButton) == 1:
            self.leftClick.emit()
        # 响应右击事件
        elif (e.button() & Qt.RightButton) == 1:
            self.rightClick.emit()
