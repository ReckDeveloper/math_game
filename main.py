# Main entry point for the RPG game
from engine.game_engine import GameEngine

def show_instructions():
    print("""
Welcome to the Python RPG Game!

Instructions:
- Use arrow keys or WASD to move your character.
- Press 'I' to open your inventory.
- Interact with NPCs and objects using the 'E' key.
- Defeat enemies in turn-based combat to gain experience and level up.
- Explore the world, collect items, and complete quests!

Press Enter to start the game...
""")
    input()

def main():
    show_instructions()
    game = GameEngine()
    game.run()

if __name__ == "__main__":
    main()
