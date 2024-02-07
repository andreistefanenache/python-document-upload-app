clean:
	rm -f DYNAMIC_DOCUMENT_UPLOAD*
	rm -f db.sqlite
	python3 create_db.py
test:
	pytest
