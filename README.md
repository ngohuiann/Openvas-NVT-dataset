To extract OpenVAS NVTs name and CVSS score, modify the nvt_extract.py code's gvm username and password as a non-root user.
```
python nvt_extract.py
```
The generated csv file will be saved in the directory where the nvt_extract.py file is. \n
The code will not extract NVTs without a CVSS scoring (NVTs with CVSS 0.0 will be extracted). \n\n

!Note: this python code is by no means coded securely, delete after finish running it.
