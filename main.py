import flet as ft


def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Video(playlist=[""])))


ft.app(main)
