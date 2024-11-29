from BCR_commodities import BCR_commodities_prices

if __name__ == '__main__':
    def run():
        bcr =  BCR_commodities_prices()
        precios = bcr.tabla_datos()
        return precios
    datos = run()

