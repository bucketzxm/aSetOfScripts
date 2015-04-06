import os
import sys
import zipfile
if len(sys.argv)<2:
	 print 'python %s zipfilename' % sys.argv[0]
else:
	f=zipfile.ZipFile(sys.argv[1])


	nlist=f.namelist()
	for n in nlist:
		m = unicode(n,'gb2312').encode('utf8')
		if m.endswith('/'):
			os.mkdir(m)
		else:
			file(m,'wb').write(f.read(n))
	f.close()
