from timeit import repeat


def run_sorting_algorithm(algorithm, list):
    set_up_variable = f"from __main__ import {algorithm}"\
        if algorithm != "sorted" else ""
    stmt = f"{algorithm}({list})"
    
    repetitions = repeat(setup=set_up_variable, stmt=stmt, repeat=3, number=10)
    
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(repetitions)}")