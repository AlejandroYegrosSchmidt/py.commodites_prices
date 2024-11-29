from BCR_commodities import BCR_commodities_prices

if __name__ == '__main__':
    def run():
        bcr = BCR_commodities_prices()
        df = bcr.tabla_datos()
        print(df)
        return df
    run()

