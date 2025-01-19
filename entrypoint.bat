@echo off

if "%1" == "f" (
    cd kg-frontend\kg-frontend
    npm run serve
) else if "%1" == "b" (
    cd kg-backend
    python manage.py runserver
) else (
    echo Invalid argument. Use 'f' for frontend or 'b' for backend.
)