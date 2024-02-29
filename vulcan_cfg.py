# ============================================================================= 
# Configuration file of VULCAN:  
# ============================================================================= 

# ====== Setting up the elements included in the network ======
atom_list = ['H', 'O', 'C', 'N' ,'S' ,'He' ] 
loss_ex = ['C','O','S']
# ====== Setting up paths and filenames for the input and output files  ======
# input:
network = 'thermo/SNCHO_DMS_photo_network_Tsai2024.txt'
use_lowT_limit_rates = False
gibbs_text = 'thermo/gibbs_text.txt' # (all the nasa9 files must be placed in the folder: thermo/NASA9/)
cross_folder = 'thermo/photo_cross/'
com_file = 'thermo/all_compose.txt'
atm_file = 'atm/atm_K2-18b-oceanAb03-GJ436.txt' # TP and Kzz (optional) file
sflux_file = 'atm/stellar_flux/sflux-GJ436.txt'      #sflux-GJ436.txt # sflux-HD189_B2020.txt This is the flux density at the stellar surface
top_BC_flux_file = 'atm/BC_top.txt' # the file for the top boundary conditions
bot_BC_flux_file = 'atm/BC_bot_S_organic_wCH4.txt' # the file for the lower boundary conditions

vul_ini = 'output/' # the file to initialize the abundances for ini_mix = 'vulcan_ini'
# output:
output_dir = 'output/'
plot_dir = 'plot/'
movie_dir = 'plot/movie/K2-18b-Sorg1X-ini1000ppmCH4-t3e15/'
out_name =  'K2-18b-Sorg1X-ini1000ppmCH4-t3e15.vul' # output file name

# ====== Setting up the elemental abundance ======
use_solar = False # True: using the solar abundance from Table 8. K.Lodders 2019; False: using the customized elemental abundance. 
# customized elemental abundance (only read when use_solar = False)
# O_H = 5.37E-4 *100  #*(0.793)
# C_H = 2.95E-4 *100
# N_H = 7.08E-5
# S_H = 1.41E-5
# He_H = 0.0838

# following my 2021 paper
# Asplund 2009
O_H = 4.8978E-4 *100 
C_H = 2.6915E-4 *100
N_H = 6.7608E-5 *100 
S_H = 1.3183E-5 *100 
He_H = 0.08511

ini_mix = 'EQ' # Options: 'EQ', 'const_mix', 'vulcan_ini', 'table' (for 'vulcan_ini, the T-P grids have to be exactly the same)
fastchem_met_scale = 100. # scaling factor for other elements in fastchem (e.g., if fastchem_met_scale = 0.1, other elements such as Si and Mg will take 0.1 solar values)

use_ini_cold_trap = True

# Initialsing uniform (constant with pressure) mixing ratios (only reads when ini_mix = const_mix)
const_mix = {} 

# reset the equilibirum abundances to the following uniform VMR
const_mix_with_EQ = {'CO2': 0.01, 'CH4': 1e-3} # modifed for the Hycean DMS run

# ====== Setting up photochemistry ======
use_photo = True
# astronomy input

r_star = 0.4445 # Rs = 0.48 R_sun for 45 Myr, Rs = 0.36 R_sun for 120 Myr, and 0.33 for 5 Gyr (Table 1 in Peacock 2020)

Rp = 0.2328 *7.1492E9 # Planetary radius (cm) (for computing gravity)
orbit_radius = 0.1591 # planet-star distance in A.U.

sl_angle = 58 /180.*3.14159 # the zenith angle of the star in degree (usually 58 deg for the dayside average)
f_diurnal = 1. # to account for the diurnal average of solar flux (i.e. 0.5 for Earth; 1 for tidally-locked planets) 
scat_sp = ['H2', 'He'] # the bulk gases that contribute to Rayleigh scattering
T_cross_sp = [] # warning: slower start! available atm: 'CO2','H2O','NH3', 'SH','H2S','SO2', 'S2', 'COS', 'CS2'

edd = 0.5 # the Eddington coefficient 
dbin1 = 0.1  # the uniform bin width < dbin_12trans (nm)
dbin2 = 2.   # the uniform bin width > dbin_12trans (nm)
dbin_12trans = 240. # the wavelength switching from dbin1 to dbin2 (nm)

# the frequency to update the actinic flux and optical depth
ini_update_photo_frq = 100
final_update_photo_frq = 5

# ====== Setting up ionchemistry ======
use_ion = False
if use_photo == False and use_ion == True:
    print ('Warning: use_ion = True but use_photo = False')
# photoionization needs to run together with photochemistry


# ====== Setting up parameters for the atmosphere ======
atm_base = 'H2' #Options: 'H2', 'N2', 'O2', 'CO2 -- the bulk gas of the atmosphere: changes the molecular diffsion, thermal diffusion factor, and settling velocity
rocky = False # for the surface gravity
nz = 100   # number of vertical layers
P_b = 1e6  # pressure at the bottom (dyne/cm^2)
P_t = 1e-2 # pressure at the top (dyne/cm^2)
use_Kzz = True
use_moldiff = True
use_vz = False
atm_type = 'file'  # Options: 'isothermal', 'analytical', 'file', or 'vulcan_ini' 'table'

