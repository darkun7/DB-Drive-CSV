# DB Drive CSV
This is app is can be used to access CSV file as JSON from Google Drive.
# How To Use
Send POST request on {URL} as Form Data, for example:
```
{
    "index": 1,
    "identifier": "ID"
    "csv": "https://drive.google.com/file/d/1xxk2ASmwnPeAym1or8tCl5Xi6QTcmAqh/view?usp=sharing"
}
```
## Legend:
- index: was used to find the record per row, or will return all row if empty
- identifier: column name that will be indexed
- csv: drive file url