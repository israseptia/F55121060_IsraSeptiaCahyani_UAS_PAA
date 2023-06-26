import time
import sys
import heapq

#menghitung jarak antara dua titik
def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Algoritma TSP (Traveling Salesman Problem) menggunakan pendekatan exhaustive search
def tsp(points):
    n = len(points)
    min_distance = sys.maxsize
    shortest_path = []

    def backtrack(path, visited, current_distance):
        nonlocal min_distance, shortest_path

        if len(path) == n:
            if current_distance < min_distance:
                min_distance = current_distance
                shortest_path = path[:]
                print("Ditemukan jalur terpendek baru:", shortest_path, "dengan jarak:", min_distance)

        else:
            for i in range(n):
                if not visited[i]:
                    next_point = points[i]
                    new_distance = current_distance + distance(path[-1], next_point) if path else 0
                    if new_distance < min_distance:
                        visited[i] = True
                        path.append(next_point)
                        backtrack(path, visited, new_distance)
                        path.pop()
                        visited[i] = False

    # Inisialisasi
    start_time = time.time()
    initial_point = points[0]
    visited = [False] * n
    path = [initial_point]
    visited[0] = True

    # Memulai perhitungan
    backtrack(path, visited, 0)

    end_time = time.time()
    execution_time = end_time - start_time

    return shortest_path, min_distance, execution_time

# Implementasi algoritma Dijkstra untuk mencari shortest path dalam graf terarah
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))
                print("Jarak terbaru ke", neighbor, ":", new_distance)

    return distances

# mencetak hasil perhitungan TSP
def print_tsp_result(shortest_path, distance, execution_time):
    print("\nHasil TSP:")
    print("Jalur Terpendek:", shortest_path)
    print("Jarak Total:", distance)
    print("Waktu Eksekusi:", round(execution_time, 6), "detik")

# mencetak hasil perhitungan Dijkstra
def print_dijkstra_result(distances, execution_time):
    print("\nHasil Dijkstra:")
    for node, distance in distances.items():
        print(f"Jarak dari node awal ke node {node}: {distance}")
    print("Waktu Eksekusi:", round(execution_time, 6), "detik")

# Fungsi utama
def main():
    points = [
        (0, 0),
        (1, 5),
        (2, 3),
        (5, 2),
        (6, 4),
        (7, 1)
    ]

    graph = {
        'A': {'B': 12, 'C': 10, 'G': 12},
        'B': {'A': 12, 'C': 8, 'D': 12},
        'C': {'A': 10, 'B': 8, 'D': 11, 'E': 3, 'G': 9},
        'D': {'C': 11, 'E': 11, 'F': 10},
        'E': {'C': 3, 'D': 11, 'F': 6, 'G': 7},
        'F': {'D': 10, 'E': 6, 'G': 9},
        'G': {'A': 12, 'C': 9, 'E': 7, 'F': 9}
    }

    while True:
        print("\nPilih algoritma:")
        print("1. TSP ")
        print("2. Dijkstra")
        print("3. Exit")
        choice = input("Masukkan pilihan Anda: ")

        if choice == "1":
            shortest_path, distance, execution_time = tsp(points)
            print_tsp_result(shortest_path, distance, execution_time)

        elif choice == "2":
            start_node = input("Masukkan node awal: ")
            start_time = time.time()
            distances = dijkstra(graph, start_node)
            end_time = time.time()
            execution_time = end_time - start_time
            print_dijkstra_result(distances, execution_time)

        elif choice == "3":
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
