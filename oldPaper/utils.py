from time import sleep
import os
from subprocess import call

def view_presentation(presentation):
	dummy = 'dummy'
	dummy_pdf = dummy + '.pdf'
	dummy_tex = dummy + '.tex'

	pdf_cmd = 'pdflatex'
	rm_cmd = 'rm'
	view_cmd = 'open'

	call((rm_cmd, '-rf', dummy + '*'))
	presentation.write(dummy_tex)
	call((pdf_cmd, dummy_tex))
	call((pdf_cmd, dummy_tex))
	call((pdf_cmd, dummy_tex))	
	call((view_cmd, dummy_pdf))


escape_dict={'\a':r'\a',
           '\b':r'\b',
           '\c':r'\c',
           '\f':r'\f',
           '\n':r'\n',
           '\r':r'\r',
           '\t':r'\t',
           '\v':r'\v',
           '\'':r'\'',
           '\"':r'\"',
           '\0':r'\0',
           '\1':r'\1',
           '\2':r'\2',
           '\3':r'\3',
           '\4':r'\4',
           '\5':r'\5',
           '\6':r'\6',
           '\7':r'\7',
           '\8':r'\8',
           '\9':r'\9'}

def raw(text):
    """Returns a raw string representation of text"""
    new_string=''
    for char in text:
        try: new_string+=escape_dict[char]
        except KeyError: new_string+=char
    return new_string

def grab_raw(fn):
	with open(fn, 'r') as fn:
		return raw(fn.read())

def grab_adjoint(fn):
	root = '/Users/jdr/Dropbox/INRIA Collaboration'
	path = os.path.join(root, fn)
	return '\n\\input{"%s"}\n' % path
	# return grab_raw(os.path.join(path, fn))