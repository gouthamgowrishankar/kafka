import pika
#declaring the credentials needed for connection like host, port, username, password, exchange etc
def publish(data):
    credentials = pika.PlainCredentials('user','password')
    connection= pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials= credentials))
    with connection.channel() as channel:

    #channel= connection.channel()
        print("code running")
        channel.exchange_declare('goutham', durable=True, exchange_type='topic')
        channel.queue_declare(queue= 'gouthamRabbit')
        channel.queue_bind(exchange='goutham', queue='gouthamRabbit', routing_key='gouthamRabbit')
    #messaging to queue named C
        message= data
        channel.basic_publish(exchange='goutham', routing_key='gouthamRabbit', body= message)
    #channel.close()