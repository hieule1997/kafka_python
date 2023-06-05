1. Consumer listen topic
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first_topic
2. List groups
bin/kafka-consumer-groups.sh  --list --bootstrap-server localhost:9092
3. List topic in group
bin/kafka-consumer-groups.sh --describe --group mygroup --bootstrap-server localhost:9092
4. List all topic in groups
kafka-consumer-groups.bat --bootstrap-server localhost:9092 --describe --all-groups
