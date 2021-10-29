#!/bin/bash
docker build -t pytest . && docker run -it --rm --name pytest pytest
