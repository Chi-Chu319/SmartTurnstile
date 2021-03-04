import _thread




def increment(int1, times):
	for i in range(times):
		int1 += 1
	return int1



print(_thread.start_new_thread( increment, (0, 2) ))
print(_thread.start_new_thread( increment, (0, 20) ))


