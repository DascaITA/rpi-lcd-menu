from rpilcdmenu import RpiTerminalMenu


class RpiTerminalSubMenu(RpiTerminalMenu):
    def __init__(self, base_menu):
        """
        Initialize SubMenu
        """
        #self.lcd = base_menu.lcd
        #test
        
        super(RpiTerminalMenu, self).__init__(base_menu)
