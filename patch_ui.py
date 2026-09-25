import re

with open('rebuild.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove btn-auto from jade-display
old_auto_html = '''<div style="display:flex; gap:10px;">
    <button id="btn-speed" class="hsr-btn" onclick="toggleSpeed()" style="padding:5px 10px; font-size:12px;">&#x23E9; 1x</button>
    <button id="btn-auto" class="hsr-btn" onclick="toggleAuto()" style="padding:5px 10px; font-size:12px;">&#x1F916; Auto: OFF</button>
</div>\\n            <div class="jade-badge" id="jade-display">'''
content = content.replace(old_auto_html, '<div class="jade-badge" id="jade-display">')

# Add btn-auto to battle-view header
# <div class="battle-header">
#     <div>Stage <span id="btl-stage-display"></span></div>
#     <div id="btl-turn-order"></div>
# </div>
new_auto_html = '''<div style="display:flex; gap:10px;">
        <button id="btn-speed" class="hsr-btn" onclick="toggleSpeed()" style="padding:5px 10px; font-size:12px;">&#x23E9; 1x</button>
        <button id="btn-auto" class="hsr-btn" onclick="toggleAuto()" style="padding:5px 10px; font-size:12px;">&#x1F916; Auto: OFF</button>
    </div>'''
content = content.replace(
    '<div id="btl-turn-order"></div>',
    f'<div id="btl-turn-order"></div>\\n    {new_auto_html}'
)

with open('rebuild.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("UI fixed")
