# -*- coding: utf-8 -*-
import numpy, sys, os, cgi
from PIL import Image
from cStringIO import StringIO

def application(environ, start_response):
    if environ['REQUEST_METHOD'] == 'POST':
        bert = environ.copy()
        bert['QUERY_STRING'] = ''
        post = cgi.FieldStorage(
            fp = bert['wsgi.input'],
            environ=bert,
            keep_blank_values=True
        )
        map = {'000':'!','003':'#','006':'$','009':'%','00C':'&','00F':'*','030':'+','033':',','036':'-','039':'.','03C':'0','03F':'1','060':'2','063':'3','066':'4','069':'5','06C':'6','06F':'7','090':'8','093':'9','096':':','099':';','09C':'<','09F':'=','0C0':'>','0C3':'?','0C6':'@','0C9':'A','0CC':'B','0CF':'C','0F0':'D','0F3':'E','0F6':'F','0F9':'G','0FC':'H','0FF':'I','300':'J','303':'K','306':'L','309':'M','30C':'N','30F':'O','330':'P','333':'Q','336':'R','339':'S','33C':'T','33F':'U','360':'V','363':'W','366':'X','369':'Y','36C':'Z','36F':'^','390':'_','393':'`','396':'a','399':'b','39C':'c','39F':'d','3C0':'e','3C3':'f','3C6':'g','3C9':'h','3CC':'i','3CF':'j','3F0':'k','3F3':'l','3F6':'m','3F9':'n','3FC':'o','3FF':'p','600':'q','603':'r','606':'s','609':'t','60C':'u','60F':'v','630':'w','633':'x','636':'y','639':'z','63C':'{','63F':'|','660':'}','663':'~','666':'①','669':'②','66C':'③','66F':'④','690':'⑤','693':'⑥','696':'⑦','699':'⑧','69C':'⑨','69F':'⑩','6C0':'⑪','6C3':'⑫','6C6':'⑬','6C9':'⑭','6CC':'⑮','6CF':'⑯','6F0':'⑰','6F3':'⑱','6F6':'⑲','6F9':'⑳','6FC':'⑴','6FF':'⑵','900':'⑶','903':'⑷','906':'⑸','909':'⑹','90C':'⑺','90F':'⑻','930':'⑼','933':'⑽','936':'⑾','939':'⑿','93C':'⒀','93F':'⒁','960':'⒂','963':'⒃','966':'⒄','969':'⒅','96C':'⒆','96F':'⒇','990':'⒈','993':'⒉','996':'⒊','999':'⒋','99C':'⒌','99F':'⒍','9C0':'⒎','9C3':'⒏','9C6':'⒐','9C9':'⒑','9CC':'⒒','9CF':'⒓','9F0':'⒔','9F3':'⒕','9F6':'⒖','9F9':'⒗','9FC':'⒘','9FF':'⒙','C00':'⒚','C03':'⒛','C06':'⒜','C09':'⒝','C0C':'⒞','C0F':'⒟','C30':'⒠','C33':'⒡','C36':'⒢','C39':'⒣','C3C':'⒤','C3F':'⒥','C60':'⒦','C63':'⒧','C66':'⒨','C69':'⒩','C6C':'⒪','C6F':'⒫','C90':'⒬','C93':'⒭','C96':'⒮','C99':'⒯','C9C':'⒰','C9F':'⒱','CC0':'⒲','CC3':'⒳','CC6':'⒴','CC9':'⒵','CCC':'Ⓐ','CCF':'Ⓑ','CF0':'Ⓒ','CF3':'Ⓓ','CF6':'Ⓔ','CF9':'Ⓕ','CFC':'Ⓖ','CFF':'Ⓗ','F00':'Ⓘ','F03':'Ⓙ','F06':'Ⓚ','F09':'Ⓛ','F0C':'Ⓜ','F0F':'Ⓝ','F30':'Ⓞ','F33':'Ⓟ','F36':'Ⓠ','F39':'Ⓡ','F3C':'Ⓢ','F3F':'Ⓣ','F60':'Ⓤ','F63':'Ⓥ','F66':'Ⓦ','F69':'Ⓧ','F6C':'Ⓨ','F6F':'Ⓩ','F90':'ⓐ','F93':'ⓑ','F96':'ⓒ','F99':'ⓓ','F9C':'ⓔ','F9F':'ⓕ','FC0':'ⓖ','FC3':'ⓗ','FC6':'ⓘ','FC9':'ⓙ','FCC':'ⓚ','FCF':'ⓛ','FF0':'ⓜ','FF3':'ⓝ','FF6':'ⓞ','FF9':'ⓟ','FFC':'ⓠ','FFF':'ⓡ',}
        #print post['derimagen'].value
        im = Image.open( StringIO(post['derimagen'].value) )
        im = im.convert('P', palette = Image.WEB)
        im = im.convert('RGB')
        pixels = numpy.asarray(im)
        output= ""
        for line in pixels:
            for pixel in line:
                color = ""
                for value in pixel:
                    hex = "%X" % value
                    color += hex[0]
                link = "[](/%s)" % map[color]
                output += link
            output += "  blol"
    else:
        output = "N/A"
    te = '<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"></head>'
    te += '<body>'
    te += '<script type="text/javascript">if(parent && typeof parent.lulz === "function") parent.lulz("' + output + '");</script>'
    te += '</body></html>'
    response_headers = [
        ('Content-Length', str(len(te))),
        ('Content-Type', 'text/html'),
    ]
    start_response('200 OK', response_headers)
    return [te]
