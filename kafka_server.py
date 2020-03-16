import producer_server


def run_kafka_server():
	# (done)TODO get the json file path
    input_file = "./police-department-calls-for-service.json"

    # (done)TODO fill in blanks
    producer = producer_server.ProducerServer(
        input_file=input_file,
        topic="org.sfpd.calls-for-service",
        bootstrap_servers="localhost:9092",
        client_id="proj_2_producer"
    )

    return producer


def feed():
    producer = run_kafka_server()
    producer.generate_data()


if __name__ == "__main__":
    feed()
