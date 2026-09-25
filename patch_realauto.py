import re

with open('rebuild.py', 'r', encoding='utf-8') as f:
    content = f.read()

auto_logic = '''        state.waitingForPlayer=true;
        
        // Auto Battle Intercept
        if (state.autoBattle) {
            setTimeout(async () => {
                for (let p of state.party) {
                    if (p.hp > 0 && p.energy >= p.maxEnergy) {
                        await playerAction('ultimate');
                        if (state.enemies.every(e => e.hp <= 0)) return;
                    }
                }
                let type = (state.sp >= 1 && Math.random() > 0.3) ? 'skill' : 'basic';
                playerAction(type);
            }, 800 / (state.battleSpeed || 1));
            return;
        }'''

if 'Auto Battle Intercept' not in content:
    content = content.replace('        state.waitingForPlayer=true;', auto_logic)

with open('rebuild.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Auto battle logic really injected!")
