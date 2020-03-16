import asyncio
import json

from confluent_kafka import Consumer
from confluent_kafka.admin import AdminClient

BROKER_URL = "PLAINTEXT://localhost:9092"

async def consume(topic_name):
    """Consumes data from the Kafka Topic"""
    c = Consumer({"bootstrap.servers": BROKER_URL, "group.id": "0"})
    c.subscribe([topic_name])

    while True:
        messages = c.consume(5, 1.0)
        print("consuming messages:")
        for message in messages:
            if message is None:
                print("No message received by consumer")
            elif message.error() is not None:
                print(f"Error in message: {message.error()}")
            else:
                print(f"--consumed message: {message.key()}: {message.value()}")
        print(f"consumed {len(messages)} messages")

        await asyncio.sleep(0.01)


def main():
    """Checks for topic and creates the topic if it does not exist"""
    client = AdminClient({"bootstrap.servers": BROKER_URL})

    try:
        asyncio.run(consume("org.sfpd.calls-for-service"))
    except KeyboardInterrupt as e:
        print("Shutting down consumer server")

if __name__ == "__main__":
    main()