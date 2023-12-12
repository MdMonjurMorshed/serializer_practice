## All about this repositoty
In this project serialisers.Serializer of rest-framework is used. inside the serializer class some mothods that we can overwritte. It depends  on the project's requirements.
Here validate() and to_representation() methods are overridden. Validate method is used to validate some fileds and this validate method will be called if the is_valid(raise_exception=true)
will be called from the view. to_representation() method is used to override where we want to add some extra data to the serializer.

## how to run this project
this project is already dockerized. to get the project use-
git clone <project clone url> or get the zip file
finally run-
docker-compose up --build from the terminal
 
 
