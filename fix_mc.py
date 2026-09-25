import sys, re
sys.stdout.reconfigure(encoding='utf-8')

path = r'c:\Users\Chaerul Azriel A\OneDrive\Pictures\Figma\index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# ===========================================================================
# 1. FIX MC SYSTEM:
#    - MC/Azriel is ONE character - name shown as "Azriel"
#    - 4 paths: physical(Destruction), fire(Preservation), imaginary(Harmony), remembrance(Remembrance)
#    - Eidolon per path: eidolons['mc_physical'], eidolons['mc_fire'], etc.
#    - getMcData returns name 'Azriel', id 'mc'
#    - setMcPath also updates eidolon key used
# ===========================================================================

old_mc_system = """        // ===== MC MULTI-PATH SYSTEM =====
        const mcPaths = {
            physical: {
                pathKey:'physical', subname:'Destruction', role:'Destruction',
                hp:1800, atk:320, spd:100,
                img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/8001.png',
                color:'#c084fc', element:'Physical',
                desc:'Skill: 130% ATK AoE Blade DMG. Ulti: 300% Heavy Slash semua musuh \\u26d4',
                eEffects:['E1: Skill Blade DMG +25% & chance Bleed','E2: Ulti tembus 15% DEF & regen 2 SP','E3: Skill Lvl +2','E4: Kebal Debuff saat HP < 50%','E5: Ult Lvl +2','E6: Setiap kill di Ulti memicu ledakan 200% ATK tambahan!']
            },
            fire: {
                pathKey:'fire', subname:'Preservation', role:'Preservation',
                hp:2200, atk:180, spd:100,
                img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/8003.png',
                color:'#fb923c', element:'Fire',
                desc:'Skill: Shield 1400 HP AoE + Taunt. Ulti: Regen Shield seluruh party & Cleanse \\ud83d\\udee1\\ufe0f',
                eEffects:['E1: Shield +30% & memicu Fire Counter saat diserang','E2: Ulti beri Fire RES +25% & ATK buff 20%','E3: Skill Lvl +2','E4: Counter serang melemahkan musuh 15% DEF','E5: Ult Lvl +2','E6: Shield meledak saat habis, dmg 250% ATK ke semua musuh!']
            },
            imaginary: {
                pathKey:'imaginary', subname:'Harmony', role:'Harmony',
                hp:1850, atk:220, spd:101,
                img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/8005.png',
                color:'#facc15', element:'Imaginary',
                desc:'Skill: Tim Super Break DMG +50% selama 2 turn. Ulti: AoE Imaginary + Regen Break Gauge \\u2b50',
                eEffects:['E1: Super Break DMG tim +20% extra','E2: Saat ally punya toughness penuh, Super Break DMG +30%','E3: Skill Lvl +2','E4: Break Effect tim +15%','E5: Ult Lvl +2','E6: Super Break menembus semua RES musuh!']
            },
            remembrance: {
                pathKey:'remembrance', subname:'Remembrance', role:'Remembrance',
                hp:1900, atk:230, spd:100,
                img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/8007.png',
                color:'#67e8f9', element:'Ice',
                desc:'Skill: Panggil Mem (summon) untuk serang & support. Ulti: Mem mode aktif, Ice AoE + Buff \\u2744\\ufe0f',
                eEffects:['E1: Mem mendapat +30% ATK & CRIT Rate','E2: Saat Mem serang, tim regen 1 SP','E3: Skill Lvl +2','E4: Memory DMG +25% saat Mem mode aktif','E5: Ult Lvl +2','E6: Mem dapat giliran tambahan & DMG Ice menembus RES!']
            }
        };
        // Active MC path (persisted to localStorage)
        let activeMcPath = localStorage.getItem('mcPath') || 'imaginary';
        function getMcData() {
            let p = mcPaths[activeMcPath];
            return { id:'mc', name:'Trailblazer', price:0, ...p };
        }
        window.setMcPath = function(p) {
            activeMcPath = p;
            localStorage.setItem('mcPath', p);
            let idx = charDB.findIndex(x => x.id === 'mc');
            if (idx !== -1) Object.assign(charDB[idx], getMcData());
            let pi = state.party ? state.party.findIndex(x => x.id === 'mc') : -1;
            if (pi !== -1) {
                let mc = getMcData();
                let eLvl = state.eidolons['mc'] || 0;
                let bonusMulti = 1 + eLvl * 0.10;
                let prev = state.party[pi];
                state.party[pi] = { ...mc, eLvl, maxHp: Math.floor(mc.hp * bonusMulti), hp: prev.hp,
                    atk: Math.floor(mc.atk * bonusMulti), spd: mc.spd,
                    shield: prev.shield, buffAtk: prev.buffAtk, resPen: prev.resPen,
                    energy: prev.energy, maxEnergy: 100, statuses: prev.statuses };
            }
            renderCharSelect();
            openCharModal('mc');
        };"""

