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

vm1 = Vm("Vm1", 4, 10, 0, 3, False)
vm2 = Vm("Vm2", 1, 10, 0, 1, False)
vm3 = Vm("Vm3", 1, 10, 30, 2, False)
vm4 = Vm("Vm4", 1, 10, 40, 2, False)
vm5 = Vm("Vm5", 1, 25, 35, 3, False)
vm6 = Vm("Vm6", 2, 15, 10, 2, False)
vm7 = Vm("Vm7", 2, 25, 10, 1, False)
vm8 = Vm("Vm8", 4, 5, 40, 1, False)
vm9 = Vm("Vm9", 1, 10, 35, 0, False)
vm10 = Vm("Vm10", 4, 30, 0, 2, False)

lista_vms = [vm1, vm2, vm3, vm4, vm5, vm6, vm7, vm8, vm9, vm10]

escala = []
TIME = 0
print("Tempo: ", TIME)
if len(escala) <= 4:
    n = 4 - len(escala)
    while n > 0:
        escala.append(0)
        n = n - 1
    print(escala)
else:
    print("n deu")



def exec():
    menor_at = float('inf')
    for vm in lista_vms:
        if not vm.done and vm.AT < menor_at and vm.AT >= TIME:
            menor_at = vm.AT
    
    vms_com_menor_at = [vm for vm in lista_vms if vm.AT == menor_at and not vm.done and vm.AT >= TIME]
    
    if vms_com_menor_at:
        return [vm.ID for vm in vms_com_menor_at]
    else:
        return None
    

def decidir_vm_para_executar(vm1, vm2, total_cpus):
    if vm1.vCPU == total_cpus and vm2.vCPU == total_cpus:
        # Executa a de maior prioridade
        if vm1.P < vm2.P:
            return vm1.ID
        else:
            return vm2.ID
    elif vm1.vCPU == total_cpus:
        return vm1.ID
    elif vm2.vCPU == total_cpus:
        return vm2.ID

    # Se a diferença de prioridade for 1 e a VM com menor prioridade é executável em menos da metade do tempo
    if abs(vm1.P - vm2.P) == 1:
        if vm1.P > vm2.P and vm1.ET < vm2.ET / 2:
            return vm1.ID
        elif vm2.P > vm1.P and vm2.ET < vm1.ET / 2:
            return vm2.ID

    # Se a soma das vCPUs for maior que as CPUs disponíveis
    if vm1.vCPU + vm2.vCPU > total_cpus:
        # Executa a VM de maior prioridade, desde que ela ocupe menos CPUs
        if vm1.P < vm2.P and vm1.vCPU < vm2.vCPU:
            return vm1.ID
        elif vm2.P < vm1.P and vm2.vCPU < vm1.vCPU:
            return vm2.ID

    # Caso contrário, executa a VM de maior prioridade
    if vm1.P < vm2.P:
        return vm1.ID
    else:
        return vm2.ID

print(exec())

def conta_done():
    cd = 0
    for vm in lista_vms:
        if vm.done:
            cd +=1
    print(len(lista_vms))
    print(cd)
