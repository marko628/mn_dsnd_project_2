# mn_dsnd_project_2
## Data Streaming Nanodegree Project 2 Submission

PLEASE NOTE: Please refer to "Screenshots and Supporting Materials for DSND Project 2.pdf"  for required screenshots and details of performance analysis.


## Step 3 Question 1 
First I established a baseline configuration - maxOffsetsPerTrigger=200, maxRatePerPartition unset, trigger processingTime 20 seconds.  This was roughly 32 processed rows per second. I then experimented with the above settings in combination to determine which resulted in the highest processed records per second based on the progress report. Progress reports were redirected to files to facilitate analysis.

After running 11 variations of the configuration, I came to the following conclusion:
- increasing maxOffsetsPerTrigger has a large positive impact
- decreasing trigger processingTime below 20 sec. has a large negative impact
- setting a small value for maxRatePerPartition has a modest postive impact

Specifics of testing are contained in the .pdf mentioned above.

## Step 3 Question 2
These settings performed best based on testing:

### readStream
.option("maxOffsetsPerTrigger", 2000)
.option("maxRatePerPartition", 10)

### writeStream
.trigger(processingTime = '40 seconds')

### resulting processed records per second ~334