new_mc_system = """        // ===== MC / AZRIEL MULTI-PATH SYSTEM =====
        // Azriel IS the Trailblazer. One character, 4 paths, separate eidolons per path.
        const mcPaths = {
            physical: {
                pathKey:'physical', subname:'Destruction', role:'Destruction',
                hp:1800, atk:320, spd:100,
                img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/8001.png',
                color:'#c084fc', element:'Physical \u2694\ufe0f',
                desc:'Path of Destruction. Skill: 130% ATK AoE Blade. Ulti: 300% Heavy Slash semua musuh \u26d4',
                eEffects:['E1: Blade DMG +25% & Bleed chance 30%','E2: Ulti tembus 15% DEF & regen 2 SP saat kill','E3: Skill Lvl +2, Talent Lvl +2','E4: Kebal Debuff saat HP < 50%, DMG +20%','E5: Ult Lvl +2, Basic ATK Lvl +1','E6: Kill di Ulti trigger ledakan 200% ATK ke area!']
            },
            fire: {
                pathKey:'fire', subname:'Preservation', role:'Preservation',
                hp:2200, atk:180, spd:100,
                img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/8003.png',
                color:'#fb923c', element:'Fire \ud83d\udd25',
                desc:'Path of Preservation. Skill: Shield 1400 HP AoE + Taunt. Ulti: Regen Shield & Cleanse \ud83d\udee1\ufe0f',
                eEffects:['E1: Shield Value +30% & Fire Counter saat diserang','E2: Ulti beri Fire RES +25% & ATK 20%','E3: Skill Lvl +2, Talent Lvl +2','E4: Counter melemahkan musuh 15% DEF, regen 1 SP','E5: Ult Lvl +2, Basic ATK Lvl +1','E6: Shield meledak saat habis \u2014 250% ATK ke semua musuh!']
            },
            imaginary: {
                pathKey:'imaginary', subname:'Harmony', role:'Harmony',
                hp:1850, atk:220, spd:101,
                img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/8005.png',
                color:'#facc15', element:'Imaginary \u2b50',
                desc:'Path of Harmony. Skill: Super Break DMG tim +50% (2 turn). Ulti: AoE + Regen Toughness Gauge',
                eEffects:['E1: Super Break DMG +20% extra, durasi +1 turn','E2: Ally dgn full toughness: Super Break +30%','E3: Skill Lvl +2, Talent Lvl +2','E4: Break Effect seluruh tim +15%','E5: Ult Lvl +2, Basic ATK Lvl +1','E6: Super Break menembus SEMUA RES musuh!']
            },
            remembrance: {
                pathKey:'remembrance', subname:'Remembrance', role:'Remembrance',
                hp:1900, atk:230, spd:100,
                img:'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/8007.png',
                color:'#67e8f9', element:'Ice \u2744\ufe0f',
                desc:'Path of Remembrance. Skill: Summon Mem untuk serang & support. Ulti: Mem Mode, Ice AoE',
                eEffects:['E1: Mem ATK +30% & CRIT Rate +15%','E2: Saat Mem serang, seluruh tim regen 1 SP','E3: Skill Lvl +2, Talent Lvl +2','E4: Memory DMG +25% saat Mem Mode aktif','E5: Ult Lvl +2, Basic ATK Lvl +1','E6: Mem dapat giliran ekstra & Ice DMG menembus RES!']
            }
        };

        // Active MC path (persisted to localStorage)
        let activeMcPath = localStorage.getItem('mcPath') || 'imaginary';

        function getMcEidolonKey() { return 'mc_' + activeMcPath; }

        function getMcData() {
            let p = mcPaths[activeMcPath];
            return { id:'mc', name:'Azriel', price:0, isMc:true, ...p };
        }

        window.setMcPath = function(p) {
            activeMcPath = p;
            localStorage.setItem('mcPath', p);
            // Update charDB entry
            let idx = charDB.findIndex(x => x.id === 'mc');
            if (idx !== -1) Object.assign(charDB[idx], getMcData());
            // Update party if Azriel is in it
            let pi = state && state.party ? state.party.findIndex(x => x.id === 'mc') : -1;
            if (pi !== -1) {
                let mc = getMcData();
                let eLvl = state.eidolons[getMcEidolonKey()] || 0;
                let bonusMulti = 1 + eLvl * 0.10;
                let prev = state.party[pi];
                state.party[pi] = { ...mc, eLvl,
                    maxHp: Math.floor(mc.hp * bonusMulti), hp: Math.min(prev.hp, Math.floor(mc.hp * bonusMulti)),
                    atk: Math.floor(mc.atk * bonusMulti), spd: mc.spd,
                    shield: prev.shield||0, buffAtk: prev.buffAtk||0, resPen: prev.resPen||0,
                    energy: prev.energy||0, maxEnergy: 100, statuses: prev.statuses||[] };
            }
            renderCharSelect();
            openCharModal('mc');
        };"""

