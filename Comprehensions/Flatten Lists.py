# list_rsv = [el.strip() for el in input().split("|")]
# y = {}
# count = 1
# for i in list_rsv:
#     y[count] = i
#     count += 1
#     for j in i:
#
#         if j != " ":
#             x.append(j)
#
# count = len(y)
# for key in y:
#     print(y[count], end=" ")
#     count -= 1


# list_rsv = [el.split() for el in input().split("|")]
# list_rsv.reverse()
# for el in list_rsv:
#     print(*el, end=" ")

list_rsv = [el.split() for el in input().split("|")]
list_rsv.reverse()
[print(*el, end=" ") for el in list_rsv]


