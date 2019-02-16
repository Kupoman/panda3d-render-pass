test:
	poetry run python -m pytest --color=yes

lint:
	poetry run pylint panda3d_render_pass_node

install:
	poetry install

ci: install lint test
