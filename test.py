 #!/usr/bin/env python -W ignore::DeprecationWarning
import pandas as pd
from constants import *
import warnings
import os
print('Pandas Version:\t%s' % pd.__version__)
import numpy as np
from utility import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn import preprocessing
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context('talk')
sns.set_style('white')



def load_dataset(filename):
    data=pd.read_csv(filename, sep= ' ', names =COL_HEADER)
    data.index = data.timestamp
    data=data.drop(DROP_COL_HEADER, axis=1)
    data['activity'] = data['activityID'].apply(ACTIVITY_MAP.get)
    activities = data.groupby('activity')
    data=data.drop(['activityID'],axis=1)
    return data,activities

def chest_absacc(row):
    return np.sqrt(row['IMU_chest_ax1']**2 + row['IMU_chest_ay1']**2 + row['IMU_chest_ay1']**2)/9.806

def hand_absacc(row):
    return np.sqrt(row['IMU_hand_ax1']**2 + row['IMU_hand_ay1']**2 + row['IMU_hand_ay1']**2)/9.806

def ankle_absacc(row):
    return np.sqrt(row['IMU_ankle_ax1']**2 + row['IMU_ankle_ay1']**2 + row['IMU_ankle_ay1']**2)/9.806

def prepare():
    warnings.filterwarnings("ignore")
    env = command_line_argument_parser()
    data, activities = load_dataset(env["filename"])
    data['chest_absacc'] = data.apply(chest_absacc,axis=1)
    data['hand_absacc'] = data.apply(hand_absacc,axis=1)
    data['ankle_absacc'] = data.apply(ankle_absacc,axis=1)

    ws =  env["WindowSize"]
    data['chest_absacc_max'] = pd.rolling_max(data['chest_absacc'], ws)
    data['hand_absacc_max'] =  pd.rolling_max(data['hand_absacc'], ws)
    data['ankle_absacc_max'] = pd.rolling_max(data['ankle_absacc'], ws)

    data['chest_absacc_min'] = pd.rolling_min(data['chest_absacc'], ws)
    data['hand_absacc_min'] =  pd.rolling_min(data['hand_absacc'], ws)
    data['ankle_absacc_min'] = pd.rolling_min(data['ankle_absacc'], ws)

    data['chest_acc_max_diff'] = data.chest_absacc_max - data.chest_absacc_min
    data['hand_acc_max_diff'] = data.hand_absacc_max - data.hand_absacc_min
    data['ankle_acc_max_diff'] = data.ankle_absacc_max - data.ankle_absacc_min

    activities = data.groupby('activity')
    feature_vector=['chest_acc_max_diff','hand_acc_max_diff','ankle_acc_max_diff']
    data.dropna(subset=['chest_acc_max_diff','hand_acc_max_diff','ankle_acc_max_diff'],inplace=True)

    labels = data['activity'].values

    env["data"], env["activities"],env['labels'],env['feature_vector']= data,activities,labels,feature_vector
    return env

def get_confusion_matrix(labels_predict,labels_test,activity):
    cm = confusion_matrix(labels_predict, labels_test, labels=activity.unique())
    cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    return cm,cm_normalized

def classify(env):
    data=env['data']
    feature_space = data[env['feature_vector']].values
    assert feature_space.shape[1]==len(env['feature_vector']), " Processed data set shape mismatch"
    X_train , X_test , Y_train , Y_test = train_test_split(feature_space,env['labels'],test_size=env["split_ratio"],random_state=42)
    clf = RandomForestClassifier(random_state=0)
    clf.fit(X_train,Y_train)
    labels_predicted = clf.predict(X_test)
    env["accuracy"] =  100.0*accuracy_score(labels_predicted, Y_test)
    env["confusion_matrix"] , env["normalized_confusion_matrix"] = get_confusion_matrix(labels_predicted,Y_test,data.activity)
    return env


def write_results(env):
    pwd = os.getcwd()

    if (os.path.isdir(pwd+"/"+RESULT_DIR)):
        pass
    else:
        os.mkdir(pwd+"/"+RESULT_DIR)


    dataset = env["Dataset"]
    os.chdir(pwd+"/"+RESULT_DIR)
    f=open(dataset,"w")


    f.write("\n--------------Confusion Matrix--------------------\n")
    f.write(np.array2string(env["confusion_matrix"],separator=' ,'))
    f.write("\n\n--------------normalized_confusion_matrix--------------------\n")
    f.write(np.array2string(env["normalized_confusion_matrix"], separator=' ,'))

    print env['accuracy']
    f.write("Accuracy :: \t")
    f.write(str(env["accuracy"]))
    f.close()

    data=env["data"]
    fig, ax = plt.subplots()
    sns.heatmap(env["normalized_confusion_matrix"] , annot=True, fmt=".4f", cmap='Blues', square=True,  xticklabels=data.activity.unique(),yticklabels=data.activity.unique())
    ax.set_xlabel('Predicted Activity')
    ax.set_ylabel('True Activity', )
    #plt.tight_layout()
    plt.savefig(dataset +"_normalized_confusion_matrix.pdf")
    plt.show()

    fig, ax = plt.subplots()
    sns.heatmap(env["confusion_matrix"] , annot=True, fmt=".4f", cmap='Blues', square=True,  xticklabels=data.activity.unique(),yticklabels=data.activity.unique())
    ax.set_xlabel('Predicted Activity')
    ax.set_ylabel('True Activity', )
    #plt.tight_layout()
    plt.savefig(dataset +"_confusion_matrix.pdf")
    plt.show()
    os.chdir(pwd)






if __name__ == "__main__":
    env=prepare()
    classify(env)
    write_results(env)
