test:
	python -m pytest

lint:
	pylint panda3d_render_pass_node

ci: lint test
