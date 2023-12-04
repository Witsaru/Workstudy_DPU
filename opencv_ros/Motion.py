from timeit import default_timer as timer
import graphviz
from timeit import default_timer as timer

class Motion_time():

    def __init__(self, num_action_left, num_action_right, num_product, 
                 name_flow_chart='Flow Process Chart',
                 processes = [
                     'หยิบน็อตตัวผู้',
                     'นำน็อตตัวผู้ใส่บล็อก',
                     'หยิบแหวน',
                     'นำแหวนสวมน็อตตัวผู้',
                     'หยิบน็อตตัวเมีย',
                     'นำน็อตตัวเมียมาประกอบกับน็อตผู้',
                     'โยนเก็บชิ้นงาน'
                 ]):
        self.num_action_left = num_action_left
        self.num_action_right = num_action_right
        self.num_product = num_product

        self.count_action_l = 0 
        self.step_l = 0

        self.count_action_r = 0 
        self.step_r = 0

        self.start_l = 0
        self.end_l = 0
        self.total_l = 0

        self.start_l2 = 0
        self.end_l2 = 0
        self.total_l2 = 0

        self.start_r = 0
        self.end_r = 0
        self.total_r = 0

        self.start_r2 = 0
        self.end_r2 = 0
        self.total_r2 = 0

        self.time_study_l = {}
        self.time_study_r = {}

        for i in range(0,num_action_left):
            self.time_study_l[f"Step{i+1}"] = []

        for i in range(0,num_action_right):
            self.time_study_r[f"Step{i+1}"] = []


        self.dot = graphviz.Digraph(comment = name_flow_chart )

        self.processes = processes

        self.step_proce_r = 0
        self.step_proce_l = 0

        self.id0 = [[161,178], [180,220], [150,169], [138,176]] #dist min -5
        self.id1 = [[145,171], [186,226], [165,179], [120,196]] #sho min -1 elbow max +16 arm min -3
        self.id4 = [[125,145], [185,236], [150,178], [109,140]]
        self.id5 = [[136,180], [200,265], [134,160], [85,113]]
        self.id6 = [[55,106], [70,312], [127,180], [56,325]] #elbow max+31

        self.id10 = [[170,180], [150,185], [150,178], [120,160]]
        self.id11 = [[150,178], [140,183], [165,180], [130,169]] #dist max+5 min-5 sho min -5 arm min -3
        self.id14 = [[132,145], [133,175], [140,179], [109,155]]
        self.id15 = [[135,176], [92,162], [129,165], [70,108]]
        self.id16 = [[34,93], [38,320], [124,179], [65,330]]


    def move_action_r(self, Angle_shor, Angle_elbow, Angle_arm, dist_wri):
        if self.step_r == 0:
            if self.count_action_r == 0:
                if ((self.id10[0][0] <= Angle_shor <= self.id10[0][1]) and (self.id10[1][0] <= Angle_elbow <= self.id10[1][1])) and ((self.id10[2][0] <= Angle_arm <= self.id10[2][1])and(self.id10[3][0] <= dist_wri[0] <= self.id10[3][1])):
                    # print("id 10")
                    self.start_r = timer()
                    self.step_r = 1
                    self.count_action_r += 1
                    # self.dot.node(self.processes[self.step_proce_r])

            elif self.count_action_r == 1:
                if ((self.id11[0][0] <= Angle_shor <= self.id11[0][1]) and (self.id11[1][0] <= Angle_elbow <= self.id11[1][1])) and ((self.id11[2][0] <= Angle_arm <= self.id11[2][1])and(self.id11[3][0] <= dist_wri[1] <= self.id11[3][1])):
                    # print("id 11")
                    self.start_r = timer()
                    self.end_r2 = timer()
                    self.total_r2 = round(self.end_r2 - self.start_r2,4)
                    self.time_study_r[f"Step{self.step_proce_r+1}"].append(self.total_r2)
                    self.step_r = 1
                    self.count_action_r += 1
                    self.step_proce_r += 1
                    # self.dot.node(self.processes[self.step_proce_r])
                    # self.dot.edge(self.processes[self.step_proce_r - 1], self.processes[self.step_proce_r])

            elif self.count_action_r == 2:
                if ((self.id14[0][0] <= Angle_shor <= self.id14[0][1]) and (self.id14[1][0] <= Angle_elbow <= self.id14[1][1])) and ((self.id14[2][0] <= Angle_arm <= self.id14[2][1])and(self.id14[3][0] <= dist_wri[2] <= self.id14[3][1])):
                    # print("id 14")
                    self.start_r = timer()
                    self.end_r2 = timer()
                    self.total_r2 = round(self.end_r2 - self.start_r2,4)
                    self.time_study_r[f"Step{self.step_proce_r+1}"].append(self.total_r2)
                    self.step_r = 1
                    self.count_action_r += 1
                    self.step_proce_r += 1
                    # self.dot.node(self.processes[self.step_proce_r])
                    # self.dot.edge(self.processes[self.step_proce_r - 1], self.processes[self.step_proce_r])

            elif self.count_action_r == 3:
                if ((self.id16[0][0] <= Angle_shor <= self.id16[0][1]) and (self.id16[1][0] <= Angle_elbow <= self.id16[1][1])) and ((self.id16[2][0] <= Angle_arm <= self.id16[2][1])and(self.id16[3][0] <= dist_wri[3] <= self.id16[3][1])):
                    # print("id 16")
                    self.start_r = timer()
                    self.end_r2 = timer()
                    self.total_r2 = round(self.end_r2 - self.start_r2,4)
                    self.time_study_r[f"Step{self.step_proce_r+1}"].append(self.total_r2)
                    self.count_action_r += 1
                    self.step_proce_r += 1
                    # self.dot.node(self.processes[self.step_proce_r])
                    # self.dot.edge(self.processes[self.step_proce_r - 1], self.processes[self.step_proce_r])
                    # self.dot.render('flow_process_chart', view=True)
            
            if self.count_action_r >= 4:
                self.start_r2 = timer()
                self.end_r = timer()
                self.total_r = round(self.end_r - self.start_r,4)
                self.time_study_r[f"Step{self.step_proce_r+1}"].append(self.total_r)
                self.count_action_r = 0
                self.step_proce_r = 0

        elif self.step_r == 1:
            if ((self.id15[0][0] <= Angle_shor <= self.id15[0][1]) and (self.id15[1][0] <= Angle_elbow <= self.id15[1][1])) and ((self.id15[2][0] <= Angle_arm <= self.id15[2][1])and(self.id15[3][0] <= dist_wri[4] <= self.id15[3][1])):
                # print("id 15")
                self.start_r2 = timer()
                self.end_r = timer()
                self.total_r = round(self.end_r - self.start_r,4)
                self.time_study_r[f"Step{self.step_proce_r+1}"].append(self.total_r)
                self.step_r = 0
                self.step_proce_r += 1
                # self.dot.node(self.processes[self.step_proce_r])
                # self.dot.edge(self.processes[self.step_proce_r - 1], self.processes[self.step_proce_r])
        return self.time_study_r

    def move_action_l(self, Angle_shor, Angle_elbow, Angle_arm, dist_wri):
        if self.step_l == 0:
            if self.count_action_l == 0:
                if ((self.id0[0][0] <= Angle_shor <= self.id0[0][1]) and (self.id0[1][0] <= Angle_elbow <= self.id0[1][1])) and ((self.id0[2][0] <= Angle_arm <= self.id0[2][1])and(self.id0[3][0] < dist_wri[0] <= self.id0[3][1])):
                    # print("id 0")
                    self.start_l = timer()
                    self.step_l = 1
                    self.count_action_l += 1

            elif self.count_action_l == 1:
                if ((self.id1[0][0] <= Angle_shor <= self.id1[0][1]) and (self.id1[1][0] <= Angle_elbow <= self.id1[1][1])) and ((self.id1[2][0] <= Angle_arm <= self.id1[2][1])and(self.id1[3][0] <= dist_wri[1] <= self.id1[3][1])):
                    # print("id 1")
                    self.start_l = timer()
                    self.end_l2 = timer()
                    self.total_l2 = round(self.end_r2 - self.start_r2,4)
                    self.time_study_l[f"Step{self.step_proce_l+1}"].append(self.total_l2)
                    self.step_l = 1
                    self.count_action_l += 1
                    self.step_proce_l += 1

            elif self.count_action_l == 2:
                if ((self.id4[0][0] <= Angle_shor <= self.id4[0][1]) and (self.id4[1][0] <= Angle_elbow <= self.id4[1][1])) and ((self.id4[2][0] <= Angle_arm <= self.id4[2][1])and(self.id4[3][0] <= dist_wri[2] <= self.id4[3][1])):
                    # print("id 4")
                    self.start_l = timer()
                    self.end_l2 = timer()
                    self.total_l2 = round(self.end_l2 - self.start_r2,4)
                    self.time_study_l[f"Step{self.step_proce_l+1}"].append(self.total_l2)
                    self.step_l = 1
                    self.count_action_l += 1
                    self.step_proce_l += 1

            elif self.count_action_l == 3:
                if ((self.id6[0][0] <= Angle_shor <= self.id6[0][1]) and (self.id6[1][0] <= Angle_elbow <= self.id6[1][1])) and ((self.id6[2][0] <= Angle_arm <= self.id6[2][1])and(self.id6[3][0] <= dist_wri[3] <= self.id6[3][1])):
                    # print("id 6")
                    self.start_l = timer()
                    self.end_l2 = timer()
                    self.total_l2 = round(self.end_l2 - self.start_r2,4)
                    self.time_study_l[f"Step{self.step_proce_l+1}"].append(self.total_l2)
                    self.count_action_l += 1
                    self.step_proce_l += 1
            
            if self.count_action_l >= 4:
                self.start_l2 = timer()
                self.end_l = timer()
                self.total_l = round(self.end_l - self.start_l,4)
                self.time_study_l[f"Step{self.step_proce_l+1}"].append(self.total_l)
                self.count_action_l = 0
                self.step_proce_l = 0

        elif self.step_l == 1:
            if ((self.id5[0][0] <= Angle_shor <= self.id5[0][1]) and (self.id5[1][0] <= Angle_elbow <= self.id5[1][1])) and ((self.id5[2][0] <= Angle_arm <= self.id5[2][1])and(self.id5[3][0] <= dist_wri[4] <= self.id5[3][1])):
                # print("id 5")
                self.start_l2 = timer()
                self.end_l = timer()
                self.total_l = round(self.end_l - self.start_l,4)
                self.time_study_l[f"Step{self.step_proce_l+1}"].append(self.total_l)
                self.step_l = 0
                self.step_proce_l += 1

        return self.time_study_l

    def count_process_r(self):
        return self.step_proce_r
    def count_process_l(self):
        return self.step_proce_l
    
    def body_posture_detection(self,neck_, torso):
        if neck_ < 40 and torso < 10:
            return True
        else:
            return False