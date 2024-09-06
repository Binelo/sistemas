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

    def __repr__(self) -> str:
        return f'{self.ID}'

    def info(self):
        print("ID: ", self.ID)
        print("vCPU: ", self.vCPU)
        print("Execution Time: ", self.ET)
        print("Arrival Time: ", self.AT)
        print("Priority: ", self.P)

vm1 = Vm("Vm1", 2, 10, 0, 3, False)
vm2 = Vm("Vm2", 1, 10, 20, 1, False)
vm3 = Vm("Vm3", 1, 10, 30, 2, False)
vm4 = Vm("Vm4", 1, 10, 40, 2, False)
vm5 = Vm("Vm5", 1, 25, 35, 3, False)
vm6 = Vm("Vm6", 2, 15, 10, 2, False)
vm7 = Vm("Vm7", 2, 25, 10, 1, False)
vm8 = Vm("Vm8", 4, 5, 40, 1, False)
vm9 = Vm("Vm9", 1, 10, 35, 0, False)
vm10 = Vm("Vm10", 2, 30, 0, 2, False)

lista_vms = [vm1, vm2, vm3, vm4, vm5, vm6, vm7, vm8, vm9, vm10]
all_done = False
lista_espera = []
escala = []
espaco = 4 - len(escala)
TIME = 0

def preenche_lista(vm):
    if espaco - vm.vCPU >= 0:
        for i in range(0, vm.vCPU):
            escala.append(vm.ID)
        return escala
    else:
        return("n deu")



def exec():
    menor_at = float('inf')
    for vm in lista_vms:
        if not vm.done and vm.AT < menor_at and vm.AT >= TIME:
            menor_at = vm.AT
    
    vms_com_menor_at = [vm for vm in lista_vms if vm.AT == menor_at and not vm.done and vm.AT >= TIME]
    
    if vms_com_menor_at:
        return [vm for vm in vms_com_menor_at]
    else:
        return None
    

def decidir_vm_para_executar(lista, total_cpus):
    vm_escolhida = lista[0]
    for i in range(0, len(lista) - 1):
    
        if vm_escolhida.vCPU == total_cpus and lista[i + 1].vCPU == total_cpus:
            # Executa a de maior prioridade
            if vm_escolhida.P < lista[i + 1].P:
                vm_escolhida = vm_escolhida
            else:
                vm_escolhida = lista[i + 1]
        elif vm_escolhida.vCPU == total_cpus:
            vm_escolhida = vm_escolhida
        elif lista[i + 1].vCPU == total_cpus:
            vm_escolhida = lista[i + 1]

        # Se a diferença de prioridade for 1 e a VM com menor prioridade é executável em menos da metade do tempo
        if abs(vm_escolhida.P - lista[i + 1].P) == 1:
            if vm_escolhida.P > lista[i + 1].P and vm_escolhida.ET < lista[i + 1].ET / 2:
                vm_escolhida = vm_escolhida
            elif lista[i + 1].P > vm_escolhida.P and lista[i + 1].ET < vm_escolhida.ET / 2:
                vm_escolhida = lista[i + 1]

        # Se a soma das vCPUs for maior que as CPUs disponíveis
        if vm_escolhida.vCPU + lista[i + 1].vCPU > total_cpus:
            # Executa a VM de menor prioridade, desde que ela ocupe menos CPUs
            if vm_escolhida.P < lista[i + 1].P and vm_escolhida.vCPU < lista[i + 1].vCPU:
                vm_escolhida = vm_escolhida
            elif lista[i + 1].P < vm_escolhida.P and lista[i + 1].vCPU < vm_escolhida.vCPU:
                vm_escolhida = lista[i + 1]

        # Caso contrário, executa a VM de maior prioridade
        if vm_escolhida.P < lista[i + 1].P:
            vm_escolhida = vm_escolhida
        else:
            vm_escolhida = lista[i + 1]
    lista.remove(vm_escolhida)
    lista_espera.extend(lista)
    return vm_escolhida

def conta_done():
    cd = 0
    for vm in lista_vms:
        if vm.done:
            cd +=1
    print(len(lista_vms))
    print(cd)

while not all_done:
    lista_at = exec()
    if len(lista_at) == 1:
        preenche_lista(lista_at[0])
    elif len(lista_at) > 1:
        preenche_lista(decidir_vm_para_executar(lista_at, espaco))
    print(escala)
    all_done = True