content = content.replace(old_mc_system, new_mc_system)

# ===========================================================================
# 2. Update getMcData name from 'Trailblazer' to 'Azriel' and remove azriel separate entry
# ===========================================================================

# Remove azriel as separate charDB entry (it's now merged into MC)
old_azriel_entry = """            // ---- FREE STARTERS ----
            { id: 'azriel',     name: 'Azriel',      role: 'Destruction',  hp: 1800, atk: 280, spd: 104, price: 1500,    img: 'https://cdn.jsdelivr.net/gh/Mar-7th/StarRailRes@master/icon/avatar/8001.png', desc: 'Skill: 150% ATK Blast. Ulti: 300% ATK Heavy Blast \ud83d\udca5', eEffects: ['E1: DMG Skill naik 20%', 'E2: Ulti tembus DEF', 'E3: Level Traces +2', 'E4: Kebal Debuff', 'E5: Level Maksimal +2', 'E6: Serangan memicu efek area 2x lipat!'] },"""

new_azriel_section = """            // ---- FREE STARTERS ----"""

content = content.replace(old_azriel_entry, new_azriel_section)

# ===========================================================================
# 3. Fix starters to not include 'azriel' anymore (MC replaces it)
# ===========================================================================
content = content.replace(
    "const starters = ['mc', 'danheng', 'march7', 'natasha'];",
    "const starters = ['mc', 'danheng', 'march7', 'natasha']; // mc = Azriel/Trailblazer"
)

# ===========================================================================
# 4. FIX NEW CHARACTER IMAGE IDs (correct CDN IDs based on research)
# Correct IDs: Jiaoqiu=1218, Feixiao=1220, Yunli=1221, Lingsha=1222, Moze=1223,
#              Fugue=1225, Sunday=1313, Boothill=1315, Rappa=1317
# ===========================================================================
img_fixes = [
    # Feixiao: was 1224, correct is 1220
    ("icon/avatar/1224.png", "icon/avatar/1220.png"),
    # Boothill: was 1222, correct is 1315
    ("icon/avatar/1222.png", "icon/avatar/1315.png"),
    # Yunli: was 1225, correct is 1221
    ("icon/avatar/1225.png", "icon/avatar/1221.png"),
    # Jiaoqiu: was 1223, correct is 1218
    ("icon/avatar/1223.png", "icon/avatar/1218.png"),
    # Sunday: was 1227, correct is 1313
    ("icon/avatar/1227.png", "icon/avatar/1313.png"),
    # Fugue: was 1312, correct is 1225
    ("icon/avatar/1312.png", "icon/avatar/1225.png"),
    # Rappa: was 1314, correct is 1317
    ("icon/avatar/1314.png", "icon/avatar/1317.png"),
    # Gallagher: was 1301 - gallagher IS 1301, keep
    # Lingsha: was 1317, correct is 1222
    ("icon/avatar/1317.png", "icon/avatar/1222.png"),
    # Moze: was 1228, correct is 1223
    ("icon/avatar/1228.png", "icon/avatar/1223.png"),
]
for old_img, new_img in img_fixes:
    content = content.replace(old_img, new_img)

# ===========================================================================
# 5. Fix openCharModal to use per-path eidolon key for MC
# ===========================================================================
old_modal_eidolon = """            if (id === 'mc') {
                let idx = charDB.findIndex(x => x.id === 'mc');
                if (idx !== -1) Object.assign(charDB[idx], getMcData());
            }
            let c = charDB.find(x => x.id === id);
            if (!c) return;
            let isLocked = !state.unlockedIds.includes(c.id);
            let isSel = state.selectedIds.includes(c.id);
            let eLvl = state.eidolons[c.id] || 0;
            let ePrice = 500 + (eLvl * 300);"""

