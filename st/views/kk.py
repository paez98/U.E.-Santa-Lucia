import reflex as rx

def create_icon(
    alt_text, icon_height, icon_tag, icon_width
):
    """Creates an icon with specified attributes."""
    return rx.icon(
        alt=alt_text,
        tag=icon_tag,
        height=icon_height,
        width=icon_width,
    )


def create_nav_link(link_url, link_text):
    """Creates a styled navigation link."""
    return rx.el.a(
        link_text,
        href=link_url,
        transition_duration="300ms",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        font_weight="500",
        _hover={"color": "#2563EB"},
        padding_left="0.75rem",
        padding_right="0.75rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.375rem",
        color="#1F2937",
        font_size="0.875rem",
        line_height="1.25rem",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
    )


def create_mobile_nav_link(link_url, link_text):
    """Creates a styled mobile navigation link."""
    return rx.el.a(
        link_text,
        href=link_url,
        display="block",
        transition_duration="300ms",
        transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
        font_weight="500",
        _hover={"color": "#2563EB"},
        padding_left="0.75rem",
        padding_right="0.75rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.375rem",
        font_size="1rem",
        line_height="1.5rem",
        color="#1F2937",
        transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
    )


def create_subheading(heading_text):
    """Creates a subheading with specific styling."""
    return rx.heading(
        heading_text,
        font_weight="600",
        margin_bottom="0.5rem",
        font_size="1.25rem",
        line_height="1.75rem",
        as_="h3",
    )


def create_section_heading(heading_text):
    """Creates a section heading with specific styling."""
    return rx.heading(
        heading_text,
        font_weight="700",
        margin_bottom="2rem",
        font_size="1.875rem",
        line_height="2.25rem",
        as_="h2",
    )


def create_paragraph(paragraph_text):
    """Creates a styled paragraph."""
    return rx.text(
        paragraph_text,
        margin_bottom="1rem",
        color="#374151",
    )


def create_colored_text(text_color, text_content):
    """Creates text with a specified color."""
    return rx.text(text_content, color=text_color)


def create_feature_icon(alt_text, icon_tag):
    """Creates a feature icon with specific styling."""
    return rx.icon(
        alt=alt_text,
        tag=icon_tag,
        height="3rem",
        margin_bottom="1rem",
        color="#2563EB",
        width="3rem",
    )


