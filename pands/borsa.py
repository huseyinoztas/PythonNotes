import yfinance as yf
import pandas as pd


# VAKBN
# AKBNK
# ADESE
# ENKAI

adese = yf.Ticker('ADESE.IS')

hist_df = adese.history(period="max")


df = pd.DataFrame()


df['ds_tz'] = hist_df.index
df['ds'] = df['ds_tz'].dt.tz_localize(None) 
df.drop(columns=['ds_tz'],inplace=True) 
df['y'] = hist_df['Close'].values

print(df.tail(10))##istenilen veri adedi

