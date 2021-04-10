from rpilcdmenu import RpiI2cMenu


class RpiI2cSubMenu(RpiI2cMenu):
    def __init__(self, base_menu):
        """
        Initialize SubMenu
        """
        self.lcd = base_menu.lcd

        super(RpiI2cMenu, self).__init__(base_menu)