def create_feature_box(
    icon_alt_text,
    icon_tag,
    feature_title,
    feature_description,
):
    """Creates a feature box with an icon, title, and description."""
    return rx.box(
        create_feature_icon(
            alt_text=icon_alt_text, icon_tag=icon_tag
        ),
        create_subheading(heading_text=feature_title),
        create_colored_text(
            text_color="#374151",
            text_content=feature_description,
        ),
        background_color="#ffffff",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_event_box(
    event_title, event_description, event_date
):
    """Creates an event box with title, description, and date."""
    return rx.box(
        create_subheading(heading_text=event_title),
        create_paragraph(paragraph_text=event_description),
        create_colored_text(
            text_color="#2563EB", text_content=event_date
        ),
        background_color="#ffffff",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_simple_text(text_content):
    """Creates a simple text element."""
    return rx.text(text_content)


def create_hover_link(link_url, link_text):
    """Creates a link with hover effect."""
    return rx.el.a(
        link_text,
        href=link_url,
        _hover={"color": "#60A5FA"},
    )


def create_list_item_link(link_url, link_text):
    """Creates a list item containing a link."""
    return rx.el.li(
        create_hover_link(
            link_url=link_url, link_text=link_text
        )
    )


def create_social_icon_link(icon_alt_text, icon_tag):
    """Creates a social media icon link."""
    return rx.el.a(
        create_icon(
            alt_text=icon_alt_text,
            icon_height="1.5rem",
            icon_tag=icon_tag,
            icon_width="1.5rem",
        ),
        href="#",
        _hover={"color": "#60A5FA"},
    )


def create_logo():
    """Creates the school logo."""
    return rx.flex(
        rx.el.a(
            create_icon(
                alt_text="School Logo",
                icon_height="2rem",
                icon_tag="book-open",
                icon_width="2rem",
            ),
            href="#",
            transition_duration="300ms",
            transition_timing_function="cubic-bezier(0.4, 0, 0.2, 1)",
            _hover={"color": "#1E40AF"},
            color="#2563EB",
            transition_property="background-color, border-color, color, fill, stroke, opacity, box-shadow, transform",
        ),
        display="flex",
        align_items="center",
    )


def create_desktop_nav():
    """Creates the desktop navigation menu."""
    return rx.box(
        rx.flex(
            create_nav_link(link_url="#", link_text="Home"),
            create_nav_link(
                link_url="#about", link_text="About Us"
            ),
            create_nav_link(
                link_url="#services", link_text="Services"
            ),
            create_nav_link(
                link_url="#events", link_text="Events"
            ),
            display="flex",
            align_items="baseline",
            margin_left="2.5rem",
            column_gap="1rem",
        ),
        display=rx.breakpoints(
            {"0px": "none", "768px": "block"}
        ),
    )


def create_header():
    """Creates the header with logo and navigation."""
    return rx.flex(
        create_logo(),
        create_desktop_nav(),
        rx.box(
            rx.el.button(
                create_icon(
                    alt_text="Menu",
                    icon_height="1.5rem",
                    icon_tag="menu",
                    icon_width="1.5rem",
                ),
                type="button",
                _focus={
                    "outline-style": "none",
                    "box-shadow": "0 0 0 var(--ring-offset-width) var(--ring-offset-color), var(--ring-shadow)",
                    "--ring-offset-width": "2px",
                    "--ring-offset-color": "#1F2937",
                    "--ring-color": "#ffffff",
                },
                _hover={"color": "#2563EB"},
                color="#1F2937",
            ),
            display=rx.breakpoints({"768px": "none"}),
        ),
        display="flex",
        height="4rem",
        align_items="center",
        justify_content="space-between",
    )


def create_mobile_nav():
    """Creates the mobile navigation menu."""
    return rx.box(
        create_mobile_nav_link(
            link_url="#", link_text="Home"
        ),
        create_mobile_nav_link(
            link_url="#about", link_text="About Us"
        ),
        create_mobile_nav_link(
            link_url="#services", link_text="Services"
        ),
        create_mobile_nav_link(
            link_url="#events", link_text="Events"
        ),
        display="flex",
        flex_direction="column",
        padding_bottom="0.75rem",
        padding_top="0.5rem",
        padding_left=rx.breakpoints(
            {"0px": "0.5rem", "640px": "0.75rem"}
        ),
        padding_right=rx.breakpoints(
            {"0px": "0.5rem", "640px": "0.75rem"}
        ),
        gap="0.25rem",
    )


def create_nav_bar():
    """Creates the full navigation bar including mobile and desktop versions."""
    return rx.box(
        rx.box(
            create_header(),
            max_width="80rem",
            margin_left="auto",
            margin_right="auto",
            padding_left=rx.breakpoints(
                {
                    "0px": "1rem",
                    "640px": "1.5rem",
                    "1024px": "2rem",
                }
            ),
            padding_right=rx.breakpoints(
                {
                    "0px": "1rem",
                    "640px": "1.5rem",
                    "1024px": "2rem",
                }
            ),
        ),
        rx.box(
            create_mobile_nav(),
            display=rx.breakpoints({"768px": "none"}),
        ),
        backdrop_blur="blur(12px)",
        background_color="#ffffffcc",
        left="0",
        right="0",
        box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
        position="sticky",
        top="0",
        z_index="50",
    )


def create_hero_section():
    """Creates the hero section with main heading and tagline."""
    return rx.box(
        rx.heading(
            "Welcome to Our School",
            font_weight="700",
            margin_bottom="1rem",
            font_size="2.25rem",
            line_height="2.5rem",
            as_="h1",
        ),
        rx.text(
            "Empowering minds, shaping futures.",
            font_size="1.25rem",
            line_height="1.75rem",
        ),
        max_width="80rem",
        margin_left="auto",
        margin_right="auto",
        padding_left=rx.breakpoints(
            {
                "0px": "1rem",
                "640px": "1.5rem",
                "1024px": "2rem",
            }
        ),
        padding_right=rx.breakpoints(
            {
                "0px": "1rem",
                "640px": "1.5rem",
                "1024px": "2rem",
            }
        ),
    )


def create_about_content():
    """Creates the content for the About Us section."""
    return rx.box(
        rx.box(
            create_paragraph(
                paragraph_text="Our school is dedicated to providing a nurturing environment where students can thrive academically and personally. With a focus on innovation and character development, we prepare our students for the challenges of the future."
            ),
            create_colored_text(
                text_color="#374151",
                text_content="Founded in 1990, we have a rich history of academic excellence and community engagement.",
            ),
        ),
        rx.box(
            rx.image(
                src="https://replicate.delivery/yhqm/1gnBeWMuQZ0gMSA8ekPb8a7FmsX4m6ntrqTteCUkRefbnCLbC/out-0.webp",
                alt="A modern school building with large windows and a welcoming entrance",
                border_radius="0.5rem",
                box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
            )
        ),
        gap="2rem",
        display="grid",
        grid_template_columns=rx.breakpoints(
            {
                "0px": "repeat(1, minmax(0, 1fr))",
                "768px": "repeat(2, minmax(0, 1fr))",
            }
        ),
    )


def create_about_section():
    """Creates the full About Us section."""
    return rx.box(
        rx.box(
            create_section_heading(heading_text="About Us"),
            create_about_content(),
            max_width="80rem",
            margin_left="auto",
            margin_right="auto",
            padding_left=rx.breakpoints(
                {
                    "0px": "1rem",
                    "640px": "1.5rem",
                    "1024px": "2rem",
                }
            ),
            padding_right=rx.breakpoints(
                {
                    "0px": "1rem",
                    "640px": "1.5rem",
                    "1024px": "2rem",
                }
            ),
        ),
        id="about",
        padding_top="4rem",
        padding_bottom="4rem",
    )


def create_services_section():
    """Creates the Services section with feature boxes."""
    return rx.box(
        create_section_heading(heading_text="Our Services"),
        rx.box(
            create_feature_box(
                icon_alt_text="Academic Programs",
                icon_tag="book",
                feature_title="Academic Programs",
                feature_description="Comprehensive curriculum covering all major subjects with advanced placement options.",
            ),
            create_feature_box(
                icon_alt_text="Arts and Music",
                icon_tag="music",
                feature_title="Arts and Music",
                feature_description="Vibrant arts program including visual arts, music, and performing arts.",
            ),
            create_feature_box(
                icon_alt_text="Sports",
                icon_tag="trophy",
                feature_title="Sports",
                feature_description="Competitive sports teams and physical education programs for all students.",
            ),
            gap="2rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(3, minmax(0, 1fr))",
                }
            ),
        ),
        max_width="80rem",
        margin_left="auto",
        margin_right="auto",
        padding_left=rx.breakpoints(
            {
                "0px": "1rem",
                "640px": "1.5rem",
                "1024px": "2rem",
            }
        ),
        padding_right=rx.breakpoints(
            {
                "0px": "1rem",
                "640px": "1.5rem",
                "1024px": "2rem",
            }
        ),
    )


