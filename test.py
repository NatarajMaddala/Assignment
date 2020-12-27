import code as x
import threading
from threading import *
path = x.create_file() # Path for creating a file run only once
path = 'data.json'
x.create('Andhra Pradesh', 'Vijayawada', path, 20)
x.read('Andhra Pradesh', path)
x.create('Telangana', 'Hyderabad', path, 20)
x.delete('Telangana', path)
t1=Thread(target=(x.delete),args=('Karnataka',path)) # This code can also access db using multiple threads
t2=Thread(target=(x.create),args=('Maharashtra','Mumbai',path))
t2.start()
t1.start()