# DB Drive CSV
This is app is can be used to access CSV file as JSON from Google Drive.
# How To Use
1. Create file/ upload file to Google Drive
2. There's 2 file extention that supported:
 - *File with extension **.CSV***
Send POST request as form data to url https://dbdrive.herokuapp.com/
you may use example below:
```
{ 
"index": 1, 
"identifier": "ID"
"csv": "https://drive.google.com/file/d/1xxk2ASmwnPeAym1or8tCl5Xi6QTcmAqh/view?usp=sharing" 
}
```
 - *File with extension **.XLS** or **.XLSX***
Send POST request as form data to url https://dbdrive.herokuapp.com/xls
you may use example below:
```
{
"index": 1, 
"identifier": "ID" 
"xls": "https://docs.google.com/spreadsheets/d/1DM_-HOWXMsPmshnIq-wfJq7Jtc4pacLC6bUC8c1XzpU/edit?usp=sharing"
}
```
## Legend:
- index: was used to find the record per row, or will return all row if empty
- identifier: column name that will be indexed
- csv or xls: drive file url
