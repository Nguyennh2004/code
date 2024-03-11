class HCN : 
    chieu_dai = 0
    chieu_rong = 0
    def tinh_chu_vi(self) :
        return(self.chieu_dai + self.chieu_rong)*2
    def tinh_dien_tich(self) :
        return(self.chieu_dai * self.chieu_rong)

hcn_1 = HCN ()
hcn_1.chieu_dai = 30 
hcn_1.chieu_rong = 11
dien_tich = hcn_1.tinh_dien_tich()
chu_vi = hcn_1.tinh_chu_vi()
print("Diện tích là : ",dien_tich)
print("Chu vi là : ",chu_vi)
hcn_2 = HCN()
hcn_2.chieu_dai = 30
hcn_2.chieu_rong = 11
dien_tich = hcn_2.tinh_dien_tich()
chu_vi = hcn_2.tinh_chu_vi()
print("Diện tích là : ",dien_tich)
print("Chu vi là : ",chu_vi)

