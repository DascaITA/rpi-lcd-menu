from rpilcdmenu import RpiTerminalMenu


class RpiTerminalSubMenu(RpiTerminalMenu):
    def __init__(self, base_menu):
        """
        Initialize SubMenu
        """
        self.lcd = base_menu.lcd

        super(RpiTerminalMenu, self).__init__(base_menu)
