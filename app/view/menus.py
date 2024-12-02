from PyQt5.QtWidgets import QMenu


class AppMenuBar(QMenu):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        
        file_menu = self.addMenu("&File")
        
        # Add menu items
        new_action = file_menu.addAction("&New")
        new_action.setShortcut("Ctrl+N")
        #new_action.triggered.connect(self.new_file)
        
        open_action = file_menu.addAction("&Open")
        open_action.setShortcut("Ctrl+O")
        #open_action.triggered.connect(self.open_file)
        
        file_menu.addSeparator()
        
        exit_action = file_menu.addAction("&Exit")
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        
        # Edit menu
        edit_menu = self.addMenu("&Edit")
        edit_action = edit_menu.addAction("&Edit")
        #edit_action.triggered.connect(self.edit_file)