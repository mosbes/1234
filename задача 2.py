def calculate_i_by_power(power: int) -> int | str:
    mod = power % 4
    values = ['1','i','-1','-i']
    return values[mod]
for number in range (5):
    print(clculate_i_by_power(number))