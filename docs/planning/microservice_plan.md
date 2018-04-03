## Microservices
* `led_frontend` - Hosts webpage to allow changing of configs.
* `led_api` - Receive POSTS from the web UI and does stuff with them. Does logic for what to do with the different messages from led_frontend.
* `led_controller` - Deals with interfacing with the LEDs.

## Workflow
### Make config
1. Make change on led_frontend, hit apply button
2. POST with file gets sent to led_api
3. led_api saves the file.
4. led_api sends message to led_controller with config
5. led_controller reads config and does the stuff

### Apply an existing config
1. Pick config on led_frontend, hit apply button
2. POST with config name to led_api
3. led_api sends message to led_controller to apply config with the config in the message
4. led_controller reads config and does the stuff

### Delete a config
1. Go to delete menu in led_frontend
2. Pick config to delete, hit delete button and probably yes in a pop up
3. POST sent to led_api saying delete this config
4. led_api deletes the file from the volume and updates index of configs
