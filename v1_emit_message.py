"""
Brett Neely
5/16/2024

    This program sends a message to a queue on the RabbitMQ server.

"""

# add imports at the beginning of the file
import pika

msg_variable = "This message represents what is sent to the receiver and what is displayed to the send."

# create a blocking connection to the RabbitMQ server
conn = pika.BlockingConnection(pika.ConnectionParameters("LOCALHOST"))

# use the connection to create a communication channel
ch = conn.channel()

# use the channel to declare a queue
ch.queue_declare(queue="hello")

# use the channel to publish a message to the queue
ch.basic_publish(exchange="", routing_key="hello", body=msg_variable)

# print a message to the console for the user

# Original message: print(" [x] Sent 'Hello World!'")
# Message test 1: print(" [x] Sent 'New Message Test!'")
#print(" [x] Sent 'Now we are sending something else.'")
#print(" [x] Sent 'Third test message!'")
print(f" [x] Sent '{msg_variable}'")
# close the connection to the server
conn.close()
