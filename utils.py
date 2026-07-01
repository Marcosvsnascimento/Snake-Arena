def clicked(button, mouse):
    mx, my = mouse.get_position()

    return (
        button.x <= mx <= button.x + button.width and button.y <= my <= button.y + button.height
    )