def create_events_section():
    """Creates the Events section with event boxes."""
    return rx.box(
        create_section_heading(
            heading_text="Upcoming Events"
        ),
        rx.box(
            create_event_box(
                event_title="Annual Science Fair",
                event_description="Join us for an exciting showcase of student projects and innovations.",
                event_date="Date: May 15, 2023",
            ),
            create_event_box(
                event_title="Parent-Teacher Conference",
                event_description="An opportunity to discuss your child's progress and goals.",
                event_date="Date: June 5-6, 2023",
            ),
            create_event_box(
                event_title="Summer Sports Camp",
                event_description="A week-long camp featuring various sports and outdoor activities.",
                event_date="Date: July 10-14, 2023",
            ),
            gap="2rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(2, minmax(0, 1fr))",
                    "1024px": "repeat(3, minmax(0, 1fr))",
                }
            ),
        ),
        max_width="80rem",
        margin_left="auto",
        margin_right="auto",
        padding_left=rx.breakpoints(
            {
                "0px": "1rem",
                "640px": "1.5rem",
                "1024px": "2rem",
            }
        ),
        padding_right=rx.breakpoints(
            {
                "0px": "1rem",
                "640px": "1.5rem",
                "1024px": "2rem",
            }
        ),
    )


def create_main_content():
    """Creates the main content of the page including hero, about, services, and events sections."""
    return rx.box(
        rx.box(
            create_hero_section(),
            background_color="#2563EB",
            padding_top="5rem",
            padding_bottom="5rem",
            color="#ffffff",
        ),
        create_about_section(),
        rx.box(
            create_services_section(),
            id="services",
            background_color="#F3F4F6",
            padding_top="4rem",
            padding_bottom="4rem",
        ),
        rx.box(
            create_events_section(),
            id="events",
            padding_top="4rem",
            padding_bottom="4rem",
        ),
        padding_top="4rem",
    )


