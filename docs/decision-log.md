Decision #001

Why React instead of Next.js?

Because deployment is simpler and SSR isn't needed yet.


Decision #002

Why Vite instead of Create React App?

Because Vite is faster and more modern. It also has better support for TypeScript and other modern web development features.

Decision #003
Why FastAPI instead of Flask or Django?

Because FastAPI is faster, more modern, and has better support for asynchronous programming. It also has built-in support for data validation and serialization, which makes it easier to build APIs.



Decision #004
Why install FastAPI[Standard] instead of FastAPI?

Because `fastapi[standard]` includes Uvicorn and standard optional tooling needed to run the API locally. FastAPI itself already depends on Pydantic and Starlette.


Decision #005
Why PostgreSQL instead of SQLite?

Because PostgreSQL is more robust, scalable, and has better support for advanced features like full-text search, JSON data types, and concurrency. It is also a better choice for production environments and can handle larger datasets and more complex queries than SQLite.