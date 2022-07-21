from datetime import datetime ;
from datetime import timedelta ;

f= open('minecraft.config', 'w')

now = datetime.now();
timedelta = delta = timedelta(minutes=60)
end = now + delta ;

format  = '%y:%m:%d:%H:%M'

fromStr = now.strftime(format)
toStr = end.strftime(format)

f.write(fromStr)
f.write('\n')
f.write(toStr)
f.close()
