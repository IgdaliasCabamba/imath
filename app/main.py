import os
import sys

if getattr(sys, 'frozen', False):
    ROOT_PATH = os.path.dirname(os.path.realpath(sys.executable))
else:
    ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

MAIN_PATH = os.getcwd()

sys.path.extend([ROOT_PATH, MAIN_PATH])

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QGroupBox, QVBoxLayout, QLabel, 
    QPushButton, QLineEdit, QStatusBar, QFileDialog
)
from PyQt5.QtCore import Qt
from libs.modernwindow.window import ModernWindow
from libs.qtmd.splitter import Splitter
from view import AppMenuBar, AppToolBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(100, 100, 800, 600)
        
        self.central_widget = Splitter()
        self.setCentralWidget(self.central_widget)
        
        self.menu_bar = AppMenuBar()
        self.create_widgets()
        
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage('Ready')
    
        self.toolbar = AppToolBar()
        
        new_action = self.toolbar.addAction('New')
        new_action.setStatusTip('Create new file')
        new_action.triggered.connect(self.new_file)
        
        self.toolbar.addSeparator()
        
        edit_action = self.toolbar.addAction('Edit')
        edit_action.setStatusTip('Edit current file')
        edit_action.triggered.connect(self.edit_file)

        self.addToolBar(Qt.LeftToolBarArea, self.toolbar)
    
    def create_widgets(self):
        group_box = QGroupBox('Example Widgets')
        group_layout = QVBoxLayout()
        
        self.label = QLabel('Welcome to QtPy!')
        self.label.setAlignment(Qt.AlignCenter)
        group_layout.addWidget(self.label)
        
        self.button = QPushButton('Click Me')
        self.button.clicked.connect(self.button_clicked)
        group_layout.addWidget(self.button)
        
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText('Enter text here')
        self.line_edit.textChanged.connect(self.text_changed)
        group_layout.addWidget(self.line_edit)
        
        group_box.setLayout(group_layout)
        self.central_widget.addWidget(group_box)
    
    def button_clicked(self):
        self.label.setText('Button was clicked!')
        self.status_bar.showMessage('Button clicked', 2000)
    
    def text_changed(self, text):
        self.status_bar.showMessage(f'Text changed: {text}', 1000)
    
    def new_file(self):
        self.status_bar.showMessage('Creating new file...')
    
    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            'Open File',
            '',
            'All Files (*);;Text Files (*.txt)'
        )
        if file_name:
            self.status_bar.showMessage(f'Opening: {file_name}')
    
    def edit_file(self):
        self.status_bar.showMessage('Editing file...')


def main():
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    
    app = QApplication(sys.argv)
    
    app.setStyle('Fusion')
    app.setDesktopFileName('Imath')
    app.setApplicationVersion('0.0.1')
    app.setApplicationName('Intelligent Math')
    app.setDesktopSettingsAware(False)
    
    window = MainWindow()
    window.setWindowTitle('IMath')
    exe = ModernWindow(window)
    exe.tool_menu.setMenu(window.menu_bar)
    exe.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()