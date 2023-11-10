import HolisticModule as hm
import AssemblePats as ap
import draw_pose as dp
import Motion as M
import utils as u

import cv2
from timeit import default_timer as timer
import time

aruco_marker_memory = {}
poes_memory = {}

r_pack_move_id0_1 = []
r_pack_move_id1_2 = []
r_pack_move_id4_3 = []
r_pack_move_id5_4 = []
r_pack_move_id6_5 = []

count_step = 0
step_one_zero = 0

def Recap(cap):
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,600)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,800)

def Bootfpss(cap):
    cap.set(cv2.CAP_PROP_FPS,5)

def Thra(cap):
    cap.set(cv2.CAP_PROP_N_THREADS, 12)

def Text(image, num, posx, posy):
    cv2.putText(image, str(int(num)), (posx, posy), cv2.FONT_HERSHEY_PLAIN, 1,
                (102,102,255), 2)
              
def memory_aruco(ids_num, image):
    if ids_num not in aruco_marker_memory:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        corners, ids, _ = cv2.aruco.detectMarkers(gray, aruco_dict)
        list_posAruco = u.aruco_display(corners,ids, 17,image)
        for market_id, cX, cY in list_posAruco:
            # print(ids)
            if market_id == ids_num:
                aruco_marker_memory[ids_num] = (cX, cY)
                return aruco_marker_memory[ids_num]
    else:
        return aruco_marker_memory[ids_num]
    
def memory_pose(ids_list):
    for ids, cX, cY in ids_list :
        poes_memory[ids] = (cX, cY)
    
    return poes_memory
    
def cal_dits(point, id_point):

    if id_point is not None:
        dits = ap.findDistance(point, id_point)
        Text(image, dits, id_point[0], id_point[1])
        return dits
    else:
        pass


aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_1000)

selet = int(input('1: wedcam 2: video : '))

if selet == 1:
    cap1 = cv2.VideoCapture(2)
    # cap2 = cv2.VideoCapture(0)
elif selet == 2:
    cap1 = cv2.VideoCapture('Video/2023-10-24-155544.webm')
    # cap2 = cv2.VideoCapture('Video/2023-10-24-155544.webm')

holistic = hm.holistic_module()
motion = M.Motion_time(6,6,8)

if selet == 1:
    Recap(cap1)
    # Recap(cap2)
    # Bootfpss(cap1)
    # Bootfpss(cap2)
    Thra(cap1)
    # Thra(cap2)
elif selet == 2:
    pass

print(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT),cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap1.get(cv2.CAP_PROP_N_THREADS))
print(cap1.get(cv2.CAP_PROP_FPS))

ffcc99 = (153, 204, 255)
ccff99 = (153,255,204)

step_l = 0
step_r = 0

pTime = 0

start = timer()

time_s_assm_l = 0
time_e_assm_l = 0
time_s_mov_l = 0
time_e_mov_l = 0

time_s_assm_r = 0
time_e_assm_r = 0
time_s_mov_r = 0
time_e_mov_r = 0

l_assemble_min = (120, 115, 250)
l_assemble_max = (155, 145, 285)
l_move_min = (150, 125, 185)
l_move_max = (180, 180, 215)

r_assemble_min = (110, 120, 70)
r_assemble_max = (155, 145, 105)
r_move_min = (155, 125, 135)
r_move_max = (180, 180, 175)

deter = True

mode = 0

paused = False

if deter:
    mode = int(input("1: Top 2: Side: "))

