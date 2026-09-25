import re

with open('rebuild.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix auto battle function call
content = content.replace("useAction(type, targetId);", "playerAction(type);")

# 2. Fix Audio URLs
new_audio_html = '''
<!-- Audio Elements -->
<audio id="bgm-menu" loop preload="auto"><source src="https://actions.google.com/sounds/v1/science_fiction/dark_space.ogg" type="audio/ogg"></audio>
<audio id="bgm-battle" loop preload="auto"><source src="https://actions.google.com/sounds/v1/science_fiction/epic_orchestral_space.ogg" type="audio/ogg"></audio>
<audio id="sfx-hit" preload="auto"><source src="https://actions.google.com/sounds/v1/impacts/crash.ogg" type="audio/ogg"></audio>
<audio id="sfx-ult" preload="auto"><source src="https://actions.google.com/sounds/v1/weapons/laser_gun_fire.ogg" type="audio/ogg"></audio>
<audio id="sfx-win" preload="auto"><source src="https://actions.google.com/sounds/v1/crowds/crowd_cheer.ogg" type="audio/ogg"></audio>
'''

# Find the old audio block and replace
content = re.sub(r'<!-- Audio Elements -->.*?</audio>', new_audio_html.strip(), content, flags=re.DOTALL)

with open('rebuild.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Bugs fixed!")
