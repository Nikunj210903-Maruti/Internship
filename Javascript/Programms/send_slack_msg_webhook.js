 var emailid = request['email']
 var spread_sheet_id = getSpreadsheetId()
 var Spread_Sheet_link = "<https://docs.google.com/spreadsheets/d/" + getSpreadsheetId() + "| Click_here>"
            
var data = {
"attachments": [
{
  "color": "green",
  "pretext": "Data About Spread Sheet and Email_id",
  "fields": [ 
    {
      "title": "Email Id",
      "value": emailid,
    },
    {
      "title" : "Spred_Sheet Id",
      "value" : spread_sheet_id ,
    },
    {
      "title" : "Spraed _Sheet_link",
      "value" : Spread_Sheet_link,
    }]
}
],
};


var slack_message = {
    "method": "post",
    "contentType": "application/json",
    "payload": JSON.stringify(data),
    "muteHttpExceptions": true
 };

 var slack_msg_res =  UrlFetchApp.fetch(slack_url,slack_message)

 if (slack_msg_res.getResponseCode() == 200) {
   Logger.log(slack_msg_res); 
 }
