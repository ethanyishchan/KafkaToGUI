# from kafka import KafkaClient, KafkaConsumer
from pykafka import KafkaClient

client = KafkaClient("127.0.0.1:9092")
# consumer = KafkaConsumer('my-topic',
#                          group_id='my-group',
#                          bootstrap_servers=['localhost:9092'])

topic = client.topics['conflict']

with topic.get_sync_producer() as producer:
	for i in range(4):
		producer.produce("\{"flightId":"drone0","lat":"338.666","lon":"282.039","speed":"1.232","heading":"0.639"\}")
