all:

.PHONY: reformat
reformat:
	black .
	isort ./pixels/*

.PHONY: black
test-black:
	black --check .

.PHONY: isort
test-isort:
	isort -c
