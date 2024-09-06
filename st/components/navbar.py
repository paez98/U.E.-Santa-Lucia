import reflex as rx


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium",), href=url,
         text_decoration = None,
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.image(
                src="favicon.ico",
                width="2.25em",
                height="auto",
                border_radius="25%",
            ),
            rx.heading(
                "U.E Santa Lucia", size="7", weight="bold"
            ),
            rx.spacer(),
            rx.button(
                rx.link('Inicio', size='4', weight='medium'),
                size='3',
                variant='ghost'
            ),
            rx.menu.root(
                rx.menu.trigger(
                    rx.button(
                        rx.text('Colegio', size="4", weight='medium'),
                        rx.icon('chevron-down'),
                        variant='ghost',
                        weight='medium',
                        size='3'
                    )
                ),
                rx.menu.content(
                    rx.menu.item(
                        rx.text('Quienes somos', weight='medium')),
                    rx.menu.item(rx.text('Misión', weight='medium')),
                    rx.menu.item(rx.text('Visión', weight='medium'))
                )
            ),
            rx.menu.root(
                rx.menu.trigger(
                    rx.button(
                        rx.text(
                            "Servicios",
                            size="4",
                            weight="medium",
                        ),
                        rx.icon("chevron-down"),
                        weight="medium",
                        variant="ghost",
                        size="3",
                    ),
                ),
                rx.menu.content(
                    rx.menu.item(
                        rx.text('Preescolar', weight='medium')),
                    rx.menu.item(rx.text('Primaria', weight='medium')),
                    rx.menu.item(
                        rx.text('Media-general', weight='medium')),
                ),
            ),

            navbar_link("Contact", "/#"),
            rx.color_mode.button(),
            spacing="5",
            margin='5px',
            align='center'
        ),
        justify="between",
        align_items="center",
        padding='1em',
        backdrop_filter='blur(5px)',
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        backdrop_blur="blur(1.5rem)",
        position="sticky",
        top="0",
        z_index="50",
    )
