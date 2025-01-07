from prometheus_client import start_http_server, Gauge
import requests
import time
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Environment variables
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST')
RABBITMQ_USER = os.getenv('RABBITMQ_USER')
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD')

# Define Prometheus metrics
QUEUE_MESSAGES = Gauge('rabbitmq_individual_queue_messages',
                      'Total number of messages in queue',
                      ['host', 'vhost', 'name'])
QUEUE_MESSAGES_READY = Gauge('rabbitmq_individual_queue_messages_ready',
                            'Number of messages ready in queue',
                            ['host', 'vhost', 'name'])
QUEUE_MESSAGES_UNACK = Gauge('rabbitmq_individual_queue_messages_unacknowledged',
                            'Number of unacknowledged messages in queue',
                            ['host', 'vhost', 'name'])

class RabbitMQExporter:
    def __init__(self, host, username, password):
        self.base_url = f"http://{host}:15672/api"
        self.auth = (username, password)

    def get_queue_stats(self):
        try:
            response = requests.get(f"{self.base_url}/queues",
                                  auth=self.auth,
                                  timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching queue stats: {e}")
            return []

    def update_metrics(self):
        queues = self.get_queue_stats()
        
        for queue in queues:
            labels = {
                'host': RABBITMQ_HOST,
                'vhost': queue['vhost'],
                'name': queue['name']
            }
            
            QUEUE_MESSAGES.labels(**labels).set(queue['messages'])
            QUEUE_MESSAGES_READY.labels(**labels).set(queue['messages_ready'])
            QUEUE_MESSAGES_UNACK.labels(**labels).set(queue['messages_unacknowledged'])

def main():
    if not all([RABBITMQ_HOST, RABBITMQ_USER, RABBITMQ_PASSWORD]):
        logger.error("Missing required environment variables")
        exit(1)

    exporter = RabbitMQExporter(
        RABBITMQ_HOST,
        RABBITMQ_USER,
        RABBITMQ_PASSWORD
    )

    # Start Prometheus HTTP server
    start_http_server(8000)
    logger.info("Prometheus metrics server started on port 8000")

    # Update metrics every 15 seconds
    while True:
        try:
            exporter.update_metrics()
            time.sleep(15)
        except Exception as e:
            logger.error(f"Error updating metrics: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()