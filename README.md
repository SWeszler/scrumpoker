# Scrumpoker


## Building Server Side

1. Creating new Django project
2. Creating new Django app
3. Installing all needed Python modules
4. Configuration for Channels
5. Installing Redis
6. Configuration for Redis connection in Django settings
7. Creating Consumer, connect, disconnect and receive
8. Creating websocket testing script
9. Token Authentication https://hashnode.com/post/using-django-drf-jwt-authentication-with-django-channels-cjzy5ffqs0013rus1yb9huxvl


## Build Client Side


## Deployment To Google Cloud Run

### Enable Cloud APIs
```
gcloud services enable \
  run.googleapis.com \
  sql-component.googleapis.com \
  sqladmin.googleapis.com \
  compute.googleapis.com \
  cloudbuild.googleapis.com \
  secretmanager.googleapis.com
```

### Clone Repository
```
gig clone ...
```

### 