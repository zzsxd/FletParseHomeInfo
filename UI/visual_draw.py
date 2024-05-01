import flet as ft
from flet_navigator import VirtualFletNavigator
from UI.Pages import login, pagemain, reg

class UI:
    def __init__(self, config, db):
        super(UI, self).__init__()
        self.__vault_keys = ['current_user']
        self.__config = config
        self.__db = db
        self.__login = login.main()
        self.__pagemain = pagemain.main()
        self.__reg = reg.main()

    def main(self, page: ft.Page):
        flet_navigator = VirtualFletNavigator(
            {
                'login': self.__login.main,
                'pagemain': self.__pagemain.main,
                'reg': self.__reg.main,
            }
        )
        flet_navigator.render(page)