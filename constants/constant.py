COL_HEADER = ['timestamp','activityID','heartrate', \
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
              'IMU_ankle_oru','IMU_ankle_orv','IMU_ankle_orw', 'IMU_ankle_orx']

ACTIVITY_MAP ={1: 'lying',
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

DROP_COL_HEADER = ['heartrate' ,'IMU_hand_temp', 'IMU_chest_temp', 'IMU_ankle_temp','IMU_hand_rotx','IMU_hand_roty','IMU_hand_rotz', 'IMU_hand_magx','IMU_hand_magy','IMU_hand_magz','IMU_chest_rotx','IMU_chest_roty','IMU_chest_rotz', 'IMU_chest_magx','IMU_chest_magy','IMU_chest_magz', 'IMU_ankle_rotx','IMU_ankle_roty','IMU_ankle_rotz',  'IMU_ankle_magx','IMU_ankle_magy','IMU_ankle_magz', \
                   'IMU_ankle_oru','IMU_ankle_orv','IMU_ankle_orw', 'IMU_chest_oru','IMU_chest_orv','IMU_chest_orw','IMU_hand_oru','IMU_hand_orv','IMU_hand_orw']

RESULT_DIR = "Result_PAMAP2"
