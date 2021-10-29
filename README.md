1. Run `run.sh`. This will build a docker image and run it in a container named `pytest`. You will see the test script periodically loggin `sleeping...`
2. In a second terminal run `docker container stop pytest`. You will see the container printing the output of the script's `shut_down()` function
