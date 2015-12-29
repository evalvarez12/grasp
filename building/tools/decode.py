# encoding=utf8  
import sys  
import unicodedata as ud

reload(sys)  
sys.setdefaultencoding('utf8')


#def decode(char):
    #'''
    #Return the base character of char, by "removing" any
    #diacritics like accents or curls and strokes and the like.
    #'''
    #desc = ud.name(unicode(char))
    #cutoff = desc.find(' WITH ')
    #if cutoff != -1:
        #desc = desc[:cutoff]
    #return ud.lookup(desc)


def remove_accents(input_str):
    nkfd_form = ud.normalize('NFKD', unicode(input_str))
    return u"".join([c for c in nkfd_form if not ud.combining(c)])