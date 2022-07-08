import dropbox
import sys
import time
import os
from os.path import expanduser
from dotenv import load_dotenv

# https://www.dropboxforum.com/t5/Dropbox-API-Support-Feedback/Permananet-Access-Token/td-p/575173

load_dotenv(os.sep.join((expanduser("~"),'.env')))
api_key_dropbox = os.getenv('api_key_dropbox')
timestr = time.strftime("%Y%m%d-%H%M%S")
filename, file_extension = os.path.splitext(sys.argv[1])

if(len(sys.argv) != 2):
    print("Usage: python uploadDropbox <fileName>")
else:
    fileName= sys.argv[1]

    dbx = dropbox.Dropbox(api_key_dropbox) 

    print('/'+filename+'_'+ timestr+file_extension)

    with open(fileName, "rb") as f:
        dbx.files_upload(f.read(), '/'+filename+'_'+ timestr+file_extension, mute = False)

    f.close()
