class Vm:
    def __init__(self, ID, vCPU, ET, AT, P, done):
        self.ID = ID
        if vCPU <= 4:
            self.vCPU = vCPU
        else:
            self.vCPU = 4
        self.ET = ET
        self.AT = AT
        self.P = P
        self.done = done

    def info(self):
        print("ID: ", self.ID)
        print("vCPU: ", self.vCPU)
        print("Execution Time: ", self.ET)
        print("Arrival Time: ", self.AT)
        print("Priority: ", self.P)

vm1 = Vm("Vm1", 3, 35, 40, 3, False)
vm2 = Vm("Vm1", 1, 40, 45, 1, False)

vm1.info()
vm1.done = True
vm1.info()

lista_vms = []
lista_vms.append(vm1.ID)
lista_vms.append(vm2.ID)
past_time = 0
TIME = 0
print("Tempo: ", TIME)
if len(lista_vms) <= 4:
    n = 4 - len(lista_vms)
    while n > 0:
        lista_vms.append(0)
        n = n - 1
    print(lista_vms)
else:
    print("n deu")

