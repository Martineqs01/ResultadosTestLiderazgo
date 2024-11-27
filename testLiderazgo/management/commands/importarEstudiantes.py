from django.db import transaction
import openpyxl, pandas as pd
from django.core.management.base import BaseCommand
from testLiderazgo.models import Estudiante  # Ajusta con tu modelo real

class Command(BaseCommand):
    help = 'Importar estudiantes desde un archivo Excel'

    def add_arguments(self, parser):
        parser.add_argument('excel_file', type=str, help='Ruta al archivo Excel')

    def handle(self, *args, **kwargs):  # Este método ahora está correctamente definido dentro de la clase
        archivo = kwargs['excel_file']  # Ajusta la clave del argumento
        try:
            # Leer datos desde el archivo Excel
            df = pd.read_excel(archivo)
            estudiantes = []

            # Iterar sobre el DataFrame y crear objetos Estudiante
            for _, row in df.iterrows():
                estudiante = Estudiante(
                    nombre=row['nombre'],
                    sexo=row['sexo'],
                    localidad=row['localidad'],
                    correo_electronico=row['correo_electronico'],
                    prepa_procedencia=row['prepa_procedencia'],
                    institucion_educativa=row['institucion_educativa'],
                    programa_educativo=row['programa_educativo'],
                    semestre=row['semestre'],
                    liderazgo_kurt_lewin=row['liderazgo_kurt_lewin'],
                    liderazgo_daniel_goleman=row['liderazgo_daniel_goleman']
                )
                estudiantes.append(estudiante)

            # Insertar estudiantes en lotes
            batch_size = 130  # Puedes ajustar el tamaño del lote según sea necesario
            for i in range(0, len(estudiantes), batch_size):
                Estudiante.objects.bulk_create(estudiantes[i:i + batch_size])

            self.stdout.write(self.style.SUCCESS("Estudiantes importados exitosamente."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Ocurrió un error: {str(e)}"))
