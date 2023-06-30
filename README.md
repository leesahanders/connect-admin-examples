# connect-admin-examples


Content: 

 - shiny-python 
 - shiny-r
 - quarto-python
 - quarto-r
 - dash-app
 - streamlit 
 
 
 It uses github actions to deploy all content to the Connect server in parallel. Any failures will be recorded in the deployment log, along with relevant error messages. 
 
 Content deployed can be accessed through the admin dashboard. This works by prefacing each piece of content with connect-admin-example and then matching on the string to pull it into the connectwidgets document. 
 

 