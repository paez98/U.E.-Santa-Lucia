import reflex as rx


def footer() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.separator(size='4', color_scheme='indigo', margin_top = '1em'),
            rx.avatar(src='favicon.ico'),
            rx.heading(
                '''Colegio \nSanta Lucia''',
                white_space='pre-wrap',
                align='center',
                weight='bold',
                size='6'
            ),

            rx.flex(
                rx.box(
                    rx.flex(
                        rx.heading('Sobre nosotros'),
                        rx.button(
                            rx.link('Quienes somos'),
                            variant='ghost',
                            size='3',
                            align = 'left',
                            justify = 'left'
                        ),
                        rx.link('Mision', href='#'),
                        rx.link('Vision', href='#'),
                        direction='column',
                        # align='center'
                    ),

                ),
                rx.separator(orientation='vertical',
                             size='4', color_scheme='blue'),
                rx.box(
                    rx.flex(
                        rx.heading('Servicios'),
                        rx.link('Preescolar'),
                        rx.link('Primaria'),
                        rx.link('Media-general'),
                        direction='column',
                        # align='center'
                    )
                ),
                rx.divider(size='4', orientation='vertical'),
                rx.box(rx.heading('Actividades extras')),
                rx.separator(orientation='vertical'),

                rx.box(
                    rx.heading('Contacto')
                ),
                spacing='4'
            ),
            rx.box(
                rx.text(
                    '''Urb. Parque Valencia, Valencia Carabobo, Valencia, Carabobo 2001''',
                    white_space='pre-wrap',
                    weight='bold',
                    size='3'
                )
            ),
            align='center',
            justify='center',
            heigth = '100%'
        ),
        width='100%',
        margin_bottom='1em',
        heigth = '100%'

    )
