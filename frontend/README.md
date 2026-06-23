# Product Browser

A scalable product browsing application built with FastAPI, PostgreSQL (Neon), and React.

## Features

- Browse 200,000+ products
- Filter products by category
- Cursor-based pagination for high performance
- Snapshot consistency to prevent duplicates and missing products while data changes
- PostgreSQL indexing for fast queries
- React frontend with category filtering and Load More pagination

---

## Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- PostgreSQL (Neon)

### Frontend
- React
- Vite
- Axios

### Deployment
- Backend: Render
- Database: Neon
- Frontend: Vercel

---

## Database Design

Product schema:

```sql
id
name
category
price
created_at
updated_at
```

Index used:

```sql
CREATE INDEX idx_products_updated_id
ON products(updated_at DESC, id DESC);
```

This index supports efficient cursor pagination.

---

## Pagination Approach

Instead of OFFSET pagination, cursor pagination is used.

Example:

GET /products

Response:

```json
{
  "products": [...],
  "next_cursor": "...",
  "snapshot": "..."
}
```

Next page:

```http
GET /products?cursor=XXX&snapshot=YYY
```

Benefits:

- Faster on large datasets
- Avoids expensive OFFSET scans
- Consistent performance even with 200k+ rows

---

## Snapshot Consistency

To prevent duplicates and missing products while data changes:

1. First request generates a snapshot timestamp.
2. Every subsequent request uses the same snapshot.
3. Only products visible at that snapshot are returned.

This ensures users see a stable dataset while browsing.

---

## Running Locally

### Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend:

```text
http://localhost:8000
```

Swagger Docs:

```text
http://localhost:8000/docs
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

## API Endpoints

### Get Products

```http
GET /products
```

Query Parameters:

| Parameter | Description |
|------------|-------------|
| category | Filter by category |
| cursor | Pagination cursor |
| snapshot | Snapshot timestamp |
| limit | Number of products |

Example:

```http
GET /products?category=Electronics
```

---

## Improvements With More Time

- Search functionality
- Infinite scrolling
- Redis caching
- Automated testing
- Docker deployment

---

## AI Usage

AI tools were used to:

- Accelerate implementation
- Generate boilerplate code
- Review architecture choices

All code was reviewed, tested, and understood before integration.
