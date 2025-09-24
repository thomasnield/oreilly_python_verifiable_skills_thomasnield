from enum import Enum  
  
# Implement an enum for ColorTheme  
# that has the values LIGHT, DARK, DRACULA, and HIGH_CONTRAST.  
# Loop through the four values  
# Then set a color_theme variable to DRACULA  
  
class ColorTheme(Enum):  
    LIGHT = 1  
    DARK = 2  
    DRACULA = 3  
    HIGH_CONTRAST = 4  
  
for ct in ColorTheme:  
    print(ct)  
  
color_theme = ColorTheme.DRACULA  
  
print(f"The color theme was set to: {color_theme}")