import urllib
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
"""
Programa para extraer el precio de los commodities de la Bolsa de comercio de Rosario
"""

class datatree():
    def __init__(self,endpoint=None):
        self.endpoint = endpoint
        self.url = f'https://www.bcr.com.ar/es/mercados/mercado-de-granos/cotizaciones/cotizaciones-internacionales/chicagokansas-cme-group-{self.endpoint}'
    def bs4_soup(self):
        thepage = urllib.request.urlopen(self.url)
        soup = BeautifulSoup(thepage,"html.parser")
        fecha_cierre=soup.find(class_="c1",colspan="5")
        fecha_cierre = fecha_cierre.get_text()
        return soup, fecha_cierre
    def select_tabla(self):
        #### manejo de errores###
        # En ocasiones la pagina cambia el nombre de la tabla a ser extraída,
        # por lo que es necesario menejar el error agregando las excepciones, es decir los nombres de las tablas
        soup, fecha_cierre = self.bs4_soup()
        opcion = ['sheet','sheet--12','sheet--2','sheet--3']
        for i in opcion:
            try:
                tabla = soup.find(id=i, class_="table")
                td = tabla.find_all("td")
                tr = tabla.find_all("tr")
            except:
                pass
        return td, tr,fecha_cierre
    def commodities_prices(self):
        td, tr,fecha_cierre = self.select_tabla()
        cantidad_tr_fila = len(tr)- 5  # cantidad de tr/filas en la tabla, se resta 3 tr que corresponden al encabezado de la tablas y 2 tr que corresponden al pie de la tabla
        cantidad_td =len(td)
        campofecha_X = 11  # La fecha inicia en el td 11
        campofecha_Y = len(td) - campofecha_X - 1

        ## ubicamos las columas de cada precio de los commodities
        Trigo_Chicago_1_X= campofecha_X+1
        Trigo_Chicago_1_Y= campofecha_Y-1

        Trigo_Chicago_2_X= campofecha_X+3
        Trigo_Chicago_2_Y= campofecha_Y-3

        Maiz_Chicago_3_X= campofecha_X+5
        Maiz_Chicago_3_Y= campofecha_Y-5

        Soja_Chicago_4_X= campofecha_X+7
        Soja_Chicago_4_Y= campofecha_Y-7

        AceiteSoja_Chicago_5_X= campofecha_X+9
        AceiteSoja_Chicago_5_Y= campofecha_Y-9

        HarinaSoja_Chicago_6_X= campofecha_X+11
        HarinaSoja_Chicago_6_Y= campofecha_Y-11

        contador = 0
        datos = []
        while contador != cantidad_tr_fila:
            ## el primer bucle for extrae las fechas de los contratos
            for i in td[campofecha_X:-campofecha_Y]:
                fecha_contrato_futuro = i.text
                fecha_contrato_futuro = (str.replace(fecha_contrato_futuro, "Dic", "01/12"))
                fecha_contrato_futuro = (str.replace(fecha_contrato_futuro, "Nov", "01/11"))
                fecha_contrato_futuro = (str.replace(fecha_contrato_futuro, "Oct", "01/10"))
                fecha_contrato_futuro = (str.replace(fecha_contrato_futuro, "Sep", "01/09"))
                fecha_contrato_futuro = (str.replace(fecha_contrato_futuro, "Ago", "01/08"))
                fecha_contrato_futuro = (str.replace(fecha_contrato_futuro, "Jul", "01/07"))
                fecha_contrato_futuro = (str.replace(fecha_contrato_futuro, "Jun", "01/06"))
                fecha_contrato_futuro = (str.replace(fecha_contrato_futuro, "May", "01/05"))
                fecha_contrato_futuro = (str.replace(fecha_contrato_futuro, "Abr", "01/04"))
                fecha_contrato_futuro = (str.replace(fecha_contrato_futuro, "Mar", "01/03"))
                fecha_contrato_futuro = (str.replace(fecha_contrato_futuro, "Feb", "01/02"))
                fecha_contrato_futuro = (str.replace(fecha_contrato_futuro, "Ene", "01/01"))
                fecha_contrato_futuro = (str.replace(fecha_contrato_futuro, "-", "/"))
                fecha_contrato_futuro = fecha_contrato_futuro
                campofecha_X=campofecha_X + 13
                campofecha_Y = campofecha_Y -13

            ## a partir de estos bucles se extraen los precios de los los contratos
            for i in td[Trigo_Chicago_1_X:-Trigo_Chicago_1_Y]:
                TrigoChicago1 = i.text
                if TrigoChicago1 == "":
                    TrigoChicago1 = "0,0"
                TrigoChicago1 = float(TrigoChicago1.replace(",","."))
                Trigo_Chicago_1_X=Trigo_Chicago_1_X+13
                Trigo_Chicago_1_Y=Trigo_Chicago_1_Y-13

            for i in td[Trigo_Chicago_2_X:-Trigo_Chicago_2_Y]:
                TrigoChicago2 = i.text
                if TrigoChicago2 == "":
                    TrigoChicago2 = "0,0"
                TrigoChicago2 = float(TrigoChicago2.replace(",", "."))
                Trigo_Chicago_2_X = Trigo_Chicago_2_X + 13
                Trigo_Chicago_2_Y = Trigo_Chicago_2_Y - 13

            for i in td[Maiz_Chicago_3_X:-Maiz_Chicago_3_Y]:
                MaizChicago3 = i.text
                if MaizChicago3 == "":
                    MaizChicago3 = "0,0"
                MaizChicago3 = float(MaizChicago3.replace(",","."))
                Maiz_Chicago_3_X = Maiz_Chicago_3_X + 13
                Maiz_Chicago_3_Y = Maiz_Chicago_3_Y - 13

            for i in td[Soja_Chicago_4_X:-Soja_Chicago_4_Y]:
                SojaChicago4 = i.text
                if SojaChicago4 == "":
                    SojaChicago4 = "0,0"
                SojaChicago4 = float(SojaChicago4.replace(",", "."))
                Soja_Chicago_4_X = Soja_Chicago_4_X + 13
                Soja_Chicago_4_Y = Soja_Chicago_4_Y - 13

            for i in td[AceiteSoja_Chicago_5_X:-AceiteSoja_Chicago_5_Y]:
                AceiteSojaChicago5 = i.text
                if AceiteSojaChicago5 == "":
                    AceiteSojaChicago5 = "0,0"
                AceiteSojaChicago5 = float(AceiteSojaChicago5.replace(",", "."))
                AceiteSoja_Chicago_5_X = AceiteSoja_Chicago_5_X + 13
                AceiteSoja_Chicago_5_Y = AceiteSoja_Chicago_5_Y - 13

            for i in td[HarinaSoja_Chicago_6_X:-HarinaSoja_Chicago_6_Y]:
                HarinaSojaChicago6 = i.text
                if HarinaSojaChicago6  == "":
                    HarinaSojaChicago6  = "0,0"
                HarinaSojaChicago6  = float(HarinaSojaChicago6 .replace(",", "."))
                HarinaSoja_Chicago_6_X = HarinaSoja_Chicago_6_X + 13
                HarinaSoja_Chicago_6_Y = HarinaSoja_Chicago_6_Y - 13

            datos.append([fecha_contrato_futuro, TrigoChicago1, TrigoChicago2, MaizChicago3, SojaChicago4, AceiteSojaChicago5, HarinaSojaChicago6, fecha_cierre,self.endpoint])
            #print(fecha_contrato_futuro, "-", TrigoChicago1, "-", TrigoChicago2, "-", MaizChicago3, "-", SojaChicago4,"-",AceiteSojaChicago5,"-",HarinaSojaChicago6,"-", fecha_cierre, 'Realizado', contador)
            contador += 1
        return datos

