from tracemalloc import start, stop, get_traced_memory
import cProfile, pstats, io

def memory(func):
    """A Decorator that measures memory usage"""
    def wrapper(*args, **kwargs):
        start()
        result = func(*args, **kwargs)      # actual func gets executed (read_data())
        print(f"Memory usage: {get_traced_memory()}")
        stop()
        return result
    return wrapper

def profiling(func):
    """A decorator that uses cProfile to profile a function"""
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = func(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval
    return wrapper

def make_list(some_record):
    row = some_record.split()
    data = [ float(item) for item in row ]
    return data

def make_tuple(some_record):
    row = some_record.split()
    temp = [ float(item) for item in row ]
    data = tuple(temp)
    return data

def make_dict(some_record):
    parts = some_record.split()
    return {"x": float(parts[0]), "y": float(parts[1]), "z": float(parts[2])}

class Point:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

def make_point_instance(some_record):
    parts = some_record.split()
    p = Point(parts[0], parts[1], parts[2])
    return p

# line = "-1.5796459414274868 1.4362045785284654 -0.7896035854418733"
def read_data():
    records = [ ]
    with open("../data_files/points.txt") as f:
        for line in f:
            records.append(make_point_instance(line))
    return records
        
@profiling
def minimum():
    """Returns a tuple of minimum of 'x', 'y' and 'z' coordinates"""
    data = read_data()
    x_min = min([ item.x for item in data ])
    y_min = min([ item.y for item in data ])
    z_min = min([ item.z for item in data ])
    return (x_min, y_min, z_min)

def maximum():
    """Returns a tuple of maximum of 'x', 'y' and 'z' coordinates"""
    data = read_data()
    x_max = max([ item['x'] for item in data ])
    y_max = max([ item['y'] for item in data ])
    z_max = max([ item['z'] for item in data ])
    return (x_max, y_max, z_max)

def average():
    """Returns a tuple of average of 'x', 'y' and 'z' coordinates"""
    data = read_data()
    x_sum = sum([ item['x'] for item in data ])
    y_sum = sum([ item['y'] for item in data ])
    z_sum = sum([ item['z'] for item in data ])
    return (x_sum/len(data), y_sum/len(data), z_sum/len(data))