new_modal_eidolon = """            if (id === 'mc') {
                let idx = charDB.findIndex(x => x.id === 'mc');
                if (idx !== -1) Object.assign(charDB[idx], getMcData());
            }
            let c = charDB.find(x => x.id === id);
            if (!c) return;
            let isLocked = !state.unlockedIds.includes(c.id);
            let isSel = state.selectedIds.includes(c.id);
            // MC uses per-path eidolon key
            let eidolonKey = (id === 'mc') ? getMcEidolonKey() : id;
            let eLvl = state.eidolons[eidolonKey] || 0;
            let ePrice = 500 + (eLvl * 300);"""

content = content.replace(old_modal_eidolon, new_modal_eidolon)

# Fix upgradeEidolon button to pass correct key for MC
old_upgrade_btn = """                    ${eLvl < 6
                        ? `<button class="hsr-btn" style="width:100%; border-color:var(--jade-pink); color:var(--jade-pink);" onclick="upgradeEidolon('${c.id}', ${ePrice})">Upgrade Eidolon E${eLvl+1} (\\ud83d\\udc8e ${ePrice})</button>`
                        : `<button class="hsr-btn" disabled style="width:100%">Max Eidolon (E6) \\u2605</button>`}"""

new_upgrade_btn = """                    ${eLvl < 6
                        ? `<button class="hsr-btn" style="width:100%; border-color:var(--jade-pink); color:var(--jade-pink);" onclick="upgradeEidolon('${eidolonKey}', ${ePrice})">Upgrade Eidolon E${eLvl+1} (\ud83d\udc8e ${ePrice})</button>`
                        : `<button class="hsr-btn" disabled style="width:100%">Max Eidolon (E6) \u2605</button>`}"""

content = content.replace(old_upgrade_btn, new_upgrade_btn)

# ===========================================================================
# 6. Fix upgradeEidolon function to handle mc_ keys and refresh MC modal
# ===========================================================================
old_upgrade_fn = """        window.upgradeEidolon = async (id, price) => {
            if(state.stellarJade >= price) {
                state.stellarJade -= price;
                state.eidolons[id] = (state.eidolons[id] || 0) + 1;
                await saveUserData();
                openCharModal(id); // Refresh modal biar keliatan langsung naik
                renderCharSelect();
            } else alert("Stellar Jade lu kurang ngab buat Eidolon!");
        }"""

new_upgrade_fn = """        window.upgradeEidolon = async (eidolonKey, price) => {
            if(state.stellarJade >= price) {
                state.stellarJade -= price;
                state.eidolons[eidolonKey] = (state.eidolons[eidolonKey] || 0) + 1;
                await saveUserData();
                // For MC paths, open mc modal; otherwise use key as charId
                let charId = eidolonKey.startsWith('mc_') ? 'mc' : eidolonKey;
                openCharModal(charId);
                renderCharSelect();
            } else alert("Stellar Jade lu kurang ngab buat Eidolon!");
        }"""

content = content.replace(old_upgrade_fn, new_upgrade_fn)

# ===========================================================================
# 7. Fix party building - use mc_ eidolon key when building party from MC
# ===========================================================================
old_party_build = """                let eLvl = state.eidolons[c.id] || 0;"""
# There may be multiple of these - only fix the one in buildParty context
# Look for the pattern in startBattle / buildParty section
# We'll do a targeted replace for the party build section
content = content.replace(
    "let eLvl = state.eidolons[c.id] || 0;\n                let bonusMulti = 1 + eLvl * 0.10;\n                return { ...c,",
    "let eLvl = state.eidolons[c.id === 'mc' ? getMcEidolonKey() : c.id] || 0;\n                let bonusMulti = 1 + eLvl * 0.10;\n                return { ...c,"
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
checks = {
    'MC system': "getMcEidolonKey" in content,
    'Azriel name in getMcData': "name:'Azriel'" in content,
    'Azriel removed from charDB': "{ id: 'azriel'" not in content,
    'Feixiao img 1220': "icon/avatar/1220.png" in content,
    'Boothill img 1315': "icon/avatar/1315.png" in content,
    'Yunli img 1221': "icon/avatar/1221.png" in content,
    'Jiaoqiu img 1218': "icon/avatar/1218.png" in content,
    'Sunday img 1313': "icon/avatar/1313.png" in content,
    'Rappa img 1317': "icon/avatar/1317.png" in content,
    'Lingsha img 1222': "icon/avatar/1222.png" in content,
    'Moze img 1223': "icon/avatar/1223.png" in content,
}
for k, v in checks.items():
    print(f"{'OK' if v else 'FAIL'}: {k}")
print(f"\nTotal lines: {content.count(chr(10))}")
