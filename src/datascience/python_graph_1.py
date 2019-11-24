import plotly

plotly.tools.set_credentials_file(username='arunangsu', api_key='Kolkata@15')
import plotly.tools as tls

tls.embed('https://plot.ly/~cufflinks/8')
print(plotly.__version__)
