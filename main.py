# pylint: disable=C0200

import matplotlib.pyplot as plt
import networkx as nx
import networkx.algorithms.approximation as nx_app
import matplotlib.animation as animation

def list_path(G):      
    list_path = []
    for node in G.nodes:
        for adj in G.adj[node]:
            list_path.append([node, adj])

    return list_path
    
def dfs(G, from_node, route, passed_path, longest):
    route = route + [from_node]
    if len(passed_path) == len(list_path(G)):
        return route
    for to_node in G.adj[from_node]:
        if (([from_node, to_node] not in passed_path) or ([to_node, from_node] not in passed_path)):
        # if ((self.result[from_node][to_node] is False) & (self.result[to_node][from_node] is False)):
            if longest is None or len(route) > len(longest):
                new_passed_path = passed_path + [[from_node, to_node]] + [[to_node, from_node]]
                new_route = dfs(G, to_node, route, new_passed_path, longest)
                if new_route != None:
                    longest = new_route
        
    return longest

def solution(G, start):
    return dfs(G, start, [], [], None)

def visualize_solution(G):
    # Initialize the plot
    fig, ax = plt.subplots()
    pos = nx.kamada_kawai_layout(G)
    # pos = nx.spring_layout(G)
    
    for node in G.nodes:
        solution_path = solution(G, node)
        if solution_path is not None:
            print(solution_path)

            # Initial drawing
            nx.draw_networkx_nodes(G, pos, ax=ax, node_color='gray')
            nx.draw_networkx_edges(G, pos, ax=ax, edge_color='black', style='dashed')
            nx.draw_networkx_labels(G, pos, ax=ax)
            
            # Function to update the plot for each iteration
            def update(i):
                ax.clear()
                nx.draw_networkx_nodes(G, pos, ax=ax, node_color='gray')
                nx.draw_networkx_edges(G, pos, ax=ax, edge_color='black', style='dashed')
                nx.draw_networkx_labels(G, pos, ax=ax)

                path = solution_path[:i+1]
                edge_lables = {}
                for k in range(len(path)-1):
                    edge_lables[(path[k], path[k+1])] = k+1
                    
                nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='blue')
                nx.draw_networkx_edges(G, pos, edgelist=list(zip(path[:-1], path[1:])), edge_color='red', width=3)
                nx.draw_networkx_edge_labels(G, pos, font_size=5, edge_labels=edge_lables)

                return ax
                
            # Create the animation
            ani = animation.FuncAnimation(fig, update, frames=len(solution_path), interval=500, repeat=False)

            # Save the animation
            Writer = animation.writers['ffmpeg']
            writer = Writer(fps=5, metadata=dict(artist='KitaviSs'), bitrate=1800)
            ani.save('pass_all_edges_without_duplicating.mp4', writer=writer)

            plt.show()

            break

if __name__ == '__main__':
    # Flower
    nodes_list1 = [1,2,3,4,5,6,7,8,9]
    edges_list1 = [
        (1,2),
        (1,3),
        (2,3),
        (2,4),
        (2,7),
        (2,5),
        (3,5),
        (3,8),
        (3,6),
        (4,7),
        (5,7),
        (5,8),
        (6,8),
        (7,8),
        (7,9),
        (8,9)]
    
    # Simple square
    nodes_list2 = [1,2,3,4]
    edges_list2 = [
        (1, 0),
        (0, 2),
        (2, 1),
        (0, 3),
        (3, 4),
        (3, 2),
        (3, 1),
        (2, 4)]
    
    # 3 stars
    nodes_list3 = [i+1 for i in range(25)]
    edges_list3 = [
        (1,5),
        (1,6),
        (2,8),
        (2,9),
        (3,11),
        (3,12),
        (4,5),
        (4,14),
        (5,6),
        (5,14),
        (6,7),
        (6,15),
        (7,8),
        (7,15),
        (7,16),
        (8,9),
        (8,16),
        (9,10),
        (9,17),
        (10,11),
        (10,17),
        (10,18),
        (11,12),
        (11,18),
        (12,13),
        (12,19),
        (13,19),
        (14,23),
        (14,20),
        (15,20),
        (15,24),
        (16,24),
        (16,21),
        (17,21),
        (17,25),
        (18,25),
        (18,22),
        (19,22),
        (19,26),
        (20,23),
        (20,24),
        (21,24),
        (21,25),
        (22,25),
        (22,26)]
    
    # noel tree
    nodes_list4 = [i+1 for i in range(17)]
    edges_list4 = [
        (1,3),
        (1,6),
        (2,4),
        (2,5),
        (3,4),
        (4,5),
        (4,8),
        (5,6),
        (5,11),
        (7,9),
        (7,10),
        (8,9),
        (9,10),
        (9,12),
        (10,11),
        (10,15),
        (12,13),
        (13,14),
        (13,16),
        (14,15),
        (14,17),
        (16,17)]

    G = nx.Graph()
    G.add_nodes_from(nodes_list3)
    G.add_edges_from(edges_list3)

    # G = nx.gnp_random_graph(7, 0.8)
    # nx.draw(G, with_labels=True)
    # plt.show()

    visualize_solution(G)