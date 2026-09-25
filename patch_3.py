import re

OUT = 'rebuild.py'

with open(OUT, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. State for SU Resonance
content = content.replace(
    'suStage: 1,',
    'suStage: 1, suPath: "Destruction", suResonance: 0,'
)

# 2. Path Selection before SU starts
# In window.goSUMode
content = content.replace(
    'window.goSUMode = () => {',
    '''window.goSUMode = () => {
    let p = prompt("Pilih Path Resonance untuk Simulated Universe:\\n1. Destruction (AoE DMG)\\n2. Hunt (Single Target Nuke)\\n3. Abundance (AoE Heal)\\nKetik 1, 2, atau 3:", "1");
    if(p==="1" || p.toLowerCase()==="destruction") state.suPath = "Destruction";
    else if(p==="2" || p.toLowerCase()==="hunt") state.suPath = "Hunt";
    else if(p==="3" || p.toLowerCase()==="abundance") state.suPath = "Abundance";
    else { alert("Dibatalkan."); return; }
    state.suResonance = 0;
'''
)

# 3. Add Resonance Button to Battle UI
reso_btn_html = '''
        <div id="su-resonance-container" style="display:none; text-align:center; margin-bottom:10px;">
            <button id="btn-resonance" class="hsr-btn" style="background:var(--accent-orange); width:100%; font-weight:bold; color:#000; box-shadow:0 0 10px var(--accent-orange);" onclick="useResonance()">&#x26A1; PATH RESONANCE (0%)</button>
        </div>
'''
content = content.replace(
    '<div id="battle-log"></div>',
    reso_btn_html + '\\n        <div id="battle-log"></div>'
)

# Show resonance button only in SU
content = content.replace(
    'document.getElementById(\'battle-log\').innerHTML=\'\';',
    'document.getElementById(\'battle-log\').innerHTML=\'\';\n    document.getElementById(\'su-resonance-container\').style.display = state.gameMode==="su" ? "block" : "none";'
)

# 4. Fill Resonance Energy
fill_reso_js = '''
    if(state.gameMode==='su' && state.suResonance < 100) {
        state.suResonance += 25; // 25% per action
        if(state.suResonance > 100) state.suResonance = 100;
        let btn = document.getElementById('btn-resonance');
        btn.innerHTML = `&#x26A1; PATH RESONANCE (${state.suResonance}%)`;
        btn.style.boxShadow = state.suResonance === 100 ? "0 0 20px #fff" : "0 0 10px var(--accent-orange)";
    }
'''
content = content.replace(
    '// End turn',
    fill_reso_js + '\\n        // End turn'
)

# 5. useResonance function
reso_logic = '''
window.useResonance = async () => {
    if(state.suResonance < 100) return;
    state.suResonance = 0;
    document.getElementById('btn-resonance').innerHTML = `&#x26A1; PATH RESONANCE (0%)`;
    document.getElementById('btn-resonance').style.boxShadow = "0 0 10px var(--accent-orange)";
    
    playSFX("ult");
    writeLog(`&#x26A1; PATH RESONANCE: ${state.suPath.toUpperCase()} ACTIVATE!`, 'system');
    
    if(state.suPath === "Destruction") {
        state.enemies.forEach(e => {
            if(e.hp > 0) { e.hp -= 2000; writeLog(`- Resonance hits ${e.name} for 2000 DMG!`, 'damage'); }
        });
    } else if(state.suPath === "Hunt") {
        let e = state.enemies.find(x => x.hp > 0);
        if(e) { e.hp -= 5000; writeLog(`- Resonance nukes ${e.name} for 5000 DMG!`, 'damage'); }
    } else if(state.suPath === "Abundance") {
        state.party.forEach(p => {
            if(p.hp > 0) {
                p.hp += 2000;
                let m = charDB.find(x=>x.id===p.id).hp;
                if(p.hp > m) p.hp = m;
                writeLog(`- Resonance heals ${p.name} for 2000 HP!`, 'heal');
            }
        });
    }
    
    updateBattleUI();
    checkWinCondition();
};
'''
content = content.replace('window.navigateTo = (v) => {', reso_logic + '\\nwindow.navigateTo = (v) => {')


with open(OUT, 'w', encoding='utf-8') as f:
    f.write(content)
print("Features 4 patched successfully!")
