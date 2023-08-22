#!/bin/bash

alembic upgrade head

cd src/users

uvicorn main:app --bind=0.0.0.0:8001