Kzz_prof = 'Pfunc' # Options: 'const','file' or 'Pfunc' (Kzz increased with P^-0.4)
K_max = 1e5        # for Kzz_prof = 'Pfunc'
K_p_lev = 0.01     # for Kzz_prof = 'Pfunc'


vz_prof = 'const'  # Options: 'const' or 'file'
gs = 1243.         # surface gravity (cm/s^2)  (HD189:2140  HD209:936)
Tiso = 1000 # only read when atm_type = 'isothermal'
# setting the parameters for the analytical T-P from (126)in Heng et al. 2014. Only reads when atm_type = 'analytical' 
# T_int, T_irr, ka_L, ka_S, beta_S, beta_L
para_warm = [120., 1500., 0.1, 0.02, 1., 1.]
para_anaTP = para_warm
const_Kzz = 1.E10 # (cm^2/s) Only reads when use_Kzz = True and Kzz_prof = 'const'
const_vz = 0 # (cm/s) Only reads when use_vz = True and vz_prof = 'const'

# frequency for updating dz and dzi due to change of mu
update_frq = 100 

# ====== Setting up the boundary conditions ======
# Boundary Conditions:
use_topflux = False

use_botflux = True

use_fix_sp_bot = {'N2':0.006, 'CO2':0.01} # , 'N2':0.00658 fixed mixing ratios at the lower boundary
diff_esc = ['H'] # species for diffusion-limit escape at TOA
max_flux = 1e13  # upper limit for the diffusion-limit fluxes

use_sat_surfaceH2O = True


# modifed for the Hycean DMS run
use_fix_H2He = True
use_fix_layer_co2 = True
# modifed for the Hycean DMS run

# ====== Reactions to be switched off  ======
remove_list = [315,316] # 315,316, 465,466, 817,818  ,729,730,731,732  315,316 in pairs e.g. [1,2]

# == Condensation ======
use_relax = ['H2O']

use_condense = True

use_settling = True
start_conden_time = 0
stop_conden_time = 1e3 # after this time to fix the condensable species
condense_sp = ['H2O']     
non_gas_sp = ['H2O_l_s']
r_p = {'H2O_l_s': 5e-3}  # particle radius in cm (1e-4 = 1 micron)
rho_p = {'H2O_l_s': 1} # particle density in g cm^-3
fix_species = ['H2O', 'H2O_l_s']      # fixed the condensable species after condensation-evapoation EQ has reached  
fix_species_time = stop_conden_time  
fix_species_from_coldtrap_lev = True

humidity = 0.5

# ====== steady state check ======
st_factor = 0.5
conv_step = 500

# ====== Setting up numerical parameters for the ODE solver ====== 
ode_solver = 'Ros2' # case sensitive
use_print_prog = True
use_print_delta = False
print_prog_num = 500  # print the progress every x steps 
dttry = 1.E-10

trun_min = 3e13
runtime = 3e15

dt_min = 1.E-10
#dt_max = 5e13
dt_max = 1e12

dt_var_max = 2.
dt_var_min = 0.5
count_min = 120
count_max = int(20000)
atol = 1.E-1 # Try decreasing this if the solutions are not stable
mtol = 1e-18 #1.E-20  
mtol_conv = 1e-15 #1.E-18
pos_cut = 0
nega_cut = -1.
loss_eps = 1
yconv_cri = 0.01 # for checking steady-state
slope_cri = 1.e-4
yconv_min = 0.1
flux_cri = 0.1
flux_atol = 1. # the tol for actinc flux (# photons cm-2 s-1 nm-1)
### use with caution
conver_ignore = ['HC3N'] # added 2023. to get rid off non-convergent species, e.g. HC3N without sinks 

# ====== Setting up numerical parameters for Ros2 ODE solver ====== 
rtol = 0.75             # relative tolerence for adjusting the stepsize 
post_conden_rtol = 2.75  # switched to this value after fix_species_time

# ====== Setting up for ouwtput and plotting ======
# plotting:
plot_TP = 0
use_live_plot = 1
use_live_flux = 0
use_plot_end = False
use_plot_evo = False
use_save_movie = 1
use_flux_movie = False
plot_height = False
use_PIL = True 
live_plot_frq = 10
save_movie_rate = 20
y_time_freq = 1  #  storing data for every 'y_time_freq' step
plot_spec = ['H2O',  'CO2','CH4', 'CO', 'NH3', 'H2S', 'SO2','CH3SCH3' ] # 'CH3S2CH3', 'CS', 'COS','SO', 'S2'
# output:
output_humanread = False
use_shark = False
save_evolution = 0  # save the evolution of chemistry (y_time and t_time) for every save_evo_frq step
save_evo_frq = 100
