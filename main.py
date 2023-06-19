
import yfinance as yf

print("You can write somthing from here \n ADS.DE BMW.DE CBK.DE SAP.DE ALV.DE \n SAP.DE ALV.DE BAS.DE BAYN.DE BEI.DE \n CON.DE FRE.DE DBK.DE DB1.DE LHA.DE DPW.DE \n DTE.DE EOAN.DE HEI.DE HEN3.DE IFX.DE LIN.DE MRK.DE MUV2.DE \n PSM.DE RWE.DE SIE.DE TKA.DE VOW3.DE VNA.DE MBG.DE")
print("Please, choose at least 2 stocks and write them with the space")
st = list(map(str, input().split()))
# stocks = ['ADS.DE', 'BMW.DE', 'CBK.DE', 'SAP.DE', 'ALV.DE']
# # , 'SAP.DE', 'ALV.DE', 'BAS.DE', 'BAYN.DE', 'BEI.DE', 'CON.DE',
# #       'FRE.DE', 'DBK.DE', 'DB1.DE', 'LHA.DE', 'DPW.DE', 'DTE.DE', 'EOAN.DE', 'HEI.DE', 'HEN3.DE',
# #     'IFX.DE', 'LIN.DE', 'MRK.DE', 'MUV2.DE', 'PSM.DE', 'RWE.DE', 'SIE.DE', 'TKA.DE', 'VOW3.DE', 'VNA.DE', 'MBG.DE']
stocks = st
stocks.sort()

market_data = yf.download(stocks, '2018-01-01', '2022-01-01')
market_data = market_data['Adj Close']
market_data_corr = market_data.pct_change().corr()

print("Correlations matrix of your chosen stocks")
print(market_data_corr)

data_ = []
for i in range(len(market_data_corr.columns)):
    j = 0
    while j < i:
        data_.append(market_data_corr.iloc[i][j])
        j += 1
