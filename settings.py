class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        #Screen settings
        self.screen_wight = 1000
        self.screen_height = 600
        self.bg_color = (0,0,0)
        #Ship settings
        self.ship_speed_factor = 1.5
        #Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = 230, 230, 230
        self.bullets_allowed = 3