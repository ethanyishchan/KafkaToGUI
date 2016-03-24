from pykafka import KafkaClient
import json
import requests
import time


print "1"
client = KafkaClient("127.0.0.1:9092")
print "2"

# def consume():
#     conflict_topic = client.topics['status']
#     consumer = conflict_topic.get_simple_consumer()
#     for message in consumer:
#         if message is not None:
#             print message.offset, message.value

def postPosition(url, pos):
	r = requests.post(url, verify=False,data= pos)

topic_name = "status"
topic = client.topics[topic_name]
consumer = topic.get_simple_consumer()
for msg in consumer:
	if msg is not None:
		# time.sleep(1)
		json_string = msg.value
		json_status = json.loads(json_string)
		position = json_status['flightId'] + "~" + json_status['lat'] + "~" +  json_status['lon']	 + "~" + json_status['heading']
		print "posting: ", position
		postPosition("http://127.0.0.1:5000/conflict", position)
