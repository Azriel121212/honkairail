import re

with open('rebuild.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Imports
content = content.replace(
    'import { getFirestore, doc, setDoc, getDoc } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-firestore.js";',
    'import { getFirestore, doc, setDoc, getDoc, collection, query, orderBy, limit, getDocs } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-firestore.js";'
)

# 2. State update
content = content.replace(
    'const state = {',
    'const state = { highestCasualStage: 0, playerName: "", '
)

# 3. Auth update
content = content.replace(
    'if (user) {\n        try {',
    'if (user) {\n        try {\n            state.playerName = user.displayName || user.email.split("@")[0];'
)

# 4. loadUserData update
content = content.replace(
    'state.stellarJade = d.stellarJade || 2000;',
    'state.stellarJade = d.stellarJade || 2000;\n        state.highestCasualStage = d.highestCasualStage || 0;\n        state.playerName = d.playerName || state.playerName;'
)

# 5. saveUserData update
content = content.replace(
    'stellarJade:state.stellarJade, unlockedIds:state.unlockedIds,',
    'stellarJade:state.stellarJade, unlockedIds:state.unlockedIds,\n        highestCasualStage: state.highestCasualStage, playerName: state.playerName,'
)

# 6. HTML insertion for leaderboard
leaderboard_html = '''
<div style="max-width:800px;margin:30px auto;background:rgba(0,0,0,0.6);border:2px solid #333;border-radius:12px;padding:20px;box-shadow:0 0 20px rgba(59,130,246,0.2);">
    <h3 style="text-align:center;color:var(--accent-blue);font-family:'Orbitron';text-shadow:0 0 10px rgba(59,130,246,0.5);margin-bottom:15px;">&#x1F3C6; TOP 10 CASUAL PLAYERS &#x1F3C6;</h3>
    <div id="leaderboard-list" style="display:flex;flex-direction:column;gap:10px;">
        <div style="text-align:center;color:#888;">Memuat Leaderboard...</div>
    </div>
</div>
'''

content = content.replace(
    '<div class="page" id="story-view"',
    leaderboard_html + '\\n<div class="page" id="story-view"'
)

# 7. Add loadLeaderboard JS
leaderboard_js = '''
window.loadLeaderboard = async () => {
    try {
        const q = query(collection(db, "playerSaves"), orderBy("highestCasualStage", "desc"), limit(10));
        const querySnapshot = await getDocs(q);
        let html = '';
        let rank = 1;
        querySnapshot.forEach((doc) => {
            let data = doc.data();
            let stg = data.highestCasualStage || 0;
            if (stg > 0) {
                let color = rank===1?'#fbbf24':rank===2?'#94a3b8':rank===3?'#b45309':'#ccc';
                let icon = rank===1?'&#x1F947;':rank===2?'&#x1F948;':rank===3?'&#x1F949;':`#${rank}`;
                html += `<div style="display:flex;justify-content:space-between;background:rgba(255,255,255,0.05);padding:10px 15px;border-radius:8px;border-left:4px solid ${color};">
                    <span style="color:${color};font-weight:bold;">${icon} ${data.playerName || 'Unknown'}</span>
                    <span style="color:#4ade80;">Stage ${stg}</span>
                </div>`;
                rank++;
            }
        });
        if (!html) html = '<div style="text-align:center;color:#888;">Belum ada data</div>';
        document.getElementById('leaderboard-list').innerHTML = html;
    } catch(e) {
        console.error("Leaderboard error:", e);
    }
};

'''
content = content.replace(
    'function navigateTo(pageId) {',
    leaderboard_js + '\\nfunction navigateTo(pageId) {\\n    if (pageId==="main-menu-view") loadLeaderboard();'
)

# 8. Highest Casual Stage update
content = content.replace(
    'state.currentStage++;',
    'state.currentStage++;\\n        if(state.gameMode==="casual") state.highestCasualStage = Math.max(state.highestCasualStage||0, state.currentStage);'
)

with open('rebuild.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Leaderboard logic added!")
