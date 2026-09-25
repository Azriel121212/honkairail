import re
import subprocess

html = open('index.html', encoding='utf-8').read()
script = re.search(r'<script.*?>([\s\S]*)</script>', html).group(1)
open('test.js', 'w', encoding='utf-8').write(script)

result = subprocess.run(['node', '-c', 'test.js'], capture_output=True, text=True)
print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)
