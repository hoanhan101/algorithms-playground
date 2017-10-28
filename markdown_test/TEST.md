# Rule Engine

## Sketch REST API
Returned data are in JSON format.

### Important Alerts
Returns adviser's important alerts.
* **URL:** `id/important_alerts`
* **Method:** `GET`
* **Params:**
    * **Required:** Adviser ID where `id=[integer]`
* **Return:**
    * **Code:** 200
    * **Example:** 
      ```
      { 
        'id': 1, 
        'category': 'FWT'
        'title': 'FWT approval required'
        'advisses': ['advisee_id': 1234, 'advisee_id': 5678] 
      }
      ```
* **Error:**
    * **Code:** 404 NOT FOUND
    * **Example:**
      ```
      { 
        'response': 'NO IMPORTANT ALERTS' 
      }
      ```
