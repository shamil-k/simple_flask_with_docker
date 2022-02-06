# simple_flask_with_docker

# To run the Docker
    docker build . -t Container_Name  
    docker run Container_Name 
    docker run Container_Name app.py # if we have only executer in ENTRYPOINT
    docker run Container_Name python3 app.py # if we are not specifying cdm and enntri point and give it has argument
