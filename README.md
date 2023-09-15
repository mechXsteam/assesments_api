# assesments_api
- created a basic blueprint
- SQL queries are yet to be figured out
- our data should look like this [link](https://docs.google.com/spreadsheets/d/1-K3_bilY_AuDV3m43ReABzCrfWNGktjgtDuyPTzWaKk/edit?usp=sharing)
- result calculation strategy
  - created a user_response model which will store all the user responses against ques_id and section_id
  - question model will contain ques, options and correct ans against section_id
  - pull them via section id, match and calculate marks.
