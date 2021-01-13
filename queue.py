from ram import ram, ram_fetch, ram_store

# queue -> queue
# enqueue(queue, value)
# dequeue(queue)
# queue_is_empty(queue)
# queue_peek(queue)

# [0]: 10 - start 
# [1]: 10 - end

queue = ram_store(ram_store(ram, 0, 10), 1, 10)

def enqueue(queue, value):
	end = ram_fetch(queue, 1)
	add_value = ram_store(queue, end, value)
	increment_end = ram_store(add_value, 1, end + 1)
	return increment_end

def dequeue(queue):
	start = ram_fetch(queue, 0)
	increment_start = ram_store(queue, 0, start + 1)
	return increment_start

def queue_is_empty(queue):
	start = ram_fetch(queue, 0)
	end = ram_fetch(queue, 1)
	return start == end

def queue_peek(queue):
	start = ram_fetch(queue, 0)
	return ram_fetch(queue, start)
