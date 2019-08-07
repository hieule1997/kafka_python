import json
from time import sleep

from kafka import KafkaConsumer

if __name__ == '__main__':
    parsed_topic_name = 'parsed_recipes'
    # Notify if a recipe has more than 200 calories
    calories_threshold = 200

    consumer = KafkaConsumer(parsed_topic_name, auto_offset_reset='earliest',
                             bootstrap_servers=['192.168.30.94:9092'], api_version=(0,10,2,0), consumer_timeout_ms=1000)
    for msg in consumer:
        record = json.loads(msg.value)
        calories = int(record['calories'])
        title = record['title']

        if calories > calories_threshold:
            print('Alert: {} calories count is {}'.format(title, calories))
        sleep(3)

    if consumer is not None:
        consumer.close()