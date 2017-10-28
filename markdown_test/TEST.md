# Rule Engine

## Sketch REST API
Returned data are in JSON format.

### Important Alerts
Returns advisor's important alerts.
* **URL:** `id/important_alerts`
* **Method:** `GET`
* **Params:**
    * **Required:** `id=[integer]`
* **Success Response:**
    * **Code:** 200 
        <br/>
      **Content:** `{ id : 12, name : "Michael Bloom" }`
* **Error Response:**
    * **Code:** 404 NOT FOUND
        <br/>
      **Content:** `{ error : "User doesn't exist" }`
* **Sample Call:**
  ```javascript
    $.ajax({
      url: "/users/1",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```