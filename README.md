# Abstract Data Types Implemented in RAM

## Table of Contents
1. [Intruduction](#introduction)
2. [Arrays](#array)
3. [Queues](#queue)
4. [Stacks](#stack)

## Introduction

An array, queue, and stack are implemented using the RAM implentation which can be found here: [RAM Implementation](https://github.com/tansonlee/ram)

## Array

This ADT that holds a predetermined number of elements which can be accessed in any order.

There are 6 operations implemented:
* `make_array(size)`: O(1), creates an empty array with the specified size
* `array_store(array, index, value)`: O(1), stores the value at the index in the array
* `array_fetch(array, index)`: O(1), fetches the value store at the index in the array
* `array_length(array)`: O(1), returns the length of the array
* `build_array(size, procedure)`: O(size) * O(procedure), creates an array with the elements procedure(i) where i = 0, 1, ..., size - 1
* `array_map(array, procedure)`: O(size) * O(procedure), returns an array where each element has been transformed by procedure


```python
from array import *

a = build_array(10, lambda x : x * x)
b = array_store(a, 2, 100)

for i in range(array_length(b)):
	print(array_fetch(b, i))
# prints 0 1 100 9 16 25 36 49 64 81

c = array_map(b, lambda x : x > 30)
for i in range(array_length(c)):
	print(array_fetch(c, i))
# prints False False True False False False True True True True

```


## Queue

This ADT is a first in first out structure which means the first element to enter the queue is the first to leave the queue.

There are 5 operations implemented, they all take O(1) time:
* `queue`: the empty queue
* `queue_is_empty(queue)`: returns True if the queue is empty False otherwise
* `enqueue(queue, value)`: returns a queue with all the elements of queue and value
* `dequeue(queue)`: returns a queue with all the elements of queue except the first element
* `queue_peak(queue)`: returns the first element of the queue

```python
from queue import *

print(queue_is_empty(queue))
# prints True

a = enqueue(enqueue(enqueue(queue, 10), 100), 1000)

print(queue_peek(a))
# prints 10

b = dequeue(a)
print(queue_peek(b))
# prints 100

c = dequeue(dequeue(b))
print(queue_is_empty(c))
# prints True
```

## Stack

This ADT is a first in last out data structure which means the first element added to the stack is the last element to leave.

There are 5 operations implemented, they all take O(1) time:
* `stack`: returns the empty stack
* `stack_is_empty(stack)`: returns True when the stack is empty, False otherwise
* `stack_push(stack, value)`: returns a stack with the elements of stack and value
* `stack_pop(stack)`: returns a stack without the last element
* `stack_peek(stack)`: returns the last element in the stack

```python
from stack import *

a = stack_push(stack_push(stack_push(stack, 10), 100), 1000)

print(stack_peek(a))
# prints 1000

b = stack_pop(a)
print(stack_peek(b))
# prints 100

c = stack_pop(b)
print(stack_peek(c))
# prints 10
```

