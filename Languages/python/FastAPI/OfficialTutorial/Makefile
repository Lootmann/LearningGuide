PORT=8888

run:
	uvicorn main:my_app --reload --port $(PORT)

docs:
	google-chrome http://127.0.0.1:$(PORT)/docs

redocs:
	google-chrome http://127.0.0.1:$(PORT)/redoc
