##Giới thiệu Kafka
Apache Kafka là một nền tảng phát triển trực tuyến phân tán.Nó rất hữu ích để xây dựng các đường ống dữ liệu truyền phát thời gian thực để lấy dữ liệu giữa các hệ thống hoặc ứng dụng, Một tính năng hữu ích khác là các úng dụng phát trực tuyến thời gian thực có thể chuyển đổi luồng dữ liệu hoặc phản úng trên luồng dữ liệu. Hướng dẫn này sẽ giúp bạn cài đặt Apache Kafka trên Ubuntu Server

### Bước 1 : Thiết lập cài đặt môi trường

```
sudo apt update
sudo apt install default-jdk
```

### Bước 2: Download Apache Kafka

```
wget http://www-us.apache.org/dist/kafka/2.2.1/kafka_2.12-2.2.1.tgz
tar xzf kafka_2.12-2.2.1.tgz
mv kafka_2.12-2.2.1 /usr/local/kafka
```
### Bước 3: Khởi động Kafka Server
Kafka sử dụng Zookeeper , vì vậy trước tiên hãy khởi động Zookeeper trên hệ thống của bạn . Bạn có thể sử dụng tập lệnh có sẵn với Kafka để bắt đầu phiên bản Zookeeper

```
cd /usr/local/kafka
bin/zookeeper-server-start.sh config/zookeeper.properties

```
Giờ bạn hãy bắt đầu khởi động Kafka Server:
```
bin/kafka-server-start.sh config/server.properties

[2018-03-13 10:47:45,989] INFO Kafka version : 1.0.1 (org.apache.kafka.common.utils.AppInfoParser)
[2018-03-13 10:47:45,995] INFO Kafka commitId : c0518aa65f25317e (org.apache.kafka.common.utils.AppInfoParser)
[2018-03-13 10:47:46,006] INFO [KafkaServer id=0] started (kafka.server.KafkaServer)
```
### Bước 4 : Tạo topic trong Kafka

```
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic testTopic


Created topic "testTopic".
```
Kiểm tra các topic đã được tạo 

```
bin/kafka-topics.sh --list --zookeeper localhost:2181

testTopic
```
### Bước 5  : Gửi tin nhắn tới Kafka
the "producer" là một quá trình chịu trách nhiệm đưa dữ liệu vào kafka. Kafka đi kèm với dòng lệnh máy khách sẽ lấy đầu vào tiêu chuẩn và gửi nó dưới dạng tin nhắn đến cụm kafka. Mặc định kafka gửi mỗi dòng là một tin nhắn riêng  
Tiếp tục the Producer nhập một vài tin nhắn vào console để gửi đến server
```
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic testTopic

>Welcome to kafka
>This is my first topic
>
```
Bạn có thể thoát lệnh hoặc giữ terminal chạy để kiểm tra thêm.
Bây giờ hãy mở một terminal cho tiến trình Kafka của consumer ở bước tiếp theo

### Bước 6: Sử dụng Kafka Consumer
Kafka cũng có dòng lệnh cho consumer để đọc dữ liệu từ cụm Kafka và hiển thị thông báo đến đầu ra tiêu chuẩn  

```
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic testTopic --from-beginning

Welcome to kafka
This is my first topic
```