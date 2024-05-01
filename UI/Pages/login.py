import flet as ft

def main(page: ft.Page):
    def login_btn(e):
        #твой код для кнопки войти
        pass

    page.title = "Страница входа"
    page.bgcolor = "#828282"  # Установить белый цвет фона страницы

    logo_text = ft.Text(value='RealtorParser\n'
                              '\n'
                              '\n'
                              '\n'
                              '\n', text_align=ft.TextAlign.CENTER, size=36, color='black')
    name_page = ft.Text(value='Вход', text_align=ft.TextAlign.CENTER, size=32, color='black')
    login_text = ft.Text(value='Логин', text_align=ft.TextAlign.CENTER, size=20, color='black')
    user_login = ft.TextField(width=334, height=41)
    password_text = ft.Text(value='Пароль', text_align=ft.TextAlign.CENTER, size=20, color='black')
    user_password = ft.TextField(width=334, height=41, password=True, can_reveal_password=True)
    login_button = ft.FilledButton(text='Войти', width=334, height=41, on_click=login_btn)
    reg_button = ft.FilledButton(text='Зарегестрироваться', width=334, height=41)


    page.add(
        ft.Row([
            logo_text
        ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([ft.Column([name_page], alignment=ft.MainAxisAlignment.CENTER)], ft.MainAxisAlignment.CENTER),
        ft.Row([
            ft.Column([
                login_text,
                user_login,
                password_text,
                user_password,
                login_button,
                reg_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)