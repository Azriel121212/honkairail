import re

with open('rebuild.py', 'r', encoding='utf-8') as f:
    content = f.read()

mission_html = '''
<!-- Daily Missions Modal -->
<div id="mission-modal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.8); z-index:9999; justify-content:center; align-items:center;">
    <div class="glass-panel" style="width:400px; text-align:center;">
        <h2 style="color:var(--accent-blue); margin-bottom:15px;">&#x1F4DD; Misi Harian</h2>
        <div id="mission-list" style="display:flex; flex-direction:column; gap:10px; margin-bottom:20px;">
            <!-- Rendered via JS -->
        </div>
        <button class="hsr-btn" onclick="document.getElementById('mission-modal').style.display='none'">Tutup</button>
    </div>
</div>
'''

if 'id="mission-modal"' not in content:
    content = content.replace('<body>\\n', '<body>\\n' + mission_html)

with open('rebuild.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Mission modal added!")
