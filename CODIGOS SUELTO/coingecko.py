from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

precios = cg.get_price(ids='bitcoin,litecoin,ethereum', vs_currencies='usd')
monedas = cg.get_coins_list()
trending = cg.get_search_trending()

for moneda in monedas:
    print('id: ', moneda['id'])
    print('name: ', moneda['name'])
    print('symbol: ', moneda['symbol'])
    print('--------------------------------------------------')

print(trending)

