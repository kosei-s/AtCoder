from copy import copy


N, Q = map(int, input().split())

graphs = []
outputs = []
for i in range(Q):
    query = tuple(map(int, input().split()))

    if query[0] == 1:
        x, y = query[1], query[2]
        x_exists, y_exists = False, False
        for i, graph in enumerate(graphs):
            if graph[-1] == x:
                x_exists = True
                x_index = i
            elif graph[0] == y:
                y_exists = True
                y_index = i
            elif x_exists and y_exists:
                break
        if (not x_exists) and (not y_exists):
            graphs.append([x, y])
        elif x_exists and (not y_exists):
            graphs[x_index].append(y)
        elif (not x_exists) and y_exists:
            graphs[y_index].insert(0, x)
        else:
            graphs.append(graphs[x_index] + graphs[y_index])
            if x_index > y_index:
                big, small = x_index, y_index
            else:
                big, small = y_index, x_index
            graphs.pop(big)
            graphs.pop(small)
    elif query[0] == 2:
        x, y = query[1], query[2]
        for i, graph in enumerate(graphs):
            found = False
            for j, train in enumerate(graph):
                if train == x:
                    x_graph_index = i
                    x_order_index = j
                    found = True
                    break
            if found:
                break
        target_graph = copy(graphs[x_graph_index])
        graphs.pop(x_graph_index)
        graphs.append(target_graph[:x_order_index+1])
        graphs.append(target_graph[x_order_index+1:])
    else:
        x = query[1]
        for i, graph in enumerate(graphs):
            found = False
            for j, train in enumerate(graph):
                if train == x:
                    x_graph_index = i
                    found = True
                    break
            if found:
                break
        outputs.append(' '.join(map(str, graphs[x_graph_index])))

for output in outputs:
    print(output)
