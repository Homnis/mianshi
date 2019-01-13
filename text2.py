import math,copy


def find_way(points):
    numbers = len(points)
    if numbers <= 1:
        return [], 0

    connected_points = [points[0]]
    not_connect = points[1:]
    ways = []
    length = 0
    for i in range(numbers - 1):
        # 求出所有已连接的点和所有未连接的点中最短的距离
        a, b = connected_points[0], not_connect[0]
        length_between = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)  # 勾股定理求距离
        for m in connected_points:
            for n in not_connect:
                try_length = math.sqrt((m[0] - n[0]) ** 2 + (m[1] - n[1]) ** 2)
                if try_length < length_between:  # 如果有更短的
                    length_between = try_length
                    a, b = m, n
        same_points = points.count(a)
        if a==b:
            # print(a,b)
            # print(points.index(a))
            new_list=copy.deepcopy(points)
            position = 0 # 是删除了几个数据
            for position in range(same_points-1):
                # print(new_list, "++++++++++++++++++++++++++",position)
                former_position=new_list.index(a)+position
                # print("former:",former_position)
                new_list.remove(a)
                # print("数组：",[[points.index(a) + position * 2, new_list.index(a) + 1 + position]])
                if [former_position, new_list.index(a) + 1 + position] not in ways:
                    ways.append([former_position,new_list.index(a)+1+position])
                    # print(points)
                    # print("new:",new_list)
                    # print([former_position,new_list.index(a)+1+position],"------------------------",position)
                    position+=1
                    # print(ways,"*****************************",position)
        elif same_points>1:
            if [points.index(a)+same_points-1, points.index(b)] not in ways:
                new_list = copy.deepcopy(points)
                for i in range(same_points-1):
                    new_list.remove(a)
                ways.append([new_list.index(a)+same_points-1, points.index(b)])
                print(ways, "*****************************")
        else:
            print(points)
            print("****************************",a,b)
            if [points.index(a), points.index(b)] not in ways:
                ways.append([points.index(a), points.index(b)])
                print("现在的数据：",ways)
        # print(a, b)
        connected_points.append(b)  # 已连接点集中记录点b
        not_connect.remove(b)  # 未连接点集中删除点b
        # print("not_connect",not_connect)
        # print("connected:",connected_points)
        length += length_between  # 记录总长度

    return ways, length


# a = find_way([[79, 30], [79, 30], [79, 72], [79, 72], [37, 17], [79, 72] ,[44, 66], [9, 33], [74, 81], [23, 51], [83, 82]])
# a = find_way([[79, 30],[79, 72], [37, 17], [79, 72], [44, 66], [9, 33], [79, 72], [74, 81], [23, 51], [83, 82]])
a = find_way([[79, 30],[79, 72], [79, 30],[37, 17], [79, 72], [44, 66], [9, 33], [79, 72], [74, 81], [23, 51], [83, 82]])
print(a)
