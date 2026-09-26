from collections import Counter
from .utils import validate_list, round_answer

def mean(values):
    values = validate_list(values)
    return round_answer(sum(values) / len(values))

def median(values):
    values = sorted(validate_list(values))
    middle = len(values) // 2
    if len(values) % 2:
        return round_answer(values[middle])
    return round_answer((values[middle - 1] + values[middle]) / 2)

def mode(values):
    values = validate_list(values)
    counts = Counter(values)
    highest = max(counts.values())
    if highest == 1:
        return "No mode."
    modes = [v for v, count in counts.items() if count == highest]
    return modes[0] if len(modes) == 1 else modes

def data_range(values):
    values = validate_list(values)
    return max(values) - min(values)

def minimum(values):
    return min(validate_list(values))

def maximum(values):
    return max(validate_list(values))
