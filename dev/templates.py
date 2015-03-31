# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 19:03:11 2015

@author: jmmauricio
"""
import numpy as np

template_file = r'/home/jmmauricio/Documents/public/jmmauricio6/RESEARCH/benches/ieee_12_generic/doc/source/_static/plot_eigenvalues_template.js'
output_file = r'/home/jmmauricio/Documents/public/jmmauricio6/RESEARCH/benches/ieee_12_generic/doc/build/html/_static/plot_eigenvalues_base.js'

template = open(template_file,'r')

template_str = template.read()

base_x =2.0* np.array([ -34.609999999999999, -34.609999999999999, -36.399999999999999, -34.68, -32.450000000000003, -20.829999999999998, -20.829999999999998, -23.760000000000002, -23.469999999999999, -22.440000000000001, -21.27, -17.539999999999999, -15.609999999999999, -1.2, -1.2, -2.7000000000000002, -2.7000000000000002, -10.039999999999999, -0.059999999999999998, -0.059999999999999998, -5.29, -5.29, -6.8399999999999999, -5.8600000000000003, -4.6399999999999997, -4.6399999999999997, -4.4500000000000002, -3.46, 0.0, -0.34999999999999998, -0.34999999999999998, -0.10000000000000001, -0.98999999999999999, -1.46, -1.78, -1.78, -2.0699999999999998, -33.329999999999998, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0])
base_x_list = list(base_x)
xs= "{base: 'base_x', pvs_10: 'pvs_10_x'}"
columns= [
  ["base_x"]+base_x_list,
  ["base", 3.7999999999999998, -3.7999999999999998, 0.0, 0.0, 0.0, 7.46, -7.46, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 8.3699999999999992, -8.3699999999999992, 7.1399999999999997, -7.1399999999999997, 0.0, 5.1500000000000004, -5.1500000000000004, 3.9900000000000002, -3.9900000000000002, 0.0, 0.0, 0.62, -0.62, 0.0, 0.0, 0.0, 0.14999999999999999, -0.14999999999999999, 0.0, 0.0, 0.0, 0.40999999999999998, -0.40999999999999998, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  ["pvs_10_x",-34.850000000000001, -34.850000000000001, -36.420000000000002, -34.710000000000001, -32.719999999999999, -20.789999999999999, -20.789999999999999, -23.829999999999998, -23.600000000000001, -22.57, -21.27, -17.510000000000002, -15.779999999999999, -1.23, -1.23, -3.2000000000000002, -3.2000000000000002, -10.32, -0.080000000000000002, -0.080000000000000002, -2.1400000000000001, -2.1400000000000001, -4.8499999999999996, -4.8499999999999996, -4.1200000000000001, -4.1200000000000001, -6.8899999999999997, 0.0, -0.20999999999999999, -0.10000000000000001, -0.59999999999999998, -1.02, -1.45, -1.8600000000000001, -1.8600000000000001, -2.21, -3.3300000000000001, -5.8399999999999999, -5.6399999999999997, -4.6799999999999997, -4.6799999999999997, -4.4299999999999997, -4.4500000000000002, -33.329999999999998, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0],
  ["pvs_10", 3.8399999999999999, -3.8399999999999999, 0.0, 0.0, 0.0, 7.46, -7.46, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 8.3699999999999992, -8.3699999999999992, 7.5, -7.5, 0.0, 5.0, -5.0, 4.6799999999999997, -4.6799999999999997, 2.96, -2.96, 4.2199999999999998, -4.2199999999999998, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.38, -0.38, 0.0, 0.0, 0.0, 0.0, 0.58999999999999997, -0.58999999999999997, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]            
  ]
type = "'scatter'"

replace_dict = {'{xs}':xs,'{columns}':columns,'{type}':type}

for item in replace_dict:
    template_str = template_str.replace(item,str(replace_dict[item]))    

output_str = template_str   
#output_str = template_str.format(columns='hola')

output = open(output_file,'w')
output.write(output_str)

template.close()
output.close()