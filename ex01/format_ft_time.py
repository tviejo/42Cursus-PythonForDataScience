import time

current_time = time.time()
formated_time = f"{current_time:,.4f}"
Scientific_time = f"{current_time:.2e}"
print("Seconds since January 1, 1970:", formated_time, "or", Scientific_time, "in scientific notation")