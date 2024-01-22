import random
import time

class TicTacToe:
    
    def __init__(self):
        """
        Initialise un objet TicTacToe avec un plateau de jeu vide, les joueurs,
        le niveau de difficulté par défaut, et les scores.
        """

        # Initialisation du tableau de jeu 3x3 avec des espaces vides
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        # Joueur actuel ('X' par défaut)
        self.current_player = 'X'
        # Joueur IA ('O')
        self.ai_player = 'O'
        # Joueur humain ('X')
        self.human_player = 'X'
        # Niveau de difficulté de l'IA (3 par défaut)
        self.ai_difficulty = 3

    def print_board(self):
        """
        Affiche le plateau de jeu.
        """

        print("  0 | 1 | 2 ")
        print(" -----------")
        for i in range(3):
            print(f"{i}| {self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]} |")
            print(" -----------")

    def is_valid_move(self, row, col):
        """
        Vérifie si un coup est valide aux coordonnées données.

        :param row: Ligne du coup.
        :param col: Colonne du coup.
        :return: True si le coup est valide, False sinon.
        """

        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' '

    def make_move(self, row, col, player):

        """
        Effectue un coup sur le plateau de jeu.

        :param row: Ligne du coup.
        :param col: Colonne du coup.
        :param player: Le joueur effectuant le coup.
        :return: True si le coup a été effectué avec succès, False sinon.
        """

        if self.is_valid_move(row, col):
            self.board[row][col] = player
            return True
        return False

    def switch_player(self):
        """
        Change le joueur actuel.
        """
        self.current_player = self.ai_player if self.current_player == self.human_player else self.human_player

    def check_winner(self, player):
        """
        Vérifie s'il y a un gagnant sur le plateau.

        :param player: Le joueur à vérifier.
        :return: True s'il y a un gagnant, False sinon.
        """

        for i in range(3):
            # Vérifie si toutes les cellules de la ligne i, j ont le symbole du joueur
            if all(self.board[i][j] == player for j in range(3)) or \
               all(self.board[j][i] == player for j in range(3)):
                return True
        # Vérifie si toutes les cellules de les diagonales principale ont le symbole du joueur
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2 - i] == player for i in range(3)):
            return True
        # Aucun gagnant
        return False

    def is_board_full(self):
        """
        Vérifie si le plateau de jeu est plein.

        :return: True si le plateau est plein, False sinon.
        """
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def minimax(self, depth, maximizing_player):
        """
        Implémente l'algorithme minimax pour l'IA.

        :param depth: La profondeur de la récursion.
        :param maximizing_player: Un booléen indiquant si l'IA cherche à maximiser son score.
        :return: Le score évalué pour la position actuelle.
        """

        # Si l'IA a gagné, retourne un score élevé (10 moins la profondeur pour encourager des victoires plus rapides)
        if self.check_winner(self.ai_player):
            return 10 - depth
        # Si le joueur humain a gagné, retourne un score bas (profondeur moins 10 pour pénaliser les victoires humaines)
        elif self.check_winner(self.human_player):
            return depth - 10
        # Si la partie est un match nul, retourne un score neutre (0)
        elif self.is_board_full():
            return 0

        # Si l'IA cherche à maximiser son score
        if maximizing_player:
            max_eval = float('-inf')
            # Parcours toutes les cellules du plateau
            for i in range(3):
                for j in range(3):
                    # Si la cellule est vide
                    if self.board[i][j] == ' ':
                        # Simule le coup de l'IA
                        self.board[i][j] = self.ai_player
                        # Évalue le score résultant en appelant récursivement minimax pour le joueur humain
                        eval = self.minimax(depth + 1, False)
                        # Annule le coup 
                        self.board[i][j] = ' '
                        # Met à jour le maximum des scores évalués
                        max_eval = max(max_eval, eval)
            return max_eval
        else:
            # Si le joueur humain cherche à minimiser le score
            min_eval = float('inf')
            # Parcours toutes les cellules du plateau
            for i in range(3):
                for j in range(3):
                    # Si la cellule est vide
                    if self.board[i][j] == ' ':
                        # Simule le coup du joueur humain
                        self.board[i][j] = self.human_player
                        # Évalue le score résultant en appelant récursivement minimax pour l'IA
                        eval = self.minimax(depth + 1, True)
                        # Annule le coup 
                        self.board[i][j] = ' '
                        # Met à jour le minimum des scores évalués
                        min_eval = min(min_eval, eval)
            return min_eval

    def find_best_move(self):
        """
        Trouve le meilleur coup pour l'IA en utilisant l'algorithme minimax.

        :return: Les coordonnées du meilleur coup.
        """

        # Initialise la meilleure valeur à moins l'infini et le meilleur coup à None
        best_val = float('-inf')
        best_move = None

        # Parcours toutes les cellules du plateau
        for i in range(3):
            for j in range(3):
                # Vérifie si la cellule est vide
                if self.board[i][j] == ' ':
                    # Joue temporairement le coup pour l'IA
                    self.board[i][j] = self.ai_player
                    # Évalue le coup en utilisant l'algorithme minimax
                    move_val = self.minimax(0, False)
                    # Annule le coup pour revenir à l'état précédent (backtracking)
                    self.board[i][j] = ' '

                    # Compare la valeur évaluée avec la meilleure valeur actuelle
                    if move_val > best_val:
                        # Met à jour la meilleure valeur et le meilleur coup
                        best_move = (i, j)
                        best_val = move_val

        return best_move

    def get_human_move(self):
        """
        Obtient le coup du joueur humain depuis l'entrée utilisateur.

        :return: Les coordonnées du coup choisi par le joueur humain.
        """

        while True:
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))
                if self.is_valid_move(row, col):
                    return row, col
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def play(self):
        """
        Fonction principale pour jouer au jeu.

        Gère les tours des joueurs, les mouvements, et vérifie le résultat du jeu.
        """

        print("Welcome to Tic-Tac-Toe!")

        while True:
            self.print_board()

            if self.current_player == self.human_player:
                print(f"{self.current_player}'s turn:")
                row, col = self.get_human_move()
            else:
                print(f"{self.current_player}'s turn:")
                time.sleep(1)  # Une pause 
                if self.ai_difficulty == 3:  # IA difficile
                    print("AI is thinking...")
                    row, col = self.find_best_move()
                elif self.ai_difficulty == 2:  # IA moyenne
                    print("AI is making a move...")
                    # Choix aléatoire entre un coup difficile et un coup normal
                    row, col = self.find_best_move() if random.choice([True, False]) else random.choice(self.get_empty_cells())
                else:  # IA facile
                    print("AI is making a move...")
                    row, col = random.choice(self.get_empty_cells())

            self.make_move(row, col, self.current_player)

            if self.check_winner(self.current_player):
                self.print_board()
                if self.current_player == self.human_player:
                    print(f"Player '{self.current_player}': wins!")
                else:
                    print(f"Player '{self.current_player}': wins!")
                break
            elif self.is_board_full():
                self.print_board()
                print("It's a tie!")
                break

            self.switch_player()
            print("\n")

    def get_empty_cells(self):
        """
        Retourne une liste de coordonnées pour les cellules vides sur le plateau.

        :return: Une liste de tuples représentant les coordonnées des cellules vides.
        """

        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']

    def set_ai_difficulty(self):
        """
        Définit le niveau de difficulté de l'IA en demandant à l'utilisateur de choisir.

        :return: None
        """

        print("Choose AI difficulty level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Challenging")
        self.ai_difficulty = int(input("Enter the desired difficulty level (1, 2, or 3): "))
        while self.ai_difficulty not in [1, 2, 3]:
            print("Invalid choice. Please choose 1, 2, or 3.")
            self.ai_difficulty = int(input("Enter the desired difficulty level (1, 2, or 3): "))


def main():
    """
    Fonction principale pour exécuter le jeu.

    Gère la boucle principale du jeu, les choix des joueurs, et l'exécution du jeu.
    """

    while True:
        tic_tac_toe = TicTacToe()

        tic_tac_toe.set_ai_difficulty()

        tic_tac_toe.play()

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()

