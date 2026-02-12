import flet as ft

def main(page: ft.Page):
    page.title = "اپلیکیشن من"
    page.rtl = True
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(ft.Icons.PHONE_ANDROID, size=80, color=ft.Colors.BLUE),
                ft.Text("سلام دنیا! 🎉", size=30, weight=ft.FontWeight.BOLD),
                ft.Text("اولین اپلیکیشن اندرویدی من با Flet", size=16),
                ft.ElevatedButton(
                    text="کلیک کن!",
                    on_click=lambda e: page.open(
                        ft.SnackBar(content=ft.Text("آفرین! کار کرد! 🚀"))
                    ),
                ),
            ],
        )
    )

ft.app(target=main)
