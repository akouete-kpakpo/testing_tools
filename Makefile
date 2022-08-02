include .makefile_env

pytest:
	${PYTEST} -m "${mark}" ${var}
.PHONY: pytest

ut-py:
	@echo "+++ut-py:"
	${PYTEST} ${TEST_PATH} -m ut
.PHONY: ut-py
