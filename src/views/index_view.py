#  ##   ###
#  Import LIBRARIES
import flet as ft
from flet import Column, ElevatedButton, Icons, Image, Row, Text

#  Import FILES
#  ##   ###


def IndexView(page):
    page.title = "Home Page"

    #  Image on the righthandside
    image = Image(
        src="https://images.unsplash.com/photo-1515378960530-7c0da6231fb1?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        # src="https://via.placeholder.com/150",  # Replace with your image URL
        width=300,
        height=300,
        fit=ft.ImageFit.CONTAIN,
    )

    # Text for the left handside
    text_one = Text(
        "Imagination is more important than knowledge. For knowledge is limited, whereas imagination embraces the entire world, stimulating progress, giving birth to evolution”",
        size=35,
        width=600,
        text_align="center",
    )
    text_two = Text(
        "Albert Einstein",
        size=20,
    )

    #  A clickable icon button to display ther PDF articles
    contact_button = ElevatedButton(
        icon=Icons.CONTACT_PAGE,
        text="Contacts",
        on_click=lambda e: print("Contacts"),
    )

    #  Page content rendering
    content = Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment="center",
        controls=[
            Row(
                # vertical_alignment="center",
                controls=[
                    image,
                    Column(
                        alignment="center",
                        horizontal_alignment="center",
                        spacing=15,
                        controls=[
                            text_one,
                            text_two,
                            contact_button,
                        ],
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            ),
        ],
    )

    return content
