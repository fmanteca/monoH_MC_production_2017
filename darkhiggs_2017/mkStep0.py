import os 
import sys
import create_cfgFile

NAMES = {"darkHiggs_theta_0p01_gq_0p25_gx_1p0_mhs_160_mx_100_mZp_1000_WW", "darkHiggs_theta_0p01_gq_0p25_gx_1p0_mhs_160_mx_100_mZp_1200_WW", "darkHiggs_theta_0p01_gq_0p25_gx_1p0_mhs_160_mx_100_mZp_1500_WW", "darkHiggs_theta_0p01_gq_0p25_gx_1p0_mhs_160_mx_100_mZp_195_WW", "darkHiggs_theta_0p01_gq_0p25_gx_1p0_mhs_160_mx_100_mZp_250_WW", "darkHiggs_theta_0p01_gq_0p25_gx_1p0_mhs_160_mx_100_mZp_295_WW", "darkHiggs_theta_0p01_gq_0p25_gx_1p0_mhs_160_mx_100_mZp_300_WW", "darkHiggs_theta_0p01_gq_0p25_gx_1p0_mhs_160_mx_100_mZp_500_WW", "darkHiggs_theta_0p01_gq_0p25_gx_1p0_mhs_160_mx_150_mZp_1000_WW", "darkHiggs_theta_0p01_gq_0p25_gx_1p0_mhs_160_mx_150_mZp_1500_WW", "darkHiggs_theta_0p01_gq_0p25_gx_1p0_mhs_160_mx_150_mZp_195_WW", "darkHiggs_theta_0p01_gq_0p25_gx_1p0_mhs_160_mx_150_mZp_250_WW", "darkHiggs_theta_0p01_gq_0p25_gx_1p0_mhs_160_mx_150_mZp_295_WW", "darkHiggs_theta_0p01_gq_0p25_gx_1p0_mhs_160_mx_150_mZp_300_WW", "darkHiggs_theta_0p01_gq_0p25_gx_1p0_mhs_160_mx_200_mZp_1200_WW", "darkHiggs_theta_0p01_gq_0p25_gx_1p0_mhs_160_mx_200_mZp_250_WW", "darkHiggs_theta_0p01_gq_0p25_gx_1p0_mhs_160_mx_200_mZp_295_WW", "darkHiggs_theta_0p01_gq_0p25_gx_1p0_mhs_160_mx_200_mZp_300_WW", "darkHiggs_theta_0p01_gq_0p25_gx_1p0_mhs_160_mx_200_mZp_500_WW"}

for n in NAMES:
    os.system('python create_cfgFile.py ' + n + ' ' + n + '.lhe')
