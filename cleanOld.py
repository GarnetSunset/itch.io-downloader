import os
import shutil

downloadDir = os.environ['temp'] + "\itchiotempdir"
shutil.rmtree(downloadDir)
