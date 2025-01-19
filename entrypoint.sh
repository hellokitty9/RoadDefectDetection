#!/bin/bash

if [ "$1" = "f" ]; then
    cd kg-frontend/kg-frontend
    npm run serve
elif [ "$1" = "b" ]; then
    cd kg-backend
    python manage.py runserver
else
    echo "Invalid argument. Use 'f' for frontend or 'b' for backend."
fi