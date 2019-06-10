# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# fix random seed for reproducibility
np.random.seed(7)

length = 1000  # [m]
interval = 0.1  # [m]
orig = np.arange(length, step=interval)
tl = orig


# parameters:
noise = np.random.normal(10, 2, size=int(length/interval))
penetration = np.sin(orig*0.01)
penetration = penetration + np.cos(orig*0.25)
penetration = penetration + np.cos(orig*7)
penetration = penetration + np.sin(orig*0.2)
penetration = penetration + np.cos(orig*0.013)
penetration = penetration + noise

adv_force = np.random.normal(10000, 2500, size=int(length/interval))

rpm = np.full(int(length/interval), 5)
idx = np.where(adv_force > 15000)[0]
rpm[idx] = 4
idx = np.where(adv_force < 5000)[0]
rpm[idx] = 6

speed = penetration * rpm

noise = np.random.normal(2, 0.7, size=int(length/interval))
torque = np.cos(orig)
torque = torque + np.sin(orig*4)
torque = torque + np.cos(orig*7)
torque = torque + np.sin(orig*0.2)
torque = torque + np.sin(orig*0.05)
torque = torque + noise
torque = np.where(torque <= 0, np.median(torque), torque)


# save data as csv file
df = pd.DataFrame({'tunnellength [m]': tl,
                   'penetration [mm/rot]': penetration,
                   'advance_force [kN]': adv_force,
                   'rev_per_min [rot/min]': rpm,
                   'advance_speed [mm/min]': speed,
                   'torque [MNm]': torque})

df.to_csv('synth_TBM_data.csv', index=False)