"""
Extrar datos bajo demanda
# El endpoint son los numero finales que aparecen al final de la url
# 'https://www.bcr.com.ar/es/mercados/mercado-de-granos/cotizaciones/cotizaciones-internacionales/chicagokansas-cme-group-2953'
"""
class BCR_commodities_prices:
    def __init__(self):
        self.datafrom = int(input("Ingrese el endpoint inicial: "))
        self.datato = int(input("Ingrese el endpoint final: "))
    def tabla_datos(self):
        """
        Obtiene los datos de commodities para el rango de endpoints y los organiza en un DataFrame.
        """
        bd = {
            "fecha_contrato_futuro": [],
            "trigo_chicago_1": [],
            "trigo_chicago_2": [],
            "maiz_chicago_3": [],
            "soja_chicago_4": [],
            "aceite_soja_chicago_5": [],
            "harina_soja_chicago_6": [],
            "fecha_cierre": [],
            "endpoint": []
        }

        for i in range(self.datafrom, self.datato):
            try:
                datos = datatree(endpoint=i).commodities_prices()
                # Validar que los datos tengan la longitud esperada
                for _ in datos:
                    if datos and len(datos[0]) >= 9:
                        bd["fecha_contrato_futuro"].append(datos[0][0])
                        bd["trigo_chicago_1"].append(datos[0][1])
                        bd["trigo_chicago_2"].append(datos[0][2])
                        bd["maiz_chicago_3"].append(datos[0][3])
                        bd["soja_chicago_4"].append(datos[0][4])
                        bd["aceite_soja_chicago_5"].append(datos[0][5])
                        bd["harina_soja_chicago_6"].append(datos[0][6])
                        bd["fecha_cierre"].append(datos[0][7])
                        bd["endpoint"].append(datos[0][8])
                    else:
                        print(f"Datos incompletos o vacíos para el endpoint {i}")
            except Exception as e:
                print(f"Error procesando el endpoint {i}: {e}")

        df = pd.DataFrame(bd)
        return df
    
