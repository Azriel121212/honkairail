import re

with open('rebuild.py', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    'if (state.autoBattle) {\\n            setTimeout(async () => {',
    'if (state.autoBattle) {\\n            state.waitingForPlayer = true;\\n            setTimeout(async () => {'
)

with open('rebuild.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Auto battle logic fixed!")
