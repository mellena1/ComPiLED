## Docker
* Run everything in a container. Use docker-compose to orchestrate the deployment of the containers.
* Have to set up the `led_runner` using `--privileged` so it has permissions to edit the GPIO pins.
* Also need to attach a volume to `led_api` so that it can store the configs on disk.
