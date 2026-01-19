import numbers, math

def get_avg(data):
    if not data:
        return 0
    if all(isinstance(x, numbers.Number) for x in data):
        return sum(data) / len(data)
    raise ValueError("All elements must be numbers to calculate average.")

def get_sd(data):
    if not data:
        return 0
    if all(isinstance(x, numbers.Number) for x in data):
        avg = get_avg(data)
        variance = sum((x - avg) ** 2 for x in data) / len(data)
        return variance ** 0.5
    raise ValueError("All elements must be numbers to calculate standard deviation.")    

def get_log_avg(data):
    if not data:
        return 0
    if all(isinstance(x, numbers.Number) and x > 0 for x in data):
        log_data = [math.log(x) for x in data]
        return sum(log_data) / len(data)
    raise ValueError("All elements must be positive numbers to calculate log average.")

def get_log_sd(data):
    if not data:
        return 0
    if all(isinstance(x, numbers.Number) and x > 0 for x in data):
        log_data = [math.log(x) for x in data]
        log_avg = sum(log_data) / len(log_data)
        variance = sum((x - log_avg) ** 2 for x in log_data) / len(log_data)
        return variance ** 0.5
    raise ValueError("All elements must be positive numbers to calculate log standard deviation.")
    