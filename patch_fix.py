import re

with open('rebuild.py', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    "if (state.gameMode==='casual') playBGM('menu'); navigateTo('casual-view');",
    "if (state.gameMode==='casual') { playBGM('menu'); navigateTo('casual-view'); }"
)

content = content.replace(
    "else playBGM('menu'); navigateTo('main-menu-view');",
    "else { playBGM('menu'); navigateTo('main-menu-view'); }"
)

with open('rebuild.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Syntax errors fixed!")
