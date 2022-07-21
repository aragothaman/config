from datetime import datetime ;
from datetime import timedelta ;
import json

f= open('minecraft.config', 'w')

now = datetime.now();
timedelta = delta = timedelta(minutes=60)
end = now + delta ;

format  = '%y:%m:%d:%H:%M'

fromStr = now.strftime(format)
toStr = end.strftime(format)

props = {}
props['action'] = 'allow'
props['from'] = fromStr
props['to'] = toStr

appStrings = []
appStrings.append('minecraft')
appStrings.append('anotherApp')

props['apps'] = appStrings

config = json.dumps(props)
print(config)

f.write(config)
f.close()
