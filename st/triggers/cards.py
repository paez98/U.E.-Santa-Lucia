import reflex as rx



class ImageState(rx.State,):
    image_src: str = "favicon.ico"
    bg = 'red'
    text = str
    
    def change_heading(self):
        self.text = str
        rx.heading('progra')
    def change_image(self):
        self.image_src = "img.jpg"
        self.bg = 'blue'

    def reset_image(self):
        self.image_src = "favicon.ico"
        self.bg = 'red'

def carta():
    return rx.card(
        rx.heading('Progra'),
        rx.image(src=ImageState.image_src, width ='20em'),
        bg = ImageState.bg,
        on_mouse_over=ImageState.change_heading,
        
        
        on_mouse_leave=ImageState.reset_image,
    )