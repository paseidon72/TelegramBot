# def some(num):
#     if num <= 1:
#         return 1
#     else:
#         return num * some(num - 1)
#
# def sum2(num):
#     result = 1
#     count = 1
#     while count <= num:
#         result *= count
#         count += 1
#     return result
def sum(num, st):
    if st == 0:
        return 1
    else:
        return num * sum(num, st - 1)

print(sum(5, 8))
