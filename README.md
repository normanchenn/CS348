# CS348
Running Docker
```bash
docker compose up --build -d
docker attach cs348-<service>-1
```

Loading DB
```
psql -h localhost -p 5432 -U <username> -d <name>
\i db/create_db.sql
```

The retrieval of mock data can be found at http://localhost:5000/api/v1/test/<key>.
