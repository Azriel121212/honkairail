import re
import os

OUT = 'rebuild.py'

with open(OUT, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. State updates for Auto Battle, Speed, and Daily Missions
content = content.replace(
    'playerName: "",',
    'playerName: "", autoBattle: false, battleSpeed: 1, dailyMissions: { date: new Date().toLocaleDateString(), progress: { playCasual:0, useUlt:0, winBattle:0 }, claimed: [] }, '
)

content = content.replace(
    'highestCasualStage: state.highestCasualStage, playerName: state.playerName,',
    'highestCasualStage: state.highestCasualStage, playerName: state.playerName, dailyMissions: state.dailyMissions,'
)

content = content.replace(
    'state.playerName = d.playerName || state.playerName;',
    '''state.playerName = d.playerName || state.playerName;
        if (d.dailyMissions && d.dailyMissions.date === new Date().toLocaleDateString()) {
            state.dailyMissions = d.dailyMissions;
        } else {
            state.dailyMissions = { date: new Date().toLocaleDateString(), progress: { playCasual:0, useUlt:0, winBattle:0 }, claimed: [] };
        }'''
)

# 2. Audio HTML & JS
audio_html = '''
<!-- Audio Elements -->
<audio id="bgm-menu" loop preload="auto"><source src="https://cdn.pixabay.com/download/audio/2022/03/15/audio_73e721b0bc.mp3" type="audio/mpeg"></audio>
<audio id="bgm-battle" loop preload="auto"><source src="https://cdn.pixabay.com/download/audio/2022/01/18/audio_821db9a288.mp3" type="audio/mpeg"></audio>
<audio id="sfx-hit" preload="auto"><source src="https://cdn.pixabay.com/download/audio/2022/03/15/audio_1067d5ce39.mp3" type="audio/mpeg"></audio>
<audio id="sfx-ult" preload="auto"><source src="https://cdn.pixabay.com/download/audio/2022/03/10/audio_c8c8a73467.mp3" type="audio/mpeg"></audio>
<audio id="sfx-win" preload="auto"><source src="https://cdn.pixabay.com/download/audio/2021/08/04/audio_0625c1539c.mp3" type="audio/mpeg"></audio>
'''
content = content.replace('<body>', f'<body>\\n{audio_html}')

audio_js = '''
window.playBGM = (type) => {
    document.getElementById('bgm-menu').pause();
    document.getElementById('bgm-battle').pause();
    if(type === 'menu') document.getElementById('bgm-menu').play().catch(e=>console.log(e));
    if(type === 'battle') document.getElementById('bgm-battle').play().catch(e=>console.log(e));
};
window.playSFX = (type) => {
    let a;
    if(type === 'hit') a = document.getElementById('sfx-hit');
    if(type === 'ult') a = document.getElementById('sfx-ult');
    if(type === 'win') a = document.getElementById('sfx-win');
    if(a) { a.currentTime = 0; a.play().catch(e=>console.log(e)); }
};
'''
content = content.replace('window.navigateTo = (v) => {', audio_js + '\\nwindow.navigateTo = (v) => {')

content = content.replace('navigateTo(\'main-menu-view\');', 'playBGM(\'menu\'); navigateTo(\'main-menu-view\');')
content = content.replace('navigateTo(\'casual-view\');', 'playBGM(\'menu\'); navigateTo(\'casual-view\');')
# Ensure battle bgm starts
content = content.replace('window.startBattle = async function startBattle(prebuiltEnemies) {', 'window.startBattle = async function startBattle(prebuiltEnemies) {\\n    playBGM(\'battle\');')


# 3. Sleep function modifier
content = content.replace(
    'function sleep(ms) { return new Promise(r=>setTimeout(r,ms)); }',
    'function sleep(ms) { return new Promise(r=>setTimeout(r,ms / (state.battleSpeed || 1))); }'
)

# 4. Auto-Battle UI and Toggle Logic
auto_btn_html = '''<div style="display:flex; gap:10px;">
    <button id="btn-speed" class="hsr-btn" onclick="toggleSpeed()" style="padding:5px 10px; font-size:12px;">&#x23E9; 1x</button>
    <button id="btn-auto" class="hsr-btn" onclick="toggleAuto()" style="padding:5px 10px; font-size:12px;">&#x1F916; Auto: OFF</button>
</div>'''
content = content.replace('<div class="jade-badge" id="jade-display">', f'{auto_btn_html}\\n            <div class="jade-badge" id="jade-display">')

auto_js = '''
window.toggleSpeed = () => {
    state.battleSpeed = state.battleSpeed === 1 ? 2 : 1;
    document.getElementById('btn-speed').innerHTML = `&#x23E9; ${state.battleSpeed}x`;
};
window.toggleAuto = () => {
    state.autoBattle = !state.autoBattle;
    document.getElementById('btn-auto').innerHTML = state.autoBattle ? `&#x1F916; Auto: ON` : `&#x1F916; Auto: OFF`;
    document.getElementById('btn-auto').style.background = state.autoBattle ? 'rgba(59,130,246,0.5)' : '';
};
'''
content = content.replace('window.navigateTo = (v) => {', auto_js + '\\nwindow.navigateTo = (v) => {')

# 5. Injecting Auto-Battle Logic into advanceTurn
# We need to find `function advanceTurn() {` and modify the block where it waits for user input if `!current.isEnemy`.
# We'll replace the return with an auto-battle trigger if auto is true.
# Let's search for the `// Tunggu input player` block
auto_logic = '''
    if (!current.isEnemy) {
        if (state.autoBattle) {
            setTimeout(async () => {
                // Check if any party member has full energy to cast ult
                for (let p of state.party) {
                    if (p.hp > 0 && p.energy >= 100) {
                        await processUlt(p.id);
                        if (state.enemies.every(e => e.hp <= 0)) return; // end battle
                    }
                }
                
                // Pick target
                let targetId = state.enemies.find(e => e.hp > 0)?.id;
                if (targetId) {
                    // Decide skill or basic
                    let type = (state.sp >= 1 && Math.random() > 0.3) ? 'skill' : 'basic';
                    useAction(type, targetId);
                }
            }, 800 / (state.battleSpeed || 1));
            return;
        }
        return; // Tunggu input player
    }
'''
content = content.replace('return; // Tunggu input player', auto_logic)


with open(OUT, 'w', encoding='utf-8') as f:
    f.write(content)
print("Features 1 and 2 patched successfully!")
