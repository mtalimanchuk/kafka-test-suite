Send message from `payload.json` file:

```python kafkasuite.py produce -b 127.0.0.1:9092 -t topic_name -f payload.json```

Read messages continuously:

```python kafkasuite.py consume -b 127.0.0.1:9092 -t topic_name```
