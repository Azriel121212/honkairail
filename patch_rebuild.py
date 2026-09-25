import re

with open('rebuild.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update charDB stats based on price
def replacer(m):
    id_str = m.group(1)
    name = m.group(2)
    role = m.group(3)
    hp = int(m.group(4))
    atk = int(m.group(5))
    spd = m.group(6)
    price = int(m.group(7))
    rest = m.group(8)
    
    # Adjust stats based on price
    if price <= 1000:
        new_atk = 180
        new_hp = 1400
    elif price <= 1500:
        new_atk = 220
        new_hp = 1500
    elif price <= 2000:
        new_atk = 260
        new_hp = 1600
    elif price <= 2500:
        new_atk = 300
        new_hp = 1800
    else: # 3000+
        new_atk = 380
        new_hp = 2200

    # Exceptions for specific roles
    if role == 'Abundance' or role == 'Preservation':
        new_hp += 600
        new_atk -= 50
    elif role == 'Hunt' or role == 'Destruction' or role == 'Erudition':
        new_atk += 40
        new_hp -= 200
        
    return f"{{ id:'{id_str}', name:'{name}', role:'{role}', hp:{new_hp}, atk:{new_atk}, spd:{spd}, price:{price}, {rest}"

content = re.sub(r"\{\s*id:'([^']+)',\s*name:'([^']+)',\s*role:'([^']+)',\s*hp:(\d+),\s*atk:(\d+),\s*spd:(\d+),\s*price:(\d+),\s*(img:.*?)", replacer, content)

# 2. Healer Logic Update
old_heal1 = "let healAmt = Math.floor(member.atk*(action==='ultimate'?2.5:action==='skill'?2.0:1.2));"
new_heal1 = "let healAmt = action==='ultimate'? Math.floor(member.atk*1.5 + 1200) : action==='skill'? Math.floor(member.atk*1.0 + 800) : Math.floor(member.atk*0.5 + 400);"

old_heal2 = "healTargets.forEach(p=>healAlly(p, Math.floor(healAmt/(healTargets.length||1))));"
new_heal2 = "healTargets.forEach(p=>healAlly(p, healAmt));"

content = content.replace(old_heal1, new_heal1)
content = content.replace(old_heal2, new_heal2)

# 3. Team suggestions Update
teams_match = re.search(r"const teams = \[(.*?)\];", content, re.DOTALL)
if teams_match:
    new_teams = """
        {name:'&#x1F7E0; Super Break (MC)', tag:'SUPER BREAK', clr:'#f59e0b', chars:['mc','firefly','ruanmei','gallagher']},
        {name:'&#x1F7E0; Super Break v2',   tag:'SUPER BREAK', clr:'#f59e0b', chars:['mc','rappa','fugue','lingsha']},
        {name:'&#x1F7E0; Boothill Break',   tag:'BREAK',       clr:'#fb923c', chars:['boothill','fugue','ruanmei','gallagher']},
        {name:'&#x1F534; DoT Premium',      tag:'DOT',         clr:'#a855f7', chars:['kafka','blackswan','ruanmei','huohuo']},
        {name:'&#x1F534; DoT Budget',       tag:'DOT',         clr:'#c084fc', chars:['sampo','guinaifen','asta','lynx']},
        {name:'&#x1F534; Hypercarry Acheron',tag:'NUKE',       clr:'#ef4444', chars:['acheron','jiaoqiu','blackswan','gallagher']},
        {name:'&#x1F534; Acheron F2P',      tag:'NUKE',        clr:'#ef4444', chars:['acheron','pela','guinaifen','gallagher']},
        {name:'&#x1F535; FUA Feixiao',      tag:'FUA',         clr:'#3b82f6', chars:['feixiao','moze','robin','aventurine']},
        {name:'&#x1F535; Yunli Counter',    tag:'FUA',         clr:'#6366f1', chars:['yunli','robin','sunday','huohuo']},
        {name:'&#x1F535; Clara Protection', tag:'COUNTER',     clr:'#6366f1', chars:['clara','march7','tingyun','lynx']},
        {name:'&#x1F535; Aglaea Summon',    tag:'SUMMON',      clr:'#a855f7', chars:['aglaea','sunday','ruanmei','huohuo']},
        {name:'&#x1F7E1; Premium FUA',      tag:'FUA',         clr:'#eab308', chars:['topaz','ratio','robin','aventurine']},
        {name:'&#x1F7E1; Jing Yuan FUA',    tag:'FUA',         clr:'#eab308', chars:['jingyuan','sparkle','tingyun','huohuo']},
        {name:'&#x1F7E3; Mono Quantum',     tag:'QUANTUM',     clr:'#d946ef', chars:['seele','silverwolf','sparkle','fuxuan']},
        {name:'&#x1F7E3; Qingque Gambler',  tag:'GAMBLER',     clr:'#d946ef', chars:['qingque','sparkle','silverwolf','fuxuan']},
        {name:'&#x1F535; Jingliu Hyper',    tag:'HYPER',       clr:'#3b82f6', chars:['jingliu','bronya','ruanmei','luocha']},
        {name:'&#x1F7E2; Blade Hyper',      tag:'HYPER',       clr:'#10b981', chars:['blade','bronya','sparkle','luocha']},
        {name:'&#x1F7E1; DHIL Hypercarry',  tag:'HYPER',       clr:'#eab308', chars:['dhil','sparkle','tingyun','huohuo']},
        {name:'&#x1F7E1; Premium Ratio',    tag:'FUA',         clr:'#eab308', chars:['ratio','moze','robin','aventurine']},
        {name:'&#x1F7E3; Herta Kurukuru',   tag:'MEME',        clr:'#14b8a6', chars:['herta','jade','ruanmei','aventurine']},
        {name:'&#x1F7E3; Mono Physical',    tag:'PHYSICAL',    clr:'#9ca3af', chars:['argenti','luka','robin','clara']},
        {name:'&#x1F7E2; Starter F2P',      tag:'F2P',         clr:'#22c55e', chars:['mc','danheng','march7','natasha']}
    """
    content = content.replace(teams_match.group(1), new_teams)

with open('rebuild.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Rebuild.py successfully patched.")
