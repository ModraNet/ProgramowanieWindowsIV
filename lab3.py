class RGB():
    def __init__(self, R_value, G_value, B_value):
        self.R_value = R_value
        self.G_value = G_value
        self.B_value = B_value
        
    def get_R(self):
        return self.R_value
    def get_G(self):
        return self.G_value
    def get_B(self):
        return self.B_value
        
    def set_R(self, R_value):
        self.R_value = R_value
    def set_G(self, G_value):
        self.G_value = G_value
    def set_B(self, B_value):
        self.B_value = B_value
        
    def __str__(self):
        return "(" + self.R_value + "," + self.G_value + "," + self.B_value + ")"

class RGBController():
    def __init__(self, R, G, B):
        self.R = R
        self.G = G
        self.B = B
    def ShowRGB(R,G,B):
        print("["+str(R)+","+str(G)+","+str(B)+"]")
    def Mix(R1,G1,B1,R2,G2,B2):
        R3=R1+R2
        G3=G1+G2
        B3=B1+B2
        if(R3>255):
            R3=255
        if(G3>255):
            G3=255
        if(B3>255):
            B3=255
        return R3,G3,B3