#!/bin/bash
#9. Catch me if you can!
curl -sL 0.0.0.0:5000/catch_me -X PUT -d "You got me!" -H "Origin: HolbertonSchool"
