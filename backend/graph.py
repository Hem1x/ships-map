# from datetime import datetime
#
# # date = datetime.today()
# #
# # print(date)
#
# date_string = "12.01.21 10:00"
# date_format = "%d.%m.%y %H:%M"
#
# datetime_object = datetime.strptime(date_string, date_format)
#
# print(datetime_object)

# ребро - длина в чем?
# миля морская = 1852 метра
# from math import radians, sin, cos, sqrt, atan2
#
# def distance(lat1, lon1, lat2, lon2):
#     # переводим координаты из градусов в радианы
#     lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
#
#     # расчет разницы между координатами
#     dlat = lat2 - lat1
#     dlon = lon2 - lon1
#
#     # расчет расстояния по формуле Гаверсинуса
#     a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
#     c = 2 * atan2(sqrt(a), sqrt(1-a))
#     distance = 6371 * c * 0.539957  # 6371 - средний радиус Земли в км, 0.539957 - коэффициент перевода в морские мили
#
#     return distance
#
# print(distance(71.015415, 73.198547, 68.680693, 73.424512))

# dist = {
#     1:215.16416724886025,
#     2:261.2195893541316,
#     3:70.85270491892756,
#     4:414.1149630578018,
#     5:173.3405451002353,
#     6:234.37207017355294,
#     7:62.16654544448847,
#     8:21.835836752582637,
#     9:47.241955730302784,
#     10:46.48764447282277,
#     11:9.262398887445135,
#     12:19.76249919505339,
#     13:9.523092177033249,
#     14:140.25547793936343
# }

# points = [(1, 1), (2, 2)]

# for i in range(0, len(points)):
#     if i % 2 == 0:
#         dist
#         print(i)



#
#
# graph = {
#     1 : {14},
#     2 : {12, 13, 14},
#     3 : {13},
#     4 : {12, 11, 10},
#     5 : {11},
#     6 : {10, 9},
#     7 : {9, 8},
#     8 : {8, 7},
#     9 : {7, 6, 3},
#     10 : {3, 2},
#     11 : {2, 1},
#     12 : {1, 4},
#     13 : {4, 5},
#     14 : {5, 16}
# }

import requests




