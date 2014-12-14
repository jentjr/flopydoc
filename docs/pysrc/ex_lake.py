# ExampleLake - Flopy example of multi-layer steady model with one fixed head cell 
# This is an example of steady flow in a multi-layer model. 
# Heads are fixed along all outer boundaries to 100 meters. 
# In the center cell in the top layer, the head is fixed to 90 meters. 
 
# Import the Python packages that we need 
import mf 
import numpy as np 
import mfreadbinaries as mfrdbin 
import matplotlib.pyplot as mtpl 
import os 
import tempfile 
 
# name an path of the MODFLOW run 
name = 'ExLake' 
# Define the folder workspace (optionnal, if omitted the output files 
# will be created in the folder where this script is located). 
model_ws = os.path.join(tempfile.gettempdir(), '00MF_ws') 
# Define the MODFLOW exe path, name and version 
# As specified below, it requires that the user copies the MODFLOW-exe-file in the workspace folder. 
# Alternatively, indicate the full path where the MODFLOW-exe-file is located. 
mfexepath = 'mf2k.exe' 
version = 'mf2k' # mf2k or mf2005 
 
# Define the problem. 
# A grid of N by N cells. 
#Size of model is L by L, aquifer thickness H, hydraulic conductivity is k. 
Nlay = 10 
N = 101 
L = 400.0 
H = 50.0 
k = 1.0 
T = k*H / Nlay 
 
# Create the modflow model 
ml = mf.modflow(modelname=name, exe_name=mfexepath, version = version, model_ws = model_ws) 
 
# Add the Discretization package 
Hlay = H / Nlay 
bot = [] 
for i in range(1,Nlay): 
    bot.extend( (-float(i)/Nlay * H, -float(i)/Nlay * H) ) 
bot.append(-H) 
delrow = delcol = L/(N-1) 
discret = mf.mfdis(ml,N,N,Nlay,delr=delrow,delc=delcol,top=0.0,botm=bot) 
discret.write_file() 
 
# Add the Basic package 
Nhalf = (N-1)/2 
ibound = np.ones((N,N,Nlay),'int') 
ibound[0,:,:] = -1; ibound[-1,:,:] = -1; ibound[:,0,:] = -1; ibound[:,-1,:] = -1 
ibound[Nhalf,Nhalf,0]=-1 
start=100.0*np.ones((N,N)) 
start[Nhalf,Nhalf] = 90 
bas = mf.mfbas(ml,ibound=ibound,strt=start) 
bas.write_file() 
 
# Add the BlockCenterFlow package, the Output Control package, and the PCG solver package 
vc = k / (H/Nlay) 
bcf = mf.mfbcf(ml,laycon=0,tran=T,vcont=vc) 
bcf.write_file() 
oc = mf.mfoc(ml) 
oc.write_file() 
pcg = mf.mfpcg(ml) 
pcg.write_file() 
 
print '\nMODFLOW packages created.\nRunning MODFLOW...\n' 
 
# Write all MODFLOW files, call MODFLOW, and read the heads back into Python 
ml.write_name_file() 
ml.run_model(pause = False) 
h_MF_fn = os.path.join(ml.model_ws, name + '.hds') 
h = mfrdbin.mfhdsread(ml, 'LF95').read_all(h_MF_fn) 
h1 = h[1] 
del h 
 
print '\nExporting plots' 
 
# Store some arrays for plotting 
x = np.linspace(-L/2,L/2,N) 
xg,yg = np.meshgrid(x,x) 
 
#Contour the heads in the first layer 
mtpl.figure() 
valg = h1[0][:,:,:] 
mtpl.contour(xg,yg,valg[:,:,0],np.linspace(90,100,51)) 
mtpl.axis('scaled') 
mtpl.title('Heads contour in the first layer') 
plt_export_fn = os.path.join(ml.model_ws, '_plt_0_headscontours.png') 
mtpl.savefig(plt_export_fn,dpi=150) 
 
#Make a cross-sectional figure of layers 1, 2, and 10 
mtpl.figure() 
mtpl.plot(xg[0,:],valg[:,50,0],label='Top layer') 
mtpl.plot(xg[0,:],valg[:,50,1],label='Second layer') 
mtpl.plot(xg[0,:],valg[:,50,9],label='Bottom layer') 
mtpl.title('Cross-section view of column #50') 
mtpl.legend(loc='best') 
plt_export_fn = os.path.join(ml.model_ws, '_plt_1_crosssection.png') 
mtpl.savefig(plt_export_fn,dpi=150) 
mtpl.close('all') 
 
print '\nSuccessful FloPy run!\nOutput written in %s' % ml.model_ws