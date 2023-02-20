import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtDataVisualization import (Q3DScatter, QScatterDataItem,
                                       QScatterDataArray)

class Scatter3D(QWidget):
    def __init__(self):
        super().__init__()
        # Create 3D scatter plot widget
        self.scatter = Q3DScatter()
        self.container = QWidget.createWindowContainer(self.scatter)
        # Set plot title and add data
        self.scatter.setWindowTitle("3D Scatter Plot Example")
        self.add_data()
        # Set the main window properties and layout
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("3D Plot Example")
        layout = QVBoxLayout()
        layout.addWidget(self.container)
        self.setLayout(layout)
        self.show()

    def add_data(self):
        # Create data array for scatter plot
        data_array = QScatterDataArray()
        data_item = QScatterDataItem()
        data_item.setPosition(QVector3D(0.5, 0.5, 0.5))
        data_item.setColor(Qt.red)
        data_array.append(data_item)
        # Add data to scatter plot
        self.series = QScatter3DSeries(data_array)
        self.series.setMesh(QAbstract3DSeries.MeshSphere)
        self.series.setItemSize(0.1)
        self.scatter.addSeries(self.series)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Scatter3D()
    sys.exit(app.exec_())
