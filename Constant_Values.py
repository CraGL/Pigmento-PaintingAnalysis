import numpy as np


cie1931raw =np.array([
    360,0.000129900000,0.000003917000,0.000606100000,
    365,0.000232100000,0.000006965000,0.001086000000,
    370,0.000414900000,0.000012390000,0.001946000000,
    375,0.000741600000,0.000022020000,0.003486000000,
    380,0.001368000000,0.000039000000,0.006450001000,
    385,0.002236000000,0.000064000000,0.010549990000,
    390,0.004243000000,0.000120000000,0.020050010000,
    395,0.007650000000,0.000217000000,0.036210000000,
    400,0.014310000000,0.000396000000,0.067850010000,
    405,0.023190000000,0.000640000000,0.110200000000,
    410,0.043510000000,0.001210000000,0.207400000000,
    415,0.077630000000,0.002180000000,0.371300000000,
    420,0.134380000000,0.004000000000,0.645600000000,
    425,0.214770000000,0.007300000000,1.039050100000,
    430,0.283900000000,0.011600000000,1.385600000000,
    435,0.328500000000,0.016840000000,1.622960000000,
    440,0.348280000000,0.023000000000,1.747060000000,
    445,0.348060000000,0.029800000000,1.782600000000,
    450,0.336200000000,0.038000000000,1.772110000000,
    455,0.318700000000,0.048000000000,1.744100000000,
    460,0.290800000000,0.060000000000,1.669200000000,
    465,0.251100000000,0.073900000000,1.528100000000,
    470,0.195360000000,0.090980000000,1.287640000000,
    475,0.142100000000,0.112600000000,1.041900000000,
    480,0.095640000000,0.139020000000,0.812950100000,
    485,0.057950010000,0.169300000000,0.616200000000,
    490,0.032010000000,0.208020000000,0.465180000000,
    495,0.014700000000,0.258600000000,0.353300000000,
    500,0.004900000000,0.323000000000,0.272000000000,
    505,0.002400000000,0.407300000000,0.212300000000,
    510,0.009300000000,0.503000000000,0.158200000000,
    515,0.029100000000,0.608200000000,0.111700000000,
    520,0.063270000000,0.710000000000,0.078249990000,
    525,0.109600000000,0.793200000000,0.057250010000,
    530,0.165500000000,0.862000000000,0.042160000000,
    535,0.225749900000,0.914850100000,0.029840000000,
    540,0.290400000000,0.954000000000,0.020300000000,
    545,0.359700000000,0.980300000000,0.013400000000,
    550,0.433449900000,0.994950100000,0.008749999000,
    555,0.512050100000,1.000000000000,0.005749999000,
    560,0.594500000000,0.995000000000,0.003900000000,
    565,0.678400000000,0.978600000000,0.002749999000,
    570,0.762100000000,0.952000000000,0.002100000000,
    575,0.842500000000,0.915400000000,0.001800000000,
    580,0.916300000000,0.870000000000,0.001650001000,
    585,0.978600000000,0.816300000000,0.001400000000,
    590,1.026300000000,0.757000000000,0.001100000000,
    595,1.056700000000,0.694900000000,0.001000000000,
    600,1.062200000000,0.631000000000,0.000800000000,
    605,1.045600000000,0.566800000000,0.000600000000,
    610,1.002600000000,0.503000000000,0.000340000000,
    615,0.938400000000,0.441200000000,0.000240000000,
    620,0.854449900000,0.381000000000,0.000190000000,
    625,0.751400000000,0.321000000000,0.000100000000,
    630,0.642400000000,0.265000000000,0.000049999990,
    635,0.541900000000,0.217000000000,0.000030000000,
    640,0.447900000000,0.175000000000,0.000020000000,
    645,0.360800000000,0.138200000000,0.000010000000,
    650,0.283500000000,0.107000000000,0.000000000000,
    655,0.218700000000,0.081600000000,0.000000000000,
    660,0.164900000000,0.061000000000,0.000000000000,
    665,0.121200000000,0.044580000000,0.000000000000,
    670,0.087400000000,0.032000000000,0.000000000000,
    675,0.063600000000,0.023200000000,0.000000000000,
    680,0.046770000000,0.017000000000,0.000000000000,
    685,0.032900000000,0.011920000000,0.000000000000,
    690,0.022700000000,0.008210000000,0.000000000000,
    695,0.015840000000,0.005723000000,0.000000000000,
    700,0.011359160000,0.004102000000,0.000000000000,
    705,0.008110916000,0.002929000000,0.000000000000,
    710,0.005790346000,0.002091000000,0.000000000000,
    715,0.004109457000,0.001484000000,0.000000000000,
    720,0.002899327000,0.001047000000,0.000000000000,
    725,0.002049190000,0.000740000000,0.000000000000,
    730,0.001439971000,0.000520000000,0.000000000000,
    735,0.000999949300,0.000361100000,0.000000000000,
    740,0.000690078600,0.000249200000,0.000000000000,
    745,0.000476021300,0.000171900000,0.000000000000,
    750,0.000332301100,0.000120000000,0.000000000000,
    755,0.000234826100,0.000084800000,0.000000000000,
    760,0.000166150500,0.000060000000,0.000000000000,
    765,0.000117413000,0.000042400000,0.000000000000,
    770,0.000083075270,0.000030000000,0.000000000000,
    775,0.000058706520,0.000021200000,0.000000000000,
    780,0.000041509940,0.000014990000,0.000000000000,
    785,0.000029353260,0.000010600000,0.000000000000,
    790,0.000020673830,0.000007465700,0.000000000000,
    795,0.000014559770,0.000005257800,0.000000000000,
    800,0.000010253980,0.000003702900,0.000000000000,
    805,0.000007221456,0.000002607800,0.000000000000,
    810,0.000005085868,0.000001836600,0.000000000000,
    815,0.000003581652,0.000001293400,0.000000000000,
    820,0.000002522525,0.000000910930,0.000000000000,
    825,0.000001776509,0.000000641530,0.000000000000,
    830,0.000001251141,0.000000451810,0.000000000000])