def create_footer_content():
    """Creates the content for the footer including contact info, quick links, and social media."""
    return rx.flex(
        rx.box(
            create_subheading(heading_text="Contact Us"),
            create_simple_text(
                text_content="123 School Street, City, State 12345"
            ),
            create_simple_text(
                text_content="Phone: (123) 456-7890"
            ),
            create_simple_text(
                text_content="Email: info@ourschool.edu"
            ),
            margin_bottom=rx.breakpoints(
                {"0px": "1.5rem", "768px": "0"}
            ),
            width=rx.breakpoints(
                {"0px": "100%", "768px": "33.333333%"}
            ),
        ),
        rx.box(
            create_subheading(heading_text="Quick Links"),
            rx.list(
                create_list_item_link(
                    link_url="#", link_text="Home"
                ),
                create_list_item_link(
                    link_url="#about", link_text="About Us"
                ),
                create_list_item_link(
                    link_url="#services",
                    link_text="Services",
                ),
                create_list_item_link(
                    link_url="#events", link_text="Events"
                ),
            ),
            margin_bottom=rx.breakpoints(
                {"0px": "1.5rem", "768px": "0"}
            ),
            width=rx.breakpoints(
                {"0px": "100%", "768px": "33.333333%"}
            ),
        ),
        rx.box(
            create_subheading(heading_text="Follow Us"),
            rx.flex(
                create_social_icon_link(
                    icon_alt_text="Facebook",
                    icon_tag="facebook",
                ),
                create_social_icon_link(
                    icon_alt_text="Twitter",
                    icon_tag="twitter",
                ),
                create_social_icon_link(
                    icon_alt_text="Instagram",
                    icon_tag="instagram",
                ),
                display="flex",
                column_gap="1rem",
            ),
            width=rx.breakpoints(
                {"0px": "100%", "768px": "33.333333%"}
            ),
        ),
        display="flex",
        flex_wrap="wrap",
        justify_content="space-between",
    )


def create_footer():
    """Creates the full footer section."""
    return rx.box(
        create_footer_content(),
        rx.box(
            create_simple_text(
                text_content="© 2023 Our School. All rights reserved."
            ),
            margin_top="2rem",
            text_align="center",
        ),
        max_width="80rem",
        margin_left="auto",
        margin_right="auto",
        padding_left=rx.breakpoints(
            {
                "0px": "1rem",
                "640px": "1.5rem",
                "1024px": "2rem",
            }
        ),
        padding_right=rx.breakpoints(
            {
                "0px": "1rem",
                "640px": "1.5rem",
                "1024px": "2rem",
            }
        ),
    )


def create_school_page():
    """Creates the entire school webpage including header, main content, and footer."""
    return rx.fragment(
        rx.box(
            create_nav_bar(),
            create_main_content(),
            rx.box(
                create_footer(),
                background_color="#1F2937",
                padding_top="2rem",
                padding_bottom="2rem",
                color="#ffffff",
            ),
            background_color="#F3F4F6",
        )
    )
