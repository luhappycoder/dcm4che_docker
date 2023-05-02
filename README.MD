# Aim:
    
	A parent image for CFMM's dcm4che based applications.

## Usage example:

`docker run --rm -it luhappycoder/dcm4che:0.4 findscu -h`

## change history:

0.4:added `'echo 'EnhancedMRImageStorage:ImplicitVRLittleEndian;ExplicitVRLittleEndian'>>/opt/dcm4che-3.3.8/etc/getscu/store-tcs.properties'`, for retrieving physio dicom files. 


0.3:added `'echo 1.3.12.2.1107.5.9.1:ImplicitVRLittleEndian;ExplicitVRLittleEndian'>>/opt/dcm4che-3.3.8/etc/getscu/store-tcs.properties`, allow the getscu client to download CFMM's 9.4T data.

0.2: removed pydicom installation