cie1931raw=cie1931raw.reshape((-1,4))


Illuminantraw=np.array([360,46.638300,
                        365,49.363700,
                        370,52.089100,
                        375,51.032300,
                        380,49.975500,
                        385,52.311800,
                        390,54.648200,
                        395,68.701500,
                        400,82.754900,
                        405,87.120400,
                        410,91.486000,
                        415,92.458900,
                        420,93.431800,
                        425,90.057000,
                        430,86.682300,
                        435,95.773600,
                        440,104.865000,
                        445,110.936000,
                        450,117.008000,
                        455,117.410000,
                        460,117.812000,
                        465,116.336000,
                        470,114.861000,
                        475,115.392000,
                        480,115.923000,
                        485,112.367000,
                        490,108.811000,
                        495,109.082000,
                        500,109.354000,
                        505,108.578000,
                        510,107.802000,
                        515,106.296000,
                        520,104.790000,
                        525,106.239000,
                        530,107.689000,
                        535,106.047000,
                        540,104.405000,
                        545,104.225000,
                        550,104.046000,
                        555,102.023000,
                        560,100.000000,
                        565,98.167100,
                        570,96.334200,
                        575,96.061100,
                        580,95.788000,
                        585,92.236800,
                        590,88.685600,
                        595,89.345900,
                        600,90.006200,
                        605,89.802600,
                        610,89.599100,
                        615,88.648900,
                        620,87.698700,
                        625,85.493600,
                        630,83.288600,
                        635,83.493900,
                        640,83.699200,
                        645,81.863000,
                        650,80.026800,
                        655,80.120700,
                        660,80.214600,
                        665,81.246200,
                        670,82.277800,
                        675,80.281000,
                        680,78.284200,
                        685,74.002700,
                        690,69.721300,
                        695,70.665200,
                        700,71.609100,
                        705,72.979000,
                        710,74.349000,
                        715,67.976500,
                        720,61.604000,
                        725,65.744800,
                        730,69.885600,
                        735,72.486300,
                        740,75.087000,
                        745,69.339800,
                        750,63.592700,
                        755,55.005400,
                        760,46.418200,
                        765,56.611800,
                        770,66.805400,
                        775,65.094100,
                        780,63.382800,
                        785,63.843400,
                        790,64.304000,
                        795,61.877900,
                        800,59.451900,
                        805,55.705400,
                        810,51.959000,
                        815,54.699800,
                        820,57.440600,
                        825,58.876500,
                        830,60.312500])

