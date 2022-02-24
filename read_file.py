class Client:

    def __init__(self, index, likes, dislikes):
        self.index = index
        self.likes = set(likes)
        self.dislikes = set(dislikes)

    def __str__(self):
        return f'Client {self.index} -> [l: {",".join(self.likes)}, d:{",".join(self.dislikes)}]'


def read_file(file_name):
    ingredients_map = {}
    clients = []
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
        num_clients = int(lines[0])
        for i in range(1, 2*num_clients, 2):
            index_client = len(clients)
            likes = lines[i].split()[1:]
            dislikes = lines[i+1].split()[1:]
            for l in likes:
                if l not in ingredients_map:
                    ingredients_map[l] = set()
                ingredients_map[l].add(index_client)

            client = Client(index_client, likes, dislikes)
            clients.append(client)
    return clients, ingredients_map
