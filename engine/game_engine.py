import pygame
import random

# Game Engine Module
# Handles main loop, game states, input, and rendering

class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Python RPG Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.SysFont(None, 32)
        self.instructions = [
            "Welcome to the Python RPG Game!",
            "",
            "Game Overview:",
            "This is a modular, turn-based RPG where you explore a tile-based world,",
            "interact with NPCs, battle enemies, and manage your inventory.",
            "",
            "Main Functions:",
            "- Explore: Move your character around the world map using arrow keys or WASD.",
            "- Interact: Talk to NPCs, pick up items, and discover secrets using the 'E' key.",
            "- Combat: Engage in turn-based battles with enemies. Use strategy to win and gain experience.",
            "- Inventory: Press 'I' to view, use, or equip items and manage your gear.",
            "- Level Up: Defeat enemies to gain experience and improve your stats.",
            "",
            "Tips:",
            "- Save often and explore every area for hidden rewards.",
            "- Experiment with different equipment and strategies in combat.",
            "",
            "Press any key to start your adventure!"
        ]
        self.showing_instructions = True
        self.stage = None  # Track current stage
        self.player_pos = [100, 200]  # x, y for player
        self.enemy_pos = [300, 220]   # x, y for enemy
        self.move_speed = 5
        self.enemy_move_speed = 5
        self.enemy_direction = 1  # 1: right, -1: left
        self.game_over = False
        self.win_message = None
        self.show_question = False
        self.question_text = "How much is 1+1?"
        self.answer = ""
        self.correct_answer = "2"
        self.jump_animation = False
        self.jump_height = 0
        self.jump_direction = 1
        self.player_sad = False
        self.enemy_smile = False
        self.questions = [
            ("Quanto é 1+1?", "2"),
            ("Quanto é 2+3?", "5"),
            ("Quanto é 4+4?", "8"),
            ("Quanto é 5+7?", "12"),
            ("Quanto é 6+2?", "8"),
            ("Quanto é 3+9?", "12"),
            ("Quanto é 8+1?", "9"),
            ("Quanto é 7+6?", "13"),
            ("Quanto é 9+5?", "14"),
            ("Quanto é 10+10?", "20")
        ]
        self.question_text, self.correct_answer = self.questions[0]

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)  # Limit to 60 FPS

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if self.showing_instructions and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.showing_instructions = False
                    self.start_stage(1)
                elif event.key == pygame.K_q:
                    self.running = False
                else:
                    self.showing_instructions = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.running = False
                if self.show_question and not self.game_over:
                    if event.key == pygame.K_BACKSPACE:
                        self.answer = self.answer[:-1]
                    elif event.key == pygame.K_RETURN:
                        if self.answer.strip() == self.correct_answer:
                            self.show_question = False
                            self.jump_animation = True
                            self.player_sad = False
                            self.enemy_smile = False
                        else:
                            self.answer = ""
                            self.player_sad = True
                            self.enemy_smile = True
                    elif event.unicode.isdigit():
                        self.answer += event.unicode

    def start_stage(self, stage_number):
        self.stage = stage_number
        # Initialize the first stage (placeholder)
        print(f"Stage {stage_number} initialized!")
        # Add stage setup logic here

    def update(self):
        if self.stage == 1 and not self.game_over:
            if not self.show_question and not self.jump_animation:
                keys = pygame.key.get_pressed()
                # Player movement (WASD)
                if keys[pygame.K_w]:
                    self.player_pos[1] -= self.move_speed
                if keys[pygame.K_s]:
                    self.player_pos[1] += self.move_speed
                if keys[pygame.K_a]:
                    self.player_pos[0] -= self.move_speed
                if keys[pygame.K_d]:
                    self.player_pos[0] += self.move_speed
                # Enemy simple left-right animation
                self.enemy_pos[0] += self.enemy_move_speed * self.enemy_direction
                if self.enemy_pos[0] > 600 or self.enemy_pos[0] < 300:
                    self.enemy_direction *= -1
                # Collision detection (simple rectangle overlap)
                player_rect = pygame.Rect(self.player_pos[0], self.player_pos[1], 60, 120)
                enemy_rect = pygame.Rect(self.enemy_pos[0], self.enemy_pos[1], 60, 60)
                if player_rect.colliderect(enemy_rect):
                    q, a = random.choice(self.questions)
                    self.question_text = q
                    self.correct_answer = a
                    self.answer = ""
                    self.show_question = True
            elif self.jump_animation:
                # Animate jump (simple up and down)
                if self.jump_height < 50 and self.jump_direction == 1:
                    self.player_pos[1] -= 8
                    self.jump_height += 8
                elif self.jump_height >= 50:
                    self.jump_direction = -1
                elif self.jump_height > 0 and self.jump_direction == -1:
                    self.player_pos[1] += 8
                    self.jump_height -= 8
                else:
                    self.jump_animation = False
                    self.jump_height = 0
                    self.jump_direction = 1
                    self.game_over = True
                    self.win_message = self.font.render("The princess wins", True, (255, 105, 180))

    def render(self):
        self.screen.fill((0, 0, 0))  # Clear screen with black
        if self.showing_instructions:
            y = 40
            for line in self.instructions:
                text_surface = self.font.render(line, True, (255, 255, 255))
                self.screen.blit(text_surface, (40, y))
                y += 36
            # Draw player
            pygame.draw.ellipse(self.screen, (255, 224, 189), (self.player_pos[0], self.player_pos[1], 60, 120))
            pygame.draw.ellipse(self.screen, (139, 69, 19), (self.player_pos[0]-10, self.player_pos[1]-20, 80, 40))
            pygame.draw.ellipse(self.screen, (0, 255, 0), (self.player_pos[0]+20, self.player_pos[1]+10, 40, 20))
            pygame.draw.rect(self.screen, (128, 0, 128), (self.player_pos[0]+10, self.player_pos[1]+80, 40, 60))
            pygame.draw.circle(self.screen, (0, 0, 0), (self.player_pos[0]+20, self.player_pos[1]+40), 5)
            pygame.draw.circle(self.screen, (0, 0, 0), (self.player_pos[0]+40, self.player_pos[1]+40), 5)
            # Draw sad mouth if needed
            if self.player_sad:
                pygame.draw.arc(self.screen, (0, 0, 0), (self.player_pos[0]+20, self.player_pos[1]+70, 20, 10), 3.14, 0, 2)
            # Draw enemy
            pygame.draw.ellipse(self.screen, (255, 224, 189), (self.enemy_pos[0], self.enemy_pos[1], 60, 60))
            pygame.draw.rect(self.screen, (0, 120, 255), (self.enemy_pos[0]+15, self.enemy_pos[1]+60, 30, 50))
            pygame.draw.rect(self.screen, (21, 96, 189), (self.enemy_pos[0]+15, self.enemy_pos[1]+110, 30, 40))
            pygame.draw.circle(self.screen, (0, 0, 0), (self.enemy_pos[0]+20, self.enemy_pos[1]+30), 5)
            pygame.draw.circle(self.screen, (0, 0, 0), (self.enemy_pos[0]+40, self.enemy_pos[1]+30), 5)
            # Draw smile if needed
            if self.enemy_smile:
                pygame.draw.arc(self.screen, (0, 0, 0), (self.enemy_pos[0]+20, self.enemy_pos[1]+40, 20, 10), 0, 3.14, 2)
            # Draw Q key hint at the bottom
            hint = self.font.render("Press Q at any time to quit.", True, (255, 255, 0))
            self.screen.blit(hint, (40, 570))
            stage_hint = self.font.render("Press 1 to start Stage 1.", True, (0, 255, 0))
            self.screen.blit(stage_hint, (40, 540))
        else:
            if self.stage == 1:
                # Draw classroom background
                pygame.draw.rect(self.screen, (200, 200, 200), (60, 100, 680, 400))
                pygame.draw.rect(self.screen, (230, 220, 170), (60, 400, 680, 100))
                pygame.draw.rect(self.screen, (30, 60, 30), (120, 120, 300, 60))
                pygame.draw.rect(self.screen, (180, 220, 255), (500, 130, 180, 50))
                for i in range(4):
                    pygame.draw.rect(self.screen, (160, 82, 45), (140 + i*120, 320, 80, 40))
                pygame.draw.rect(self.screen, (120, 60, 20), (350, 250, 100, 40))
                # Draw player
                pygame.draw.ellipse(self.screen, (255, 224, 189), (self.player_pos[0], self.player_pos[1], 60, 120))
                pygame.draw.ellipse(self.screen, (139, 69, 19), (self.player_pos[0]-10, self.player_pos[1]-20, 80, 40))
                pygame.draw.ellipse(self.screen, (0, 255, 0), (self.player_pos[0]+20, self.player_pos[1]+10, 40, 20))
                pygame.draw.rect(self.screen, (128, 0, 128), (self.player_pos[0]+10, self.player_pos[1]+80, 40, 60))
                pygame.draw.circle(self.screen, (0, 0, 0), (self.player_pos[0]+20, self.player_pos[1]+40), 5)
                pygame.draw.circle(self.screen, (0, 0, 0), (self.player_pos[0]+40, self.player_pos[1]+40), 5)
                if self.player_sad:
                    pygame.draw.arc(self.screen, (0, 0, 0), (self.player_pos[0]+20, self.player_pos[1]+70, 20, 10), 3.14, 0, 2)
                # Draw enemy
                pygame.draw.ellipse(self.screen, (255, 224, 189), (self.enemy_pos[0], self.enemy_pos[1], 60, 60))
                pygame.draw.rect(self.screen, (0, 120, 255), (self.enemy_pos[0]+15, self.enemy_pos[1]+60, 30, 50))
                pygame.draw.rect(self.screen, (21, 96, 189), (self.enemy_pos[0]+15, self.enemy_pos[1]+110, 30, 40))
                pygame.draw.circle(self.screen, (0, 0, 0), (self.enemy_pos[0]+20, self.enemy_pos[1]+30), 5)
                pygame.draw.circle(self.screen, (0, 0, 0), (self.enemy_pos[0]+40, self.enemy_pos[1]+30), 5)
                if self.enemy_smile:
                    pygame.draw.arc(self.screen, (0, 0, 0), (self.enemy_pos[0]+20, self.enemy_pos[1]+40, 20, 10), 0, 3.14, 2)
                stage_text = self.font.render("Stage 1: The Adventure Begins!", True, (0, 255, 0))
                self.screen.blit(stage_text, (40, 40))
                if self.show_question:
                    # Draw question balloon
                    balloon_rect = pygame.Rect(200, 100, 400, 120)
                    pygame.draw.rect(self.screen, (255, 255, 255), balloon_rect, border_radius=20)
                    pygame.draw.rect(self.screen, (0, 0, 0), balloon_rect, 2, border_radius=20)
                    question = self.font.render(self.question_text, True, (0, 0, 0))
                    self.screen.blit(question, (balloon_rect.x + 20, balloon_rect.y + 20))
                    answer_label = self.font.render("Answer:", True, (0, 0, 0))
                    self.screen.blit(answer_label, (balloon_rect.x + 20, balloon_rect.y + 60))
                    answer_text = self.font.render(self.answer, True, (0, 0, 255))
                    self.screen.blit(answer_text, (balloon_rect.x + 120, balloon_rect.y + 60))
                if self.game_over and self.win_message:
                    self.screen.blit(self.win_message, (220, 260))
            hint = self.font.render("Press Q to quit.", True, (255, 255, 0))
            self.screen.blit(hint, (40, 570))
        pygame.display.flip()

game = GameEngine()
game.run()
pygame.quit()