Illuminantraw=Illuminantraw.reshape((-1,2))
# max_val=Illuminantraw[:,1].max()
# max_val=255.0
# Illuminantraw[:,1]/=max_val

cyantonerraw=np.array([
    380,2.16,0.126644737,
    390,1.28,0.113486842,
    400,0.76,0.097039474,
    410,0.5,0.079495614,
    420,0.41,0.063596491,
    430,0.31,0.054276316,
    440,0.22,0.049342105,
    450,0.14,0.041666667,
    460,0.12,0.033442982,
    470,0.12,0.025767544,
    480,0.13,0.019736842,
    490,0.15,0.015350877,
    500,0.2,0.012061404,
    510,0.26,0.010416667,
    520,0.38,0.010416667,
    530,0.55,0.012609649,
    540,0.8,0.01754386,
    550,1.18,0.026864035,
    560,1.73,0.039473684,
    570,2.3,0.050986842,
    580,2.72,0.058662281,
    590,2.98,0.061951754,
    600,3.22,0.069078947,
    610,3.41,0.07620614,
    620,3.44,0.079495614,
    630,3.37,0.08004386,
    640,3.24,0.076754386,
    650,3.05,0.069627193,
    660,2.84,0.061951754,
    670,2.8,0.057017544,
    680,2.9,0.057017544,
    690,2.99,0.063596491,
    700,3.1,0.075657895])

cyantonerraw=cyantonerraw.reshape((-1,3))


magentatonerraw=np.array([
    380,0.83,0.033442982,
    390,0.95,0.031798246,
    400,1.04,0.030701754,
    410,1.06,0.029057018,
    420,1.04,0.026864035,
    430,0.98,0.024671053,
    440,0.92,0.023574561,
    450,0.93,0.025767544,
    460,1.05,0.027960526,
    470,1.23,0.030701754,
    480,1.45,0.035635965,
    490,1.69,0.040570175,
    500,1.95,0.047149123,
    510,2.29,0.054824561,
    520,2.75,0.061403509,
    530,3.04,0.064692982,
    540,3.16,0.065241228,
    550,3.35,0.074561404,
    560,3.84,0.099780702,
    570,4.2,0.151864035,
    580,3.27,0.216008772,
    590,1.36,0.203947368,
    600,0.41,0.13870614,
    610,0.13,0.097039474,
    620,0.05,0.072916667,
    630,0.001,0.055921053, 
    640,0.001,0.042214912, 
    650,0.001,0.030701754, 
    660,0.001,0.025219298,
    670,0.001,0.02247807, 
    680,0.001,0.018092105, 
    690,0.001,0.016995614, 
    700,0.001,0.01370614])

magentatonerraw=magentatonerraw.reshape((-1,3))

yellowtonerraw=np.array([
    380,3.45,0.080592105,
    390,3.69,0.076754386,
    400,3.76,0.086074561,
    410,3.82,0.079495614,
    420,3.82,0.077302632,
    430,3.74,0.072916667,
    440,3.57,0.069627193,
    450,3.28,0.064144737,
    460,2.91,0.059758772,
    470,2.39,0.057565789,
    480,1.65,0.050986842,
    490,0.86,0.043311404,
    500,0.37,0.038377193,
    510,0.13,0.038925439,
    520,0.04,0.04002193,
    530,0.001,0.040570175,
    540,0.001,0.040570175,
    550,0.001,0.040570175,
    560,0.001,0.039473684,
    570,0.001,0.04002193,
    580,0.001,0.038925439,
    590,0.001,0.033991228,
    600,0.001,0.028508772,
    610,0.001,0.024671053,
    620,0.001,0.020833333,
    630,0.001,0.023574561,
    640,0.001,0.023026316,
    650,0.001,0.020285088,
    660,0.001,0.020833333,
    670,0.001,0.01754386,
    680,0.001,0.012609649,
    690,0.001,0.014254386,
    700,0.001,0.018640351])

