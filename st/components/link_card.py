import reflex as rx


def link_card() -> rx.Component:
    return rx.card(
        # rx.box(

        #     # border='1px solid #ffff',
        #     border_radius='50em',
        #     width='auto',
        #     height='100%',
        #     #bg='#5FB4EE',

        # ),
        rx.icon(
            tag='puzzle',
            size=100,
            padding='1em',
            color='#ffff'
        ),
        rx.heading('PREESCOLAR', color='#ffff'),
        border_radius='50em'
    )
