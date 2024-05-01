import flet as ft


def main(page: ft.Page):
    def reg_btn(e):
        # твой код для кнопки зарегистрироваться
        pass

    page.title = "Страница регистрации"
    page.bgcolor = "#828282"  # Установить белый цвет фона страницы

    logo_text = ft.Text(value='RealtorParser\n'
                              '\n'
                              '\n'
                              '\n'
                              '\n', text_align=ft.TextAlign.CENTER, size=36, color='black')
    name_page = ft.Text(value='Регистрация', text_align=ft.TextAlign.CENTER, size=32, color='black')
    name_text = ft.Text(value='Имя', text_align=ft.TextAlign.CENTER, size=20, color='black')
    name_field = ft.TextField(width=334, height=41)
    sur_name_text = ft.Text(value='Фамилия', text_align=ft.TextAlign.CENTER, size=20, color='black')
    sur_name_field = ft.TextField(width=334, height=41)
    email_text = ft.Text(value='Почта', text_align=ft.TextAlign.CENTER, size=20, color='black')
    email_field = ft.TextField(width=334, height=41)
    login_text = ft.Text(value='Логин', text_align=ft.TextAlign.CENTER, size=20, color='black')
    login_field = ft.TextField(width=334, height=41)
    pass_text = ft.Text(value='Пароль', text_align=ft.TextAlign.CENTER, size=20, color='black')
    pass_field = ft.TextField(width=334, height=41, password=True, can_reveal_password=True)
    reg_button = ft.FilledButton(text='Зарегестрироваться', width=334, height=41, on_click=reg_btn)

    page.add(
        ft.Row([
            logo_text
        ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([ft.Column([name_page], alignment=ft.MainAxisAlignment.CENTER)], ft.MainAxisAlignment.CENTER),
        ft.Row([
            ft.Column([
                name_text,
                name_field,
                sur_name_text,
                sur_name_field,
                email_text,
                email_field,
                login_text,
                login_field,
                pass_text,
                pass_field,
                reg_button
            ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(target=main)
