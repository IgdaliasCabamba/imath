import sys
import os

if getattr(sys, "frozen", False):
    root_path = os.path.dirname(os.path.realpath(sys.executable))
else:
    root_path = os.path.dirname(os.path.realpath(__file__))

main_path = os.getcwd()

sys.path.append(root_path)
sys.path.append(main_path)

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from libs.modernwindow.window import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IMath")
        self.setGeometry(100, 100, 800, 600)  # x, y, width, height
        
        # Create the main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        
        # Create toolbar
        self.create_toolbar()
        
        # Create menu bar
        self.create_menu_bar()
        
        # Add some example widgets
        self.create_widgets()
        
        # Create status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")
    
    def create_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        
        # Add toolbar actions
        new_action = toolbar.addAction("New")
        new_action.setStatusTip("Create new file")
        new_action.triggered.connect(self.new_file)
        
        # Add separator
        toolbar.addSeparator()
        
        # Add another action
        edit_action = toolbar.addAction("Edit")
        edit_action.setStatusTip("Edit current file")
        edit_action.triggered.connect(self.edit_file)
    
    def create_menu_bar(self):
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("&File")
        
        # Add menu items
        new_action = file_menu.addAction("&New")
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(self.new_file)
        
        open_action = file_menu.addAction("&Open")
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_file)
        
        file_menu.addSeparator()
        
        exit_action = file_menu.addAction("&Exit")
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        
        # Edit menu
        edit_menu = menubar.addMenu("&Edit")
        edit_action = edit_menu.addAction("&Edit")
        edit_action.triggered.connect(self.edit_file)
    
    def create_widgets(self):
        # Create a group box for better organization
        group_box = QGroupBox("Example Widgets")
        group_layout = QVBoxLayout()
        
        # Add a label
        self.label = QLabel("Welcome to QtPy!")
        self.label.setAlignment(Qt.AlignCenter)
        group_layout.addWidget(self.label)
        
        # Add a button
        self.button = QPushButton("Click Me")
        self.button.clicked.connect(self.button_clicked)
        group_layout.addWidget(self.button)
        
        # Add a line edit
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Enter text here")
        self.line_edit.textChanged.connect(self.text_changed)
        group_layout.addWidget(self.line_edit)
        
        group_box.setLayout(group_layout)
        self.layout.addWidget(group_box)
    
    def button_clicked(self):
        self.label.setText("Button was clicked!")
        self.status_bar.showMessage("Button clicked", 2000)  # Show for 2 seconds
    
    def text_changed(self, text):
        self.status_bar.showMessage(f"Text changed: {text}", 1000)
    
    def new_file(self):
        self.status_bar.showMessage("Creating new file...")
    
    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "",
            "All Files (*);;Text Files (*.txt)"
        )
        if file_name:
            self.status_bar.showMessage(f"Opening: {file_name}")
    
    def edit_file(self):
        self.status_bar.showMessage("Editing file...")

def main():
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    
    # Set application-wide stylesheet (optional)
    app.setStyle("Fusion")  # Other options: 'Windows', 'WindowsVista', 'Fusion'
    app.setDesktopFileName("Imath")
    app.setApplicationVersion("0.0.1")
    app.setApplicationName("Intelligent Math")
    app.setDesktopSettingsAware(False)
    
    window = MainWindow()
    exe = ModernWindow(window)
    exe.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()