from kafka import KafkaProducer
import json
import time

# Configure the Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Replace with your Kafka broker address
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize messages to JSON
)

# Define the topic name
topic = 'your_topic_name'  # Replace with your topic name

try:
    # Example message
    message = {
        'key': 'gowri',
        'timestamp': time.time()
    }

    # Publish the message
    producer.send(topic, value=message)
    print(f"Message sent: {message}")

    # Wait for all messages to be sent
    producer.flush()
except Exception as e:
    print(f"Error sending message: {e}")
finally:
    # Close the producer
    producer.close()
