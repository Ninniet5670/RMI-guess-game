import Pyro4
import random

@Pyro4.expose
class GuessingGameServer:
    def __init__(self):
        self.secret_number = self.generate_secret_number()
        self.players = {}

    def generate_secret_number(self):
        return random.randint(1, 100)

    def register_player(self, player_name):
        self.players[player_name] = random.randint(1, 100)

    def play(self, player_name, guess):
        if guess < self.secret_number:
            return "Low"
        elif guess > self.secret_number:
            return "High"
        else:
            self.secret_number = self.generate_secret_number()
            print(f'*{player_name}* guessed right! sorting the number...')
            return "Correct"

daemon = Pyro4.Daemon()
server = GuessingGameServer()
uri = daemon.register(server)

print("server URI:", uri)

ns = Pyro4.locateNS()
ns.register("guessing_game.server", uri)

print("Server ready.")

daemon.requestLoop()
