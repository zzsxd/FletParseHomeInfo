import flet as ft


def main(page: ft.Page):



    def send_msg(e):
        # твой код для: комментарии - отправить комментарий
        pass

    def studio_btns(e):
        # твой код для выбора количества комнат в фильтре
        pass

    def author(e):
        # твой код для выбора автора в фильтре
        pass

    def close_dlg(e):
        # сюда код для текстовых полей - адрес, площадь, цена, этаж (нужно сначала считать данные с этих полей)
        dlg_modal.open = False
        page.update()

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Фильтр"),
        content=ft.Column(
            [
                ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Text(value='Комнаты:', size=12),
                                ft.FilledButton(text='Студия', on_click=studio_btns),
                                ft.FilledButton(text="1", on_click=studio_btns),
                                ft.FilledButton(text="2", on_click=studio_btns),
                                ft.FilledButton(text="3", on_click=studio_btns),
                                ft.FilledButton(text="4+", on_click=studio_btns)
                            ]
                        ),
                        ft.Row([
                            ft.Text(value='Автор', size=12),
                            ft.FilledButton(text="Частное лицо", on_click=author),
                            ft.FilledButton(text="Риелтор", on_click=author)
                        ])
                    ]
                ),
                ft.Column(
                    [
                        ft.TextField(label='Адрес'),
                        ft.TextField(label='Площадь'),
                        ft.TextField(label='Цена'),
                        ft.TextField(label='Этаж')
                    ]
                )
            ]
        ),
        actions=[
            ft.TextButton("Подтвердить", on_click=close_dlg),
        ],
    )

    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    def show_bs(e):
        bs.open = True
        bs.update()

    def close_bs(e):
        bs.open = False
        bs.update()

    bs = ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                    ft.Row([ft.Text("Комментарии                                                 ", size=24), ft.FilledButton(text="Закрыть", icon="CLOSE", on_click=close_bs)]),
                    ft.Text("Олег Тинькофф: Уже в работе у другого риелтора", size=16),
                    ft.Text("Билл Гейтс: Принял", size=16),
                    ft.TextField(label="Напишите комментарий"),
                    ft.OutlinedButton(text="Отправить", icon="SEND", on_click=send_msg)
                ],
                tight=True,
            ),
            padding=10,
            border_radius=1,
        ),
        open=False,
    )

    page.title = "Главная страница"
    page.bgcolor = "#828282"  # Установить белый цвет фона страницы

    logo_text = ft.Text(value='RealtorParser',
                        text_align=ft.TextAlign.LEFT, size=36, color='black')
    parser_button = ft.FilledButton(text='Парсер', width=139, height=32)
    analys_button = ft.FilledButton(text='Анализ по агрегаторам', width=280, height=32)

    home_button = ft.FilledButton(text='Квартиры')
    home_arenda_button = ft.FilledButton(text='Квартиры (сдать)')
    home_city_button = ft.FilledButton(text='Загородная недвижимость')

    filter_button = ft.FilledButton(text='Фильтр', icon="SETTINGS", on_click=open_dlg_modal)

    table = ft.DataTable(
        border=ft.border.all(2, "white"),
        border_radius=10,
        vertical_lines=ft.border.BorderSide(1, "black"),
        horizontal_lines=ft.border.BorderSide(1, "black"),
        columns=[
            ft.DataColumn(ft.Text("Адрес")),
            ft.DataColumn(ft.Text("Этаж"), numeric=True),
            ft.DataColumn(ft.Text("Площадь"), numeric=True),
            ft.DataColumn(ft.Text("Комнаты"), numeric=True),
            ft.DataColumn(ft.Text("Цена"), numeric=True),
            ft.DataColumn(ft.Text("Опубликован")),
            ft.DataColumn(ft.Text("Сайт")),
            ft.DataColumn(ft.Text("")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Депутатская 84")),
                    ft.DataCell(ft.Text("9")),
                    ft.DataCell(ft.Text("43")),
                    ft.DataCell(ft.Text("2")),
                    ft.DataCell(ft.Text("4 300 000")),
                    ft.DataCell(ft.Text("12.12.2024")),
                    ft.DataCell(ft.Text(value="Авито")),
                    ft.DataCell(ft.IconButton(icon='COMMENT', tooltip='Комментарии', on_click=show_bs)),
                ],
            ),
        ]
    )
    page.overlay.append(bs)
    page.add(
        ft.Row([
            logo_text,
            parser_button,
            analys_button,
        ],
            alignment=ft.MainAxisAlignment.START,
        ),
        ft.Row([
            home_button, home_arenda_button, home_city_button
        ],
        ),
        ft.Row([
            filter_button,
        ],
        ),
        ft.Row([
            table,
        ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(target=main, view=ft.WEB_BROWSER)