yellowtonerraw=yellowtonerraw.reshape((-1,3))

# print cie1931raw.shape
# print Illuminantraw.shape
# print cyantonerraw.shape
# print magentatonerraw.shape
# print yellowtonerraw.shape



cie1931new=np.ones((cyantonerraw.shape[0],cie1931raw.shape[1]))
Illuminantnew=np.ones((cyantonerraw.shape[0], Illuminantraw.shape[1]))
cie1931new[:,0]=cyantonerraw[:,0]
Illuminantnew[:,0]=cyantonerraw[:,0]
k=0
for i in xrange(len(cie1931raw)):
    if cie1931raw[i,0]==cie1931new[k,0]: ###if same wavelength 
        cie1931new[k,:]=cie1931raw[i,:]
        Illuminantnew[k,:]=Illuminantraw[i,:]
        k+=1
    if k==len(cie1931new):
        break

# print cie1931new
# print Illuminantnew


def sample_by_average_wavelength(raw, length): ### like 32 to 16, 8, 4
    L=raw.shape[0]
    ratio=L/length
    samples=np.zeros((length, raw.shape[1]))
    for i in xrange(len(samples)):
        for j in xrange(ratio):
            samples[i]+=raw[i*ratio+j]
        samples[i]/=ratio
    return samples
    

def sample_by_interpolation(raw, length): #### like 16 to 14, 14 to 12, 12 to 10, 8 to 6, or 4 to 3 ?
    L=raw.shape[0]
    ratio=(L-1)*1.0/(length+1)
    samples=np.zeros((length, raw.shape[1]))
    j=1
    for i in xrange(L-1):
        if (i<(ratio*j)) and ((ratio*j)<=(i+1)) and j<=length:
#             print (ratio*j)
            samples[j-1]=raw[i]+((ratio*j)-i)*(raw[i+1]-raw[i])
            j+=1
    return samples



 ####sample data from cie1931new, Illuminantnew, cyantonerraw, magentatonerraw and yellowtonerraw.
option=3

if option==0:
    pass
else:
    if option==1:  ### 32 wavelength
        length=32
    if option==2:  ### 16 wavelength
        length=16
    if option==3:  ### 8 wavelength
        length=8
    if option==4:  ### 4 wavelength
        length=4

    cie1931new=sample_by_average_wavelength(cie1931new[1:,:],length)
    Illuminantnew=sample_by_average_wavelength(Illuminantnew[1:,:],length)
    cyantonerraw=sample_by_average_wavelength(cyantonerraw[1:,:],length)
    magentatonerraw=sample_by_average_wavelength(magentatonerraw[1:,:],length)
    yellowtonerraw=sample_by_average_wavelength(yellowtonerraw[1:,:],length)



    # ###### use 3 wavelength (OLD)
    # # length2=3
    # # cie1931new=sample_by_interpolation(cie1931new,length2)
    # # Illuminantnew=sample_by_interpolation(Illuminantnew,length2)
    # # cyantonerraw=sample_by_interpolation(cyantonerraw,length2)
    # # magentatonerraw=sample_by_interpolation(magentatonerraw,length2)
    # # yellowtonerraw=sample_by_interpolation(yellowtonerraw,length2)


    # ###### use 3 wavelength (NEW)
    # length2=3
    # cie1931new=np.ones((length2,4))
    # cie1931new[:,1:]= np.identity(length2)
    # Illuminantnew=np.ones((length2,2))

    # print "#####using wavelength number: ", len(cie1931new[:,1:])
    # print cie1931new[:,1:]
    # print Illuminantnew[:,1]



#### cmf function
R_xyzcoeff=cie1931new[:,1:].transpose()

# ### xyz to linear rgb
xyztorgb=np.array([[3.2404542, -1.5371385, -0.4985314],
                   [-0.9692660,  1.8760108,  0.0415560],
                   [0.0556434, -0.2040259,  1.0572252]
                  ])


import os,sys
import subprocess
import errno

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

            
MODEL='normal'
# MODEL='infinite'

#### only used in one variable Q recovering.
# S_Constant=1.0
S_Constant=0.1




