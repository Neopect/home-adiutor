# Main file
import Data.data as data
import Scheduler.clock as clock
import Scheduler.queue as queue


def startWiz():
    # Starts all the basic utilities to start AI
    
    # Configuration and Data files
    dataWiz = data()
    dataWiz.configRead()
    dataWiz.findSources(dataWiz.storage)

    # Scheduler
    clockWiz = clock()
    queueWiz = queue()

startWiz()
