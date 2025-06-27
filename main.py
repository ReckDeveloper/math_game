# Main entry point for the RPG game
from engine.game_engine import GameEngine

def show_instructions():
    print("""
Welcome to the Python RPG Game!

Game Overview:
This is a modular, turn-based RPG where you explore a tile-based world, interact with NPCs, battle enemies, and manage your inventory.

Main Functions:
- Explore: Move your character around the world map using arrow keys or WASD.
- Interact: Talk to NPCs, pick up items, and discover secrets using the 'E' key.
- Combat: Engage in turn-based battles with enemies. Use strategy to win and gain experience.
- Inventory: Press 'I' to view, use, or equip items and manage your gear.
- Level Up: Defeat enemies to gain experience and improve your stats.

Tips:
- Save often and explore every area for hidden rewards.
- Experiment with different equipment and strategies in combat.

Press Enter to start your adventure!
""")
    input()

def main():
    show_instructions()
    game = GameEngine()
    game.run()

if __name__ == "__main__":
    main()
