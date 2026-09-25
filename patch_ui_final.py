import re

with open('rebuild.py', 'r', encoding='utf-8') as f:
    content = f.read()

new_auto_html = '''
    <div style="display:flex; gap:10px; margin-bottom:10px; justify-content:flex-end; width:100%;">
        <button id="btn-speed" class="hsr-btn" onclick="toggleSpeed()" style="padding:5px 10px; font-size:12px;">&#x23E9; 1x</button>
        <button id="btn-auto" class="hsr-btn" onclick="toggleAuto()" style="padding:5px 10px; font-size:12px;">&#x1F916; Auto: OFF</button>
    </div>
'''

if 'id="btn-auto"' not in content:
    content = content.replace(
        '<div id="action-order-bar"><span id="aob-label">ORDER</span></div>',
        new_auto_html + '\\n        <div id="action-order-bar"><span id="aob-label">ORDER</span></div>'
    )

with open('rebuild.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Auto battle UI really fixed!")
