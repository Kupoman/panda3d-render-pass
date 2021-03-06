test:
	poetry run python -m pytest --color=yes

lint:
	poetry run pylint panda3d_render_pass

install:
	poetry install

init-screen:
	Xvfb :1 -screen 0 1024x268x16 &

publish:
	poetry build
	poetry publish --username $(PYPI_USERNAME) --password $(PYPI_PASSWORD)

ci: init-screen install lint test
