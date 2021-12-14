# Scheduler Workflow

# Sample for generating a job
1. A request is made
2. The request is sent to desired function
   - *name, command, time/frequency*
3. Clock generates a cron job
4. Clock passes the job's description to the ledger
   - *[name, command, time, enabled, job]*

