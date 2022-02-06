# simple_flask_with_docker

# To Build and run the Docker
docker build . -t Container_Name  
docker run Container_Name 

# if we have only executer in ENTRYPOINT
docker run Container_Name app.py 


# if we are not specifying cdm and ENTRYPOINT and give it has argument. Eg: If we have multiple entrypoints in different environments then we can execute in  argument rather than putting into the docker file 

docker run Container_Name python3 app.py OR
docker run --entrypoint=python3  posimage app.py
