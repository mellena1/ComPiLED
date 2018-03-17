## Microservices
* `led_frontend` - Hosts webpage to allow changing of configs.
* `led_api` - Receive POSTS from the web UI and does stuff with them. Does logic for what to do with the different messages from led_frontend.
* `led_controller` - Deals with interfacing with the LEDs.
* `led_config_manager` - Gets configs from the API and saves them (or deletes them). Also hosts a server for led_controller to get configs from.

## Workflow
### Make config
1. Make change on led_frontend, hit apply button
2. POST with file gets sent to led_api
3. led_api sends file to led_config_manager, which saves the file.
4. led_config_manager sends OK back to led_api
5. led_api sends message to led_controller to apply config
6. led_controller asks led_config_manager for the file
7. led_controller reads config and does the stuff

### Apply an existing config
1. Pick config on led_frontend, hit apply button
2. POST with config name to led_api
3. led_api sends message to led_controller to apply config
4. led_controller asks led_config_manager for the file
5. led_controller reads config and does the stuff

### Delete a config
1. Go to delete menu in led_frontend
2. Pick config to delete, hit delete button and probably yes in a pop up
3. POST sent to led_api saying delete this config
4. led_api sends delete message to led_config_manager
5. led_config manager deletes the file and updates index of configs

## Questions to be answered
* Nginx/Apache in front of led_frontend?
    * Apache could provide login stuff so I don't have to write that
