import re

OUT = 'rebuild.py'

with open(OUT, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add playSFX to animateAttack, processUlt, and endGame
content = content.replace(
    'async function animateAttack(attackerId, targetId, isEnemy) {',
    'async function animateAttack(attackerId, targetId, isEnemy) {\n    playSFX("hit");'
)

content = content.replace(
    'async function processUlt(charId) {',
    'async function processUlt(charId) {\n    playSFX("ult");\n    if(state.dailyMissions) state.dailyMissions.progress.useUlt++;'
)

content = content.replace(
    'async function endGame(isWin) {',
    'async function endGame(isWin) {\n    if(isWin) playSFX("win");'
)

# Also increment daily missions for casual mode battles
content = content.replace(
    'if (isWin && state.gameMode===\'casual\') {',
    'if (isWin && state.gameMode===\'casual\') {\n        if(state.dailyMissions) state.dailyMissions.progress.playCasual++;'
)
content = content.replace(
    'if (isWin) {',
    'if (isWin) {\n        if(state.dailyMissions) state.dailyMissions.progress.winBattle++;'
)

# 2. Daily Missions UI
mission_html = '''
<!-- Daily Missions Modal -->
<div id="mission-modal" class="modal-bg">
    <div class="modal-content glass-panel" style="max-width:500px; text-align:center;">
        <h2 style="color:var(--accent-blue); margin-bottom:15px;">&#x1F4DD; Misi Harian</h2>
        <div id="mission-list" style="display:flex; flex-direction:column; gap:10px; margin-bottom:20px;">
            <!-- Rendered via JS -->
        </div>
        <button class="hsr-btn" onclick="document.getElementById('mission-modal').style.display='none'">Tutup</button>
    </div>
</div>
'''
content = content.replace('<!-- SU Buff Modal -->', mission_html + '\\n<!-- SU Buff Modal -->')

mission_btn_html = '''<button class="hsr-btn blue" onclick="openMissions()" style="margin-left:10px;">&#x1F4DD; Misi Harian</button>'''
content = content.replace('<button class="hsr-btn" onclick="signOut(auth)"', mission_btn_html + '\\n<button class="hsr-btn" onclick="signOut(auth)"')

mission_js = '''
const MISSION_DATA = [
    { id:'playCasual', title:'Main Casual Mode 1x', target: 1, reward: 50 },
    { id:'useUlt', title:'Gunakan Ultimate 3x', target: 3, reward: 50 },
    { id:'winBattle', title:'Menangkan 1 Pertempuran', target: 1, reward: 50 }
];

window.openMissions = () => {
    let html = '';
    MISSION_DATA.forEach(m => {
        let prog = state.dailyMissions.progress[m.id] || 0;
        let isClaimed = state.dailyMissions.claimed.includes(m.id);
        let isDone = prog >= m.target;
        html += `<div style="background:rgba(255,255,255,0.05); padding:10px; border-radius:8px; display:flex; justify-content:space-between; align-items:center;">
            <div style="text-align:left;">
                <div style="font-weight:bold;">${m.title}</div>
                <div style="font-size:12px; color:#aaa;">Progres: ${Math.min(prog, m.target)}/${m.target}</div>
            </div>
            <div>
                ${isClaimed ? `<span style="color:#888;">Terklaim</span>` 
                  : isDone ? `<button class="hsr-btn blue" style="padding:5px 10px; font-size:12px;" onclick="claimMission('${m.id}', ${m.reward})">Klaim ${m.reward}&#x1F48E;</button>` 
                  : `<span style="color:#ef4444;">Belum Selesai</span>`}
            </div>
        </div>`;
    });
    document.getElementById('mission-list').innerHTML = html;
    document.getElementById('mission-modal').style.display = 'flex';
};

window.claimMission = async (id, reward) => {
    if (!state.dailyMissions.claimed.includes(id)) {
        state.dailyMissions.claimed.push(id);
        state.stellarJade += reward;
        await saveUserData();
        openMissions();
        document.getElementById('jade-display').innerText = '&#x1F48E; ' + state.stellarJade;
        let mj = document.getElementById('menu-jade-display');
        if (mj) mj.innerHTML = '&#x1F48E; ' + state.stellarJade;
        alert(`Berhasil klaim ${reward} Stellar Jade!`);
    }
};
'''
content = content.replace('window.navigateTo = (v) => {', mission_js + '\\nwindow.navigateTo = (v) => {')


with open(OUT, 'w', encoding='utf-8') as f:
    f.write(content)
print("Features 3 patched successfully!")
