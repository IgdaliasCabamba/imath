import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QToolBar, QAction, QLabel)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set window properties
        self.setWindowTitle('Vertical Right Toolbar App')
        self.setGeometry(100, 100, 800, 600)

        # Create central widget and main layout
        central_widget = QWidget()
        main_layout = QHBoxLayout()
        
        # Main content area (placeholder)
        main_content = QLabel('Main Content Area')
        main_content.setAlignment(Qt.AlignCenter)
        
        # Create vertical toolbar on the right
        toolbar = QToolBar('Vertical Toolbar')
        toolbar.setOrientation(Qt.Vertical)
        toolbar.setMovable(False)
        
        # Add actions to toolbar
        action1 = QAction(QIcon(), 'Action 1', self)
        action1.triggered.connect(self.on_action1)
        toolbar.addAction(action1)
        
        action2 = QAction(QIcon(), 'Action 2', self)
        action2.triggered.connect(self.on_action2)
        toolbar.addAction(action2)
        
        action3 = QAction(QIcon(), 'Action 3', self)
        action3.triggered.connect(self.on_action3)
        toolbar.addAction(action3)
        
        # Add widgets to main layout
        main_layout.addWidget(main_content, 4)  # 4/5 width for content
        main_layout.addWidget(toolbar, 1)  # 1/5 width for toolbar
        
        # Set layout
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def on_action1(self):
        print("Action 1 triggered")

    def on_action2(self):
        print("Action 2 triggered")

    def on_action3(self):
        print("Action 3 triggered")

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()