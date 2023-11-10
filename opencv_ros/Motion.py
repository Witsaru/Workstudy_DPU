from timeit import default_timer as timer
import graphviz

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

        self.start = 0
        self.end = 0
        self.total = 0

        self.dot = graphviz.Digraph(comment = name_flow_chart )

        self.processes = processes

        self.step_proce_r = 0

        self.id0 = [[161,178], [180,211], [162,169], [138,176]] #dist min -5
        self.id1 = [[151,171], [186,226], [173,179], [138,196]] #sho min -1 elbow max +16 arm min -3
        self.id4 = [[128,136], [218,236], [174,178], [109,120]]
        self.id5 = [[136,152], [240,265], [134,151], [95,113]]
        self.id6 = [[55,106], [70,312], [127,180], [56,325]] #elbow max+31

        self.id10 = [[173,178], [164,185], [166,178], [128,155]]
        self.id11 = [[158,178], [157,183], [170,176], [135,169]] #dist max+5 min-5 sho min -5 arm min -3
        self.id14 = [[132,136], [133,138], [175,179], [109,120]]
        self.id15 = [[139,176], [92,162], [129,165], [39,108]]
        self.id16 = [[34,93], [38,284], [124,179], [86,330]]


    def move_action_r(self, Angle_shor, Angle_elbow, Angle_arm, dist_wri):
        if self.step_r == 0:
            if self.count_action_r == 0:
                if ((self.id10[0][0] <= Angle_shor <= self.id10[0][1]) and (self.id10[1][0] <= Angle_elbow <= self.id10[1][1])) and ((self.id10[2][0] <= Angle_arm <= self.id10[2][1])and(self.id10[3][0] < dist_wri[0] <= self.id10[3][1])):
                    print("id 10")
                    self.step_r = 1
                    self.count_action_r += 1
                    self.dot.node(self.processes[self.step_proce_r])

            elif self.count_action_r == 1:
                if ((self.id11[0][0] <= Angle_shor <= self.id11[0][1]) and (self.id11[1][0] <= Angle_elbow <= self.id11[1][1])) and ((self.id11[2][0] <= Angle_arm <= self.id11[2][1])and(self.id11[3][0] <= dist_wri[1] <= self.id11[3][1])):
                    print("id 11")
                    self.step_r = 1
                    self.count_action_r += 1
                    self.step_proce_r += 1
                    self.dot.node(self.processes[self.step_proce_r])
                    self.dot.edge(self.processes[self.step_proce_r - 1], self.processes[self.step_proce_r])

            elif self.count_action_r == 2:
                if ((self.id14[0][0] <= Angle_shor <= self.id14[0][1]) and (self.id14[1][0] <= Angle_elbow <= self.id14[1][1])) and ((self.id14[2][0] <= Angle_arm <= self.id14[2][1])and(self.id14[3][0] <= dist_wri[2] <= self.id14[3][1])):
                    print("id 14")
                    self.step_r = 1
                    self.count_action_r += 1
                    self.step_proce_r += 1
                    self.dot.node(self.processes[self.step_proce_r])
                    self.dot.edge(self.processes[self.step_proce_r - 1], self.processes[self.step_proce_r])

            elif self.count_action_r == 3:
                if ((self.id16[0][0] <= Angle_shor <= self.id16[0][1]) and (self.id16[1][0] <= Angle_elbow <= self.id16[1][1])) and ((self.id16[2][0] <= Angle_arm <= self.id16[2][1])and(self.id16[3][0] <= dist_wri[3] <= self.id16[3][1])):
                    print("id 16")
                    self.count_action_r += 1
                    self.step_proce_r += 1
                    self.dot.node(self.processes[self.step_proce_r])
                    self.dot.edge(self.processes[self.step_proce_r - 1], self.processes[self.step_proce_r])
                    self.dot.render('flow_process_chart', view=True)
            
            if self.count_action_r >= 4:
                self.count_action_r = 0
                self.step_proce_r = 0

        elif self.step_r == 1:
            if ((self.id15[0][0] <= Angle_shor <= self.id15[0][1]) and (self.id15[1][0] <= Angle_elbow <= self.id15[1][1])) and ((self.id15[2][0] <= Angle_arm <= self.id15[2][1])and(self.id15[3][0] <= dist_wri[4] <= self.id15[3][1])):
                print("id 15")
                self.step_r = 0
                self.step_proce_r += 1
                self.dot.node(self.processes[self.step_proce_r])
                self.dot.edge(self.processes[self.step_proce_r - 1], self.processes[self.step_proce_r])

    def move_action_l(self, Angle_shor, Angle_elbow, Angle_arm, dist_wri):
        if self.step_l == 0:
            if self.count_action_l == 0:
                if ((self.id0[0][0] <= Angle_shor <= self.id0[0][1]) and (self.id0[1][0] <= Angle_elbow <= self.id0[1][1])) and ((self.id0[2][0] <= Angle_arm <= self.id0[2][1])and(self.id0[3][0] < dist_wri[0] <= self.id0[3][1])):
                    print("id 0")
                    self.step_l = 1
                    self.count_action_l += 1

            elif self.count_action_l == 1:
                if ((self.id1[0][0] <= Angle_shor <= self.id1[0][1]) and (self.id1[1][0] <= Angle_elbow <= self.id1[1][1])) and ((self.id1[2][0] <= Angle_arm <= self.id1[2][1])and(self.id1[3][0] <= dist_wri[1] <= self.id1[3][1])):
                    print("id 1")
                    self.step_l = 1
                    self.count_action_l += 1

            elif self.count_action_l == 2:
                if ((self.id4[0][0] <= Angle_shor <= self.id4[0][1]) and (self.id4[1][0] <= Angle_elbow <= self.id4[1][1])) and ((self.id4[2][0] <= Angle_arm <= self.id4[2][1])and(self.id4[3][0] <= dist_wri[2] <= self.id4[3][1])):
                    print("id 4")
                    self.step_l = 1
                    self.count_action_l += 1

            elif self.count_action_l == 3:
                if ((self.id6[0][0] <= Angle_shor <= self.id6[0][1]) and (self.id6[1][0] <= Angle_elbow <= self.id6[1][1])) and ((self.id6[2][0] <= Angle_arm <= self.id6[2][1])and(self.id6[3][0] <= dist_wri[3] <= self.id6[3][1])):
                    print("id 6")
                    self.count_action_l += 1
            
            if self.count_action_l >= 4:
                self.count_action_l = 0

        elif self.step_l == 1:
            if ((self.id5[0][0] <= Angle_shor <= self.id5[0][1]) and (self.id5[1][0] <= Angle_elbow <= self.id5[1][1])) and ((self.id5[2][0] <= Angle_arm <= self.id5[2][1])and(self.id5[3][0] <= dist_wri[4] <= self.id5[3][1])):
                print("id 5")
                self.step_l = 0