from confluent_kafka import Consumer, KafkaError
import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd

# Kafka configuration
conf = {
    'bootstrap.servers': 'b-1.monstercluster1.6xql65.c3.kafka.eu-west-2.amazonaws.com:9092',
    'group.id': 'your_group_id',
    'auto.offset.reset': 'earliest',
}

consumer = Consumer(conf)
consumer.subscribe(['monster-damage'])

# Dash App
app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Interval(
            id='interval-component',
            interval=1*1000,  # in milliseconds
            n_intervals=0
    ),
    dash_table.DataTable(
        id='live-update-table',
        columns=[{"name": "Messages", "id": "Messages"}],
        data=[],
        page_size=10,
    )
])

@app.callback(
    Output('live-update-table', 'data'),
    [Input('interval-component', 'n_intervals')]
)
def update_table(n):
    data = []
    msg = consumer.poll(1.0)
    
    if msg and not msg.error():
        message = msg.value().decode('utf-8')
        data.append({"Messages": message})
        
    # you can append more messages if needed or process them further
    return data

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
