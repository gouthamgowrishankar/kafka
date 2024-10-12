from kafka import KafkaConsumer
import json

# Configure the Kafka consumer
consumer = KafkaConsumer(
    'your_topic_name',  # Replace with your topic name
    bootstrap_servers='localhost:9092',  # Replace with your Kafka broker address
    auto_offset_reset='earliest',  # Start reading from the earliest message
    enable_auto_commit=True,  # Automatically commit offsets
    group_id='your_group_id',  # Consumer group ID
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Deserialize JSON messages
)

try:
    print("Consuming messages from Kafka topic...")
    for message in consumer:
        print(f"Received message: {message.value}")
except KeyboardInterrupt:
    print("Consumer interrupted")
finally:
    # Close the consumer
    consumer.close()
