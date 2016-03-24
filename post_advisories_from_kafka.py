from pykafka import KafkaClient
import json
import requests
import time
# from json import jsonify

print "1"
client = KafkaClient("127.0.0.1:9092")
print "2"

# def consume():
#     conflict_topic = client.topics['status']
#     consumer = conflict_topic.get_simple_consumer()
#     for message in consumer:
#         if message is not None:
#             print message.offset, message.value


def postAdvisories(url, pos):
	r = requests.post(url, verify=False,data= pos)

topic_name = "advisory"

gufi_1 = "drone1"
gufi_2 = "drone2"
gufi_3 = "drone3"

topic = client.topics[topic_name]
consumer = topic.get_simple_consumer()
for msg in consumer:
	if msg is not None:
		# time.sleep(1)
		json_string = msg.value
		json_status = json.loads(json_string)
		# print json_string
		json_packet_list = json_status['advisories']
		print json_packet_list
		postAdvisories("http://127.0.0.1:5000/consume_advisory", json.dumps(json_packet_list))

		# for gufi_packet in json_packet_list:
		# 	# print json_packet['gufi']
		# 	if gufi_packet['gufi'] == gufi_1:
		# 		print gufi_packet
		# 		pass
		# 	elif gufi_packet['gufi'] == gufi_2:
		# 		# print gufi_packet
		# 		pass
		# 	elif gufi_packet['gufi'] == gufi_3:
		# 		# print gufi_packet
		# 		pass
		# 	else:
		# 		pass
		# print json_packet
		# if json_packet['clearOfConflict'] == 'true':
		# 	pass
		# else:
		# 	print json_packet
		

		# position = json_status['flightId'] + "~" + json_status['lat'] + "~" +  json_status['lon']	 + "~" + json_status['heading']
		# print "posting: ", position
		# postAdvisories("http://127.0.0.1:5000/consume_advisory", position)
