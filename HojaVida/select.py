class Informacion_Per ():
    def documento ():

        select_documento = [('Cedula Ciudadania' , 'Cedula Ciudadania'),
                            ('Cedula Extranjera' , 'Cedula Extranjera'),
                            ('Pasaporte' , 'Pasaporte'),
                            ('Tarjeta Identidad' , 'Tarjeta Identidad')
                            ]

        return select_documento

    def genero ():

        select_genero = [('Masculino' , 'Masculino'),
                        ('Femenino' ,'Femenino'),
                        ('Otro' , 'Otro')
                        ]

        return select_genero

    def estado_civil ():

        select_civil = [('Casado' , 'Casado'),
                        ('Union libre' , 'Union libre'),
                        ('Soltero' , 'Soltero')
                        ]

        return select_civil
