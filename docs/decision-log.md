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

Decision #006
Why ruff instead of other linters?

Ruff provides both formatting and linting, supports Python 3.14, and keeps the backend toolchain small.

Decision #007
Why MIT license?

MIT was selected because Forge is an open portfolio and learning project, and permissive reuse lowers friction. Others may use Forge as a reference or starting point for their own projects, as long as they include the copyright notice and license in their own work.
