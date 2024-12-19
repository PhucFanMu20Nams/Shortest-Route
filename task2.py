import itertools

class ParcelDelivery:
    def __init__(self, cities, distances, grid_coordinates):
        self.cities = cities
        self.distances = distances
        self.grid_coordinates = grid_coordinates

    def get_user_input(self, city_name):
        while True:
            coordinates = self.grid_coordinates.get(city_name, 'No coordinates available')
            user_input = input(f"Going to deliver parcel in {city_name} (Coordinates: {coordinates})? (Yes/No): ").strip().lower()
            if user_input in ['yes', 'no']:
                return user_input == 'yes'
            else:
                print("Invalid input. Please enter 'Yes' or 'No'.")

    def find_optimal_routes(self):
        """Find and print the optimal delivery routes based on user-selected cities."""
        # Display starting point
        print(f"Starting in Hà Nội with coordinates: {self.grid_coordinates['Hà Nội']}")

        # Create a list of selected cities based on user input (excluding 'Hà Nội', which is always included)
        selected_cities = [city for city in self.cities if city != 'Hà Nội' and self.get_user_input(city)]

        if not selected_cities:
            print("No cities selected.")
            return

        # Generate all permutations of the selected cities
        permutations = itertools.permutations(selected_cities)

        # Calculate all routes and distances
        routes = []
        for each_route in permutations:
            route = ['Hà Nội'] + list(each_route) + ['Hà Nội']
            total_distance = 0

            # Calculate the total distance for the route
            for i in range(len(route) - 1):
                total_distance += self.distances.get((route[i], route[i + 1]), 0)

            # Append the route and distance to the routes list
            routes.append((route, total_distance))

        # Sort routes by total distance in ascending order
        routes.sort(key=lambda x: x[1])

        # Extract the shortest distance value
        min_distance = routes[0][1]

        # Display optimal routes with numbering
        route_count = 1
        for route, total_distance in routes:
            if total_distance == min_distance:
                print(f"Route {route_count}: " + " -> ".join(route) + f" | Total Distance: {total_distance} km")
                print("Backup Plan (Grid Coordinates):", " ".join(
                    f"{city}: {self.grid_coordinates.get(city, 'No coordinates available')}" for city in route
                ))
                route_count += 1

# Data distance
distances = {
    # Hanoi distance to the defined city
    ("Hà Nội", "Đà Nẵng"): 780, ("Đà Nẵng", "Hà Nội"): 780,
    ("Hà Nội", "Hồ Chí Minh"): 1650, ("Hồ Chí Minh", "Hà Nội"): 1650,
    ("Hà Nội", "Hải Phòng"): 110, ("Hải Phòng", "Hà Nội"): 110,
    ("Hà Nội", "Nha Trang"): 1050, ("Nha Trang", "Hà Nội"): 1050,
    ("Hà Nội", "Đà Lạt"): 1300, ("Đà Lạt", "Hà Nội"): 1300,

    # Da Nang distance to the defined city
    ("Đà Nẵng", "Hồ Chí Minh"): 830, ("Hồ Chí Minh", "Đà Nẵng"): 830,
    ("Đà Nẵng", "Hải Phòng"): 860, ("Hải Phòng", "Đà Nẵng"): 860,
    ("Đà Nẵng", "Nha Trang"): 510, ("Nha Trang", "Đà Nẵng"): 510,
    ("Đà Nẵng", "Đà Lạt"): 650, ("Đà Lạt", "Đà Nẵng"): 650,

    # Ho Chi Minh distance to the defined city
    ("Hồ Chí Minh", "Hải Phòng"): 1700, ("Hải Phòng", "Hồ Chí Minh"): 1700,
    ("Hồ Chí Minh", "Nha Trang"): 420, ("Nha Trang", "Hồ Chí Minh"): 420,
    ("Hồ Chí Minh", "Đà Lạt"): 290, ("Đà Lạt", "Hồ Chí Minh"): 290,

    # Hai Phong distance to the defined city
    ("Hải Phòng", "Nha Trang"): 1130, ("Nha Trang", "Hải Phòng"): 1130,
    ("Hải Phòng", "Đà Lạt"): 1210, ("Đà Lạt", "Hải Phòng"): 1210,

    # Nha Trang distance to the defined city
    ("Nha Trang", "Đà Lạt"): 220, ("Đà Lạt", "Nha Trang"): 220,
}

# List of cities used in the program
cities = ['Hà Nội', 'Đà Nẵng', 'Hồ Chí Minh', 'Hải Phòng', 'Đà Lạt', 'Nha Trang']

# Grid coordinates for cities
grid_coordinates = {
    "Hà Nội": (0, 0),
    "Đà Nẵng": (0, -5),
    "Hồ Chí Minh": (0, -8),
    "Hải Phòng": (2, 0),
    "Nha Trang": (0, -7),
    "Đà Lạt": (-2, -6),
}

# Initialize and run the ParcelDelivery program
parcel_delivery = ParcelDelivery(cities, distances, grid_coordinates)
parcel_delivery.find_optimal_routes()
