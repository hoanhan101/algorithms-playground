# Rule Engine

## Sketch REST API Endpoint
Returned data are in JSON format.

### Important Alerts
Returns adviser's important alerts.
* **URL:** `/faculty_id/important_alerts`
* **Method:** `GET`
* **Params:**
    * **Required:** `faculty_id=[integer]`
* **Return:**
    * **Code:** 200
    * **Example:** 
      ```
      { 
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

### Upcoming Events
Returns upcoming events and deadline
* **URL:** `/upcoming_events`
* **Method:** `GET`
* **Params:** None
* **Return:**
    * **Code:** 200
    * **Example:** 
      ```
      { 
        'date': '10/03/2017'
        'text': 'Faculty meeting'
      }
      ```
* **Error:**
    * **Code:** 404 NOT FOUND
    * **Example:**
      ```
      { 
        'response': 'NO UPCOMING EVENTS/DEADLINE' 
      }
      ```

### 3-day Schedule
Return adviser's schedule for 3 days in a row, including today.
* **URL:** `/faculty_id/schedule/3-day`
* **Method:** `GET`
* **Params:**
    * **Required:** `faculty_id=[integer]`
* **Return:**
    * **Code:** 200
    * **Example:** 
      ```
      { 
        [
          { 'time': '10:10 AM', 'text': 'Faculty Meeting'},
          { 'time': '9:30 AM', 'text': 'Office Hour'},
          { 'time': '10:10 AM', 'text': 'Plan Day'}
        ]
      }
      ```
* **Error:**
    * **Code:** 404 NOT FOUND
    * **Example:**
      ```
      { 
        'response': 'NO SCHEDULE FOR THE NEXT 3 DAYS' 
      }
      ```
    
### Note
Return 3 last modified notes
* **URL:** `/faculty_id/recent_note`
* **Method:** `GET`
* **Params:**
    * **Required:** `faculty_id=[integer]`
* **Return:**
    * **Code:** 200
    * **Example:** 
      ```
      { 
        [
          { 'date': '09/28/17', 'text': 'Plan for next class'},
          { 'date': '09/26/17', 'text': 'Meeting with Andrew'},
          { 'date': '09/23/17', 'text': 'Print out homeworks'}
        ]
      }
      ```
* **Error:**
    * **Code:** 404 NOT FOUND
    * **Example:**
      ```
      { 
        'response': 'NO NEW NOTE' 
      }
      ```
      
### Adding Note
Return 3 last modified notes
* **URL:** `/faculty_id/note/add`
* **Method:** `POST`
* **Params:**
    * **Required:** `faculty_id=[integer]`
* **Return:**
    * **Code:** 200
    * **Example:** 
      ```
      {
        'date': '09/28/17', 'text': 'Plan for next class' 
      }
      ```
* **Error:**
    * **Code:** 404 NOT FOUND
    * **Example:**
      ```
      { 
        'response': 'FAILED TO ADD NOTE' 
      }
      ```
    
### List of Advisees
Return a list of Advisees with basic information: picture, name, term, pronoun, quick notification.
* **URL:** `/faculty_id/advisees`
* **Method:** `GET`
* **Params:**
    * **Required:** `faculty_id=[integer]`
* **Return:**
    * **Code:** 200
    * **Example:** 
      ```
      { 
        [
          { 
            'student_id': '1234', 
            'first_name': 'Rick', 
            'last_name': 'Sanchez', 
            'term': 1,
            'pronoun': 'he/him',
            'quick_notification': 'Incoming Plan Meeting'
          }, 
          ...
        ]
      }
      ```
* **Error:**
    * **Code:** 404 NOT FOUND
    * **Example:**
      ```
      { 
        'response': 'CAN'T FIND ANY ADVISEES' 
      }
      ```
   
### Advisee/Adivising
Return advising information for an advisee
* **URL:** `/student_id/advising`
* **Method:** `GET`
* **Params:**
    * **Required:** `student_id=[integer]`
* **Return:**
    * **Code:** 200
    * **Example:** 
      ```
      { 
        [
          { 
            'student_id': '1234', 
            'first_name': 'Rick', 
            'last_name': 'Sanchez', 
            'term': 1,
            'pronoun': 'he/him',
            'graduation_date': '06/01/2021',
            'deadlines': [{'date': '09/20/2017', 'text': 'Plan Essay due to Advisor'}],
            'warning': [{'type': 'Acedemic Concern Form', 'link': 'https://www.bennington.edu'}]
          }, 
          ...
        ]
      }
      ```
* **Error:**
    * **Code:** 404 NOT FOUND
    * **Example:**
      ```
      { 
        'response': 'NO DEADLINES OR WARNING' 
      }
      ```

   
    