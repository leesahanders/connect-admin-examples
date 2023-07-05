# connect-admin-examples

It uses github actions to deploy all content to the Connect server in parallel. Any failures will be recorded in the deployment log, along with relevant error messages. 
 
Content deployed can be accessed through the admin dashboard. This works by prefacing each piece of content with connect-admin-example and then matching on the string to pull it into the connectwidgets document. 
 
 Environment variables can be set during deployment, refer to: <https://github.com/rstudio/actions/tree/main/connect-publish#update-env> 
 
 For github actions further refer to: 
 
- Solutions article: <https://solutions.posit.co/operations/deploy-methods/ci-cd/github-actions/> 
- rstudo-actions sample yaml: <https://github.com/rstudio/actions/blob/main/examples/connect-publish.yaml> 

Content: 

 - shiny-python 
 - shiny-r
 - quarto-python
 - quarto-r
 - dash-app
 - streamlit 
 
 Write the manifests from the main project directory: 
 ```r
 rsconnect::writeManifest(appDir="connectwidgets-success-dashboard")
 ```

 

 