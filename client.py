import Pyro4

server_uri = "PYRONAME:guessing_game.server"
server = Pyro4.Proxy(server_uri)

player_name = input("Digit your name: ")
server.register_player(player_name)

print("Guess the secret number between 1 and 100 (or digit -1 to logoff):")
while True:
    guess = int(input("Your guess: "))
    if guess == -1:
        print("Logoff.")
        break

    result = server.play(player_name, guess)
    print(result)
    if result == "Correct":
        print("Congratulations! you guessed right!")
        break
