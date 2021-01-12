def process_numbers (num):
    numbers = []
    try:
        for value in num:
            if(str(value).isnumeric()):
                numbers.append(int(value))
            numbers.sort()    
    finally:
        return numbers

def process_names (all_names):
    names = []
    try:
        for value in all_names:
            if(not str(value).isnumeric()):
                names.append(value)
        names.sort()
    finally:
        return names