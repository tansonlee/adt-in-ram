from ram import ram, ram_store, ram_fetch, core_dump

# make_array(size)
# array_store(array, index, value)
# array_fetch(array, index)
# array_length(array)
# build_array(size, procedure)
# array_map(array, procedure)


# store pointer to array at address 0 ([0]===2)
# store length of array at address 1
# start array at address 2

def make_array(size):
	return ram_store(ram_store(ram, 0, 2), 1, size)

def array_store(array, index, value):
	size = ram_fetch(array, 1)
	if index >= size:
		return array
	elif index < 0:
		return array
	else:
		address = index + 2
		return ram_store(array, address, value)

def array_fetch(array, index):
	size = ram_fetch(array, 1)
	if index >= size:
		return None
	elif index < 0:
		return None
	else:
		address = index + 2
		return ram_fetch(array, address)

def build_array(size, procedure):
	my_array = make_array(size)
	for i in range(size):
		value = procedure(i)
		my_array = array_store(my_array, i, value)
	return my_array

def array_map(array, procedure):
	size = ram_fetch(array, 1)
	my_array = make_array(size)
	for i in range(size):
		stored_value = array_fetch(array, i)
		new_value = procedure(stored_value)
		my_array = array_store(my_array, i, new_value)
	return my_array

def array_length(array):
	return ram_fetch(array, 1)
