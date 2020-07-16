class Clinic:
    def __init__(self):
        self.patient_list = []
    
    def show_wating_count(self):
        print('ただ今の待ち人数は' + len(self.patient_list) + '人です。')
    
    def reserve(self,patient):
        if self._check_revesed(patient):
            print('予約済みです。')
        else :
            print(patient.name + 'さん予約を完了しました。')
            self.patient_list.append(patient)
    
    def diagnosis(self,patient_id = None):
        patient = None
        if patient.patient_id == None:
            if len(patient.list) > 0:
                patient = self.patient_list[0]
        else :
            for i in self.patient_list:
                if i.patient_list_id == patient_id:
                    patient = i
        
        if patient == None:
            print('診察する患者がいません。')
        else :
            print(patient.name + 'さん、' + patient.sysmptom + 'ですね。')
            print('診察終わりました。お大事に。')
        
    def _check_revesed(self,patient):
        for i in self.patient_list:
            if i.patient_id == patient.patient_id:
                return True
            return False