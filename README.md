## Migrations ##

### Create models ###
Create models in directory `src/db/models/<new_models_file>`
Import new models in `src/migrations/env.py` file

### Create migrations ###
`alembic revision --autogenerate -m “Migration name”`

### Apply migrations ###
`alembic upgrade head`

---

## URL docs ##

### API ###
`http://127.0.0.1:8000/docs/`


## Dependencies docs ##

`https://beta.ruff.rs/docs/` 

`https://docs.sqlalchemy.org/en/20/`
