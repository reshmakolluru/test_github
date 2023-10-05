import faust
from faust.types import TP, Message
import pandas as pd
import config
from process_mix_events import Process_CSVA_EVENTS as p
tp_instances = []

app = faust.App(config.CONSUMER_GRP,broker='kafka://kafka:9092',consumer_auto_offset_reset="earliest")
partition=0
offset = 0

topic = app.topic("test1")


@app.agent(topic)
async def receive(stream):
    async for event in stream.take(10000, within=10):
        df = pd.DataFrame(event)
        print(df['appid'])
        await p().process_kafka_events(df)
        print(event)