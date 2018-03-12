## Docker
* Run everything in a container. Use docker-compose to orchestrate the deployment of the containers.
* Have to set up the `led_runner` using `--privileged` so it has permissions to edit the GPIO pins.
* Also need to attach a volume to `led_config_manager` so that it can store the configs on disk.

### Questions to answer
* How to lock down the api (or would something like apache take care of that as long as api calls are through apache)?
