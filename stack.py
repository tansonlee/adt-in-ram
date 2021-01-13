from ram import ram, ram_fetch, ram_store

# stack -> stack
# stack_push(stack, value) -> stack
# stack_pop(stack) -> stack
# stack_peek(stack) -> value
# stack_is_empty(stack) -> boolean

# [0]: address of the next availible spot
# [10]: start of the stack

stack = ram_store(ram, 0, 10)

def stack_is_empty(stack):
	next_availible = ram_fetch(stack, 0)
	return next_availible == 10

def stack_push(stack, value):
	next_availible = ram_fetch(stack, 0)
	store_val = ram_store(stack, next_availible, value)
	increment_availible = ram_store(store_val, 0, next_availible + 1)
	return increment_availible

def stack_pop(stack):
	next_availible = ram_fetch(stack, 0)
	decrement_availible = ram_store(stack, 0, next_availible - 1)
	return decrement_availible

def stack_peek(stack):
	next_availible = ram_fetch(stack, 0)
	return ram_fetch(stack, next_availible - 1)
