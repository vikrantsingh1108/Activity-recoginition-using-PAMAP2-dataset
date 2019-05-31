import glob
import pandas as pd
print('Pandas Version:\t%s' % pd.__version__)
import numpy as np
import os
import argparse
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context('talk')
sns.set_style('white')



def command_line_argument_parser():
	parser = argparse.ArgumentParser()
	parser = argparse.ArgumentParser(description='Help for Command line arguments')
	parser.add_argument("dat_file", help="Name of Configuration File")
	command_line_params = parser.parse_args()
	transform(command_line_params.dat_file)

def transform(filename):
	print "here"
	data = pd.read_csv(filename, sep=' ',
					  names=['timestamp','activityID','heartrate', \
							 'IMU_hand_temp','IMU_hand_ax1','IMU_hand_ay1','IMU_hand_az1', \
							 'IMU_hand_ax2','IMU_hand_ay2','IMU_hand_az2', \
							 'IMU_hand_rotx','IMU_hand_roty','IMU_hand_rotz', \
							 'IMU_hand_magx','IMU_hand_magy','IMU_hand_magz', \
							 'IMU_hand_oru','IMU_hand_orv','IMU_hand_orw', 'IMU_hand_orx', \
							 'IMU_chest_temp','IMU_chest_ax1','IMU_chest_ay1','IMU_chest_az1', \
							 'IMU_chest_ax2','IMU_chest_ay2','IMU_chest_az2', \
							 'IMU_chest_rotx','IMU_chest_roty','IMU_chest_rotz', \
							 'IMU_chest_magx','IMU_chest_magy','IMU_chest_magz', \
							 'IMU_chest_oru','IMU_chest_orv','IMU_chest_orw', 'IMU_chest_orx', \
							 'IMU_ankle_temp','IMU_ankle_ax1','IMU_ankle_ay1','IMU_ankle_az1', \
							 'IMU_ankle_ax2','IMU_ankle_ay2','IMU_ankle_az2', \
							 'IMU_ankle_rotx','IMU_ankle_roty','IMU_ankle_rotz', \
							 'IMU_ankle_magx','IMU_ankle_magy','IMU_ankle_magz', \
							 'IMU_ankle_oru','IMU_ankle_orv','IMU_ankle_orw', 'IMU_ankle_orx'])

	dt = 1.0/100.0 # the activities were with 50Hz
	#data.index = np.arange(0, len(data)*dt, dt)
	#data.index.name='time'
	data.index = data.timestamp

	data=data.drop(['heartrate' ,'IMU_hand_temp', 'IMU_chest_temp', 'IMU_ankle_temp','IMU_hand_rotx','IMU_hand_roty','IMU_hand_rotz', 'IMU_hand_magx','IMU_hand_magy','IMU_hand_magz','IMU_chest_rotx','IMU_chest_roty','IMU_chest_rotz', 'IMU_chest_magx','IMU_chest_magy','IMU_chest_magz', 'IMU_ankle_rotx','IMU_ankle_roty','IMU_ankle_rotz',  'IMU_ankle_magx','IMU_ankle_magy','IMU_ankle_magz'], axis=1)

	activitymap = {1: 'lying',
				   2: 'sitting',
				   3: 'standing',
				   4: 'walking',
				   5: 'running',
				   6: 'cycling',
				   7: 'Nordic walking',
				   9: 'watching TV',
				   10: 'computer work',
				   11: 'car driving',
				   12: 'ascending stairs',
				   13: 'descending stairs',
				   16: 'vacuum cleaning',
				   17: 'ironing',
				   18: 'folding laundry',
				   19: 'house cleaning',
				   20: 'playing soccer',
				   24: 'rope jumping',
				   0: 'other'}

	data['activity'] = data['activityID'].apply(activitymap.get)
	data.drop(data.index[(data.activity!='lying') & (data.activity!='sitting') & (data.activity!='standing') & (data.activity!='ascending stairs') & (data.activity!='cycling') & (data.activity!='running') & (data.activity!='walking') & (data.activity!='ironing')], inplace=True)
	activities = data.groupby('activity')
	data=data.drop(['activityID'],axis=1)

	data.drop(data[data.activity=='lying'].iloc[:1000].index, inplace=True)
	data.drop(data[data.activity=='lying'].iloc[-1000:].index, inplace=True)
	data.drop(data[data.activity=='sitting'].iloc[:1000].index, inplace=True)
	data.drop(data[data.activity=='sitting'].iloc[-1000:].index, inplace=True)
	data.drop(data[data.activity=='running'].iloc[:1000].index, inplace=True)
	data.drop(data[data.activity=='running'].iloc[-1000:].index, inplace=True)
	data.drop(data[data.activity=='ascending stairs'].iloc[:1000].index, inplace=True)
	data.drop(data[data.activity=='ascending stairs'].iloc[-1000:].index, inplace=True)
	data.drop(data[data.activity=='walking'].iloc[:1000].index, inplace=True)
	data.drop(data[data.activity=='walking'].iloc[-1000:].index, inplace=True)
	data.drop(data[data.activity=='cycling'].iloc[:1000].index, inplace=True)
	data.drop(data[data.activity=='cycling'].iloc[-1000:].index, inplace=True)
	data.drop(data[data.activity=='standing'].iloc[:1000].index, inplace=True)
	data.drop(data[data.activity=='standing'].iloc[-1000:].index, inplace=True)
	data.drop(data[data.activity=='ironing'].iloc[:1000].index, inplace=True)
	data.drop(data[data.activity=='ironing'].iloc[-1000:].index, inplace=True)

	"""
	data.dropna(subset=['activityID','heartrate' , 'IMU_hand_temp', 'IMU_chest_temp', 'IMU_ankle_temp',
						  'IMU_hand_rotx','IMU_hand_roty','IMU_hand_rotz',
						  'IMU_hand_magx','IMU_hand_magy','IMU_hand_magz',
						  'IMU_chest_rotx','IMU_chest_roty','IMU_chest_rotz',
						  'IMU_chest_magx','IMU_chest_magy','IMU_chest_magz',
						  'IMU_ankle_rotx','IMU_ankle_roty','IMU_ankle_rotz',
						  'IMU_ankle_magx','IMU_ankle_magy','IMU_ankle_magz',
						 ], inplace=True)
	"""

	filename=filename.split(".")[0]
	np.savetxt(filename+".csv",data, fmt= '%s')

if __name__ == "__main__":
	#command_line_argument_parser()
	files = glob.glob("*.dat")
	for i in files:
		transform(i)

	
