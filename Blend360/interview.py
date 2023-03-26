
def quarter_maths(year, quarter, quarters_to_add):
    
    total_quarters = quarter + quarters_to_add
    
    quarters_left = total_quarters % 4
    years_to_add = total_quarters // 4
    
    new_year = year + years_to_add
    new_quarter = quarters_left
    return new_year, new_quarter

print(quarter_maths(year=2020, quarter=4, quarters_to_add=-7))

from typing import Union
from collections import defaultdict

def compress(input: Union[str, int, None]) -> list:

    result_dict = defaultdict(int)
    
    try: 
        for char in input:
            result_dict[char] += 1

        result = list(result_dict.items())

    except:
        result = []

    return result

print(compress("55555"))  # 19