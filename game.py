import random
class Game:

    moves = ["P", "R", "S"]

    
    mp = {"R": "Rock", "P": "Paper", "S": "Scissors"}

    prompt = "%sPlease enter a%s: R(rock) or P(paper) or S(scissors): "
    prompt1 = prompt % ("", " move")
    prompt2 = prompt % ("Wrong move! ", " correct move")

    def __init__(self):
        self.player_move = None
        self.cpu_move = None

    def get_user_input(self):
        print(self.prompt1)

        while (user_input := input().upper()) not in self.moves:
            print(self.prompt2)

        self.player_move = user_input

    def get_cpu_input(self):
        self.cpu_move = random.choice(self.moves)

    def display_moves(self):
        print(f"Player({self.mp[self.player_move]}) : CPU({self.mp[self.cpu_move]})")

    def result(self):
        """
        returns 1 if player wins, 0 if draw -1 if player lose
        """
        if self.player_move == self.cpu_move:
            print("It's a draw!")
            return 0

        if self.player_move == "P":
            return 1 if self.cpu_move == "R" else -1

        if self.player_move == "R":
            return 1 if self.cpu_move == "S" else -1

        if self.player_move == "S":
            return 1 if self.cpu_move == "P" else -1

    def play(self):
        while True:
            self.get_user_input()
            self.get_cpu_input()
            self.display_moves()

            result = self.result()
            if result == 0:
                print("\nLet's get started again! \n")
            elif result == 1:
                print("You win!")
                break
            else:
                print("You lose!")
                break

game = Game()
game.play()
