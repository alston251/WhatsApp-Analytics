# WhatsApp-Analytics

This program parses a WhatsApp conversation exported _chat.txt file to count the number of messages sent by each user and plots a pie chart of the results.

##Prerequisites:
The matplotlib module is required to plot the output data.

##Instructions:

Obtain WhatsApp conversation _chat.txt file:

1. Go to the contact info page on WhatsApp.

2. Select "Export Chat".

3. Select "Without Media" when prompted.

4. Save the file via email, dropbox or any other means.

Use WhatsApp_Analytics.py parser:

5. Type the following in Terminal: 
```
python whatsApp_analytics.py [file path to exported _chat.txt]
```

Optional: 
```
--tocsv [output file path]
```

Can be added to export a .CSV file. 
Note: .csv file extension not required in output path.
