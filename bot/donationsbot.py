import bitso

#Flow for transfer api
try:
    import config
except ImportError as error:
    print "No se encontro tus claves bancarias y de BITSO, Favor de crear un archivo config.py conteniendo estas"

#get the balances
foundation_balance = api.balances()

#print foundation_balance.mxn.available
#print foundation_balance.btc.available

if foundation_balance.mxn.available > 100:
 print api.spei_withdrawal(amount=foundation_balance.mxn.available, first_names=FIRST_NAMES, last_names=LAST_NAMES, clabe=CLABE, notes_ref=NOTES_REF, numeric_ref=NUMERIC_REF)

#moving to btc automatic sell wallet address
#print api.btc_withdrawal(str(foundation_balance.btc.available), WALLET_AUTOMATIC_SELL)
