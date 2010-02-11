#!/usr/bin/python2.6

from datetime import datetime
from ftplib import FTP
from os import listdir
from os.path import isdir
 
HOST = 'example.com'
USER = 'user'
PASS = 'pass'
 
def main():
    log('Connecting to \'%s\' as user \'%s\'...' % (HOST, USER))
    ftp = FTP(HOST, USER, PASS)
     
    for file_name in listdir('.'):
        if not isdir(file_name):
            log('Transferring \'%s\'...' % file_name)
            send_file(ftp, file_name)
            log('done')
     
    ftp.quit()
    log('Script complete')
 
def send_file(ftp, file_name):
    with open(file_name, 'r') as f:
        ftp.storlines('STOR %s' % file_name, f)
 
def log(message, new_line=True):
    if new_line:
        print '%s - %s' % (datetime.now(), message)
 
if __name__ == "__main__":
    main()
