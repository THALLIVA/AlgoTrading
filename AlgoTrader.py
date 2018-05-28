from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

ts = TimeSeries(key='MYQVQFDERJGBAOM5', output_format='pandas')
data, meta_data = ts.get_batch_stock_quotes(symbols='MSFT,FB,AAPL')

plt.plot()
plt.title('Intraday Times Series for the MSFT stock (1 min)')
plt.show()

