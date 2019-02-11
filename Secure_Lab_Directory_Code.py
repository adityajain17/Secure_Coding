import subprocess
subprocess.call('mkdir Adi',shell=True)
i=0
for i in range(10):
    subprocess.call('mkdir C:\\Users\\User\\Desktop\\Adi\\SubFolder'+str(i+1),shell=True)
    j=0
    for j in range(10):
        subprocess.call('abc >C:\\Users\\User\\Desktop\\Adi\\SubFolder'+str(i+1)+str('/17BCE7066')+str(i*10+j+1)+'.txt',shell=True)
