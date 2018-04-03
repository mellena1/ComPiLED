#! /bin/bash
export LEDAPIPATH=$(echo $BASH_SOURCE | sed "s|\./||")
export LEDAPIPATH=$(echo $LEDAPIPATH | sed -E 's|/?symlink\-to\-gopath\.sh||')
ln -s $(pwd)/$LEDAPIPATH $GOPATH/src/led_api
