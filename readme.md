<h2>Building a regression prediction model for the number of deaths in a given month and year. </h2>
<h3> To build this application we will use linear regression model we can choose the other models as welll such as FFNN with relu activation function. </h3>
<h4> HTTP methods (Hypertext transfer protocol ). They are famous 4 methods called verbs.</h4>

- Client communicates with the server using http requests. 
<h5> Following are the HTTP verbs used by the rest API. </h5>


- Get -> Read the data from server (To read URI).
- Post -> To create the data.
- Put -> To update the data.
- Delete -> To delete the data.



<h2> In this section we will see what we have used to deploy the model in streamlit </h2>

- Creating the stramlit dashboard.
- Creating the dash board that takes the input data as year and months.
- Then predicting the number of deths in that year and month.
- Dataset is given in the below link.
https://opendata.muenchen.de/dataset/monatszahlen-verkehrsunfaelle/resource/40094bd6-f82d-4979-949b-26c8dc00b9a7

<h3> The deployed model Final link is given below. Please feel free to test it 🤠 </h3>

https://deathspredictions.streamlit.app/


<h2>In this senction we will see how can we deploy the model using docker containers(light weight isolated software packages) in AWS service.</h2>

- Dockerize the file in Dickerization folder with all the dependencies.
- Create the docker image.
- Push the image to docker hub.
- Deploy the app in AWS EC2 free version instance ( In this between many steps are involved.) 
