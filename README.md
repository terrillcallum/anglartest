# Django + Angular Example

This repository contains a minimal example of a Django REST backend using SQLite and MongoDB with an Angular frontend. Docker Compose sets up all services.

## Running

```bash
docker-compose up --build
```

* Backend: http://localhost:8000/api/items/
* Mongo items: http://localhost:8000/api/mongo-items/
* Frontend: http://localhost:4200

The backend seeds a few items with quantities and the Angular UI renders them in a bar chart.