out = cv2.VideoWriter('test_workstudy_angle.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (800,600))

while cap1.isOpened():

    if not paused:

        success1, image = cap1.read()

        if not success1:
            print('Ignoring empty camera frame.')

            break

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    id_0 = memory_aruco(0, image)
    id_1 = memory_aruco(1, image)
    id_2 = memory_aruco(2, image)
    id_3 = memory_aruco(3, image)
    id_4 = memory_aruco(4, image)
    id_5 = memory_aruco(5, image)
    id_6 = memory_aruco(6, image)
    # print(id_2)

    id_10 = memory_aruco(10, image)
    id_11 = memory_aruco(11, image)
    id_12 = memory_aruco(12, image)
    id_13 = memory_aruco(13, image)
    id_14 = memory_aruco(14, image)
    id_15 = memory_aruco(15, image)
    id_16 = memory_aruco(16, image)

    if deter:

        if mode == 1:
            holistic.show_action(image, draw=False)
            # image_mask = holistic.segmentation_mask_(image)

        elif mode == 2:
            holistic.show_action(image, draw=False)

        list_pose = holistic.finepos(image)
        list_hands = holistic.finehand(image)

        if len(list_pose) > 0:

            r_shoulder = list_pose[12]
            l_shoulder = list_pose[11]

            r_elbow = list_pose[14]
            r_wrist = list_pose[16]

            l_elbow = list_pose[13]
            l_wrist = list_pose[15]


            # listener = keyboard.Listener(on_release=action_move)
            # listener.start()

            if mode == 1 :

                drawPose = dp.DrawPose(image, list_pose)

                A_arm_r = ap.findAngle(r_elbow,r_wrist)
                A_arm_l = ap.findAngle(l_elbow,l_wrist)

                A_shr_l = ap.findAngle(l_shoulder,l_elbow)
                A_shr_r = ap.findAngle(r_shoulder,r_elbow)

                A_elbow_l = ap.findAngle_elbow(l_shoulder, l_elbow, l_wrist)
                A_elbow_r = ap.findAngle_elbow(r_shoulder, r_elbow, r_wrist)

                bwee_shor = ap.findDistance(l_shoulder, r_shoulder)

                distan_id_0 = cal_dits(l_wrist, id_0)
                distan_id_1 = cal_dits(l_wrist, id_1)
                distan_id_2 = cal_dits(l_wrist, id_2)
                distan_id_3 = cal_dits(l_wrist, id_3)
                distan_id_4 = cal_dits(l_wrist, id_4)
                distan_id_5 = cal_dits(l_wrist, id_5)
                distan_id_6 = cal_dits(l_wrist, id_6)

                distan_id_10 = cal_dits(r_wrist, id_10)
                distan_id_11 = cal_dits(r_wrist, id_11)
                distan_id_12 = cal_dits(r_wrist, id_12)
                distan_id_13 = cal_dits(r_wrist, id_13)
                distan_id_14 = cal_dits(r_wrist, id_14)
                distan_id_15 = cal_dits(r_wrist, id_15)
                distan_id_16 = cal_dits(r_wrist, id_16)
                motion.move_action_r(A_shr_r,A_elbow_r,A_arm_r,[distan_id_10, distan_id_11, distan_id_14, distan_id_16, distan_id_15])
                # motion.move_action_l(A_shr_l,A_elbow_l,A_arm_l,[distan_id_0, distan_id_1, distan_id_4, distan_id_6, distan_id_5])

                # action_move()

                # distan_id_10 = ap.findDistance(l_wrist, id_10)
                # distan_id_11 = ap.findDistance(l_wrist, id_11)
                # distan_id_12 = ap.findDistance(l_wrist, id_12)
                # distan_id_16 = ap.findDistance(l_wrist, id_16)

                drawPose.draw_top_pos()

                Text(image, A_shr_r, r_shoulder[0], r_shoulder[1])
                Text(image, A_elbow_r, r_elbow[0], r_elbow[1])
                Text(image, A_arm_r, r_wrist[0], r_wrist[1])

                Text(image, A_shr_l, l_shoulder[0], l_shoulder[1])
                Text(image, A_elbow_l, l_elbow[0], l_elbow[1])
                Text(image, A_arm_l, l_wrist[0], l_wrist[1])

                Text(image, bwee_shor, l_shoulder[0] + 100, l_shoulder[1])

            elif mode == 2:
                l_shoulder = list_pose[11][1::]
                l_hip = list_pose[23][1::]
                l_ear = list_pose[7][1::]

                r_shoulder = list_pose[12][1::]
                r_hip = list_pose[24][1::]
                r_ear = list_pose[8][1::] 

                neck = ap.findAngle(r_shoulder,r_ear)
                torso = ap.findAngle(r_hip,r_shoulder)

                posture = motion.body_posture_detection(neck, torso)

                drawPose = dp.DrawPose(image, list_pose, list_hands)
                drawPose.draw_side_pos(image,detection= posture, rad_circle= 5, size_line= 2)

            # print(f'angle_l: {A_arm_l} angle_r: {- (A_arm_r - 180)}')
            # print(f'arm_l:{A_arm_l},{A_shr_l},{A_elbow_l} arm_r:{A_arm_r},{A_shr_r},{A_elbow_r}')
            # print(f'arm_l:{action_l} arm_r:{action_r}')


    cv2.putText(image, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)
    # cv2.putText(image2, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                # (255, 0, 0), 3)
    
    # out.write(image)

    cv2.imshow("Top", image)
    # cv2.imshow("mark", image_mask)
    # cv2.imshow("Side", image2)

    if cv2.waitKey(5) & 0xFF == 27:
        break

    elif cv2.waitKey(5) & 0xFF  == ord('p'):
        paused = not paused

    elif cv2.waitKey(5) & 0xFF == ord("s"):
        if step_one_zero == 0:
            if count_step == 0:
                r_pack_move_id0_1.append([A_shr_l,A_elbow_l,A_arm_l,distan_id_0])
                print("Save Done! id 0")
                count_step +=1
                step_one_zero = 1

            elif count_step == 1:
                r_pack_move_id1_2.append([A_shr_l,A_elbow_l,A_arm_l,distan_id_1])
                print("Save Done! id 1")
                count_step +=1
                step_one_zero = 1

            elif count_step == 2:
                r_pack_move_id4_3.append([A_shr_l,A_elbow_l,A_arm_l,distan_id_4])
                print("Save Done! id 4")
                count_step +=1
                step_one_zero = 1
                        
            elif count_step == 3:
                r_pack_move_id6_5.append([A_shr_l,A_elbow_l,A_arm_l,distan_id_6])
                print("Save Done! id 6")
                count_step +=1

            if count_step >= 4:
                count_step = 0
                    
            elif step_one_zero == 1:
                r_pack_move_id5_4.append([A_shr_l,A_elbow_l,A_arm_l,distan_id_5])
                print("Save Done! id 5")
                step_one_zero = 0
        
cap1.release()
cv2.destroyAllWindows()
end = timer()
print(end - start)
print(f'list_id0: {r_pack_move_id0_1}')
print(f'list_id1: {r_pack_move_id1_2}')
print(f'list_id4: {r_pack_move_id4_3}')
print(f'list_id5: {r_pack_move_id5_4}')
print(f'list_id6: {r_pack_move_id6_5}')
aruco_marker_memory = {}