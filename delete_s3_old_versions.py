import json
import sys
import os

bucket=sys.argv[1]
key=sys.argv[2]

os.system('aws s3api list-object-versions --bucket '+bucket+' --prefix '+key+' >> file_list.json')

with open('file_list.json','r') as jf:
	all=json.load(jf)
        for i in all['Versions']:
		if i['IsLatest'] == False:
                	delete_command = 'aws s3api delete-object --bucket '+bucket+' --key '+i['Key']+' --version-id '+i['VersionId']
                	os.system(delete_command)

