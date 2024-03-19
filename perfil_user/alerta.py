import sweetify

class alertas:
    def save (request , Titulo:str):
        sweetify.success (request, Titulo , text='La informacion ha sido guardada', persistent='True')
