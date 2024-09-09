import json
import os
import re
import pandas as pd

def main()->None:
    with open('subject_not_present.txt','r') as f:
        vid_ids = [file.replace('\n','') for file in f.readlines()]
    
    train_label_path = "train_engagement_labels.csv"
    validation_label_path = "validation_engagement_labels.csv"
    
    train_label,validation_label = pd.read_csv(train_label_path),pd.read_csv(validation_label_path)
    train_out,validation_out = [],[]
    for i in range(train_label.shape[0]):
        if train_label.iloc[i,1] in vid_ids:
            continue
        train_out.append({
            'video_id':train_label.iloc[i,1].split(".")[0],
            'q':"This is a video of a student performing tasks in an online setting. Choose whether the student is 'Not Engaged','Barely Engaged', 'Engaged', or 'Highly Engaged'.",
            'a':"The student is {}.".format(train_label.iloc[i,-1])
        })
    pattern = r"^subject_74_.*_vid_.*_.*\.mp4$"
    for j in range(validation_label.shape[0]):
        if re.match(pattern, validation_label.iloc[j,1]):
            continue
        validation_out.append({
            'video_id':validation_label.iloc[j,1].split(".")[0],
            'q':"This is a video of a student performing tasks in an online setting. Choose whether the student is 'Not Engaged','Barely Engaged', 'Engaged', or 'Highly Engaged'.",
            'a':"The student is {}.".format(validation_label.iloc[j,-1])
        })
        
    with open("train_engagement_labels.json", "w") as f:
        json.dump(train_out, f,indent=4)
        
    validation_label = pd.read_csv(validation_label_path)
    with open("validation_engagement_labels.json", "w") as f:
        json.dump(validation_out, f,indent=4)
    
    return

if __name__ == "__main__":
    main()