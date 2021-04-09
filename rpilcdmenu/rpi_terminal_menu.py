from rpilcdmenu.base_menu import BaseMenu

class RpiTerminalMenu(BaseMenu):
    def __init__(self):
        """
        Initialize menu
        """
        super(self.__class__, self).__init__()

    def message(self, text):
        """ Send long string to LCD. 17th char wraps to second line"""
        print(text)
        return self

    def displayTestScreen(self):
        """
        Display test screen to see if your LCD screen is wokring
        """
        self.message('Hum. body 36,6\xDFC\nThis is test')

        return self

    def render(self):
        """
        Render menu
        """
        if len(self.items) == 0:
            self.message('Menu is empty')
            return self
        elif len(self.items) <= 2:
            options = (self.current_option == 0 and ">" or " ") + self.items[0].text
            if len(self.items) == 2:
                options += "\n" + (self.current_option == 1 and ">" or " ") + self.items[1].text
            print(options)
            self.message(options)
            return self

        options = ">" + self.items[self.current_option].text

        if self.current_option + 1 < len(self.items):
            options += "\n " + self.items[self.current_option + 1].text
        else:
            options += "\n " + self.items[0].text

        self.message(options)

        return self
