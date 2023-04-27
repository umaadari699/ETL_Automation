import base64
import glob
import boto3
import os
from datetime import datetime, timedelta
import dateutil.utils

today = datetime.today()
today_dt = today.strftime('%Y-%m-%d')
ysterday = today - timedelta(days=1)
Yesterday_dt = ysterday.strftime('%Y-%m-%d')
print(today_dt, Yesterday_dt)

# Below line Latest Created/Modified file will Return
#print(max([os.path.join(path, d) for d in os.listdir(path)], key=os.path.getmtime))
print(" file_path " + " create_date " + " modified_date ")
# 3 lines for, to Return Latest
path = r'C:\Users\uma.adari\PycharmProjects\pythonProject4'
file_type = '/*.xlsx'
files = glob.glob(path + file_type) # path for files loading
l = list() # empty list
Store_files = [] # one more empty list for adding
list_of_files = files #
for x in list_of_files:
  s = x
  if (s.__contains__("2023-04-27")):
      print('Files which meets specific date ' + x)
      Store_files.append(x.split('\\')[-1:])
print(Store_files)
# To return latest created(getctime)/Modified file(getmtime)
max_file = max(files, key=os.path.getctime)
print("Latest Created sheet  "  + max_file)

# below code return all files with Create and Modified dates
# ==========================================================
fdpaths = [path + "/" + fd for fd in os.listdir(path)]

for fdpath in fdpaths:
  statinfo = os.stat(fdpath)
  create_date = datetime.fromtimestamp(statinfo.st_ctime)
  Cr_dt = create_date.strftime('%d-%m-%Y')
  modified_date = datetime.fromtimestamp(statinfo.st_mtime)
  md_dt = modified_date.strftime('%d-%m-%Y')
  if fdpath.__contains__(Yesterday_dt):
    print('Files which meets specific date  ' + fdpath)
  #print(fdpath, create_date, modified_date) # Return all files with Create and Modified dates
