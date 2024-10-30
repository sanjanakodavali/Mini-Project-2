class Board:
    def __init__(self):
        
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def printBoard(self):
        
        print("-" * 17)
        print("|R\\C| 0 | 1 | 2 |")
        print("-" * 17)
        for i in range(3):
            print(f"| {i} | {self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]} |")
            print("-" * 17)

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = 'X'
        self.turns = 0

    def switchPlayer(self):
        
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'

    def validateEntry(self, row, col):
        
        if not (0 <= row < 3 and 0 <= col < 3):
            print("Invalid entry: try again.")
            print("Row & column numbers must be either 0, 1, or 2.")
            return False
        elif self.board.board[row][col] != " ":
            print("That cell is already taken.")
            print("Please make another selection.")
            return False
        return True

    def checkFull(self):
        
        return all(cell != " " for row in self.board.board for cell in row)

    def checkWin(self):
        
        b = self.board.board
        player = self.turn

        
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] == player or b[0][i] == b[1][i] == b[2][i] == player:
                return True
        if b[0][0] == b[1][1] == b[2][2] == player or b[0][2] == b[1][1] == b[2][0] == player:
            return True
        return False

    def checkEnd(self):
        
        if self.checkWin():
            print(f"{self.turn} IS THE WINNER!!!")
            return True
        elif self.checkFull():
            print("DRAW! NOBODY WINS!")
            return True
        return False

    def playGame(self):
        
        repeat = "y"
        while repeat[0].lower() == "y":
            self.board = Board()  
            self.turns = 0
            self.turn = 'X'
            print("New Game: X goes first.")
            self.board.printBoard()

            while True:
                print(f"\n{self.turn}'s turn.")
                print(f"Where do you want your {self.turn} placed?")
                print("Please enter row number and column number separated by a comma.")
                row, col = map(int, input().split(","))
                print(f"You have entered row #{row}")
                print(f"          and column #{col}")
                
                if not self.validateEntry(row, col):
                    continue

                print("Thank you for your selection.")
                self.board.board[row][col] = self.turn
                self.turns += 1

                
                if self.checkEnd():
                    self.board.printBoard()
                    break

                self.board.printBoard()
                self.switchPlayer()

            print()
            repeat = input("Another game? Enter Y or y for yes.\n")
        print("Thank you for playing")


if __name__ == "__main__":
    game = Game()
    game.playGame()
