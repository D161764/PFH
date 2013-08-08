#-------------------------------------------------------------------------------
# Name:        UNIX Hash 3xploit3r
# Purpose:
#
# Author:      D1617 64
#
# Created:     09-08-2013
# Copyright:   (c) D1617 64 2013
# Licence:     <PFH02>
#-------------------------------------------------------------------------------
import crypt
def testpass(cryptword):
    salt=cryptword[0:2]
    dicfile=open('passlist..txt','r')
    for wrd in dicfile.readlines():
        wrd=wrd.strip('\n')
        cryptpass=crypt.crypt(wrd,salt)
        if (cryptpass==cryptword):
            print('[+] password found',wrd)
        else:
            print('[+] no password found')
def main():
    unixhash=raw_input('[+] Unix Hash :')
    testpass(unixhash)
main()
