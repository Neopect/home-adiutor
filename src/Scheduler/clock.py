# Clock Module

# This module is responsible for keeping track of habits and processes 
# that are reoccuring and consistant. The purpose of this module is to 
# make viewing, editing, and organizing events with a universal tracking 
# system using cron. (With the added hope of performance improvements)



class Clock:
    def __init__():
        from crontab import CronTab
        global cron, ledger
        ledger = []
        cron = CronTab(user=True) # Maybe make a dedicated user for this

    def event_Add(self, name, comm, time):
        # global cron, ledger
        job = cron.new(command=comm, comment = name)
        job.setall(time)
        cron.write()

        ledger.append([name, comm, time, True, job])
        
    def event_Edit(name, data, time, enabled):
        job = cron.find_comment(name)
        job.set_command(data)
        job.setall(time)
        if enabled == True:
            job.enable()
        else:
            job.enable(False)
        for count, value in enumerate(ledger):
            if value[0] == name:
                ledger[count] = [name, data, time, enabled, job]

        cron.write()

    def event_Remove(name):
        for x in ledger:
            if x[0] == name:
                cron.remove(x[4])
                ledger.remove(x)
                break
    
    def even_find(parm, enabled):
        results = []
        for job in ledger:
            for items in job:
                if items == results and enabled == False:
                    results.append(job[0])
                elif items == results and enabled == True and job[3] == True:
                    results.append(job[0])
        return results




test = Clock()

test.event_Add('test', 'echo "Hello humans"', )