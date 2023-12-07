file = open("input/input_05.txt")

input = [line for line in file.read().strip("\n").split("\n\n")]

def create_transformation_map(input_string):
    return [{'dest_start': int(transforma.split()[0]), 'source_start': int(transforma.split()[1]), 'length': int(transforma.split()[2])} for transforma in input_string]

def range_matching(interval,transform):
    interval_begin = interval[0]
    interval_length = interval[1]
    transform_begin = transform[0]
    transform_length = transform[1]
    # transform outside interval, nothing to be done
    if (interval_begin + interval_length <= transform_begin) or (transform_begin + transform_length <= interval_begin):
        return 0
    # interval fully inside transform, nothing to be done
    elif transform_begin <= interval_begin and interval_begin + interval_length <= transform_begin + transform_length:
        return 0
    # ending side of interval outreach transform
    elif transform_begin <= interval_begin and interval_begin + interval_length > transform_begin + transform_length:
        return 1
    # starting side of interval outreach transform
    elif transform_begin > interval_begin and interval_begin + interval_length <= transform_begin + transform_length:
        return 2
    # both sides of interval outreach transform
    else:
        return 3

def split_intervals_for_transformation(intervals,transform_map):
    changed = True
    while changed:
        changed = False
        interval_counter = 0
        while not changed and interval_counter < len(intervals):
            transform_counter = 0
            while not changed and transform_counter < len(transform_map):
                interval_transform_match = range_matching(intervals[interval_counter],transform_map[transform_counter])
                if interval_transform_match % 2:
                    lower_interval = (intervals[interval_counter][0],sum(transform_map[transform_counter])-intervals[interval_counter][0])
                    higher_interval = (sum(transform_map[transform_counter]),sum(intervals[interval_counter])-(sum(transform_map[transform_counter]))+1)
                    intervals.pop(interval_counter)
                    intervals.append(lower_interval)
                    intervals.append(higher_interval)
                    changed = True
                elif interval_transform_match == 2:
                    lower_interval = (intervals[interval_counter][0],transform_map[transform_counter][0]-intervals[interval_counter][0])
                    higher_interval = (transform_map[transform_counter][0],intervals[interval_counter][1]-(transform_map[transform_counter][0]-intervals[interval_counter][0]))
                    intervals.pop(interval_counter)
                    intervals.append(lower_interval)
                    intervals.append(higher_interval)
                    changed = True
                if not changed:
                    transform_counter += 1
            if not changed:
                interval_counter += 1
    return intervals


seeds = [(int(input[0][7:].split()[i]),int(input[0][7:].split()[i+1])) for i in range(0,len(input[0][7:].split()),2)]
prepared_intervals = seeds

transform_maps = [create_transformation_map(input[i].split("\n")[1:]) for i in range(1,8)]
locations = []

for i in range(7):
    transformed_intervals = []
    prepared_intervals = split_intervals_for_transformation(prepared_intervals,[(transform['source_start'],transform['length']) for transform in transform_maps[i]])
    temp_intervals = []
    for interval in prepared_intervals:
        interval_transformed = False
        for j in range(len(transform_maps[i])):
            if not interval_transformed and 0 <= interval[0] - transform_maps[i][j]["source_start"] < transform_maps[i][j]["length"]:
                temp_intervals.append((interval[0]-transform_maps[i][j]["source_start"] + transform_maps[i][j]["dest_start"],interval[1]))
                transformed_intervals.append(interval)
                interval_transformed = True
    for interval in transformed_intervals:
        prepared_intervals.remove(interval)
    temp_intervals += prepared_intervals
    prepared_intervals = temp_intervals

print(min([interval[0] for interval in prepared_intervals]))
