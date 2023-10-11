from kafka import KafkaConsumer
import logging
logging.basicConfig(level=logging.DEBUG)


# Setup
topic_name = 'retail_transactions'
msk_brokers = 'b-1.monstercluster1.6xql65.c3.kafka.eu-west-2.amazonaws.com:9092'  # Comma separated list of MSK brokers

consumer = KafkaConsumer(topic_name,
                         bootstrap_servers=msk_brokers,
                         auto_offset_reset='earliest',  # Start reading from the beginning of the topic
                         group_id='my-group')           # Consumer group ID for offset management

# Poll for messages
for message in consumer:
    print(f"Received message {message.value} from topic {message.topic}")