import pygame
import sys
import math
import random
# Importing global constants, textures, and custom object classes from external files
from settings import *
from player import BowlingBall
from pin import Pin
from gamedata import TOURNAMENTS, OPPONENTS

class Game:
    def __init__(self):
        """Initializes Pygame, creates the game window, loads fonts, and builds the initial states."""
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Official Canadian 5-Pin Bowling - Tournament Mode")
        self.clock = pygame.time.Clock() # Controls the frame rate (FPS)
        
        # --------------------
        # TYPOGRAPHY & FONTS
        # --------------------
        # Pre-loading multiple font sizes to use across scoreboards, titles, and menus
        self.label_font = pygame.font.SysFont("Arial", 14, bold=True)
        self.mini_font = pygame.font.SysFont("Courier New", 12, bold=True)
        self.score_font = pygame.font.SysFont("Arial", 18, bold=True)
        self.font = pygame.font.SysFont("Courier New", 14, bold=True)
        self.large_font = pygame.font.SysFont("Arial", 22, bold=True)
        self.heading_font = pygame.font.SysFont("Arial", 30, bold=True)
        self.anim_font = pygame.font.SysFont("Impact", 72, bold=True)
        
        # --------------------
        # STATE MACHINE TRACKING
        # --------------------
        # game_state acts as a router directing whether to draw a specific menu or the live alley
        self.game_state = "MENU" 
        self.menu_buttons = []  # Selection grid for ball colors/types
        self.tour_buttons = []  # Selection list for leagues/tours
        self.stop_buttons = []  # Selection grid for regional bowling alleys
        self.prov_buttons = []  # Selection list for player home provinces
        self.opp_buttons = []   # Selection list for chosen AI rival
        
        # --------------------
        # USER CONFIG SEEDING
        # --------------------
        # Empty slots to hold whatever items the player clicks on during the setup phase
        self.selected_ball_profile = None
        self.selected_tour = None
        self.selected_stop = None
        self.selected_province = None
        self.selected_opponent = None

        # Lane aesthetic settings defaults (modified dynamically depending on venue selection)
        self.current_lane_color = LANE_COLOR
        self.current_gutter_color = GUTTER_COLOR

        # --------------------
        # TURN CONTROL & GAME STATE
        # --------------------
        self.current_turn = "PLAYER" # Toggle variable between "PLAYER" and "OPPONENT"
        self.current_frame = 1       # Tracks game progression up to 10 frames
        self.current_ball_attempt = 1 # Track shots 1, 2, or 3 within the active frame

        # --------------------
        # PLAYER DATA MATRIX
        # --------------------
        self.frame_displays = [[] for _ in range(10)]     # Strings drawn inside score box (e.g. ['X', '-'])
        self.frame_types = [""] * 10                       # Categories: "STRIKE", "SPARE", "OPEN"
        self.frame_raw_rolls = [[] for _ in range(10)]     # Base point arrays for roll tracking math
        self.cumulative_scores = [0] * 10                  # Frame running totals after calculating bonuses
        self.total_score = 0

        # --------------------
        # AI DATA MATRIX
        # --------------------
        self.ai_frame_displays = [[] for _ in range(10)]
        self.ai_frame_types = [""] * 10
        self.ai_frame_raw_rolls = [[] for _ in range(10)]
        self.ai_cumulative_scores = [0] * 10
        self.ai_total_score = 0
        
        # Artificial timing clocks to make AI opponents appear to spend time aiming
        self.ai_thinking_timer = 0
        self.ai_has_aimed = False

        self.game_complete = False
        self.pins_group = pygame.sprite.Group() # Sprites container holding the 5 active pins
        
        # Celebration Animation controls
        self.is_animating = False
        self.anim_type = ""        # "STRIKE" or "SPARE"
        self.anim_variant = 0      # Random seed determining look of graphic splash
        self.anim_timer = 0        # Lifespan duration counter of the text banner
        self.particles = []        # Floating shapes container for explosion effects
        
        # Immediately build up positions for our first main screen menu grid
        self.build_menu_grid()

    # ==========================================
    # MENU BUILDERS (Grid & Button Generator Math)
    # ==========================================
    def build_menu_grid(self):
        """Generates coordinate matrices to construct clickable boxes for the Ball Catalog screen."""
        self.menu_buttons = []
        start_y = 120
        for category, items in BALL_CATALOG.items():
            start_y += 35
            row_x = 60
            for item in items:
                rect = pygame.Rect(row_x, start_y, 185, 45)
                self.menu_buttons.append({"rect": rect, "profile": item, "category": category})
                row_x += 205
            start_y += 65

    def build_tournament_menu(self):
        """Generates list coordinates to pick from the available Tournaments."""
        self.tour_buttons = []
        for i, tour in enumerate(TOURNAMENTS):
            rect = pygame.Rect(150, 160 + (i * 80), 500, 55)
            self.tour_buttons.append({"rect": rect, "tour": tour})

    def build_stops_menu(self):
        """Generates split column row layouts to choose a specific bowling alley lane stop."""
        self.stop_buttons = []
        for i, stop in enumerate(self.selected_tour["stops"]):
            col = i % 2
            row = i // 2
            rect = pygame.Rect(60 + (col * 350), 160 + (row * 90), 320, 65)
            self.stop_buttons.append({"rect": rect, "stop": stop})

    def build_province_menu(self):
        """Generates button configurations for selected Canadian provinces."""
        self.prov_buttons = []
        provinces = ["Alberta", "Newfoundland", "Ontario"]
        for i, prov in enumerate(provinces):
            rect = pygame.Rect(250, 180 + (i * 80), 300, 55)
            self.prov_buttons.append({"rect": rect, "province": prov})

    def build_opponents_menu(self):
        """Fetches and displays listed rival profiles grouped inside gamedata under selected province."""
        self.opp_buttons = []
        for i, opp in enumerate(OPPONENTS[self.selected_province]):
            rect = pygame.Rect(200, 150 + (i * 70), 400, 50)
            self.opp_buttons.append({"rect": rect, "opponent": opp})

    # ==========================================
    # GAME CONTROL INCEPTION
    # ==========================================
    def assign_alley_theme(self):
        """Modifies colors depending on venue descriptions to match wood patterns or cosmic lanes."""
        center_name = self.selected_stop["center"].lower()
        if "panorama" in center_name:
            self.current_lane_color = (210, 160, 110) 
            self.current_gutter_color = (40, 30, 25)
        elif "paradise" in center_name:
            self.current_lane_color = (245, 220, 180) 
            self.current_gutter_color = (20, 45, 30)  
        elif "sherwood" in center_name:
            self.current_lane_color = (230, 190, 140) 
            self.current_gutter_color = (60, 20, 20)  
        elif "neb" in center_name:
            self.current_lane_color = (190, 180, 210) 
            self.current_gutter_color = (15, 10, 30)   
        elif "echo" in center_name or "midtown" in center_name:
            self.current_lane_color = (222, 184, 135) 
            self.current_gutter_color = (40, 40, 40)
        elif "plaza" in center_name or "holiday" in center_name:
            self.current_lane_color = (175, 210, 230) 
            self.current_gutter_color = (10, 25, 40)
        else:
            self.current_lane_color = (240, 205, 160) 
            self.current_gutter_color = (35, 35, 35)

    def start_game(self):
        """Spawns user ball profile configurations, sets the pins, and flips state machine to live play."""
        self.ball = BowlingBall(self.selected_ball_profile)
        self.assign_alley_theme()
        self.setup_5_pins()
        self.game_state = "PLAYING"

    def setup_5_pins(self):
        """Resets pin array layout back to the standard V-shape for Canadian 5-Pin bowling."""
        self.pins_group.empty()
        # Custom coordinates array defining standard placement configurations
        positions = [(370, 145), (410, 175), (450, 205), (490, 175), (530, 145)]
        for i, pos in enumerate(positions):
            # Creates each Pin with assigned score value maps (Canadian scoring: 2, 3, 5, 3, 2 points)
            pin = Pin(pos[0], pos[1], PIN_VALUES[i], i)
            self.pins_group.add(pin)

    # ==========================================
    # PHYSICS & COLLISION CALCULATIONS
    # ==========================================
    def process_physics_collisions(self):
        """Handles 2D physics interaction math including ball-to-pin hits and chain-reaction pin-to-pin scatter."""
        # 1. Ball vs Pin Collisions
        for pin in self.pins_group:
            dx = pin.x - self.ball.x
            dy = pin.y - self.ball.y
            distance = math.hypot(dx, dy) # Finds straight line distance between centers
            min_dist = BALL_RADIUS + PIN_RADIUS
            
            if distance < min_dist and self.ball.state == 'launched':
                pin.is_down = True
                angle = math.atan2(dy, dx)
                ball_speed = math.hypot(self.ball.vx, self.ball.vy)
                push_force = max(ball_speed * 0.85, 3.0) 
                
                # Transfer momentum from ball velocity into pin vectors
                pin.vx = push_force * math.cos(angle)
                pin.vy = push_force * math.sin(angle)
                # Ball slows down slightly upon striking obstacles
                self.ball.vx *= 0.65
                self.ball.vy *= 0.65

        # 2. Pin vs Pin Collisions (Chain reactions)
        pins_list = self.pins_group.sprites()
        for i in range(len(pins_list)):
            for j in range(i + 1, len(pins_list)):
                p1 = pins_list[i]
                p2 = pins_list[j]
                dx = p2.x - p1.x
                dy = p2.y - p1.y
                distance = math.hypot(dx, dy)
                min_dist = PIN_RADIUS * 2
                
                if distance < min_dist:
                    # If any moving pin slides into a standing pin, knock it over too
                    p1.is_down = True
                    p2.is_down = True
                    angle = math.atan2(dy, dx)
                    # Merge their velocities together and spray outward
                    combined_v = max(math.hypot(p1.vx, p1.vy) + math.hypot(p2.vx, p2.vy), 2.5)
                    p2.vx = combined_v * 0.5 * math.cos(angle)
                    p2.vy = combined_v * 0.5 * math.sin(angle)
                    p1.vx = -combined_v * 0.5 * math.cos(angle)
                    p1.vy = -combined_v * 0.5 * math.sin(angle)

    # ==========================================
    # VISUAL ANIMATIONS ENGINE
    # ==========================================
    def trigger_celebration(self, style):
        """Initializes state configurations to interrupt core layout and paint special screen overlays."""
        self.is_animating = True
        self.anim_type = style
        self.anim_variant = random.randint(0, 4)
        self.anim_timer = 0
        self.particles = []
        
        # Build particle tracking dictionaries to create a colorful screen burst effect
        if self.anim_variant in [0, 2]: 
            for _ in range(60):
                self.particles.append({
                    'x': WIDTH // 2, 'y': HEIGHT // 2 + 50,
                    'vx': random.uniform(-7, 7), 'vy': random.uniform(-7, 7),
                    'color': random.choice([GOLD, RED, BLUE, WHITE, (0, 255, 0)]),
                    'radius': random.randint(3, 8)
                })

    # ==========================================
    # ARTIFICIAL INTELLIGENCE LOGIC METRICS
    # ==========================================
    def handle_ai_throwing_logic(self):
        """Simulates 3-second thought delay loop. Applies variable accuracy variations based on AI stats."""
        if self.ball.state == 'ready':
            self.ai_thinking_timer += 1
            
            # Phase 1: Setup trajectory guidelines midway through thinking loop (after 1 second)
            if not self.ai_has_aimed and self.ai_thinking_timer > 60:
                skill = self.selected_opponent["skill"]
                
                # Math offset variables. Low skill level introduces large random targeting angle adjustments
                accuracy_spread = (1.0 - skill) * 45
                target_offset = random.uniform(-15 - accuracy_spread, 15 + accuracy_spread)
                
                # Randomize ball starting horizontal positioning
                self.ball.x = WIDTH // 2 + random.randint(-40, 40)
                dest_x = (WIDTH // 2) + target_offset
                dest_y = 205
                
                # Calculate trigonometric trajectory values to guide path targets
                angle = math.atan2(dest_y - self.ball.y, dest_x - self.ball.x)
                self.ball.angle = math.degrees(angle)
                self.ball.power = random.uniform(11, 16)
                self.ai_has_aimed = True
                
            # Phase 2: Fire exactly at the 3-second mark (180 frames at 60 frames per second)
            if self.ai_has_aimed and self.ai_thinking_timer >= 180:
                rad = math.radians(self.ball.angle)
                # Convert power and angle measurements into vector components
                self.ball.vx = self.ball.power * math.cos(rad)
                self.ball.vy = self.ball.power * math.sin(rad)
                self.ball.state = 'launched'
                self.ai_thinking_timer = 0
                self.ai_has_aimed = False

    # ==========================================
    # ADVANCE TURN: THE CORE LOGIC CONTROLLER
    # ==========================================
    def advance_turn(self):
        """Processes pin fall configurations, appends scorecard displays, handles 10th frame rules, and updates turn indicators."""
        knocked_this_shot = 0
        f_idx = self.current_frame - 1
        
        # 1. Map status of pins BEFORE resetting simulation coordinates
        standing_map = [0] * 5
        for pin in self.pins_group.sprites():
            if pin.pin_id in range(5):
                # Pin counts as up only if not knocked down or thrown out of screen boundaries
                if not (pin.is_down or pin.y < 40 or pin.x < 240 or pin.x > 660):
                    standing_map[pin.pin_id] = 1

        # 2. Accumulate points value mappings from knocked over pins, then kill them from active simulation
        for pin in list(self.pins_group):
            if pin.is_down or pin.y < 40 or pin.x < 240 or pin.x > 660:
                knocked_this_shot += pin.value
                pin.kill()

        shot_symbol = str(knocked_this_shot) if knocked_this_shot > 0 else "-"
        frame_cleared = (len(self.pins_group) == 0)

        # ----------------------------------------------------------------------
        # PLAYER REGISTRATION REGION
        # ----------------------------------------------------------------------
        if self.current_turn == "PLAYER":
            if self.current_ball_attempt == 1:
                if frame_cleared:
                    shot_symbol = "X" # STRIKE achieved
                    if not (self.current_frame == 10 and len(self.frame_raw_rolls[9]) >= 1):
                        self.frame_types[f_idx] = "STRIKE"
                    self.trigger_celebration("STRIKE")
                
                # --- CANADIAN 5-PIN SYSTEM SHORT-HAND TRADITIONS ---
                # Check specific arrangements of remaining standing pin configurations
                elif standing_map == [1, 0, 0, 0, 0]: shot_symbol = "L"  # Left Corner Pin up
                elif standing_map == [0, 0, 0, 0, 1]: shot_symbol = "R"  # Right Corner Pin up
                elif standing_map == [1, 1, 0, 0, 0]: shot_symbol = "C"  # Left Chopoff configurations
                elif standing_map == [0, 0, 0, 1, 1]: shot_symbol = "C"  # Right Chopoff configurations
                elif standing_map == [1, 1, 0, 1, 1]: shot_symbol = "H"  # Headpin left standing completely alone
                elif standing_map == [1, 0, 0, 0, 1]: shot_symbol = "A"  # Aces (only outer corner pins left up)
            
            elif self.current_ball_attempt == 2 and frame_cleared and self.frame_types[f_idx] != "STRIKE":
                shot_symbol = "/" # SPARE achieved on second shot
                self.frame_types[f_idx] = "SPARE"
                self.trigger_celebration("SPARE")

            self.frame_displays[f_idx].append(shot_symbol)
            self.frame_raw_rolls[f_idx].append(knocked_this_shot)

            # Special 10th Frame Progression Regulations
            is_tenth = (self.current_frame == 10)
            if is_tenth:
                if frame_cleared: self.setup_5_pins() # Grant reset pins to award extra strikes
                if self.current_ball_attempt == 3:
                    self.recalculate_scores()
                    self.current_turn = "OPPONENT"
                    self.current_ball_attempt = 1
                    self.ai_thinking_timer = 0  
                    self.setup_5_pins()
                    self.ball.reset()
                    self.ball.state = 'ready'
                else:
                    self.current_ball_attempt += 1
                    self.ball.reset()
            else:
                # Normal frames 1-9 progression rules
                if frame_cleared or self.current_ball_attempt == 3:
                    if frame_cleared and self.current_ball_attempt == 1: self.frame_types[f_idx] = "STRIKE"
                    elif frame_cleared and self.current_ball_attempt == 2: self.frame_types[f_idx] = "SPARE"
                    else: self.frame_types[f_idx] = "OPEN"
                    
                    self.recalculate_scores()
                    self.current_turn = "OPPONENT" # Shift turn over to AI
                    self.current_ball_attempt = 1
                    self.ai_thinking_timer = 0  
                    self.setup_5_pins()
                    self.ball.reset()
                    self.ball.state = 'ready'
                else:
                    self.current_ball_attempt += 1
                    self.ball.reset()

        # ----------------------------------------------------------------------
        # AI OPPONENT REGISTRATION REGION (Identical mechanics mirroring above logic)
        # ----------------------------------------------------------------------
        else:
            if self.current_ball_attempt == 1:
                if frame_cleared:
                    shot_symbol = "X"
                    if not (self.current_frame == 10 and len(self.ai_frame_raw_rolls[9]) >= 1):
                        self.ai_frame_types[f_idx] = "STRIKE"
                    self.trigger_celebration("STRIKE")
                elif standing_map == [1, 0, 0, 0, 0]: shot_symbol = "L"
                elif standing_map == [0, 0, 0, 0, 1]: shot_symbol = "R"
                elif standing_map == [1, 1, 0, 0, 0]: shot_symbol = "C"
                elif standing_map == [0, 0, 0, 1, 1]: shot_symbol = "C"
                elif standing_map == [1, 1, 0, 1, 1]: shot_symbol = "H"
                elif standing_map == [1, 0, 0, 0, 1]: shot_symbol = "A"
            elif self.current_ball_attempt == 2 and frame_cleared and self.ai_frame_types[f_idx] != "STRIKE":
                shot_symbol = "/"
                self.ai_frame_types[f_idx] = "SPARE"
                self.trigger_celebration("SPARE")

            self.ai_frame_displays[f_idx].append(shot_symbol)
            self.ai_frame_raw_rolls[f_idx].append(knocked_this_shot)

            is_tenth = (self.current_frame == 10)
            if is_tenth:
                if frame_cleared: self.setup_5_pins()
                if self.current_ball_attempt == 3:
                    self.recalculate_scores()
                    self.game_complete = True # Closes match at bottom of 10th frame
                else:
                    self.current_ball_attempt += 1
                    self.ai_thinking_timer = 0  
                    self.ball.reset()
                    self.ball.state = 'ready'
            else:
                if frame_cleared or self.current_ball_attempt == 3:
                    if frame_cleared and self.current_ball_attempt == 1: self.ai_frame_types[f_idx] = "STRIKE"
                    elif frame_cleared and self.current_ball_attempt == 2: self.ai_frame_types[f_idx] = "SPARE"
                    else: self.ai_frame_types[f_idx] = "OPEN"
                    
                    self.recalculate_scores()
                    if self.current_frame < 10:
                        self.current_frame += 1 # Advance frame iteration count up
                    self.current_turn = "PLAYER" # Hand turn back to user
                    self.current_ball_attempt = 1
                    self.setup_5_pins()
                    self.ball.reset()
                else:
                    self.current_ball_attempt += 1
                    self.ai_thinking_timer = 0  
                    self.ball.reset()
                    self.ball.state = 'ready'

    # ==========================================
    # MATHEMATICAL SCORECARD RECALCULATOR
    # ==========================================
    def recalculate_scores(self):
        """Runs Canadian 5-Pin bowling algorithms. Max value per pin configuration differs from standard 10-pin."""
        # --- PLAYER MATH ENGINE ---
        p_total = 0
        for f in range(10):
            if len(self.frame_raw_rolls[f]) == 0: break
            base = sum(self.frame_raw_rolls[f])
            if f == 9: # 10th Frame simple addition loop without looking forward
                p_total += base
                self.cumulative_scores[f] = p_total
                continue
            # Strike lookup math loops to harvest base values of the next 2 shots rolled
            if self.frame_types[f] == "STRIKE":
                b, r_found, next_f = 0, 0, f + 1
                while r_found < 2 and next_f < 10:
                    for r in self.frame_raw_rolls[next_f]:
                        b += r
                        r_found += 1
                        if r_found == 2: break
                    next_f += 1
                p_total += 15 + b # Canadian Strike is 15 points flat base + bonuses
            # Spare lookup loops forward to add the single next rolled shot value
            elif self.frame_types[f] == "SPARE":
                b = self.frame_raw_rolls[f+1][0] if f + 1 < 10 and len(self.frame_raw_rolls[f+1]) > 0 else 0
                p_total += 15 + b # Canadian Spare is 15 points flat base + bonus
            else:
                p_total += base
            self.cumulative_scores[f] = p_total
        self.total_score = p_total

        # --- AI MATH ENGINE (Mirrors Player math loop) ---
        ai_total = 0
        for f in range(10):
            if len(self.ai_frame_raw_rolls[f]) == 0: break
            base = sum(self.ai_frame_raw_rolls[f])
            if f == 9:
                ai_total += base
                self.ai_cumulative_scores[f] = ai_total
                continue
            if self.ai_frame_types[f] == "STRIKE":
                b, r_found, next_f = 0, 0, f + 1
                while r_found < 2 and next_f < 10:
                    for r in self.ai_frame_raw_rolls[next_f]:
                        b += r
                        r_found += 1
                        if r_found == 2: break
                    next_f += 1
                ai_total += 15 + b
            elif self.ai_frame_types[f] == "SPARE":
                b = self.ai_frame_raw_rolls[f+1][0] if f + 1 < 10 and len(self.ai_frame_raw_rolls[f+1]) > 0 else 0
                ai_total += 15 + b
            else:
                ai_total += base
            self.ai_cumulative_scores[f] = ai_total
        self.ai_total_score = ai_total

    # ==========================================
    # CORE APPLICATION LIFE LOOPS
    # ==========================================
    def run(self):
        """Infinite loop driving game ticks, checking user input inputs, and drawing updates."""
        while True:
            self.handle_events() # Catch mouse/keyboard actions
            if self.game_state == "PLAYING" and not self.game_complete and not self.is_animating:
                if self.current_turn == "OPPONENT":
                    self.handle_ai_throwing_logic()
                self.update() # Process positioning vectors
            self.draw() # Paint graphical items to surface
            self.clock.tick(FPS) # Maintain locked frame speed threshold

    def handle_events(self):
        """Intercepts hardware clicks and maps coordinates into structural selection menus."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            pos = pygame.mouse.get_pos() if event.type == pygame.MOUSEBUTTONDOWN else (0,0)
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Flow chart logic router passing parameters depending on state selection screens
                if self.game_state == "MENU":
                    for btn in self.menu_buttons:
                        if btn["rect"].collidepoint(pos):
                            self.selected_ball_profile = btn["profile"]
                            self.build_tournament_menu()
                            self.game_state = "CHOOSE_TOUR"
                            break
                elif self.game_state == "CHOOSE_TOUR":
                    for btn in self.tour_buttons:
                        if btn["rect"].collidepoint(pos):
                            self.selected_tour = btn["tour"]
                            self.build_stops_menu()
                            self.game_state = "CHOOSE_STOP"
                            break
                elif self.game_state == "CHOOSE_STOP":
                    for btn in self.stop_buttons:
                        if btn["rect"].collidepoint(pos):
                            self.selected_stop = btn["stop"]
                            self.build_province_menu()
                            self.game_state = "CHOOSE_PROVINCE"
                            break
                elif self.game_state == "CHOOSE_PROVINCE":
                    for btn in self.prov_buttons:
                        if btn["rect"].collidepoint(pos):
                            self.selected_province = btn["province"]
                            self.build_opponents_menu()
                            self.game_state = "CHOOSE_OPPONENT"
                            break
                elif self.game_state == "CHOOSE_OPPONENT":
                    for btn in self.opp_buttons:
                        if btn["rect"].collidepoint(pos):
                            self.selected_opponent = btn["opponent"]
                            self.start_game() # Configuration data locked. Launch game.
                            break
            else:
                # Feed controls to physics classes directly if match is running active operations
                if self.game_state == "PLAYING" and self.current_turn == "PLAYER" and not self.game_complete and not self.is_animating:
                    self.ball.handle_input(event)
                # Restart logic catching
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r and self.game_complete:
                    self.__init__() # Wipe current variables clean and reload boot loops

    def update(self):
        """Moves sprites across the window according to momentum components."""
        self.ball.update()
        self.pins_group.update()
        self.process_physics_collisions()
        # If ball completes roll sequence and rolls past gutter limits, wait briefly, then advance turn
        if self.ball.state == 'done':
            pygame.time.delay(300)
            self.advance_turn()

    def handle_animations(self):
        """Animates moving explosion shapes and prints massive overlay headers across screen center fields."""
        self.anim_timer += 1
        text_str = "STRIKE!" if self.anim_type == "STRIKE" else "SPARE!"
        base_color = GOLD if self.anim_type == "STRIKE" else BLUE

        if self.anim_variant in [0, 2]:
            for p in self.particles:
                p['x'] += p['vx']
                p['y'] += p['vy']
                pygame.draw.circle(self.screen, p['color'], (int(p['x']), int(p['y'])), p['radius'])
        txt_surface = self.anim_font.render(text_str, True, base_color)
        self.screen.blit(txt_surface, (WIDTH // 2 - txt_surface.get_width() // 2, HEIGHT // 2))

        if self.anim_timer >= 90: # Keep animation visible for exactly 90 frames (1.5 seconds)
            self.is_animating = False
            self.recalculate_scores()

    # ==========================================
    # RENDERING & DRAWING PROCEDURES
    # ==========================================
    def draw_tour_menus(self):
        """Draws layout selections for tours, stops, provinces, and AI configurations depending on states."""
        self.screen.fill((20, 25, 35))
        mouse_pos = pygame.mouse.get_pos()

        if self.game_state == "CHOOSE_TOUR":
            title = self.heading_font.render("SELECT BOWLING TOUR", True, GOLD)
            self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 40))
            for btn in self.tour_buttons:
                bg = (45, 65, 90) if btn["rect"].collidepoint(mouse_pos) else (30, 40, 55)
                pygame.draw.rect(self.screen, bg, btn["rect"], 0, 8)
                pygame.draw.rect(self.screen, GOLD, btn["rect"], 2, 8)
                txt = self.large_font.render(btn["tour"]["tour_name"], True, WHITE)
                self.screen.blit(txt, (btn["rect"].x + 20, btn["rect"].y + 14))

        elif self.game_state == "CHOOSE_STOP":
            title = self.heading_font.render(f"SELECT TOURNAMENT ALLEY STOP", True, GOLD)
            self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 30))
            for btn in self.stop_buttons:
                bg = (45, 65, 90) if btn["rect"].collidepoint(mouse_pos) else (30, 40, 55)
                pygame.draw.rect(self.screen, bg, btn["rect"], 0, 6)
                pygame.draw.rect(self.screen, WHITE, btn["rect"], 2, 6)
                
                st_txt = self.font.render(f"Stop {btn['stop']['stop']}: {btn['stop']['name']}", True, GOLD)
                cl_txt = self.font.render(f"{btn['stop']['center']}", True, WHITE)
                loc_txt = self.font.render(f"Loc: {btn['stop']['city']}", True, GREY)
                
                self.screen.blit(st_txt, (btn["rect"].x + 12, btn["rect"].y + 6))
                self.screen.blit(cl_txt, (btn["rect"].x + 12, btn["rect"].y + 24))
                self.screen.blit(loc_txt, (btn["rect"].x + 12, btn["rect"].y + 42))

        elif self.game_state == "CHOOSE_PROVINCE":
            title = self.heading_font.render("CHOOSE OPPONENT'S PROVINCE", True, GOLD)
            self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 40))
            for btn in self.prov_buttons:
                bg = (45, 65, 90) if btn["rect"].collidepoint(mouse_pos) else (30, 40, 55)
                pygame.draw.rect(self.screen, bg, btn["rect"], 0, 6)
                pygame.draw.rect(self.screen, GOLD, btn["rect"], 2, 6)
                txt = self.large_font.render(btn["province"], True, WHITE)
                self.screen.blit(txt, (btn["rect"].x + 20, btn["rect"].y + 14))

        elif self.game_state == "CHOOSE_OPPONENT":
            title = self.heading_font.render(f"CHOOSE {self.selected_province.upper()} RIVAL", True, GOLD)
            self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 40))
            for btn in self.opp_buttons:
                bg = (45, 65, 90) if btn["rect"].collidepoint(mouse_pos) else (30, 40, 55)
                pygame.draw.rect(self.screen, bg, btn["rect"], 0, 6)
                pygame.draw.rect(self.screen, RED, btn["rect"], 2, 6)
                
                name_txt = self.large_font.render(btn["opponent"]["name"], True, WHITE)
                stat_txt = self.font.render(f"Avg: {btn['opponent']['avg']}", True, GOLD)
                
                self.screen.blit(name_txt, (btn["rect"].x + 20, btn["rect"].y + 12))
                self.screen.blit(stat_txt, (btn["rect"].x + 240, btn["rect"].y + 16))

    def draw_scorecard(self):
        """Paints structural scorecard boxes across top margins of the game display window."""
        pygame.draw.rect(self.screen, (14, 18, 24), (0, 0, WIDTH, 85))
        pygame.draw.line(self.screen, GOLD, (0, 84), (WIDTH, 84), 1)

        self.screen.blit(self.label_font.render("YOU", True, WHITE), (6, 14))
        self.screen.blit(self.label_font.render("OPP", True, RED), (6, 52))

        box_w = 64
        box_h = 36
        start_x = 42

        # Grid generation loop layout across frames 1 to 10
        for i in range(10):
            x = start_x + (i * box_w)
            
            # --- ROW 1: USER GRID LAYOUTS ---
            pygame.draw.rect(self.screen, (50, 70, 95), (x, 4, box_w, box_h), 1)
            self.screen.blit(self.mini_font.render(f"F{i+1}", True, GREY), (x + 4, 6))
            
            shot_str = "".join(self.frame_displays[i])
            self.screen.blit(self.score_font.render(shot_str, True, GOLD), (x + 32, 5))
            
            if len(self.frame_raw_rolls[i]) > 0:
                self.screen.blit(self.score_font.render(str(self.cumulative_scores[i]), True, WHITE), (x + 6, 20))

            # --- ROW 2: AI GRID LAYOUTS ---
            pygame.draw.rect(self.screen, (90, 50, 50), (x, 44, box_w, box_h), 1)
            
            ai_shot_str = "".join(self.ai_frame_displays[i])
            self.screen.blit(self.score_font.render(ai_shot_str, True, GOLD), (x + 32, 45))
            
            if len(self.ai_frame_raw_rolls[i]) > 0:
                self.screen.blit(self.score_font.render(str(self.ai_cumulative_scores[i]), True, RED), (x + 6, 60))

        # Render meta tracking data strings on far right side margins of scoreboard banner
        meta_x = start_x + (10 * box_w) + 12
        venue_lbl = self.mini_font.render(f"ALLEY: {self.selected_stop['center'][:14]}", True, GREY)
        opp_lbl = self.label_font.render(f"VS: {self.selected_opponent['name']}", True, RED)
        
        if self.current_turn == "PLAYER":
            turn_txt, turn_color = "YOUR TURN", GOLD
        else:
            # Converts timer loops into float representations of seconds remaining for AI
            rem_sec = max(0.0, (180 - self.ai_thinking_timer) / 60.0)
            turn_txt, turn_color = f"OPP SHOT ({rem_sec:.1f}s)", RED
            
        status_lbl = self.label_font.render(turn_txt, True, turn_color)

        self.screen.blit(venue_lbl, (meta_x, 8))
        self.screen.blit(opp_lbl, (meta_x, 32))
        self.screen.blit(status_lbl, (meta_x, 56))

    def draw(self):
        """Master window rendering workflow router."""
        if self.game_state == "MENU":
            # Draw primary opening menu configuration selections
            self.screen.fill((25, 35, 45))
            title = self.large_font.render("CHOOSE YOUR 5-PIN BOWLING BALL", True, GOLD)
            self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 35))
            current_cat = ""
            for btn in self.menu_buttons:
                if btn["category"] != current_cat:
                    current_cat = btn["category"]
                    self.screen.blit(self.large_font.render(current_cat.upper(), True, WHITE), (60, btn["rect"].y - 38))
                bg_color = (40, 60, 80) if btn["rect"].collidepoint(pygame.mouse.get_pos()) else (50, 50, 50)
                pygame.draw.rect(self.screen, bg_color, btn["rect"], 0, 6)
                pygame.draw.rect(self.screen, GOLD, btn["rect"], 2, 6)
                pygame.draw.circle(self.screen, btn["profile"]["color"], (btn["rect"].x + 22, btn["rect"].y + 22), 11)
                self.screen.blit(self.font.render(btn["profile"]["name"], True, WHITE), (btn["rect"].x + 42, btn["rect"].y + 14))
        
        elif self.game_state in ["CHOOSE_TOUR", "CHOOSE_STOP", "CHOOSE_PROVINCE", "CHOOSE_OPPONENT"]:
            self.draw_tour_menus()
            
        else:
            # Draw live active match elements (the actual alley, lane markers, ball, and pins)
            self.screen.fill(self.current_gutter_color)
            pygame.draw.rect(self.screen, self.current_lane_color, (250, 0, 400, HEIGHT))
            # Foul line marker
            pygame.draw.line(self.screen, RED, (250, HEIGHT - 120), (650, HEIGHT - 120), 4)
            # Arrow triangles drawn on lane boards
            for ax in [330, 390, 450, 510, 570]:
                pygame.draw.polygon(self.screen, BLACK, [(ax, 480), (ax - 6, 495), (ax + 6, 495)])
            
            self.pins_group.draw(self.screen)
            if self.ball.state != 'done' and not self.is_animating:
                self.screen.blit(self.ball.image, self.ball.rect)
            if not self.is_animating:
                self.ball.draw_overlays(self.screen) # Aiming arrows/guidelines
            else:
                self.handle_animations()
            
            self.draw_scorecard()
            
            # Displays bottom header labels or alternative endgame screens
            if not self.game_complete:
                info_txt = self.font.render(f"FRAME: {self.current_frame}  BALL: {self.current_ball_attempt}/3", True, WHITE)
                self.screen.blit(info_txt, (20, HEIGHT - 35))
            else:
                # Decide match outcome messaging string rules
                w_str = "YOU WIN!" if self.total_score > self.ai_total_score else "OPPONENT WINS!"
                if self.total_score == self.ai_total_score: w_str = "TIE MATCH!"
                over_txt = self.heading_font.render(f"MATCH OVER: {w_str}", True, GOLD)
                sub_txt = self.font.render(f"You: {self.total_score} | {self.selected_opponent['name']}: {self.ai_total_score}. Press 'R' to restart", True, WHITE)
                self.screen.blit(over_txt, (WIDTH // 2 - 200, HEIGHT // 2 - 20))
                self.screen.blit(sub_txt, (WIDTH // 2 - 240, HEIGHT // 2 + 30))
                
        pygame.display.flip() # Swap screen surface layouts to push updates to display hardware

# Application entry anchor
if __name__ == "__main__":
    game = Game()
    game.run()