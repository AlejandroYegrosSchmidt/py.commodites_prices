from BCR_commodities import BCR_commodities_prices

if __name__ == '__main__':
    bcr = BCR_commodities_prices()
    df = bcr.tabla_datos()
    