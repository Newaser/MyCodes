def bankers(allocation, need, available, process_num, resource_num):
    """Banker's Algorithim"""
    #Work resoures equals to available ones initially
    work = available[:]
    #No process finished initially
    finish = [False]*process_num
    
    while(True):
        """runnable process searching loop"""
        #No process is runnable initially
        runnable = False
        
        #A walking through aimed to find a runnable process
        for process in range(process_num):
            for resource in range(resource_num):
                #Judge if a certain process runnable
                #by the formula: "Finish[i]=False and Need[i,j]<=Work[j]"
                unfinished = not finish[process]
                need_met = need[process][resource] <= work[resource]
                runnable = unfinished and need_met
                #If the process runnable, break out
                if runnable:
                    break
            if runnable:
                break
                
        #If found a runnable process, pre-run it ,then do searching over again
        if runnable:
            prerun(process, resource_num, work, allocation, finish)
        #If no runnable process
        else:
            return check_safe(finish)
            

def prerun(process, resource_num, work, allocation, finish):
    """pre-run a process"""
    for resource in range(resource_num):
        work[resource] += allocation[process][resource]
        finish[process] = True


def check_safe(finish):
    """check if safe"""
    prompt = "System is not safe!"
    if all(finish):
        prompt = "System is safe!"
    return prompt
