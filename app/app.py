import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.graph_objs as go
from .generate_data import generate_ohlcv_data

# Generate or load data
df = generate_ohlcv_data('2024-01-01', '2024-01-10')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Candlestick Chart Visualization"),
    dcc.DatePickerRange(
        id='date-range',
        min_date_allowed=df['datetime'].min().date(),
        max_date_allowed=df['datetime'].max().date(),
        start_date=df['datetime'].min().date(),
        end_date=df['datetime'].max().date(),
    ),
    dcc.Graph(id='candlestick-chart'),
])

@app.callback(
    Output('candlestick-chart', 'figure'),
    Input('date-range', 'start_date'),
    Input('date-range', 'end_date')
)
def update_chart(start_date, end_date):
    filtered = df[(df['datetime'] >= pd.to_datetime(start_date)) & (df['datetime'] <= pd.to_datetime(end_date))]
    fig = go.Figure(data=[go.Candlestick(
        x=filtered['datetime'],
        open=filtered['open'],
        high=filtered['high'],
        low=filtered['low'],
        close=filtered['close'],
        increasing_line_color='green', decreasing_line_color='red',
        name='OHLC'
    )])
    fig.update_layout(xaxis_rangeslider_visible=False, title='Candlestick Chart')
    return fig

if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=8080)
