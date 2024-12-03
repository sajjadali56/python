## Prisma Client for Python

```sh
pipenv shell
pipenv install

# For every update in schema.prisma, run
# apply migrations
prisma migrate dev --name "add Post model"
# generate
prisma generate
# push
prisma db push

python main.py
```

## Faker

Faker is a library for generating fake data. It can be used to generate fake data for testing and development purposes. It is used in this project to generate fake data for testing and development purposes.

## Pyright

Pyright is a type checker for Python. It is used in this project to check the types of the code.

```sh
pip install pyright
```

Create a pyproject.toml file

```toml
[tool.pyright]
include = [
    "main.py",
]

typeCheckingMode = "strict"
```

Run pyright

```sh
pyright
```
