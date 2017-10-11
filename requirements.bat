IF NOT EXIST C:\Python27 powershell -Command "(New-Object Net.WebClient).DownloadFile('https://www.python.org/ftp/python/2.7.13/python-2.7.13.amd64.msi', 'python-2.7.msi')"
powershell -Command "(New-Object Net.WebClient).DownloadFile('https://download.microsoft.com/download/7/9/6/796EF2E4-801B-4FC4-AB28-B59FBF6D907B/VCForPython27.msi', 'VCForPython27.msi')"
IF NOT EXIST C:\Python27 python-2.7.msi
VCForPython27.msi
del VCForPython27.msi
C:\Python27\Scripts\easy_install.exe pip
C:\Python27\Scripts\pip.exe install -r requirements.txt
