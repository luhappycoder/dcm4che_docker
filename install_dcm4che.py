#!/usr/bin/env python3

import sys
import os

if len(sys.argv) != 2:
	print(
		"""Usage: python3 install_dcm4che.py install_folder(absolute path)
	    For sudoer recommend: python3 install_dcm4che.py /opt
	    For normal user recommend: python3 install_dcm4che.py $HOME/app"""
    )
	sys.exit(0)


#get version number from dcm4che_version.txt
with open('dcm4che_version.txt','r') as f:
	VERSION=f.readline()

# download and install dcm4che
DEST=f'{sys.argv[1]}'
os.makedirs(DEST,exist_ok=True)
install_cmd = f'''
wget -O temp.zip https://sourceforge.net/projects/dcm4che/files/dcm4che3/{VERSION}/dcm4che-{VERSION}-bin.zip/download
unzip -o temp.zip -d {DEST}
rm temp.zip
'''
r = os.system(install_cmd)

PROFILE=f'{os.environ["HOME"]}/.profile'
with open(PROFILE, "a+") as f:
   lines = f.readlines()
   if '#dcm4che' not in lines:
	   f.writelines(['#dcm4che\n',f'PATH="{DEST}/dcm4che-{VERSION}/bin:$PATH"\n'])

#test installation
test_cmd=f'''
. {PROFILE}
getscu -h >/dev/null
'''
r = os.system(test_cmd)

if r == 0:
    print("Install success")
else:
    print("Install fail")

# config
#For retrieving physio dicom files. without this line, all the physio series will not be retrieved with getscu
r = os.system(f'''echo "1.3.12.2.1107.5.9.1:ImplicitVRLittleEndian;ExplicitVRLittleEndian" >>{DEST}/dcm4che-{VERSION}/etc/getscu/store-tcs.properties''')

#allow the getscu client to download CFMM's 9.4T data.
r = os.system(f'''echo 'EnhancedMRImageStorage:ImplicitVRLittleEndian;ExplicitVRLittleEndian'>>{DEST}/dcm4che-{VERSION}/etc/getscu/store-tcs.properties''')

sys.exit(r)

# # this is a bash script
# LETSENCRYPT_CA_URL=https://letsencrypt.org/certs/letsencryptauthorityx3.pem.txt
# for f in $(find ${D_DIR}/etc -name cacerts.jks)
# do
#   keytool -noprompt -importcert -trustcacerts -alias letsencrypt -file <(wget -O - -o /dev/null ${LETSENCRYPT_CA_URL}) -keystore $f -storepass secret
# done


