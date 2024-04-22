import sys 
 
import os 
 
INTERP = os.path.expanduser("/var/www/www-root/data/www/xn--80asepje.xn--p1ai/.venv/bin/python3.10") 
if sys.executable != INTERP: 
   os.execl(INTERP, INTERP, *sys.argv) 
 
sys.path.append(os.getcwd()) 
 
from hello import application
application.run(host='0.0.0.0', port=20000)