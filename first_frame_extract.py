# import cv2
# import os

# #for one frame
# video_path = '/mnt/media/gadha3/fsrt/mp4/id07868/FwZFlP8nYfo/00086.mp4'
# file_name = os.path.splitext(os.path.basename(video_path))[0]
# cap = cv2.VideoCapture(video_path)

# if not cap.isOpened():
#     print("Error: Couldn't open video.")
# else:
#     ret, frame = cap.read()
#     if ret:
#         # frame_path = os.path.join(os.path.dirname(video_path), file_name + '_first_frame.png')
#         frame_path = '/mnt/media/gadha3/fsrt/self_reenactment/first_frames/'+f'{file_name}'+'.png'
        
#         cv2.imwrite(frame_path, frame)
#         print(f"First frame extracted and saved as '{frame_path}'.")
#     else:
#         print("Error: Couldn't read the first frame.")
# cap.release()

#for 2 frames

import cv2
import os

video_path = '/mnt/media/gadha3/fsrt/mp4/id02317/3fem5j6mQ5s/00009.mp4'
file_name_0 = os.path.splitext(os.path.basename(video_path))[0]
file_name_1 = f"{file_name_0}_last"  

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Couldn't open video.")
else:
    ret, first_frame = cap.read()
    if ret:
        frame_path_0 = f'/mnt/media/gadha3/fsrt/self_reenactment/first_frames/{file_name_0}_first.png'
        frame_path_1 = f'/mnt/media/gadha3/fsrt/self_reenactment/first_frames/{file_name_1}.png'
        cv2.imwrite(frame_path_0, first_frame)
        print(f"First frame extracted and saved as '{frame_path_0}'.")
        cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_FRAME_COUNT) - 1)
        ret, last_frame = cap.read()
        if ret:
            cv2.imwrite(frame_path_1, last_frame)
            print(f"Last frame extracted and saved as '{frame_path_1}'.")
        else:
            print("Error: Couldn't read the last frame.")
    else:
        print("Error: Couldn't read the first frame.")
cap.release()
