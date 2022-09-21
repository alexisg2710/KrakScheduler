all: check run

run:
	@python src/__init__.py

init:
	@pip install -r requirements.txt

check:
	@python tests/unit/__init__.py -v

clean:
	@rm -rf src/__pycache__/

.PHONY:
	run
	init
	check
	clean
