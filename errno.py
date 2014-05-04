#!/usr/bin/env python

# encoding: utf-8

import errno
import os
import sys
from workflow import Workflow, ICON_WARNING, ICON_INFO


def main(wf):

	if len(wf.args):
		try:
			err = int(wf.args[0])
		except (Exception,), e:
			wf.add_item(title='%s' % e,
				subtitle='%s' % wf.args,
				icon=ICON_WARNNG)
			err = 35
		
	try:	
		wf.add_item(title=errno.errorcode[err],
			subtitle=os.strerror(err), 
			icon=ICON_INFO)
	except (KeyError,), e:
		wf.add_item(title="Unknown error number", icon=ICON_WARNING)
	
	wf.send_feedback()

	
if __name__ == u"__main__":
	wf = Workflow()
	sys.exit(wf.run(main))

